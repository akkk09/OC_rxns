import os
import functools
from flask import Flask, request, jsonify
from flask_cors import CORS
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.MolStandardize import rdMolStandardize

# Core Dictionaries
from dicts.dict_advanced_rearrangements import ADVANCED_REARRANGEMENT_RULES
from dicts.dict_alcohols_phenols import ALCOHOL_PHENOL_RULES
from dicts.dict_aldehydes_ketones import ALDEHYDE_KETONE_RULES
from dicts.dict_alkenes import ALKENE_RULES
from dicts.dict_alkyl_halides import ALKYL_HALIDE_RULES
from dicts.dict_alkynes import ALKYNE_RULES
from dicts.dict_amines import AMINE_RULES
from dicts.dict_aromatics import AROMATIC_RULES
from dicts.dict_biomolecules import BIOMOLECULE_RULES
from dicts.dict_carboxylic import CARBOXYLIC_RULES
from dicts.dict_eas import EAS_RULES
from dicts.dict_heterocycles import HETEROCYCLE_RULES
from dicts.dict_macros import MACRO_REAGENTS
from dicts.dict_nitrogen import NITROGEN_RULES
from dicts.dict_oxidation import OXIDATION_RULES
from dicts.dict_polymers_poc import POLYMERS_POC_RULES
from dicts.dict_protecting_groups import PROTECTING_GROUP_RULES
from dicts.dict_reduction import REDUCTION_RULES

app = Flask(__name__)
CORS(app) # This automatically handles all the cross-origin routing for Vercel!

REGISTRY = {
    "advanced_rearrangements": ADVANCED_REARRANGEMENT_RULES,
    "alcohols_phenols": ALCOHOL_PHENOL_RULES,
    "aldehydes_ketones": ALDEHYDE_KETONE_RULES,
    "alkenes": ALKENE_RULES,
    "alkyl_halides": ALKYL_HALIDE_RULES,
    "alkynes": ALKYNE_RULES,
    "amines": AMINE_RULES,
    "aromatics": AROMATIC_RULES,
    "biomolecules": BIOMOLECULE_RULES,
    "carboxylic": CARBOXYLIC_RULES,
    "eas": EAS_RULES,
    "heterocycles": HETEROCYCLE_RULES,
    "macros": MACRO_REAGENTS,
    "nitrogen": NITROGEN_RULES,
    "oxidation": OXIDATION_RULES,
    "polymers_poc": POLYMERS_POC_RULES,
    "protecting_groups": PROTECTING_GROUP_RULES,
    "reduction": REDUCTION_RULES
}

# --- OPTIMIZATIONS: LRU Caching ---
@functools.lru_cache(maxsize=2048)
def get_compiled_reaction(smarts):
    return AllChem.ReactionFromSmarts(smarts)

@functools.lru_cache(maxsize=1024)
def get_tautomers_smiles(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return []
    enumerator = rdMolStandardize.TautomerEnumerator()
    tautomers = enumerator.Enumerate(mol)
    return [Chem.MolToSmiles(t) for t in tautomers if Chem.MolToSmiles(t) != smiles]

@functools.lru_cache(maxsize=1024)
def get_compiled_poison(smarts):
    return Chem.MolFromSmarts(smarts)

def execute_smarts(reactant, smarts_list):
    results = set()
    for smarts in smarts_list:
        rxn = get_compiled_reaction(smarts) 
        products = rxn.RunReactants((reactant,))
        for product_set in products:
            for p in product_set:
                try:
                    Chem.SanitizeMol(p)
                    results.add(Chem.MolToSmiles(p))
                except ValueError:
                    pass 
    return results

def apply_rules(smiles, reagent, active_modules=None, custom_dict=None):
    reactant = Chem.MolFromSmiles(smiles)
    if not reactant:
        return {"message": "Invalid molecule drawn."}

    master_rules = {}
    if active_modules is None:
        active_modules = list(REGISTRY.keys())
    
    for module in active_modules:
        if module in REGISTRY:
            master_rules.update(REGISTRY[module])
            
    if isinstance(custom_dict, dict):
        master_rules.update(custom_dict)

    all_results = set()

    if reagent in master_rules and isinstance(master_rules[reagent], list) and not any(">>" in step for step in master_rules[reagent]):
        current_smiles = [smiles]
        for step in master_rules[reagent]:
            step_results = set()
            for s in current_smiles:
                mol = Chem.MolFromSmiles(s)
                if mol:
                    step_data = master_rules.get(step, [])
                    step_smarts_list = []
                    
                    if isinstance(step_data, dict):
                        if "poisons" in step_data:
                            for poison_smarts in step_data["poisons"]:
                                poison_pattern = get_compiled_poison(poison_smarts)
                                if mol.HasSubstructMatch(poison_pattern):
                                    msg = step_data.get("poison_message", "Poisoned.")
                                    return {"message": f"Macro halted at step '{step}': {msg}"}
                        step_smarts_list = step_data.get("rules", [])
                    else:
                        step_smarts_list = step_data
                        
                    step_results.update(execute_smarts(mol, step_smarts_list))
            
            if step_results:
                current_smiles = list(step_results)
                
        return {"product_smiles": ".".join(current_smiles)} if current_smiles != [smiles] else {"message": "No reaction occurred."}

    if reagent not in master_rules:
        return {"message": "Reagent not found in active dictionaries."}

    reagent_data = master_rules[reagent]
    smarts_list = []

    if isinstance(reagent_data, dict):
        if "poisons" in reagent_data:
            for poison_smarts in reagent_data["poisons"]:
                poison_pattern = get_compiled_poison(poison_smarts)
                if reactant.HasSubstructMatch(poison_pattern):
                    return {"message": reagent_data.get("poison_message", "Reaction poisoned by an incompatible functional group.")}
        
        smarts_list = reagent_data.get("rules", [])
    else:
        smarts_list = reagent_data

    all_results.update(execute_smarts(reactant, smarts_list))

    if not all_results:
        tautomer_smiles_list = get_tautomers_smiles(smiles)
        for t_smiles in tautomer_smiles_list:
            taut_mol = Chem.MolFromSmiles(t_smiles)
            if taut_mol:
                all_results.update(execute_smarts(taut_mol, smarts_list))

    if not all_results:
        return {"message": "No reaction occurred."}
    
    return {"product_smiles": ".".join(all_results)}

# --- API ROUTES ---
@app.route('/reagents', methods=['GET'])
def get_reagents():
    reagent_map = {mod: list(rules.keys()) for mod, rules in REGISTRY.items()}
    return jsonify(reagent_map)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    result = apply_rules(
        data.get('smiles', ''), 
        data.get('reagent', ''), 
        data.get('active_modules'), 
        data.get('custom_dictionary')
    )
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)