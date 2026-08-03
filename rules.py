import json
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.MolStandardize import rdMolStandardize


from dicts.dict_reduction import REDUCTION_RULES
from dicts.dict_oxidation import OXIDATION_RULES
from dicts.dict_aromatics import AROMATIC_RULES
from dicts.dict_alkenes import ALKENE_RULES
from dicts.dict_alkynes import ALKYNE_RULES
from dicts.dict_alkyl_halides import ALKYL_HALIDE_RULES
from dicts.dict_aldehydes_ketones import ALDEHYDE_KETONE_RULES
from dicts.dict_alcohols_phenols import ALCOHOL_PHENOL_RULES
from dicts.dict_nitrogen import NITROGEN_RULES
from dicts.dict_carboxylic import CARBOXYLIC_RULES
from dicts.dict_protecting_groups import PROTECTING_GROUPS_RULES
from dicts.dict_heterocycles import HETEROCYCLE_RULES
from dicts.dict_advanced_rearrangements import ADVANCED_REARRANGEMENT_RULES


ACTIVE_RULES = {}
ACTIVE_RULES.update(REDUCTION_RULES)
ACTIVE_RULES.update(OXIDATION_RULES)
ACTIVE_RULES.update(AROMATIC_RULES)
ACTIVE_RULES.update(ALKENE_RULES)
ACTIVE_RULES.update(ALKYNE_RULES)
ACTIVE_RULES.update(ALKYL_HALIDE_RULES)
ACTIVE_RULES.update(ALDEHYDE_KETONE_RULES)
ACTIVE_RULES.update(ALCOHOL_PHENOL_RULES)
ACTIVE_RULES.update(NITROGEN_RULES)
ACTIVE_RULES.update(CARBOXYLIC_RULES)
ACTIVE_RULES.update(PROTECTING_GROUPS_RULES)
ACTIVE_RULES.update(HETEROCYCLE_RULES)
ACTIVE_RULES.update(ADVANCED_REARRANGEMENT_RULES)

MACRO_REAGENTS = {
    "I2 / NaOH (Iodoform Test)": [
        "PCC / CH2Cl2",  
        "Iodoform Cleavage"
    ],
    "O3 / H2O2 (Oxidative Ozonolysis)": [
        "O3 then Zn/H2O",
        "Tollens' Reagent"
    ]
}

def execute_smarts(reactant, smarts_list):
    results = set()
    for smarts in smarts_list:
        rxn = AllChem.ReactionFromSmarts(smarts)
        products = rxn.RunReactants((reactant,))
        for product_set in products:
            for p in product_set:
                try:
                    Chem.SanitizeMol(p)
                    results.add(Chem.MolToSmiles(p))
                except Exception:
                    results.add(Chem.MolToSmiles(p))
    return results

def apply_rules(smiles, reagent):
    reactant = Chem.MolFromSmiles(smiles)
    if not reactant:
        return {"message": "Invalid molecule drawn."}

    all_results = set()

    if reagent in MACRO_REAGENTS:
        current_smiles = [smiles]
        for step in MACRO_REAGENTS[reagent]:
            step_results = set()
            for s in current_smiles:
                mol = Chem.MolFromSmiles(s)
                if mol:
                    step_results.update(execute_smarts(mol, ACTIVE_RULES.get(step, [])))
            if step_results:
                current_smiles = list(step_results)
        return {"product_smiles": ".".join(current_smiles)} if current_smiles != [smiles] else {"message": "No reaction occurred."}

    if reagent not in ACTIVE_RULES:
        return {"message": "Reagent not programmed."}

    all_results.update(execute_smarts(reactant, ACTIVE_RULES[reagent]))

    if not all_results:
        enumerator = rdMolStandardize.TautomerEnumerator()
        tautomers = enumerator.Enumerate(reactant)
        
        for taut in tautomers:
            if Chem.MolToSmiles(taut) != smiles:
                all_results.update(execute_smarts(taut, ACTIVE_RULES[reagent]))

    if not all_results:
        return {"message": "No reaction occurred."}
    
    return {"product_smiles": ".".join(all_results)}

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/reagents':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            all_reagents = list(ACTIVE_RULES.keys()) + list(MACRO_REAGENTS.keys())
            self.wfile.write(json.dumps(all_reagents).encode('utf-8'))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/predict':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            result = apply_rules(data.get('smiles', ''), data.get('reagent', ''))
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode('utf-8'))
        else:
            self.send_error(404, "Endpoint not found")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    print(f"Loaded {len(ACTIVE_RULES)} base reagents and {len(MACRO_REAGENTS)} macros.")
    print(f"Starting simulator... Open your browser to http://localhost:{port}")
    HTTPServer(('0.0.0.0', port), RequestHandler).serve_forever()