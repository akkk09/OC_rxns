# ==========================================
# POLYMERS & PRACTICAL ORGANIC CHEMISTRY (POC) ENGINE
# ==========================================

# --- POC TRAPS & POISONS ---
TERTIARY_AMINES = ["[NX3H0](-[#6])(-[#6])-[#6]", "[nx3H0]"]
TERTIARY_ALCOHOLS = ["[CX4H0]-[OH]"]
NON_PHENOLS = ["[CX4]-[OH]"]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
POLYMERS_POC_RULES = {

    # ==========================================
    # 1. PRACTICAL ORGANIC CHEMISTRY (TESTS)
    # ==========================================

    # --- THE HINSBERG TEST (Amine Separation) ---
    "Ph-SO2Cl (Hinsberg Reagent)": {
        "rules": [
            # 1-degree Amines -> N-Alkylbenzenesulfonamide (Soluble in alkali due to remaining N-H proton)
            "[c]-[S](=O)(=O)[Cl].[NX3H2:1]-[#6:2] >> [c]-[S](=O)(=O)-[NH1:1]-[#6:2]",
            
            # 2-degree Amines -> N,N-Dialkylbenzenesulfonamide (Insoluble in alkali, lacks N-H proton)
            "[c]-[S](=O)(=O)[Cl].[NX3H1:1](-[#6:2])-[#6:3] >> [c]-[S](=O)(=O)-[N:1](-[#6:2])-[#6:3]"
        ],
        "poisons": TERTIARY_AMINES,
        "poison_message": "Tertiary amines completely lack the N-H protons required to react with benzenesulfonyl chloride (Hinsberg reagent). They remain unreacted and dissolve only in acids!"
    },

    # --- BRADY'S REAGENT (Carbonyl Detection) ---
    "2,4-DNP / H+ (Brady's Reagent)": {
        "rules": [
            # Both Aldehydes and Ketones form a yellow/orange/red 2,4-Dinitrophenylhydrazone precipitate
            "[CX3:1]=O >> [C:1]=N-[NH]-[c]1[cH][c](-[N+](=O)[O-])[cH][c](-[N+](=O)[O-])[cH]1"
        ],
        "poisons": ["[CX3](=O)[OH]", "[CX3](=O)-[O]-[#6]", "[CX3](=O)-[NX3]"], # Acids, Esters, Amides
        "poison_message": "Brady's reagent (2,4-DNP) strictly tests for aldehydes and ketones. Carboxylic acids and their derivatives do not form hydrazones due to resonance stabilization of the carbonyl!"
    },

    # --- NEUTRAL FeCl3 (Phenol Detection) ---
    "Neutral FeCl3": {
        "rules": [
            # Phenols form a brilliantly colored (usually violet) ferric-phenoxide complex
            # For the simulator, we map the phenoxide directly to the Iron(III) center
            "[c:1]-[OH] >> [c:1]-[O-]-[Fe+3]"
        ],
        "poisons": NON_PHENOLS,
        "poison_message": "Standard aliphatic alcohols do not give a positive Neutral FeCl3 test. This test is highly specific for the enol/phenol structural motif!"
    },

    # --- VICTOR MEYER TEST (Alcohol Degree) ---
    # Multi-step Macro: P/I2 -> AgNO2 -> HNO2 -> NaOH
    "Victor Meyer Sequence (Macro)": {
        "rules": [
            # 1-degree Alcohols -> Blood Red Color (Nitrolic Acid Salt)
            "[CX4H2,CX4H3:1]-[OH] >> [C:1](=N-[O-])-[N+](=O)[O-]",
            
            # 2-degree Alcohols -> Blue Color (Pseudonitrole)
            "[CX4H1:1](-[#6])(-[#6])-[OH] >> [C:1](-[N]=O)-[N+](=O)[O-]"
        ],
        "poisons": TERTIARY_ALCOHOLS,
        "poison_message": "Tertiary alcohols fail the Victor Meyer test! They convert to tertiary alkyl halides and then tertiary nitroalkanes, but they lack the alpha-hydrogen required to react with Nitrous Acid (HNO2) in the third step, remaining COLORLESS."
    },


    # ==========================================
    # 2. POLYMERIZATION ENGINE
    # ==========================================

    # --- ADDITION POLYMERS ---
    "Ziegler-Natta Catalyst / Heat (Polyolefins)": {
        "rules": [
            # Converts Alkenes to Polymers.
            # The '*' dummy atoms mathematically denote the infinite chain continuation.
            "[C:1]=[C:2] >> *-[C:1]-[C:2]-*"
        ]
    },

    # --- CONDENSATION POLYMERS ---
    "Heat / High Pressure (Condensation / Nylon / Dacron)": {
        "rules": [
            # 1. Polyamides (Nylon-6,6 / Nylon-6)
            # Diacid + Diamine -> Amide linkages with infinite chain endpoints
            "[OH]-[C:1](=O)-[#6:2]-[C:3](=O)-[OH].[NH2:4]-[#6:5]-[NH2:6] >> *-[C:1](=O)-[#6:2]-[C:3](=O)-[NH:4]-[#6:5]-[NH:6]-*",
            
            # 2. Polyesters (Terylene / Dacron)
            # Diacid + Diol -> Ester linkages with infinite chain endpoints
            "[OH]-[C:1](=O)-[#6,c:2]-[C:3](=O)-[OH].[OH]-[CX4:4]-[CX4:5]-[OH] >> *-[C:1](=O)-[#6,c:2]-[C:3](=O)-[O]-[C:4]-[C:5]-[O]-*"
        ]
    }
}