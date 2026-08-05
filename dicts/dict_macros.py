# ==========================================
# MACRO ENGINE (MULTI-STEP & COMPLEX REAGENTS)
# ==========================================

# --- THE GRIGNARD ACID-BASE TRAP ---
# Any molecule containing these functional groups will destroy the Grignard 
# reagent via a rapid acid-base reaction, producing methane gas instead of attacking.
ACIDIC_PROTONS = [
    "[OH]",             # Alcohols and Carboxylic Acids
    "[NH1,NH2]",        # Primary and Secondary Amines / Amides
    "[SH]",             # Thiols
    "[CH1]#[C]"         # Terminal Alkynes
]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
MACRO_REAGENTS = {

    # --- THE GRIGNARD SEQUENCE (CH3MgBr followed by H3O+) ---
    "1. CH3MgBr (excess) / Ether, 2. H3O+": {
        "rules": [
            # 1. Formaldehyde -> 1-degree Alcohol (Ethanol)
            "[CH2:1]=O >> [C:1](-[OH])-[CH3]",
            
            # 2. Aldehydes -> 2-degree Alcohols
            "[CH1:1]=O >> [C:1](-[OH])-[CH3]",
            
            # 3. Ketones -> 3-degree Alcohols
            "[CH0:1](=O)(-[#6])-[#6] >> [C:1](-[OH])-[CH3]",
            
            # 4. Esters / Acid Chlorides -> 3-degree Alcohols (DOUBLE ADDITION)
            # The leaving group [OX2,Cl] is ejected, and TWO methyl groups are added to the carbonyl carbon.
            "[CX3:1](=O)-[OX2,Cl] >> [C:1](-[OH])(-[CH3])-[CH3]",
            
            # 5. Nitriles -> Ketones (Addition followed by hydrolysis of the imine)
            "[C:1]#[N:2] >> [C:1](=O)-[CH3]",
            
            # 6. Carbon Dioxide (CO2) -> Acetic Acid
            "O=C=O >> [CH3]-[C](=O)[OH]",
            
            # 7. Epoxides -> 1-degree or 2-degree Alcohols (Regioselective SN2 Ring Opening)
            # Grignard attacks the LESS sterically hindered carbon of the epoxide (the CH2).
            # The '1' notation denotes the 3-membered oxirane ring.
            "[CH2:1]1-[O]-[#6:2]1 >> [CH3]-[C:1]-[C:2]-[OH]"
        ],
        
        "poisons": ACIDIC_PROTONS,
        "poison_message": "Grignard reagents are powerful bases! Because this molecule contains an acidic proton (e.g., -OH, -NH, or a terminal alkyne), an acid-base reaction will occur instantly to form methane gas, destroying the nucleophile before it can attack the electrophile."
    }
}