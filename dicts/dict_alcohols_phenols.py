ALCOHOL_PHENOL_RULES = {
    # 1. Lucas Test (Conc. HCl / Anhydrous ZnCl2)
    # Converts alcohols to alkyl chlorides. (Note: 3° reacts instantly, 1° requires heat).[cite: 1]
    "HCl / anhy. ZnCl2 (Lucas Reagent)": [
        "[#6:1]-[OH] >> [#6:1]-[Cl]" #[cite: 1]
    ],

    # 2. Acid-Catalyzed Dehydration (Forms Alkenes)[cite: 1]
    "Conc. H2SO4 / Heat": [
        "[CH3,CH2,CH:1]-[C:2]-[OH] >> [C:1]=[C:2]" #[cite: 1]
    ],

    # 3. Williamson Ether Synthesis (using Methyl Iodide as the halide)[cite: 1]
    "Na then CH3I": [
        "[#6:1]-[OH] >> [#6:1]-[O]-[CH3]" #[cite: 1]
    ],

    # 4. Reimer-Tiemann Reaction (Phenol specifically)[cite: 1]
    "CHCl3 / aq. NaOH": [
        "[c:1](-[OH])[cH:2] >> [c:1](-[OH])[c:2]-[C](=O)[H]" #[cite: 1]
    ],

    # 5. Kolbe's Reaction (Phenol specifically)[cite: 1]
    "CO2 / NaOH, then H+": [
        "[c:1](-[OH])[cH:2] >> [c:1](-[OH])[c:2]-[C](=O)[OH]" #[cite: 1]
    ],

    # 6. Reduction of Phenol to Benzene[cite: 1]
    "Zn dust / Heat": [
        "[c:1]-[OH] >> [c:1]-[H]" #[cite: 1]
    ],

    # ==========================================
    # OLYMPIAD LEVEL ADDITIONS
    # ==========================================

    # 7. Pinacol-Pinacolone Rearrangement
    # Acid-catalyzed rearrangement of 1,2-diols to ketones with alkyl migration.
    "H+ / Heat (Pinacol Rearrangement)": [
        "[C:1]([OH])-[C:2]([OH]) >> [C:1](=O)-[CH:2]"
    ],

    # 8. Malaprade Reaction (Periodate Cleavage)
    # Cleaves 1,2-diols into two carbonyl compounds.
    "NaIO4 or HIO4": [
        "[C:1]([OH])-[C:2]([OH]) >> [C:1]=O.[C:2]=O"
    ],

    # 9. Mitsunobu Reaction (Azide formation)
    # Inverts stereocenter of an alcohol to form an azide (simplified SMARTS).
    "PPh3, DEAD, DPPA": [
        "[#6:1]-[OH] >> [#6:1]-[N]=[N+]=[N-]"
    ]
}