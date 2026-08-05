# ==========================================
# AMINES & DIAZONIUM ENGINE (EXHAUSTIVE OLYMPIAD & GRADUATE LEVEL)
# ==========================================

# --- ADVANCED STRUCTURAL CLASSIFICATIONS & POISONS ---
PRIMARY_ALIPHATIC_AMINE = ["[CX4H2,CX4H3]-[NX3H2]"]
SECONDARY_AMINE = ["[NX3H1](-[#6])-[#6]", "[nx3H1]"] 
TERTIARY_AMINE = ["[NX3H0](-[#6])(-[#6])-[#6]"]
TERTIARY_AROMATIC_AMINE = ["[c]1[cH][cH][cH][cH][c]1-[NX3H0](-[#6])-[#6]"]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
AMINE_RULES = {

    # ==========================================
    # 1. AMINE SYNTHESIS & DEGRADATION PROTOCOLS
    # ==========================================

    "Potassium Phthalimide followed by Hydrazine / EtOH (Gabriel Phthalimide Primary Amine Synthesis)": {
        "rules": [
            # Nucleophilic substitution of alkyl halides by potassium phthalimide followed by hydrazinolysis 
            # to selectively synthesize pure primary aliphatic amines without polyalkylation side products.
            "[CX4H2:1]-[Cl,Br,I] >> [C:1]-[NX3H2]"
        ],
        "poisons": ["[CX4H0](-[*])(-[*])(-[*])-[Cl,Br,I]"],
        "poison_message": "Gabriel Phthalimide failure: Tertiary alkyl halides undergo rapid E2 elimination rather than SN2 displacement with phthalimide salts."
    },

    "Br2 / Aqueous NaOH (Hofmann Bromamide Degradation / Carbon Chain Decarbonylation)": {
        "rules": [
            # Conversion of primary unsubstituted amides into primary amines with the net loss 
            # of a single carbonyl carbon atom via an isocyanate intermediate.
            "[#6:1]-[CX3](=O)-[NX3H2] >> [#6:1]-[NX3H2]"
        ],
        "poisons": ["[#6:1]-[CX3](=O)-[NX3H1]-[#6]"],
        "poison_message": "Hofmann degradation failure: Requires an unsubstituted primary amide ($R-CONH_2$). Secondary and tertiary amides lack the necessary N-H protons required to form the bromamide intermediate."
    },

    "Fe / Concentrated HCl or Sn / HCl (Chemoselective Nitro Reduction to Anilines)": {
        "rules": [
            # Reduction of aromatic nitro groups to primary aromatic amines (anilines) 
            # leaving other sensitive functional groups intact.
            "[c:1]-[N+](=O)[O-] >> [c:1]-[NX3H2]"
        ]
    },

    # ==========================================
    # 2. QUALITATIVE AMINE IDENTIFICATION TESTS
    # ==========================================

    "CHCl3 / Alcoholic KOH, Thermal Flash (Carbylamine Isocyanide Test)": {
        "rules": [
            # Primary Aliphatic or Aromatic Amines -> Isocyanides (Carbylamines) characterized by an intensely foul stench.
            # Generated via alpha-elimination of chloroform forming dichlorocarbene followed by nucleophilic attack and dual base elimination.
            "[CX4,c:1]-[NX3H2:2] >> [C:1]-[N+:2]#[C-]"
        ],
        "poisons": SECONDARY_AMINE + TERTIARY_AMINE,
        "poison_message": "Carbylamine Test failure: Strictly specific for primary (1°) amines. Secondary and tertiary amines lack the necessary two N-H protons required to form the intermediate imidoyl chloride/isocyanide network."
    },

    "Benzenesulfonyl Chloride / Aqueous KOH (Hinsberg Separation Test)": {
        "rules": [
            # 1. Primary Amine -> N-alkylbenzenesulfonamide (Contains acidic remaining N-H, dissolving clear in aqueous alkali)
            "[CX4:1]-[NX3H2:2] >> [c]1[cH][cH][cH][cH][cH]1-C(=O)-[NH1:2]-[C:1]", 
            
            # 2. Secondary Amine -> N,N-dialkylbenzenesulfonamide (Lacks acidic N-H; remains as an insoluble solid precipitate in alkali)
            "[#6:1]-[NX3H1:2]-[#6:3] >> [c]1[cH][cH][cH][cH][cH]1-C(=O)-[N:2](-[#6:1])-[#6:3]"
        ],
        "poisons": TERTIARY_AMINE,
        "poison_message": "Hinsberg test failure: Tertiary amines cannot react to form sulfonamides because they lack an N-H bond; they remain completely unreactive and insoluble until treated with mineral acid."
    },

    # ==========================================
    # 3. NITROUS ACID BIFURCATION & DIAZOTIZATION CASCADE
    # ==========================================

    "NaNO2 / Aqueous HCl, 0-5°C (Nitrosation & Diazotization Cascade)": {
        "rules": [
            # 1. Aromatic Primary Amines -> Stable Aromatic Diazonium Salts (via resonance-stabilized diazo transition states)
            "[c:1]-[NX3H2] >> [c:1]-[N+]#[N]",
            
            # 2. Aliphatic Primary Amines -> Unstable Aliphatic Diazonium Intermediates collapsing to Carbocations (Yielding Alcohols/Alkenes)
            "[CX4:1]-[NX3H2] >> [C:1]-[OH]",
            
            # 3. Secondary Amines (Aliphatic or Aromatic) -> N-Nitrosamines (Yellow oily liquids or crystalline solids)
            "[#6,c:1]-[NX3H1:2]-[#6,c:3] >> [#6,c:1]-[N:2](-[#6,c:3])-[N]=O",

            # 4. Tertiary Aromatic Amines (e.g., N,N-Dimethylaniline) -> Para-Nitrosation via Electrophilic Aromatic Substitution (NO+ attack)
            "[c:1]1[cH][cH][c](-[NX3H0](-[#6])-[#6])[cH][cH]1 >> [c:1]1[cH][c](-[N]=O)[c](-[NX3H0](-[#6])-[#6])[cH][cH]1"
        ]
    },

    # ==========================================
    # 4. DIAZONIUM TRANSFORMATIONS & DISPLACEMENT PATHWAYS
    # ==========================================

    "CuCl / HCl (Sandmeyer Chlorination)": {
        "rules": [
            # Radical-mediated atom transfer converting aromatic diazonium salts into aryl chlorides
            "[c:1]-[N+]#[N] >> [c:1]-[Cl]"
        ],
        "poisons": ["[CX4]-[N+]#[N]"],
        "poison_message": "Sandmeyer failure: Aliphatic diazonium matrices spontaneously fragment into reactive carbocations and nitrogen gas long before copper catalysis can intervene."
    },
    
    "CuBr / HBr (Sandmeyer Bromination)": {
        "rules": [
            "[c:1]-[N+]#[N] >> [c:1]-[Br]"
        ]
    },

    "CuCN / KCN (Sandmeyer Cyanation - Carbon Chain Step-Up)": {
        "rules": [
            "[c:1]-[N+]#[N] >> [c:1]-C#N"
        ]
    },
    
    "Copper Powder / HCl or HBr (Gattermann Halogenation)": {
        "rules": [
            # Alternative copper powder catalysis yielding aryl halides under modified conditions
            "[c:1]-[N+]#[N] >> [c:1]-[Cl]"
        ]
    },

    "KI / Ambient Warmth (Aromatic Iodination)": {
        "rules": [
            # Iodide acts directly as a nucleophile without requiring transition metal copper catalysts
            "[c:1]-[N+]#[N] >> [c:1]-[I]"
        ]
    },

    "HBF4 followed by Thermal Decomposition (Balz-Schiemann Fluorination)": {
        "rules": [
            # Precipitation of stable aryl diazonium tetrafluoroborate salts followed by thermal pyrolysis to yield aryl fluorides
            "[c:1]-[N+]#[N] >> [c:1]-[F]"
        ]
    },

    "Warm H2O / Acid Hydrolysis (Diazonium Phenol Synthesis)": {
        "rules": [
            # Nucleophilic displacement of nitrogen gas by water yielding substituted phenols
            "[c:1]-[N+]#[N] >> [c:1]-[OH]"
        ]
    },

    "H3PO2 / H2O or Absolute Ethanol (Reductive Deamination Eraser)": {
        "rules": [
            # Hydrogen atom abstraction reducing the diazonium group cleanly back down to an unsubstituted C-H aromatic vertex
            "[c:1]-[N+]#[N] >> [c:1]"
        ]
    },

    # ==========================================
    # 5. DIAZONIUM ELECTROPHILIC AROMATIC COUPLING
    # ==========================================

    "Activated Ring / Controlled pH (Azo Dye Coupling)": {
        "rules": [
            # Electrophilic aromatic substitution where the terminal nitrogen of the diazonium ion attacks 
            # the para-position of strongly activated rings (phenols under basic conditions or anilines under acidic conditions).
            "[c:1]-[N+]#[N].[c:2]1[cH][cH][cH][cH][cH]1 >> [c:1]-[N]=[N]-[c:2]1[cH][cH][cH][cH][cH]1"
        ]
    }
}