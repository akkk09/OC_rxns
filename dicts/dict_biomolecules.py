# ==========================================
# CARBOHYDRATES & BIOMOLECULES ENGINE (EXHAUSTIVE OLYMPIAD LEVEL)
# ==========================================

# --- ADVANCED STRUCTURAL IDENTIFIERS & POISONS ---
KETOSE_TRAP = ["[CH2](-[OH])-[C](=O)-[CH1](-[OH])"] 
ALPHA_AMINO_ACID = ["[NX3H2,NX3H3+]-[CX4H1]-[CX3](=O)[OH,O-]"]
PROTECTED_AMINE_PROTECTION = ["[CX4](C)(C)(C)-OC(=O)-[NX3H1]"] # Boc-protected amino acids
PROTECTED_ACID_PROTECTION = ["[CX4](C)(C)(C)-[OX2]-C(=O)"] # t-Butyl ester protected acids

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
BIOMOLECULE_RULES = {

    # ==========================================
    # 1. CARBOHYDRATE CHEMISTRY & STRUCTURAL PROOFS
    # ==========================================
    
    "Bromine Water / Aqueous Buffer (Mild Aldose Oxidation)": {
        "rules": [
            # Selective oxidation of the C1 aldehyde group of aldoses to yield aldonic acids 
            # while leaving primary and secondary alcohol matrices untouched.
            "[CH1:1]=O >> [C:1](=O)[OH]"
        ],
        "poisons": KETOSE_TRAP,
        "poison_message": "Bromine Water oxidation failure: Mild aqueous bromine is chemoselective for aldoses. Ketoses (such as fructose) resist oxidation under these conditions due to the lack of a free aldehyde hydrogen."
    },
    
    "Concentrated Nitric Acid / Thermal Oxidation (Aldaric Acid Synthesis)": {
        "rules": [
            # Vigorous oxidation converting both the terminal C1 aldehyde and C6 primary alcohol 
            # into carboxylic acid groups, yielding symmetrical or unsymmetrical aldaric (glucaric) acids.
            "[CH1:1]=O >> [C:1](=O)[OH]",
            "[CH2:1]-[OH] >> [C:1](=O)[OH]"
        ]
    },

    "Excess Hydriodic Acid / Red Phosphorus, 100°C (Exhaustive Deoxygenation)": {
        "rules": [
            # Reduction of all polyhydroxy aldehyde/ketone systems down to straight-chain alkanes (n-hexane proof).
            "[CH1:1]=O >> [CH3:1]",
            "[C:1](=O)-[#6] >> [CH2:1]-C",
            "[CX4:1]-[OH] >> [C:1]"
        ]
    },

    "Excess Phenylhydrazine (3 Equivalents) / Mild Heat (Osazone Crystallization)": {
        "rules": [
            # 1. Aldoses (Glucose, Mannose, Galactose matrices): Oxidation at C2 followed by triple condensation,
            # resulting in identical crystalline osazone networks that prove epimeric configurations at C3, C4, C5.
            "[CH1:1](=O)-[CH1:2]-[OH] >> [C:1](=N-[NH]-[c]1ccccc1)-[C:2](=N-[NH]-[c]1ccccc1)",
            
            # 2. Ketoses (Fructose matrices): Oxidation of terminal C1 and C2 yielding the identical osazone framework.
            "[CH2:1](-[OH])-[C:2]=O >> [C:1](=N-[NH]-[c]1ccccc1)-[C:2](=N-[NH]-[c]1ccccc1)"
        ],
        "poisons": ["[CH1](=O)-[CH2]-[#6]"], 
        "poison_message": "Osazone formation failure: Requires an adjacent alpha-hydroxyl carbonyl (acyloin) system. Standard isolated aldehydes/ketones consume only a single equivalent to yield basic hydrazones."
    },

    "Acetic Anhydride / Pyridine (Pentaacetate Derivatization)": {
        "rules": [
            # Exhaustive acetylation of all free hydroxyl groups and the anomeric center 
            # to confirm the exact number of hydroxyl functionalities in an aldose or ketose.
            "[CX4:1]-[OH] >> [C:1]-[O]-C(=O)-CH3",
            "[CH1:1]=O >> [C:1]-[O]-C(=O)-CH3"
        ]
    },

    # ==========================================
    # 2. AMINO ACIDS, PEPTIDES & PROTEIN STRUCTURE
    # ==========================================

    "Ninhydrin / Thermal Deamination (Ruhemann's Purple Assay)": {
        "rules": [
            # Oxidative decarboxylation of alpha-amino acids yielding carbon dioxide, an aldehyde corresponding to the R-group,
            # and condensation with a second ninhydrin molecule to form the characteristic purple chromophore.
            "[NX3]-[CX4H1:1](-[#6:2])-[CX3](=O)[OH] >> [C:1](=O)-[#6:2].O=C=O"
        ],
        "poisons": ["[NX3]-[CX4]-[CX4]-[CX3](=O)[OH]"], # Non-alpha amino acids
        "poison_message": "Ninhydrin test failure: Strictly specific for alpha-amino acids. Beta, gamma, or unactivated amino acids do not undergo the requisite concerted decarboxylative deamination."
    },

    "DCC / HOBt Coupling (Carbodiimide-Mediated Peptide Synthesis)": {
        "rules": [
            # Dehydrative condensation coupling a carboxylic acid component with an alpha-amino component 
            # to generate an invariant peptide amide linkage.
            "[CX3:1](=O)[OH].[NX3H2:2]-[CX4] >> [C:1](=O)-[NH1:2]-[CX4]"
        ]
    },

    "Boc2O / Base (Tert-Butylloxycarbonyl Amine Protection)": {
        "rules": [
            # Protection of primary and secondary amine termini in amino acids to prevent self-condensation 
            # during peptide chain elongation.
            "[NX3H2:1]-[CX4] >> [N:1](C(=O)OC(C)(C)C)"
        ]
    },

    "Trifluoroacetic Acid / CH2Cl2 (Boc Deprotection)": {
        "rules": [
            # Acidolytic cleavage of Boc protecting groups back to free ammonium trifluoroacetate salts.
            "[NX3H1:1]-C(=O)-OC(C)(C)C >> [N:1]H2"
        ]
    },

    "Sanger's Reagent (1-fluoro-2,4-dinitrobenzene) followed by Hydrolysis (N-Terminal Sequencing)": {
        "rules": [
            # Nucleophilic aromatic substitution (SNAr) labeling the N-terminal amine of a peptide chain,
            # allowing acid-catalyzed hydrolysis to isolate the tagged N-terminal dinitrophenyl amino acid.
            "[NX3H2:1]-[CX4] >> [N:1]--[c]1[cH][c](-[N+](=O)[O-])[cH][c](-[N+](=O)[O-])[cH]1" # Representational N-aryl tag mapping
        ]
    },

    "Edman's Reagent (Phenyl Isothiocyanate) followed by Acid Cleavage (Stepwise Sequencing)": {
        "rules": [
            # Cyclization yielding an anilinothiazolinone derivative which converts to a stable phenylthiohydantoin (PTH) 
            # amino acid without cleaving the remaining internal peptide backbone.
            "[NX3H2:1]-[CX4]-[CX3](=O)-[NH1] >> [N:1]-C(=S)-NH-c1ccccc1" # Structural thiourea intermediate mapping
        ]
    }
}