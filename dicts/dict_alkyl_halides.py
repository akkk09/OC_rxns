ALKYL_HALIDE_RULES = {
    # 1. Nucleophilic Substitution (Aqueous KOH)[cite: 4]
    "Aq. KOH / NaOH": [
        "[#6:1]-[Cl,Br,I] >> [#6:1]-[OH]" #[cite: 4]
    ],

    # 2. Ambident Nucleophile: Cyanide vs Isocyanide[cite: 4]
    "KCN (Alcoholic)": [
        "[#6:1]-[Cl,Br,I] >> [#6:1]-[C]#N" #[cite: 4]
    ],
    "AgCN (Alcoholic)": [
        "[#6:1]-[Cl,Br,I] >> [#6:1]-[N+]#[C-]" #[cite: 4]
    ],

    # 3. Ambident Nucleophile: Nitrite vs Nitro[cite: 4]
    "KNO2": [
        "[#6:1]-[Cl,Br,I] >> [#6:1]-[O]-[N]=O" #[cite: 4]
    ],
    "AgNO2": [
        "[#6:1]-[Cl,Br,I] >> [#6:1]-[N+](=[O])[O-]" #[cite: 4]
    ],

    # 4. Halogen Exchange: Finkelstein Reaction[cite: 4]
    "NaI / Acetone": [
        "[#6:1]-[Cl,Br] >> [#6:1]-[I]" #[cite: 4]
    ],

    # 5. Halogen Exchange: Swarts Reaction[cite: 4]
    "AgF / Hg2F2 / CoF2": [
        "[#6:1]-[Cl,Br,I] >> [#6:1]-[F]" #[cite: 4]
    ],

    # 6. Elimination: Dehydrohalogenation (Alcoholic KOH)[cite: 4]
    "Alc. KOH / Heat": [
        "[CH3,CH2,CH:1]-[C:2]-[Cl,Br,I] >> [C:1]=[C:2]" #[cite: 4]
    ],

    # 7. Grignard Reagent Formation[cite: 4]
    "Mg / Dry Ether": [
        "[#6:1]-[Cl,Br,I:2] >> [#6:1]-[Mg]-[Cl,Br,I:2]" #[cite: 4]
    ],

    # ==========================================
    # OLYMPIAD LEVEL ADDITIONS
    # ==========================================

    # 8. Gabriel Phthalimide Synthesis (Simplified)
    # Exclusively produces pure 1° aliphatic amines.
    "Potassium Phthalimide then Hydrazine": [
        "[CH3,CH2:1]-[Cl,Br,I] >> [CH3,CH2:1]-[NH2]"
    ],

    # 9. Corey-House Synthesis (Cross-Coupling)
    # Replaces the halogen with a methyl group via Gilman reagent (Me2CuLi).
    "(CH3)2CuLi (Gilman Reagent)": [
        "[#6:1]-[Cl,Br,I] >> [#6:1]-[CH3]"
    ],
    
    # 10. E2 Elimination via Bulky Base
    # Forces Hofmann (less substituted) alkene formation.
    "t-BuOK (Potassium tert-butoxide)": [
        "[CH3:1]-[CH2:2]-[CH:3]([Cl,Br,I])-[CH3:4] >> [CH2:1]=[CH:2]-[CH2:3]-[CH3:4]"
    ]
}