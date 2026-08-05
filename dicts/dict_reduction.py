# ==========================================
# REDUCTION ENGINE (LiAlH4, NaBH4, Chemoselectivity)
# ==========================================

# --- 1. STRONG REDUCER (LiAlH4) ---
# Reduces almost all polar pi-bonds.
LIALH4_RULES = [
    # 1. Aldehydes -> 1-degree Alcohols
    "[CH1:1]=O >> [C:1]-[OH]",
    
    # 2. Ketones -> 2-degree Alcohols 
    # (Matches a carbonyl carbon bonded to two other carbons)
    "[CH0:1](=O)(-[#6])-[#6] >> [C:1]-[OH]",
    
    # 3. Carboxylic Acids -> 1-degree Alcohols
    "[CX3:1](=O)[OH] >> [C:1]-[OH]",
    
    # 4. Esters -> 1-degree Alcohol + Side Alcohol (CLEAVAGE)
    # The dot (.) splits the ester into two separate molecules
    "[CX3:1](=O)-[OX2:2]-[#6:3] >> [C:1]-[OH].[OH]-[C:3]",
    
    # 5. Acid Chlorides -> 1-degree Alcohols
    "[CX3:1](=O)[Cl] >> [C:1]-[OH]",
    
    # --- THE NITROGEN TRAPS ---
    # 6. Amides -> Amines (Oxygen is lost, C-N bond remains intact!)
    "[CX3:1](=O)-[NX3:2] >> [C:1]-[N:2]",
    
    # 7. Nitriles -> 1-degree Amines
    "[C:1]#[N:2] >> [C:1]-[N:2]",
    
    # 8. Nitro Groups -> 1-degree Amines
    "[N+:1](=O)[O-] >> [N:1]"
]

# --- 2. MILD REDUCER (NaBH4) ---
# Highly chemoselective. Only reduces Aldehydes, Ketones, and Acid Chlorides.
NABH4_RULES = [
    # 1. Aldehydes -> 1-degree Alcohols
    "[CH1:1]=O >> [C:1]-[OH]",
    
    # 2. Ketones -> 2-degree Alcohols
    "[CH0:1](=O)(-[#6])-[#6] >> [C:1]-[OH]",
    
    # 3. Acid Chlorides -> 1-degree Alcohols
    "[CX3:1](=O)[Cl] >> [C:1]-[OH]"
    
    # Notice the INTENTIONAL ABSENCE of rules for Esters, Acids, and Amides.
    # If NaBH4 is applied to a molecule with an Ester, the engine will safely ignore it.
]

# ==========================================
# 3. THE REAGENT DICTIONARY
# ==========================================
REDUCTION_RULES = {
    
    # --- HYDRIDE DONORS ---
    "LiAlH4 / Ether (Strong Reduction)": {
        "rules": LIALH4_RULES
    },
    "NaBH4 / EtOH (Chemoselective Reduction)": {
        "rules": NABH4_RULES
    },
    "DIBAL-H / -78°C (Ester/Nitrile to Aldehyde)": {
        "rules": [
            # Partial reduction at cold temperatures stops at the Aldehyde
            "[CX3:1](=O)-[OX2:2]-[#6:3] >> [C:1]=O.[OH]-[C:3]", # Ester -> Aldehyde + Alcohol
            "[C:1]#[N:2] >> [C:1]=O" # Nitrile -> Aldehyde (after hydrolysis)
        ],
        "poisons": ["[CX3](=O)[OH]"],
        "poison_message": "DIBAL-H does not efficiently reduce carboxylic acids."
    },
    
    # --- CLEMMENSEN & WOLFF-KISHNER ---
    # Both completely strip the carbonyl oxygen to yield an alkane
    "Zn(Hg) / conc. HCl (Clemmensen Reduction)": {
        "rules": [
            "[CH1:1]=O >> [C:1]",                # Aldehyde -> Alkane
            "[CH0:1](=O)(-[#6])-[#6] >> [C:1]"   # Ketone -> Alkane
        ],
        "poisons": ["[OH]"],
        "poison_message": "Clemmensen uses highly acidic conditions (conc. HCl). Acid-sensitive groups like alcohols may undergo unwanted substitution or elimination."
    },
    "NH2NH2 / KOH, heat (Wolff-Kishner Reduction)": {
        "rules": [
            "[CH1:1]=O >> [C:1]",
            "[CH0:1](=O)(-[#6])-[#6] >> [C:1]"
        ],
        "poisons": ["[CX4]-[Cl,Br,I]"],
        "poison_message": "Wolff-Kishner uses highly basic conditions (KOH). Base-sensitive groups like alkyl halides will undergo E2 elimination instead!"
    }
}