# ==========================================
# OXIDATION ENGINE (EXHAUSTIVE OLYMPIAD & GRADUATE LEVEL)
# ==========================================

# --- 1. REDUCTIVE OZONOLYSIS ---
# Cleaves C=C and C#C pi systems to corresponding carbonyls (aldehydes, ketones, and 1,2-dicarbonyls)
# without over-oxidizing to carboxylic acids.
REDUCTIVE_OZONOLYSIS = [
    # Alkene Cleavage (Uppercase C distinguishes aliphatic from aromatic rings)
    "[C:1]=[C:2] >> [C:1]=O.[C:2]=O",
    
    # Alkyne Cleavage (Yields 1,2-dicarbonyls without carbon-carbon single bond scission)
    "[C:1]#[C:2] >> [C:1](=O)-[C:2](=O)"
]

# --- 2. OXIDATIVE CLEAVAGE (OZONOLYSIS WORKUP & HOT KMnO4) ---
# Aggressive cleavage of C=C and C#C bonds, converting aldehydes to carboxylic acids 
# and terminal unsubstituted carbons completely down to carbon dioxide (CO2).
OXIDATIVE_CLEAVAGE = [
    # ALKENE CLEAVAGE COMBINATIONS (substituent-dependent hydrogen tracking):
    # 1. Tetrasubstituted Alkene -> Two Ketones
    "[CH0:1]=[CH0:2] >> [C:1]=O.[C:2]=O",
    
    # 2. Trisubstituted Alkene -> Ketone + Carboxylic Acid
    "[CH0:1]=[CH1:2] >> [C:1]=O.[OH]-[C:2]=O",
    
    # 3. Disubstituted Terminal Alkene (Geminal) -> Ketone + CO2
    "[CH0:1]=[CH2:2] >> [C:1]=O.O=C=O",
    
    # 4. Disubstituted Internal Alkene -> Two Carboxylic Acids
    "[CH1:1]=[CH1:2] >> [OH]-[C:1]=O.[OH]-[C:2]=O",
    
    # 5. Monosubstituted Terminal Alkene -> Carboxylic Acid + CO2
    "[CH1:1]=[CH2:2] >> [OH]-[C:1]=O.O=C=O",
    
    # 6. Unsubstituted Ethene -> Two Equivalents of CO2
    "[CH2:1]=[CH2:2] >> O=C=O.O=C=O",
    
    # ALKYNE CLEAVAGE COMBINATIONS:
    # 7. Internal Alkyne -> Two Carboxylic Acids
    "[CH0:1]#[CH0:2] >> [OH]-[C:1]=O.[OH]-[C:2]=O",
    
    # 8. Terminal Alkyne -> Carboxylic Acid + CO2
    "[CH0:1]#[CH1:2] >> [OH]-[C:1]=O.O=C=O"
]

# ==========================================
# 3. THE REAGENT DICTIONARY
# ==========================================
OXIDATION_RULES = {
    
    # ==========================================
    # A. REDUCTIVE CLEAVAGE PATHWAYS
    # ==========================================

    "O3 / Zn, H2O or DMS (Reductive Ozonolysis)": {
        "rules": REDUCTIVE_OZONOLYSIS
    },
    
    # ==========================================
    # B. OXIDATIVE CLEAVAGE PATHWAYS
    # ==========================================

    "O3 / Aqueous H2O2 (Oxidative Ozonolysis)": {
        "rules": OXIDATIVE_CLEAVAGE
    },
    
    "Hot Aqueous KMnO4 / OH- / Thermal Reflux (Harsh Oxidative Cleavage)": {
        "rules": OXIDATIVE_CLEAVAGE
    },
    
    # ==========================================
    # C. ALCOHOL OXIDATION & SELECTIVITY PROTOCOLS
    # ==========================================

    "PCC / Anhydrous CH2Cl2 (Mild Pyridinium Chlorochromate Oxidation)": {
        "rules": [
            "[CH2:1]-[OH] >> [C:1]=O",  # Primary alcohols -> Aldehydes (stops at aldehyde stage)
            "[CH1:1]-[OH] >> [C:1]=O"    # Secondary alcohols -> Ketones
        ],
        "poisons": ["[CH0]-[OH]"],
        "poison_message": "Alcohol oxidation failure: Tertiary alcohols resist oxidation under mild and strong conditions due to the absolute lack of an alpha-hydrogen atom."
    },
    
    "KMnO4 / Aqueous H+ or Jones Reagent CrO3 / H2SO4 (Strong Acidic Oxidation)": {
        "rules": [
            "[CH2:1]-[OH] >> [OH]-[C:1]=O",  # Primary alcohols -> Carboxylic Acids (exhaustive oxidation)
            "[CH1:1]-[OH] >> [C:1]=O"         # Secondary alcohols -> Ketones
        ],
        "poisons": ["[CH0]-[OH]"],
        "poison_message": "Strong oxidation failure: Tertiary alcohols lack the enolizable alpha-hydrogen required for chromium or permanganate-mediated bond cleavage."
    }
}