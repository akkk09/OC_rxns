# ==========================================
# ALKENE ADDITION ENGINE (MARKOVNIKOV LOGIC)
# ==========================================

def generate_markovnikov(nu_smarts):
    """
    Generates SMARTS for Markovnikov addition.
    The Nucleophile adds to the more substituted carbon (fewer Hydrogens).
    """
    return [
        # 1. Asymmetric: Terminal Alkene (C=C-R or C=C(R)R) 
        # C1 has 2H, C2 has 1H or 0H. Nucleophile goes to C2.
        f"[CH2:1]=[CH1,CH0:2] >> [C:1]-[C:2]-{nu_smarts}",
        
        # 2. Asymmetric: Trisubstituted Alkene (R-CH=C(R)R)
        # C1 has 1H, C2 has 0H. Nucleophile goes to C2.
        f"[CH1:1]=[CH0:2] >> [C:1]-[C:2]-{nu_smarts}",
        
        # 3. Symmetric Ties (Ethene, Disubstituted internal, Tetrasubstituted internal)
        # Yields a mix or identical products. RDKit maps equal probability natively.
        f"[CH2:1]=[CH2:2] >> [C:1]-[C:2]-{nu_smarts}",
        f"[CH1:1]=[CH1:2] >> [C:1]-[C:2]-{nu_smarts}",
        f"[CH0:1]=[CH0:2] >> [C:1]-[C:2]-{nu_smarts}"
    ]

def generate_anti_markovnikov(nu_smarts):
    """
    Generates SMARTS for Anti-Markovnikov addition.
    The Nucleophile adds to the less substituted carbon (more Hydrogens).
    """
    return [
        # 1. Asymmetric: Terminal Alkene
        # C1 has 2H, C2 has 1H or 0H. Nucleophile goes to C1.
        f"[CH2:1]=[CH1,CH0:2] >> [C:1](-{nu_smarts})-[C:2]",
        
        # 2. Asymmetric: Trisubstituted Alkene
        # C1 has 1H, C2 has 0H. Nucleophile goes to C1.
        f"[CH1:1]=[CH0:2] >> [C:1](-{nu_smarts})-[C:2]",
        
        # 3. Symmetric Ties
        f"[CH2:1]=[CH2:2] >> [C:1](-{nu_smarts})-[C:2]",
        f"[CH1:1]=[CH1:2] >> [C:1](-{nu_smarts})-[C:2]",
        f"[CH0:1]=[CH0:2] >> [C:1](-{nu_smarts})-[C:2]"
    ]

# ==========================================
# 3. THE REAGENT DICTIONARY
# ==========================================
ALKENE_RULES = {
    # --- HYDROHALOGENATION ---
    "HBr": {
        "rules": generate_markovnikov("[Br]"),
        "poisons": ["[O]-[O]"],
        "poison_message": "Presence of peroxides triggers a radical mechanism, leading to anti-Markovnikov hydrobromination. Use 'HBr / Peroxide' instead."
    },
    "HCl": {
        "rules": generate_markovnikov("[Cl]") # Peroxide effect does not apply to HCl!
    },
    "HBr / Peroxide (Kharasch Effect)": {
        "rules": generate_anti_markovnikov("[Br]")
    },

    # --- HYDRATION (ALCOHOL SYNTHESIS) ---
    "H2O / H+ (Acid Catalyzed Hydration)": {
        "rules": generate_markovnikov("[OH]")
    },
    "B2H6 / THF, H2O2 / OH- (Hydroboration-Oxidation)": {
        "rules": generate_anti_markovnikov("[OH]")
    },
    
    # --- HALOGENATION (ANTI-ADDITION) ---
    # RDKit will just map the 2D graph, stereochemistry can be added later if needed.
    "Br2 / CCl4 (Test for Unsaturation)": {
        "rules": [
            "[C:1]=[C:2] >> [C:1](-[Br])-[C:2](-[Br])"
        ]
    },
    "Cl2 / CCl4": {
        "rules": [
            "[C:1]=[C:2] >> [C:1](-[Cl])-[C:2](-[Cl])"
        ]
    }
}