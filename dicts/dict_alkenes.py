ALKENE_RULES = {
    # 1. Catalytic Hydrogenation (Syn addition of H2)[cite: 3]
    "H2 / Pd-C": [
        "[C:1]=[C:2] >> [CH:1]-[CH:2]" #[cite: 3]
    ],

    # 2. Halogenation (Anti addition of Bromine)[cite: 3]
    "Br2 / CCl4": [
        "[C:1]=[C:2] >> [C:1]([Br])-[C:2]([Br])" #[cite: 3]
    ],

    # 3. Hydrohalogenation[cite: 3]
    "HBr": [
        "[C:1]=[C:2] >> [CH:1]-[C:2]-[Br]" #[cite: 3]
    ],

    # 4. Acid-Catalyzed Hydration[cite: 3]
    "H2O / H+": [
        "[C:1]=[C:2] >> [CH:1]-[C:2]-[OH]" #[cite: 3]
    ],

    # 5. Reductive Ozonolysis[cite: 3]
    "O3 then Zn/H2O": [
        "[C:1]=[C:2] >> [C:1]=O.[C:2]=O" #[cite: 3]
    ],

    # ==========================================
    # OLYMPIAD LEVEL ADDITIONS
    # ==========================================

    # 6. Oxidative Ozonolysis
    # Cleaves double bonds and further oxidizes aldehydes to carboxylic acids.
    "O3 then H2O2": [
        "[CH:1]=[CH:2] >> [C:1](=O)[OH].[C:2](=O)[OH]",
        "[C:1]=[CH:2] >> [C:1]=O.[C:2](=O)[OH]"
    ],

    # 7. Hydroboration-Oxidation
    # Anti-Markovnikov syn-addition of water.
    "BH3.THF then H2O2, OH-": [
        "[CH2:1]=[CH:2]-[#6:3] >> [CH2:1]([OH])-[CH2:2]-[#6:3]"
    ],

    # 8. Epoxidation
    # Forms an oxirane (epoxide) ring.
    "mCPBA (Epoxidation)": [
        "[C:1]=[C:2] >> [C:1]1-[C:2]-O1"
    ],

    # 9. Syn-Dihydroxylation
    # Adds two hydroxyl groups to the same face of the alkene.
    "OsO4 then NaHSO3 OR Cold dilute KMnO4 (Baeyer's)": [
        "[C:1]=[C:2] >> [C:1]([OH])-[C:2]([OH])"
    ],
    
    # 10. Simmons-Smith Cyclopropanation
    # Stereospecific addition of a carbene to form a cyclopropane ring.
    "CH2I2 / Zn(Cu)": [
        "[C:1]=[C:2] >> [C:1]1-[C:2]-[CH2]1"
    ]
}