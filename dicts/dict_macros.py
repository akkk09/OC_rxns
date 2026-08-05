# ==========================================
# MACRO ENGINE (MULTI-STEP & COMPLEX REAGENTS - OLYMPIAD LEVEL)
# ==========================================

# --- THE GRIGNARD ACID-BASE TRAP ---
# Any molecule containing these functional groups will destroy the Grignard 
# reagent via a rapid acid-base reaction, producing alkane gas instead of attacking.
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

    # ==========================================
    # 1. ORGANOMETALLIC ADDITION SEQUENCES
    # ==========================================

    "1. CH3MgBr (excess) / Ether, 2. H3O+ (Grignard Nucleophilic Addition)": {
        "rules": [
            # 1. Formaldehyde -> Primary Alcohol (Ethanol)
            "[CH2:1]=O >> [C:1](-[OH])-[CH3]",
            
            # 2. Aldehydes -> Secondary Alcohols
            "[CH1:1]=O >> [C:1](-[OH])-[CH3]",
            
            # 3. Ketones -> Tertiary Alcohols
            "[CH0:1](=O)(-[#6])-[#6] >> [C:1](-[OH])-[CH3]",
            
            # 4. Esters / Acid Chlorides -> Tertiary Alcohols (Double Addition via Ketone Intermediate)
            "[CX3:1](=O)-[OX2,Cl] >> [C:1](-[OH])(-[CH3])-[CH3]",
            
            # 5. Nitriles -> Ketones (Addition followed by hydrolysis of the imine intermediate)
            "[C:1]#[N:2] >> [C:1](=O)-[CH3]",
            
            # 6. Carbon Dioxide (CO2) -> Acetic Acid via Carboxylation
            "O=C=O >> [CH3]-[C](=O)[OH]",
            
            # 7. Epoxides -> Alcohols via Regioselective SN2 Ring Opening (Attack at less hindered carbon)
            "[CH2:1]1-[O]-[#6:2]1 >> [CH3]-[C:1]-[C:2]-[OH]"
        ],
        "poisons": ACIDIC_PROTONS,
        "poison_message": "Grignard reaction failure: Grignard reagents are powerful strong bases. Because this substrate contains an acidic proton (e.g., -OH, -NH, or terminal alkyne), an instantaneous acid-base proton transfer occurs to form alkane gas, destroying the nucleophile before electrophilic attack can take place."
    },

    # ==========================================
    # 2. CONJUGATE ADDITIONS & OLEFINATIONS
    # ==========================================

    "Li[Cu(CH3)2] / Ether - Gilman Reagent (Conjugate 1,4-Addition to Enones)": {
        "rules": [
            # Soft organocuprate nucleophiles selectively target the beta-carbon of alpha,beta-unsaturated carbonyls (Michael addition)
            "[#6:1]=[CX3:2]-[CX3:3](=O)-[#6:4] >> [CH3]-[C:1]-[CH2:2]-[C:3](=O)-[#6:4]"
        ]
    },

    "Ph3P=CH2 / THF (Wittig Olefination - Carbonyl to Alkene Conversion)": {
        "rules": [
            # Converts aldehydes and ketones into terminal or substituted alkenes via oxaphosphetane intermediates
            "[CX3:1](=O) >> [C:1]=[CH2]"
        ]
    },

    # ==========================================
    # 3. COMPLETE DEOXYGENATION PROTOCOLS
    # ==========================================

    "NH2NH2 / KOH, High Temp - Wolff-Kishner Reduction (Carbonyl to Methylene)": {
        "rules": [
            # Complete deoxygenation of aldehydes and ketones down to fully saturated methylene groups under strongly basic conditions
            "[CX3:1](=O) >> [C:1](-[H])-[H]"
        ]
    }
}