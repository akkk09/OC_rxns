# ==========================================
# REDUCTION ENGINE (LiAlH4, NaBH4, & CHEMOSELECTIVITY - OLYMPIAD LEVEL)
# ==========================================

# --- 1. STRONG REDUCER (LiAlH4) ---
# Powerful hydride donor capable of reducing almost all polar pi-bonds and carboxylic derivatives.
LIALH4_RULES = [
    # 1. Aldehydes -> Primary Alcohols
    "[CH1:1]=O >> [C:1]-[OH]",
    
    # 2. Ketones -> Secondary Alcohols (carbonyl carbon bonded to two carbon centers)
    "[CH0:1](=O)(-[#6])-[#6] >> [C:1]-[OH]",
    
    # 3. Carboxylic Acids -> Primary Alcohols
    "[CX3:1](=O)[OH] >> [C:1]-[OH]",
    
    # 4. Esters -> Primary Alcohol + Cleavage Fragment Alcohol (separated via dot notation '.')
    "[CX3:1](=O)-[OX2:2]-[#6:3] >> [C:1]-[OH].[OH]-[C:3]",
    
    # 5. Acid Chlorides -> Primary Alcohols
    "[CX3:1](=O)[Cl] >> [C:1]-[OH]",
    
    # 6. Amides -> Amines (carbonyl oxygen is completely stripped, carbon-nitrogen bond remains intact)
    "[CX3:1](=O)-[NX3:2] >> [C:1]-[N:2]",
    
    # 7. Nitriles -> Primary Amines
    "[C:1]#[N:2] >> [C:1]-[N:2]",
    
    # 8. Nitro Groups -> Primary Amines
    "[N+:1](=O)[O-] >> [N:1]"
]

# --- 2. MILD REDUCER (NaBH4) ---
# Highly chemoselective hydride donor. Specifically targets aldehydes, ketones, and acid chlorides, 
# while safely leaving esters, carboxylic acids, and amides completely untouched.
NABH4_RULES = [
    # 1. Aldehydes -> Primary Alcohols
    "[CH1:1]=O >> [C:1]-[OH]",
    
    # 2. Ketones -> Secondary Alcohols
    "[CH0:1](=O)(-[#6])-[#6] >> [C:1]-[OH]",
    
    # 3. Acid Chlorides -> Primary Alcohols
    "[CX3:1](=O)[Cl] >> [C:1]-[OH]"
]

# ==========================================
# 3. THE REAGENT DICTIONARY
# ==========================================
REDUCTION_RULES = {
    
    # ==========================================
    # A. HYDRIDE DONOR REDUCTIONS
    # ==========================================

    "LiAlH4 / Ether, Followed by Aqueous Workup (Strong Exhaustive Reduction)": {
        "rules": LIALH4_RULES
    },
    
    "NaBH4 / Absolute Ethanol (Chemoselective Carbonyl Reduction)": {
        "rules": NABH4_RULES
    },
    
    "DIBAL-H / -78°C, Controlled Hydrolysis (Partial Reduction to Aldehydes)": {
        "rules": [
            # Low-temperature partial hydride delivery stopping cleanly at the aldehyde oxidation state
            "[CX3:1](=O)-[OX2:2]-[#6:3] >> [C:1]=O.[OH]-[C:3]", # Ester -> Aldehyde + Alcohol
            "[C:1]#[N:2] >> [C:1]=O"                             # Nitrile -> Aldehyde (via imine hydrolysis)
        ],
        "poisons": ["[CX3](=O)[OH]"],
        "poison_message": "DIBAL-H reaction failure: Carboxylic acids lack the electrophilic susceptibility required for efficient partial reduction under standard DIBAL-H protocols."
    },
    
    # ==========================================
    # B. COMPLETE CARBONYL DEOXYGENATION
    # ==========================================

    "Zn(Hg) / Concentrated HCl - Clemmensen Reduction (Acidic Carbonyl Deoxygenation)": {
        "rules": [
            "[CH1:1]=O >> [C:1]",                # Aldehyde -> Alkane methylene
            "[CH0:1](=O)(-[#6])-[#6] >> [C:1]"    # Ketone -> Alkane methylene
        ],
        "poisons": ["[OH]"],
        "poison_message": "Clemmensen reduction failure: Operates under aggressively acidic conditions (conc. HCl). Acid-sensitive functional groups like alcohols may undergo unwanted dehydration or substitution."
    },
    
    "NH2NH2 / KOH, Thermal Glycol Reflux - Wolff-Kishner Reduction (Basic Carbonyl Deoxygenation)": {
        "rules": [
            "[CH1:1]=O >> [C:1]",
            "[CH0:1](=O)(-[#6])-[#6] >> [C:1]"
        ],
        "poisons": ["[CX4]-[Cl,Br,I]"],
        "poison_message": "Wolff-Kishner reduction failure: Operates under strongly basic high-temperature conditions (KOH). Base-sensitive structures like alkyl halides will undergo rapid E2 elimination instead of survival."
    }
}