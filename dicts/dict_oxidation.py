# ==========================================
# OXIDATION ENGINE (OZONOLYSIS & CLEAVAGE)
# ==========================================

# --- 1. Reductive Ozonolysis ---
# Cleaves C=C to Carbonyls (Aldehydes/Ketones)
# RDKit's auto-valency handles the hydrogens perfectly. 
# =CH2 becomes Formaldehyde, =CH- becomes Aldehyde, =C< becomes Ketone.
REDUCTIVE_OZONOLYSIS = [
    # Alkene Cleavage (Uses uppercase C to avoid aromatic bonds)
    "[C:1]=[C:2] >> [C:1]=O.[C:2]=O",
    
    # Alkyne Cleavage (Yields 1,2-dicarbonyls without carbon-carbon bond breaking)
    "[C:1]#[C:2] >> [C:1](=O)-[C:2](=O)"
]

# --- 2. Oxidative Ozonolysis & Hot KMnO4 ---
# Cleaves C=C and aggressively oxidizes aldehydes to Carboxylic Acids,
# and formaldehyde completely to Carbon Dioxide (CO2).
OXIDATIVE_CLEAVAGE = [
    # ALKENE COMBINATIONS based on Hydrogen count:
    # 1. Ketone + Ketone (Tetrasubstituted)
    "[CH0:1]=[CH0:2] >> [C:1]=O.[C:2]=O",
    
    # 2. Ketone + Carboxylic Acid (Trisubstituted)
    "[CH0:1]=[CH1:2] >> [C:1]=O.[OH]-[C:2]=O",
    
    # 3. Ketone + CO2 (Disubstituted, terminal)
    "[CH0:1]=[CH2:2] >> [C:1]=O.O=C=O",
    
    # 4. Acid + Acid (Disubstituted, internal)
    "[CH1:1]=[CH1:2] >> [OH]-[C:1]=O.[OH]-[C:2]=O",
    
    # 5. Acid + CO2 (Monosubstituted, terminal)
    "[CH1:1]=[CH2:2] >> [OH]-[C:1]=O.O=C=O",
    
    # 6. CO2 + CO2 (Unsubstituted, Ethene)
    "[CH2:1]=[CH2:2] >> O=C=O.O=C=O",
    
    # ALKYNE CLEAVAGE:
    # 7. Acid + Acid (Internal Alkyne)
    "[CH0:1]#[CH0:2] >> [OH]-[C:1]=O.[OH]-[C:2]=O",
    
    # 8. Acid + CO2 (Terminal Alkyne)
    "[CH0:1]#[CH1:2] >> [OH]-[C:1]=O.O=C=O"
]

# ==========================================
# 3. THE REAGENT DICTIONARY
# ==========================================
OXIDATION_RULES = {
    
    # --- REDUCTIVE ---
    "O3 / Zn, H2O (Reductive Ozonolysis)": {
        "rules": REDUCTIVE_OZONOLYSIS
    },
    "O3 / DMS (Reductive Ozonolysis)": {
        "rules": REDUCTIVE_OZONOLYSIS
    },
    
    # --- OXIDATIVE ---
    "O3 / H2O2 (Oxidative Ozonolysis)": {
        "rules": OXIDATIVE_CLEAVAGE
    },
    "Hot KMnO4 / OH- / Heat (Oxidative Cleavage)": {
        "rules": OXIDATIVE_CLEAVAGE
    },
    
    # --- ALCOHOL OXIDATIONS (Bonus coverage) ---
    "PCC / CH2Cl2 (Mild Oxidation)": {
        "rules": [
            "[CH2:1]-[OH] >> [C:1]=O",  # 1-deg alcohol to Aldehyde
            "[CH1:1]-[OH] >> [C:1]=O"   # 2-deg alcohol to Ketone
        ],
        "poisons": ["[CH0]-[OH]"],
        "poison_message": "Tertiary alcohols resist oxidation due to the lack of an alpha-hydrogen."
    },
    "KMnO4 / H+ (Strong Oxidation)": {
        "rules": [
            "[CH2:1]-[OH] >> [OH]-[C:1]=O",  # 1-deg alcohol straight to Carboxylic Acid
            "[CH1:1]-[OH] >> [C:1]=O"        # 2-deg alcohol to Ketone
        ],
        "poisons": ["[CH0]-[OH]"],
        "poison_message": "Tertiary alcohols resist oxidation under normal conditions."
    }
}