# ==========================================
# POLYMERS & PRACTICAL ORGANIC CHEMISTRY (POC) ENGINE (EXHAUSTIVE OLYMPIAD & GRADUATE LEVEL)
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
    # 1. PRACTICAL ORGANIC CHEMISTRY (QUALITATIVE TESTS)
    # ==========================================

    "Ph-SO2Cl / Aqueous Alkali (Hinsberg Amine Separation Test)": {
        "rules": [
            # 1. Primary Amines -> N-Alkylbenzenesulfonamide (Soluble in alkali due to acidic remaining N-H proton)
            "[c]-[S](=O)(=O)[Cl].[NX3H2:1]-[#6:2] >> [c]-[S](=O)(=O)-[NH1:1]-[#6:2]",
            
            # 2. Secondary Amines -> N,N-Dialkylbenzenesulfonamide (Insoluble precipitate in alkali, lacks N-H proton)
            "[c]-[S](=O)(=O)[Cl].[NX3H1:1](-[#6:2])-[#6:3] >> [c]-[S](=O)(=O)-[N:1](-[#6:2])-[#6:3]"
        ],
        "poisons": TERTIARY_AMINES,
        "poison_message": "Hinsberg test failure: Tertiary amines completely lack the N-H protons required to react with benzenesulfonyl chloride. They remain unreacted as free amines and dissolve only upon addition of mineral acid."
    },

    "2,4-DNP / Acid Catalyst (Brady's Reagent for Carbonyl Detection)": {
        "rules": [
            # Aldehydes and Ketones form characteristic yellow, orange, or red 2,4-dinitrophenylhydrazone precipitates
            "[CX3:1]=O >> [C:1]=N-[NH]-[c]1[cH][c](-[N+](=O)[O-])[cH][c](-[N+](=O)[O-])[cH]1"
        ],
        "poisons": ["[CX3](=O)[OH]", "[CX3](=O)-[O]-[#6]", "[CX3](=O)-[NX3]"], 
        "poison_message": "Brady's test failure: 2,4-DNP specifically targets aldehydes and ketones via nucleophilic addition-elimination. Carboxylic acids, esters, and amides fail to react due to resonance stabilization of the carbonyl carbon."
    },

    "Neutral FeCl3 (Phenol Chromogenic Complex Test)": {
        "rules": [
            # Phenols form intensely colored (typically violet, green, or red) iron(III)-phenoxide coordination complexes
            "[c:1]-[OH] >> [c:1]-[O-]-[Fe+3]"
        ],
        "poisons": NON_PHENOLS,
        "poison_message": "Neutral FeCl3 test failure: Standard aliphatic alcohols do not yield colored complexes. This diagnostic test is specifically tailored for phenolic and enolic structural motifs."
    },

    "Victor Meyer Sequence / P-I2, AgNO2, HNO2, NaOH (Alcohol Classification Test)": {
        "rules": [
            # Primary Alcohols -> Blood-red color via nitrolic acid salt formation
            "[CX4H2,CX4H3:1]-[OH] >> [C:1](=N-[O-])-[N+](=O)[O-]",
            
            # Secondary Alcohols -> Deep blue color via pseudonitrole formation
            "[CX4H1:1](-[#6])(-[#6])-[OH] >> [C:1](-[N]=O)-[N+](=O)[O-]"
        ],
        "poisons": TERTIARY_ALCOHOLS,
        "poison_message": "Victor Meyer test failure: Tertiary alcohols fail to yield color because, although they convert to tertiary nitroalkanes, they lack the required alpha-hydrogen needed to react with nitrous acid (HNO2) in the third step, remaining colorless."
    },

    # ==========================================
    # 2. POLYMERIZATION & MACROMOLECULAR SYNTHESIS
    # ==========================================

    "Ziegler-Natta Catalyst / Organometallic Initiation (Chain-Growth Polyolefin Synthesis)": {
        "rules": [
            # Converts alkenes to addition polymers using coordination-insertion catalysts.
            # Dummy atoms (*) mathematically represent infinite chain continuation vectors.
            "[C:1]=[C:2] >> *-[C:1]-[C:2]-*"
        ]
    },

    "Thermal Condensation / High Pressure (Step-Growth Polyamide & Polyester Synthesis)": {
        "rules": [
            # 1. Polyamides (e.g., Nylon-6,6 / Nylon-6 step-growth condensation)
            "[OH]-[C:1](=O)-[#6:2]-[C:3](=O)-[OH].[NH2:4]-[#6:5]-[NH2:6] >> *-[C:1](=O)-[#6:2]-[C:3](=O)-[NH:4]-[#6:5]-[NH:6]-*",
            
            # 2. Polyesters (e.g., Terylene / Dacron step-growth condensation)
            "[OH]-[C:1](=O)-[#6,c:2]-[C:3](=O)-[OH].[OH]-[CX4:4]-[CX4:5]-[OH] >> *-[C:1](=O)-[#6,c:2]-[C:3](=O)-[O]-[C:4]-[C:5]-[O]-*"
        ]
    },

    "Free Radical Initiation / Peroxides (Diene Copolymerization to Synthetic Rubbers)": {
        "rules": [
            # Conjugated diene polymerization mapping for synthetic rubber formulations (e.g., Buna-S / Neoprene precursors)
            "[#6:1]=[C:2]-[C:3]=[C:4] >> *-[C:1]-[C:2]=[C:3]-[C:4]-*"
        ]
    }
}