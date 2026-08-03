OXIDATION_RULES = {
    # 1. Vigorous Oxidation (Acidic KMnO4)[cite: 9]
    "Acidic KMnO4": [
        "[CH2:1][OH:2] >> [C:1](=[O:2])[OH]", #[cite: 9]
        "[CH:1]([#6])[OH:2] >> [C:1]([#6])=[O:2]" #[cite: 9]
    ],

    # ==========================================
    # OLYMPIAD LEVEL ADDITIONS
    # ==========================================

    # 2. Mild Oxidation (PCC / PDC / DMP)
    # Stops specifically at the aldehyde without over-oxidizing to carboxylic acid.
    "PCC / CH2Cl2": [
        "[CH2:1][OH:2] >> [C:1](=[O:2])[H]",
        "[CH:1]([#6])[OH:2] >> [C:1](=[O:2])([#6])"
    ],

    # 3. Allylic Oxidation (Selenium Dioxide)
    # Selectively oxidizes allylic positions to allylic alcohols/carbonyls.
    "SeO2 / Heat": [
        "[C:1]=[C:2]-[CH3:3] >> [C:1]=[C:2]-[C:3](=O)[H]",
        "[C:1]=[C:2]-[CH2:3]-[#6:4] >> [C:1]=[C:2]-[C:3](=O)-[#6:4]"
    ],

    # 4. Benzylic / Allylic Selective Oxidation
    # Oxidizes allylic/benzylic alcohols to carbonyls while leaving saturated alcohols completely untouched.
    "MnO2 / CH2Cl2": [
        "[C:1]=[C:2]-[CH2:3][OH:4] >> [C:1]=[C:2]-[C:3](=[O:4])[H]",
        "[c]-[CH2:3][OH:4] >> [c]-[C:3](=[O:4])[H]"
    ],
    
    "HBr (excess, heat)": {
        "rules": [
            "[c:1]-[CH:2]=[CH2:3] >> [c:1]-[CH:2](Br)-[CH3:3]",
            "[c:1]-[O:2]-[CH3:3] >> [c:1]-[OH:2]"
        ],
        "poisons": [
            "[O]-[O]"
        ],
        "poison_message": "Presence of peroxides triggers a radical mechanism, leading to anti-Markovnikov hydrobromination."
    }
}
