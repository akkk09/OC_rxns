# ==========================================
# CARBOHYDRATES & BIOMOLECULES ENGINE
# ==========================================

# --- BIOMOLECULE IDENTIFIERS ---
# Ketoses (like Fructose) resist mild oxidation
KETOSE_TRAP = ["[CH2](-[OH])-[C](=O)-[CH1](-[OH])"] 

# Alpha-Amino Acids (for the Ninhydrin test)
ALPHA_AMINO_ACID = ["[NX3H2,NX3H3+]-[CX4H1,CX4H2]-[CX3](=O)[OH,O-]"]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
BIOMOLECULE_RULES = {

    # --- 1. CARBOHYDRATE OXIDATION (THE PROOF OF ALDEHYDE) ---
    "Br2 / H2O (Mild Oxidation)": {
        "rules": [
            # Selectively oxidizes the Aldehyde to a Carboxylic Acid (Glucose -> Gluconic Acid)
            # Completely ignores primary and secondary alcohols!
            "[CH1:1]=O >> [C:1](=O)[OH]"
        ],
        "poisons": KETOSE_TRAP,
        "poison_message": "Bromine water is a mild oxidizing agent. It successfully oxidizes aldoses (like Glucose) to aldonic acids, but it cannot oxidize ketoses (like Fructose)!"
    },
    
    "Conc. HNO3 / Heat (Strong Oxidation)": {
        "rules": [
            # Oxidizes BOTH the terminal aldehyde AND the terminal primary alcohol
            # (Glucose -> Saccharic / Glucaric Acid)
            "[CH1:1]=O >> [C:1](=O)[OH]",
            "[CH2:1]-[OH] >> [C:1](=O)[OH]"
        ]
    },

    # --- 2. CARBOHYDRATE REDUCTION (THE PROOF OF THE CARBON SKELETON) ---
    "HI / Red P, 100°C (Exhaustive Reduction)": {
        "rules": [
            # The "Sledgehammer". Strips all oxygen from the molecule.
            # Converts all aldehydes, ketones, and alcohols straight to alkanes.
            # (Glucose / Fructose -> n-Hexane)
            "[CH1:1]=O >> [CH3:1]",
            "[C:1](=O)-[#6] >> [CH2:1]-C",
            "[CX4:1]-[OH] >> [C:1]"
        ]
    },

    # --- 3. OSAZONE FORMATION (THE EPIMER TRAP) ---
    "Ph-NH-NH2 (3 Equivalents) / Heat": {
        "rules": [
            # 1. Aldoses (Glucose / Mannose)
            # C1 Aldehyde and C2 Alcohol are both converted to hydrazones.
            "[CH1:1](=O)-[CH1:2]-[OH] >> [C:1](=N-[NH]-[c]1ccccc1)-[C:2](=N-[NH]-[c]1ccccc1)",
            
            # 2. Ketoses (Fructose)
            # C1 Primary Alcohol and C2 Ketone are both converted to hydrazones.
            "[CH2:1](-[OH])-[C:2]=O >> [C:1](=N-[NH]-[c]1ccccc1)-[C:2](=N-[NH]-[c]1ccccc1)"
        ],
        "poisons": ["[CH1](=O)-[CH2]-[#6]"], # Lacks the adjacent alpha-hydroxyl
        "poison_message": "Osazone formation strictly requires an alpha-hydroxyl carbonyl system. Standard aldehydes and ketones will only consume 1 equivalent to form a simple hydrazone."
    },

    # --- 4. AMINO ACIDS (NINHYDRIN TEST) ---
    "Ninhydrin / Heat": {
        "rules": [
            # Strecker Degradation of Alpha-Amino Acids
            # Cleaves the amino acid into an Aldehyde, CO2, and (conceptually) Ruhemann's Purple.
            # RDKit will isolate the R-group into the corresponding aldehyde.
            "[NX3]-[CX4H1:1](-[#6:2])-[CX3](=O)[OH] >> [C:1](=O)-[#6:2].O=C=O"
        ],
        "poisons": ["[NX3]-[CX4]-[CX4]-[CX3](=O)[OH]"], # Beta or Gamma amino acids
        "poison_message": "The Ninhydrin test is highly specific for ALPHA-amino acids. Beta or gamma amino acids do not readily undergo the required decarboxylative deamination to yield Ruhemann's purple!"
    },

    # --- 5. PEPTIDE BOND FORMATION ---
    "DCC (N,N'-Dicyclohexylcarbodiimide)": {
        "rules": [
            # Bimolecular Coupling: Carboxylic Acid + Amine -> Amide (Peptide Bond)
            # The dot (.) brings two distinct amino acids together
            "[CX3:1](=O)[OH].[NX3H2:2]-[CX4] >> [C:1](=O)-[NH1:2]-[CX4]"
        ]
    }
}