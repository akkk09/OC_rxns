# ==========================================
# GOC AROMATIC SUBSTITUTION ENGINE
# ==========================================

# 1. Define Electron Donating Groups (Ortho/Para Directors)
# Contains lone pairs (+M) or alkyl groups (+I)
EDG_ATOM = "[OX2,NX3,F,Cl,Br,I,CX4]"

# 2. Define Electron Withdrawing Groups (Meta Directors)
# Contains pi-bonds to electronegative atoms (-M) or strong -I
EWG_GROUPS = [
    "[CX3]=O",        # Carbonyls (Ketones, Aldehydes, Acids, Esters)
    "[N+](=O)[O-]",   # Nitro
    "C#N",            # Cyano
    "[SX4](=O)=O",    # Sulfonic
    "[CX4](F)(F)F"    # Trifluoromethyl (-CF3)
]

def generate_goc_rules(electrophile_smarts, allow_deactivated=True):
    """
    Dynamically generates the SMARTS strings for Electrophilic Aromatic Substitution 
    based on GOC directing rules using Recursive SMARTS $(...).
    """
    rules = [
        # BASELINE: Unsubstituted Benzene
        # Matches a carbon only if all 6 carbons in the ring have hydrogens
        f"[cH:1]$(c1[cH][cH][cH][cH][cH]1) >> [c:1]-{electrophile_smarts}",
        
        # ACTIVATED / HALOGENS: Ortho Position
        f"[cH:1]$(cc-{EDG_ATOM}) >> [c:1]-{electrophile_smarts}",
        
        # ACTIVATED / HALOGENS: Para Position
        f"[cH:1]$(cccc-{EDG_ATOM}) >> [c:1]-{electrophile_smarts}"
    ]
    
    # DEACTIVATED: Meta Position
    if allow_deactivated:
        for ewg in EWG_GROUPS:
            rules.append(f"[cH:1]$(ccc-{ewg}) >> [c:1]-{electrophile_smarts}")
            
    return rules

# ==========================================
# 3. THE REAGENT DICTIONARY
# ==========================================
AROMATIC_RULES = {
    # Standard EAS reactions work on all rings
    "Cl2 / FeCl3": {
        "rules": generate_goc_rules("[Cl]")
    },
    "Br2 / FeBr3": {
        "rules": generate_goc_rules("[Br]")
    },
    "Conc. HNO3 + H2SO4": {
        "rules": generate_goc_rules("[N+](=[O])[O-]")
    },
    "Fuming H2SO4": {
        "rules": generate_goc_rules("[S](=O)(=O)[OH]")
    },
    
    # --- THE POWER OF THE POISON ENGINE ---
    # Friedel-Crafts fails on Meta-directing (deactivated) rings.
    # We set allow_deactivated=False to prevent Meta substitution, 
    # and we pass EWG_GROUPS into the poison list so the server alerts the user!
    "CH3Cl / AlCl3": {
        "rules": generate_goc_rules("[CH3]", allow_deactivated=False),
        "poisons": EWG_GROUPS,
        "poison_message": "Friedel-Crafts alkylation fails on highly deactivated (meta-directing) rings."
    },
    "CH3COCl / AlCl3": {
        "rules": generate_goc_rules("[C](=O)[CH3]", allow_deactivated=False),
        "poisons": EWG_GROUPS,
        "poison_message": "Friedel-Crafts acylation fails on highly deactivated (meta-directing) rings."
    }
}