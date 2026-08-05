# ==========================================
# GOC AROMATIC SUBSTITUTION ENGINE (EXHAUSTIVE OLYMPIAD & GRADUATE LEVEL)
# ==========================================

# 1. Advanced Electron Donating Groups (Ortho/Para Directors)
# Divided into strong (+M dominant) and moderate/weak (+I / hyperconjugation)
STRONG_EDG = "[OX2H1,OX2H0,NX3H2,NX3H1]" # Phenols, ethers, amines
WEAK_EDG = "[CX4]"                     # Alkyl chains (toluene matrices)
HALOGENS = "[F,Cl,Br,I]"                # Deactivating ortho/para directors via lone-pair resonance (+M vs -I)

EDG_ATOM = f"[{STRONG_EDG.strip('[]')},{WEAK_EDG.strip('[]')},{HALOGENS.strip('[]')}]"

# 2. Advanced Electron Withdrawing Groups (Meta Directors)
# Strong -M and -I groups that deactivate the ring toward electrophilic attack
EWG_GROUPS = [
    "[CX3]=O",          # Carbonyls (Ketones, Aldehydes, Acids, Esters)
    "[N+](=O)[O-]",     # Nitro group
    "C#N",              # Cyano group
    "[SX4](=O)=O",      # Sulfonic acid derivatives
    "[CX4](F)(F)F",     # Trifluoromethyl (-CF3)
    "[NX3+]([O-])([O-])" # Quaternary / Charged nitrogen complexes
]

# Lewis base matrices that poison Friedel-Crafts catalysts via complexation
LEWIS_BASE_POISONS = [
    "[c]-[NX3H2]",       # Free aromatic primary amines (Aniline)
    "[c]-[NX3H1]-[#6]",  # Secondary aromatic amines
    "[c]-[OX2H1]"        # Free phenols (partially complexes with strong Lewis acids)
]

def generate_goc_rules(electrophile_smarts, allow_deactivated=True):
    """
    Dynamically generates rigorous SMARTS strings for Electrophilic Aromatic Substitution (EAS) 
    utilizing Recursive SMARTS $(...) for positional electronics.
    """
    rules = [
        # BASELINE: Unsubstituted Benzene Vertex
        f"[cH:1]$(c1[cH][cH][cH][cH][cH]1) >> [c:1]-{electrophile_smarts}",
        
        # ORTHO-DIRECTING ACTIVATION MATRIX: Positioned adjacent to EDG/Halogens
        f"[cH:1]$(cc-{EDG_ATOM}) >> [c:1]-{electrophile_smarts}",
        
        # PARA-DIRECTING ACTIVATION MATRIX: Positioned 3 aromatic bonds away from EDG/Halogens
        f"[cH:1]$(cccc-{EDG_ATOM}) >> [c:1]-{electrophile_smarts}"
    ]
    
    # META-DIRECTING DEACTIVATION MATRIX: Positioned 2 aromatic bonds away from EWG matrices
    if allow_deactivated:
        for ewg in EWG_GROUPS:
            rules.append(f"[cH:1]$(ccc-{ewg}) >> [c:1]-{electrophile_smarts}")
            
    return rules

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
AROMATIC_RULES = {
    
    # ==========================================
    # 1. AROMATIC HALOGENATION
    # ==========================================
    
    "Cl2 / Anhydrous FeCl3 (Electrophilic Chlorination)": {
        "rules": generate_goc_rules("[Cl]")
    },
    
    "Br2 / Anhydrous FeBr3 (Electrophilic Bromination)": {
        "rules": generate_goc_rules("[Br]")
    },
    
    # ==========================================
    # 2. NITRATION & SULFONATION
    # ==========================================
    
    "Conc. HNO3 + Conc. H2SO4, 50-60°C (Aromatic Nitration via Nitronium Ion)": {
        "rules": generate_goc_rules("[N+](=O)[O-]")
    },
    
    "Fuming H2SO4 / SO3 (Reversible Aromatic Sulfonation)": {
        "rules": generate_goc_rules("[S](=O)(=O)[OH]")
    },
    
    # ==========================================
    # 3. FRIEDEL-CRAFTS ALKYLATION & ACYLATION
    # ==========================================

    "R-Cl / Anhydrous AlCl3 (Friedel-Crafts Alkylation)": {
        "rules": generate_goc_rules("[CH3]", allow_deactivated=False),
        "poisons": EWG_GROUPS + LEWIS_BASE_POISONS,
        "poison_message": "Friedel-Crafts Alkylation failure: Strongly deactivated (meta-directing) rings lack the nucleophilic pi-electron density to attack alkyl carbocations. Furthermore, free aromatic amines complex irreversibly with AlCl3 catalyst."
    },
    
    "R-COCl / Anhydrous AlCl3 (Friedel-Crafts Acylation)": {
        "rules": generate_goc_rules("[C](=O)[CH3]", allow_deactivated=False),
        "poisons": EWG_GROUPS + LEWIS_BASE_POISONS,
        "poison_message": "Friedel-Crafts Acylation failure: Acylation fails on deactivated aromatic matrices due to extreme electrostatic repulsion. Basic amine substrates poison the Lewis acid catalyst."
    },

    # ==========================================
    # 4. ADVANCED AROMATIC FORMYLATION
    # ==========================================

    "CO + HCl / Anhydrous AlCl3 / CuCl (Gattermann-Koch Formylation)": {
        "rules": generate_goc_rules("[CH1]=O", allow_deactivated=False),
        "poisons": EWG_GROUPS + LEWIS_BASE_POISONS,
        "poison_message": "Gattermann-Koch Formylation failure: Incompatible with severely deactivated rings, phenols, and aromatic amines due to catalyst deactivation and complexation."
    },

    "POCl3 / DMF followed by Aqueous Hydrolysis (Vilsmeier-Haack Formylation)": {
        "rules": [
            # Specifically targets highly activated electron-rich aromatic systems (phenols, dialkylanilines, heterocycles)
            "[cH:1]$(cc-[OX2H1,NX3(C)(C)]) >> [c:1]-C=O"
        ]
    }
}