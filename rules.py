import json
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.MolStandardize import rdMolStandardize

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

def execute_smarts(reactant, smarts_list):
    """Runs the RDKit SMARTS reaction and catches physical violations."""
    results = set()
    for smarts in smarts_list:
        rxn = AllChem.ReactionFromSmarts(smarts)
        products = rxn.RunReactants((reactant,))
        for product_set in products:
            for p in product_set:
                try:
                    # RDKit strict chemistry check
                    Chem.SanitizeMol(p)
                    results.add(Chem.MolToSmiles(p))
                except ValueError as e:
                    # Fails gracefully
                    print(f"Discarding physically impossible intermediate: {e}")
                    pass 
    return results

def apply_rules(smiles, reagent, active_modules=None, custom_dict=None):
    """Processes the input SMILES against the dynamically built dictionary."""
    reactant = Chem.MolFromSmiles(smiles)
    if not reactant:
        return {"message": "Invalid molecule drawn."}

    # 1. Build the dynamic master dictionary for this specific request
    master_rules = {}
    
    # If no modules specified (e.g., direct API call), default to all
    if active_modules is None:
        active_modules = list(REGISTRY.keys())
    
    # Load selected default modules from the checkboxes
    for module in active_modules:
        if module in REGISTRY:
            master_rules.update(REGISTRY[module])
            
    # Overlay custom user JSON (Overrides defaults if there is a name collision)
    if isinstance(custom_dict, dict):
        master_rules.update(custom_dict)

    all_results = set()

    # 2. Sequential Macro Handling
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
                                poison_pattern = Chem.MolFromSmarts(poison_smarts)
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

    # 3. Standard Execution
    if reagent not in master_rules:
        return {"message": "Reagent not found in active dictionaries."}

    reagent_data = master_rules[reagent]
    smarts_list = []

    if isinstance(reagent_data, dict):
        if "poisons" in reagent_data:
            for poison_smarts in reagent_data["poisons"]:
                poison_pattern = Chem.MolFromSmarts(poison_smarts)
                if reactant.HasSubstructMatch(poison_pattern):
                    return {"message": reagent_data.get("poison_message", "Reaction poisoned by an incompatible functional group.")}
        
        smarts_list = reagent_data.get("rules", [])
    else:
        smarts_list = reagent_data

    all_results.update(execute_smarts(reactant, smarts_list))

    # Tautomer check if primary attack fails
    if not all_results:
        enumerator = rdMolStandardize.TautomerEnumerator()
        tautomers = enumerator.Enumerate(reactant)
        
        for taut in tautomers:
            if Chem.MolToSmiles(taut) != smiles:
                all_results.update(execute_smarts(taut, smarts_list))

    if not all_results:
        return {"message": "No reaction occurred."}
    
    return {"product_smiles": ".".join(all_results)}


class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/reagents':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # Dynamically map each module to its specific list of reagents
            reagent_map = {}
            for module_name, module_dict in REGISTRY.items():
                reagent_map[module_name] = list(module_dict.keys())
                
            self.wfile.write(json.dumps(reagent_map).encode('utf-8'))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/predict':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            # Extract dynamic configuration sent from script.js
            smiles = data.get('smiles', '')
            reagent = data.get('reagent', '')
            active_modules = data.get('active_modules') 
            custom_dict = data.get('custom_dictionary')
            
            result = apply_rules(smiles, reagent, active_modules, custom_dict)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode('utf-8'))
        else:
            self.send_error(404, "Endpoint not found")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    print(f"Loaded {len(REGISTRY)} base dictionary modules.")
    print(f"Starting dynamic simulator on port {port}...")
    
    HTTPServer(('0.0.0.0', port), RequestHandler).serve_forever()