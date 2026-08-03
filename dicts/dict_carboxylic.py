CARBOXYLIC_RULES = {
    # 1. Acid Chloride Formation[cite: 7]
    "SOCl2": [
        "[#6:1]-[C:2](=O)[OH] >> [#6:1]-[C:2](=O)[Cl]" #[cite: 7]
    ],

    # 2. Amide Formation[cite: 7]
    "NH3 / Heat": [
        "[#6:1]-[C:2](=O)[OH] >> [#6:1]-[C:2](=O)[NH2]" #[cite: 7]
    ],

    # 3. Esterification[cite: 7]
    "CH3OH / H+ (Esterification)": [
        "[#6:1]-[C:2](=O)[OH] >> [#6:1]-[C:2](=O)[O][CH3]" #[cite: 7]
    ],

    # 4. Hell-Volhard-Zelinsky (HVZ) Reaction[cite: 7]
    "Red P / Br2 (HVZ)": [
        "[CH3,CH2,CH:1]-[C:2](=O)[OH] >> [C:1]([Br])-[C:2](=O)[OH]" #[cite: 7]
    ],

    # 5. Decarboxylation (Soda Lime)[cite: 7]
    "NaOH + CaO / Heat": [
        "[#6:1]-[C](=O)[OH] >> [#6:1]-[H]" #[cite: 7]
    ],
    
    # 6. Reduction to Primary Alcohol[cite: 7]
    "LiAlH4 then H3O+": [
        "[#6:1]-[C:2](=O)[OH] >> [#6:1]-[CH2:2]-[OH]" #[cite: 7]
    ],

    # ==========================================
    # OLYMPIAD LEVEL ADDITIONS
    # ==========================================

    # 7. Hunsdiecker Reaction
    # Silver salt of carboxylic acid reacts with halogens to form an alkyl halide with one less carbon.
    "Ag2O / Br2 / CCl4 (Hunsdiecker)": [
        "[#6:1]-[C](=O)[OH] >> [#6:1]-[Br]"
    ],

    # 8. Arndt-Eistert Homologation (Simplified)
    # Converts a carboxylic acid to its next higher homologue (Acid -> Acid Chloride -> Diazoketone -> Keten -> Acid).
    "SOCl2 then CH2N2 then Ag2O/H2O": [
        "[#6:1]-[C:2](=O)[OH] >> [#6:1]-[CH2]-[C:2](=O)[OH]"
    ],

    # 9. Beta-Keto Acid Decarboxylation
    # Occurs readily upon mild heating due to a cyclic transition state.
    "Heat (Beta-Keto Decarboxylation)": [
        "[#6:1]-[C:2](=O)-[C:3]-[C](=O)[OH] >> [#6:1]-[C:2](=O)-[CH:3]"
    ]
}