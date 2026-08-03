ALDEHYDE_KETONE_RULES = {
    # 1. Clemmensen Reduction (Zinc amalgam + conc. HCl)[cite: 2]
    "Zn-Hg / conc. HCl": [
        "[#6:1]-[C:2](=O)-[#6,H:3] >> [#6:1]-[CH2:2]-[#6,H:3]" #[cite: 2]
    ],

    # 2. Wolff-Kishner Reduction (Hydrazine + KOH + heat)[cite: 2]
    "NH2NH2 / KOH, heat": [
        "[#6:1]-[C:2](=O)-[#6,H:3] >> [#6:1]-[CH2:2]-[#6,H:3]" #[cite: 2]
    ],

    # 3. Tollens' Reagent (Ammoniacal AgNO3)[cite: 2]
    "Tollens' Reagent": [
        "[CX3H1:1](=O)-[#6:2] >> [CX3:1](=O)([O-])-[#6:2]" #[cite: 2]
    ],

    # 4. Cyanohydrin Formation (Nucleophilic Addition of HCN)[cite: 2]
    "HCN": [
        "[#6:1]-[C:2](=O)-[#6,H:3] >> [#6:1]-[C:2](O)(C#N)-[#6,H:3]" #[cite: 2]
    ],

    # 5. Iodoform Reaction (Haloform Test)[cite: 2]
    "I2 / NaOH (Iodoform Test)": [
        "[#6,H:1]-[C:2](=O)-[CH3:3] >> [#6,H:1]-[C:2](=O)[O-].[CH:3](I)(I)(I)" #[cite: 2]
    ],

    # ==========================================
    # OLYMPIAD LEVEL ADDITIONS
    # ==========================================

    # 6. Wittig Reaction (Methylenation)
    # Converts a carbonyl to an alkene using a phosphorus ylide (Ph3P=CH2 used here).
    "Ph3P=CH2 (Wittig Reagent)": [
        "[#6:1]-[C:2](=O)-[#6,H:3] >> [#6:1]-[C:2](=[CH2])-[#6,H:3]"
    ],

    # 7. Baeyer-Villiger Oxidation
    # Oxidizes ketones to esters via migration of the more substituted group.
    "mCPBA or CF3CO3H": [
        "[#6:1]-[C:2](=O)-[#6:3] >> [#6:1]-[C:2](=O)-[O]-[#6:3]" 
    ],

    # 8. Aldol Condensation (Heating)
    # Forms alpha, beta-unsaturated carbonyl compounds from enolizable aldehydes/ketones.
    "Dil. NaOH / Heat (Aldol)": [
        "[O:1]=[C:2]-[CH3:3] >> [O:1]=[C:2]-[CH:3]=[C]-[C](=O)"
    ],
    
    # 9. Cannizzaro Reaction
    # Disproportionation of aldehydes lacking alpha-hydrogens (e.g., Benzaldehyde).
    "Conc. NaOH (Cannizzaro)": [
        "[c:1]-[C:2](=O)[H] >> [c:1]-[CH2:2][OH].[c:1]-[C:2](=O)[O-]"
    ]
}