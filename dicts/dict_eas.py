# ==========================================
# EAS ENGINE (EXHAUSTIVE OLYMPIAD & GRADUATE LEVEL)
# ==========================================

# --- FRIEDEL-CRAFTS POISONS (THE JEE TRAPS) ---
# 1. Strongly deactivated rings cannot undergo Friedel-Crafts reactions.
STRONGLY_DEACTIVATED = [
    "[c]-[N+](=O)[O-]",     # Nitrobenzene
    "[c]-C#N",              # Benzonitrile
    "[c]-[CX3](=O)[OH]",    # Benzoic acid
    "[c]-[CX3](=O)[#6]",    # Phenyl ketones
    "[c]-[CX4](F)(F)F"      # Trifluoromethylbenzene
]

# 2. Lewis Base Trap: Amines complex with AlCl3, turning an activating 
# -NH2 group into a strongly deactivating -NH2AlCl3(-) group!
LEWIS_BASE_AMINES = [
    "[c]-[NX3H2]",          # Aniline
    "[c]-[NX3H1]-[#6]",     # N-Methylaniline
    "[c]-[NX3H0](-[#6])-[#6]" # N,N-Dimethylaniline
]

FC_POISONS = STRONGLY_DEACTIVATED + LEWIS_BASE_AMINES

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
EAS_RULES = {

    # ==========================================
    # 1. NITRATION & SULFONATION PATHWAYS
    # ==========================================

    "Conc. HNO3 / Conc. H2SO4 (Aromatic Nitration via Nitronium Ion)": {
        "rules": [
            # The backend GOC engine isolates the correct [cH1] based on directing groups.
            # This rule executes the transformation on that targeted carbon.
            "[c:1][cH1:2] >> [c:1][c:2]-[N+](=O)[O-]"
        ]
    },
    
    "Fuming H2SO4 / SO3 (Reversible Aromatic Sulfonation)": {
        "rules": [
            # Generates the benzenesulfonic acid derivative
            "[c:1][cH1:2] >> [c:1][c:2]-[S](=O)(=O)[OH]"
        ]
    },
    
    "Dil. H2SO4 / Heat (Aromatic Desulfonation Eraser)": {
        "rules": [
            # The "Eraser": Removes the sulfonic acid group (reverse EAS)
            "[c:1][c:2]-[S](=O)(=O)[OH] >> [c:1][cH1:2]"
        ]
    },

    # ==========================================
    # 2. HALOGENATION PATHWAYS
    # ==========================================

    "Cl2 / FeCl3 or AlCl3 (Electrophilic Chlorination)": {
        "rules": [
            "[c:1][cH1:2] >> [c:1][c:2]-[Cl]"
        ]
    },
    
    "Br2 / FeBr3 (Electrophilic Bromination)": {
        "rules": [
            "[c:1][cH1:2] >> [c:1][c:2]-[Br]"
        ]
    },

    "I2 / Aqueous HNO3 (Direct Aromatic Iodination via Oxidative Coupling)": {
        "rules": [
            # Iodination requires an oxidizing agent (like HNO3) to consume the HI byproduct and shift equilibrium forward
            "[c:1][cH1:2] >> [c:1][c:2]-[I]"
        ]
    },
    
    "Br2 / H2O (Phenol / Aniline Exhaustive 2,4,6-Tribromination)": {
        "rules": [
            # Highly activated rings without a Lewis Acid catalyst undergo rapid 2,4,6-tribromination
            "[c:1](-[OH,NH2])[cH1:2][cH0,cH1:3][cH1:4][cH0,cH1:5][cH1:6] >> [c:1](-[OH,NH2])[c:2](-[Br])[c:3][c:4](-[Br])[c:5][c:6](-[Br])"
        ],
        "poisons": ["[c]-[N+](=O)[O-]", "[c]-[CH3]"],
        "poison_message": "Exhaustive halogenation in aqueous medium strictly requires a highly activating group like -OH or -NH2. Standard or deactivated rings will not react without a Lewis acid catalyst."
    },

    # ==========================================
    # 3. FRIEDEL-CRAFTS ALKYLATION & ACYLATION
    # ==========================================

    "CH3Cl / Anhydrous AlCl3 (Friedel-Crafts Alkylation)": {
        "rules": [
            "[c:1][cH1:2] >> [c:1][c:2]-[CH3]"
        ],
        "poisons": FC_POISONS,
        "poison_message": "Friedel-Crafts Alkylation failed! If the ring is strongly deactivated (e.g., Nitrobenzene), the electrophile is too weak to attack. If the ring has an amine (e.g., Aniline), the nitrogen lone pair complexes with the AlCl3 catalyst, deactivating the ring instantly."
    },
    
    "CH3COCl / Anhydrous AlCl3 (Friedel-Crafts Acylation)": {
        "rules": [
            # Attaches an acetyl group to form a phenyl ketone
            "[c:1][cH1:2] >> [c:1][c:2]-[C](=O)[CH3]"
        ],
        "poisons": FC_POISONS,
        "poison_message": "Friedel-Crafts Acylation failed! Deactivated rings lack the electron density to attack the acylium ion, and anilines will destroy your Lewis acid catalyst."
    },

    # ==========================================
    # 4. REDUCTIVE MODIFICATIONS
    # ==========================================

    "Zn(Hg) / Conc. HCl - Clemmensen Reduction (Acyl Phenyl Ketone to Alkylbenzene)": {
        "rules": [
            # Cleans up phenyl ketones from FC acylation down to alkyl groups under acidic conditions
            "[c:1]-[CX3](=O)-[CH3] >> [c:1]-[CH2]-[CH3]"
        ]
    }
}