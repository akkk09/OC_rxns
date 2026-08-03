import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from rdkit import Chem
from rdkit.Chem import AllChem

# 1. Import all 11 modular dictionaries
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

# 2. Combine them into the active engine
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

def apply_rules(smiles, reagent):
    if reagent not in ACTIVE_RULES:
        return {"message": "Reagent not found in loaded dictionaries."}

    reactant = Chem.MolFromSmiles(smiles)
    if not reactant:
        return {"message": "Invalid molecule drawn."}

    all_results = set()
    for smarts in ACTIVE_RULES[reagent]:
        rxn = AllChem.ReactionFromSmarts(smarts)
        products = rxn.RunReactants((reactant,))
        for product_set in products:
            for p in product_set:
                try:
                    Chem.SanitizeMol(p)
                    all_results.add(Chem.MolToSmiles(p))
                except Exception:
                    all_results.add(Chem.MolToSmiles(p))

    if not all_results:
        return {"message": "No reaction occurred."}
    
    return {"product_smiles": ".".join(all_results)}

# 3. The Lightweight Server
class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Auto-populate endpoint for the frontend dropdown
        if self.path == '/reagents':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(list(ACTIVE_RULES.keys())).encode('utf-8'))
        else:
            # Serve index.html and Ketcher files normally
            super().do_GET() 

    def do_POST(self):
        # Processing endpoint for SMILES prediction
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

import os

if __name__ == '__main__':
    # The cloud provider will set the PORT environment variable. 
    # If it's not set (like on your local machine), it defaults to 8000.
    port = int(os.environ.get('PORT', 8000))
    
    print(f"Loaded {len(ACTIVE_RULES)} reagents.")
    print(f"Starting simulator on port {port}...")
    
    # 0.0.0.0 tells the server to accept connections from the outside world
    HTTPServer(('0.0.0.0', port), RequestHandler).serve_forever()