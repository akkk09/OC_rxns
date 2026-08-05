# ==========================================
# ALKYNE ENGINE (HYDRATION, REDUCTION, ACIDITY)
# ==========================================

def generate_kucherov_hydration():
    return [
        "[C:1]#[CH1:2] >> [C:1](=O)-[C:2]",
        "[CH0:1]#[CH0:2] >> [C:1](=O)-[C:2]"
    ]

def generate_hydroboration_oxidation():
    return [
        "[C:1]#[CH1:2] >> [C:1]-[C:2]=O",
        "[CH0:1]#[CH0:2] >> [C:1](=O)-[C:2]"
    ]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
ALKYNE_RULES = {
    
    # --- HYDRATION (BUILT-IN TAUTOMERIZATION) ---
    "HgSO4 / H2SO4 (Kucherov Reaction)": {
        "rules": generate_kucherov_hydration()
    },
    "B2H6 / THF, H2O2 / OH- (Alkyne Hydroboration)": {
        "rules": generate_hydroboration_oxidation()
    },
    
    # --- REDUCTION (WITH STRICT STEREOCHEMISTRY) ---
    "H2 / Lindlar Catalyst": {
        "rules": [
            # 1. Internal Alkynes -> CIS Alkene (Syn-addition)
            # Uses directional bonds ( / and \ ) to force substituents to the same side.
            "[#6:1]-[C:2]#[C:3]-[#6:4] >> [#6:1]/[CH1:2]=[CH1:3]\[#6:4]",
            
            # 2. Terminal Alkynes -> Standard Terminal Alkene (No stereochemistry possible)
            "[#6:1]-[C:2]#[CH1:3] >> [#6:1]-[CH1:2]=[CH2:3]"
        ]
    },
    "Na / Liquid NH3 (Birch Reduction)": {
        "rules": [
            # 1. Internal Alkynes -> TRANS Alkene (Anti-addition)
            # Uses directional bonds ( / and / ) to force substituents to opposite sides.
            "[#6:1]-[C:2]#[C:3]-[#6:4] >> [#6:1]/[CH1:2]=[CH1:3]/[#6:4]"
        ],
        # THE ACID-BASE TRAP (Terminal Alkynes)
        "poisons": ["[CH1]#[C]"], 
        "poison_message": "Terminal alkynes possess an acidic hydrogen. Na/NH3 acts as a strong base here, performing an acid-base reaction to form a sodium acetylide rather than reducing the bond!"
    },
    "H2 / Ni (Complete Hydrogenation)": {
        "rules": [
            "[C:1]#[C:2] >> [C:1]-[C:2]"
        ]
    },

    # --- TERMINAL ALKYNE TESTS (ACIDITY) ---
    "NaNH2 (Sodium Amide)": {
        "rules": [
            "[C:1]#[CH1:2] >> [C:1]#[C:2]-[Na]"
        ]
    },
    "Tollens' Reagent (AgNO3 / NH4OH)": {
        "rules": [
            "[C:1]#[CH1:2] >> [C:1]#[C:2]-[Ag]" 
        ]
    }
}