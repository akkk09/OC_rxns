# ==========================================
# CARBOXYLIC ACIDS & DERIVATIVES ENGINE (EXHAUSTIVE OLYMPIAD & GRADUATE LEVEL)
# ==========================================

# --- ADVANCED STRUCTURAL POISONS & CLASSIFICATIONS ---
NO_ALPHA_H = ["[CX4H0]-[CX3](=O)[OH]", "[c]-[CX3](=O)[OH]"] # Tertiary or aromatic acids lacking alpha-hydrogens
SUBSTITUTED_AMIDES = ["[CX3](=O)-[NX3H1]", "[CX3](=O)-[NX3H0]"] # Secondary and tertiary amides lacking unsubstituted NH2
CARBOXYLIC_ACID_ONLY = ["[CX3](=O)-[OH]"]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
CARBOXYLIC_RULES = {

    # ==========================================
    # 1. ACID HALIDES & DERIVATIVE SYNTHESIS
    # ==========================================

    "SOCl2 / Pyridine or PCl5 (Thionyl Chloride Conversion to Acid Chlorides)": {
        "rules": [
            # Converts Carboxylic Acids to highly reactive Acid Chlorides via chlorosulfite intermediates
            "[CX3:1](=O)[OH] >> [C:1](=O)[Cl]",
            
            # Alcohol conversion component: clean transformation of alcohols to alkyl chlorides via SN2
            "[CX4:1]-[OH] >> [C:1]-[Cl]"
        ]
    },

    "PCl3 / Thermal Conditions (Phosphorus Trichloride Acid Chlorination)": {
        "rules": [
            # Conversion of 3 equivalents of carboxylic acid per 1 equivalent of PCl3 into acid chlorides
            "[CX3:1](=O)[OH] >> [C:1](=O)[Cl]"
        ]
    },

    # ==========================================
    # 2. ESTERIFICATION & TRANSESTERIFICATION
    # ==========================================

    "Anhydrous Alcohol / Catalytic H2SO4, Reflux (Fischer Esterification Equilibrium)": {
        "rules": [
            # Bimolecular acid-catalyzed condensation: Carboxylic Acid + Alcohol -> Ester + Water
            "[CX3:1](=O)[OH].[CX4,c:2]-[OH] >> [C:1](=O)-[O]-[C,c:2]"
        ]
    },

    "Excess Alcohol / Base or Acid Catalyst (Transesterification)": {
        "rules": [
            # Exchange of alkoxy groups between an existing ester and a new alcohol solvent matrix
            "[CX3:1](=O)-[OX2]-[CX4:2].[CX4,c:3]-[OH] >> [C:1](=O)-[O]-[C,c:3]"
        ]
    },

    # ==========================================
    # 3. DECARBOXYLATION PATHWAYS (CHAIN STEP-DOWN)
    # ==========================================

    "NaOH / CaO, Thermal Fusion (Soda-Lime Decarboxylation)": {
        "rules": [
            # Harsh thermal elimination of carboxylate groups, replacing them with a carbon-hydrogen bond
            "[#6,c:1]-[CX3](=O)[OH,O-] >> [#6,c:1]"
        ]
    },

    "Mild Thermal Heating (Beta-Keto Acid Decarboxylation via Cyclic Transition State)": {
        "rules": [
            # Strictly requires a beta-carbonyl or beta-dicarbonyl group to stabilize the six-membered cyclic transition state,
            # expelling carbon dioxide and generating a substituted ketone.
            "[CX3:1](=O)-[CX4:2]-[CX3](=O)[OH] >> [C:1](=O)-[C:2]"
        ],
        "poisons": ["[CX4]-[CX3](=O)[OH]", "[c]-[CX3](=O)[OH]"], 
        "poison_message": "Decarboxylation failure: Standard carboxylic acids do not decarboxylate under mild heat. This transformation requires a beta-carbonyl partner to facilitate a cyclic concerted transition state."
    },

    "Ag2O / Br2 in CCl4 (Hunsdiecker Radical Decarboxylative Halogenation)": {
        "rules": [
            # Conversion of carboxylic acid silver salts into alkyl/aryl bromides with carbon chain step-down via CO2 loss
            "[#6:1]-[CX3](=O)-[O-][Ag+] >> [#6:1]-[Br]"
        ]
    },

    # ==========================================
    # 4. ALPHA-HALOGENATION (HVZ REACTION)
    # ==========================================

    "Br2 / Red Phosphorus (Hell-Volhard-Zelinsky Alpha-Bromination)": {
        "rules": [
            # In-situ generation of acyl bromides via phosphorus tribromide followed by rapid enolization 
            # and alpha-bromination of carboxylic acids.
            "[CX4H1,CX4H2,CX4H3:1]-[CX3](=O)[OH:2] >> [C:1](-[Br])-[C](=O)[OH:2]"
        ],
        "poisons": NO_ALPHA_H,
        "poison_message": "HVZ Reaction failure: Strictly requires at least one enolizable alpha-hydrogen. Acids like pivalic acid or benzoic acid completely fail to react."
    },

    # ==========================================
    # 5. AMIDE DEGRADATION & REDUCTIVE PATHWAYS
    # ==========================================

    "Br2 / Aqueous NaOH (Hofmann Bromamide Degradation)": {
        "rules": [
            # Chain step-down: Primary Unsubstituted Amide -> Primary Amine with the net loss of the carbonyl carbon
            "[#6,c:1]-[CX3](=O)-[NX3H2:2] >> [#6,c:1]-[N:2]"
        ],
        "poisons": SUBSTITUTED_AMIDES,
        "poison_message": "Hofmann Degradation failure: Strictly specific for primary (1°) unsubstituted amides. Secondary and tertiary amides lack the necessary protons required to form the isocyanate intermediate."
    },

    "LiAlH4 / Ether followed by Aqueous Workup (Exhaustive Acid Reduction)": {
        "rules": [
            # Powerful hydride reducing agent converting carboxylic acids directly down to primary alcohols
            "[CX3:1](=O)[OH] >> [C:1]-[OH]"
        ]
    },

    # ==========================================
    # 6. GENERAL ACID DERIVATIVE HYDROLYSIS
    # ==========================================

    "Aqueous Acid or Base / Heat (Exhaustive Derivative Hydrolysis)": {
        "rules": [
            # 1. Esters -> Carboxylic Acid + Alcohol
            "[CX3:1](=O)-[OX2]-[CX4,c:2] >> [C:1](=O)[OH].[OH]-[C,c:2],",
            
            # 2. Amides -> Carboxylic Acid + Ammonium/Amine salt
            "[CX3:1](=O)-[NX3] >> [C:1](=O)[OH]",
            
            # 3. Acid Chlorides -> Carboxylic Acid + HCl
            "[CX3:1](=O)[Cl] >> [C:1](=O)[OH]",
            
            # 4. Acid Anhydrides -> Two Equivalents of Carboxylic Acid
            "[CX3:1](=O)-[O]-[CX3:2](=O) >> [C:1](=O)[OH].[C:2](=O)[OH]"
        ]
    }
}