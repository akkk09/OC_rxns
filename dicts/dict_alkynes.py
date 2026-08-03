ALKYNE_RULES = {
    # 1. Partial Reduction: Lindlar's Catalyst (Produces cis-alkene)[cite: 5]
    "H2 / Lindlar's Catalyst": [
        "[C:1]#[C:2] >> [CH:1]=[CH:2]" #[cite: 5]
    ],

    # 2. Partial Reduction: Birch Reduction (Produces trans-alkene)[cite: 5]
    "Na / liq. NH3": [
        "[C:1]#[C:2] >> [CH:1]=[CH:2]" #[cite: 5]
    ],
    
    # 3. Complete Hydrogenation (Alkane formation)[cite: 5]
    "H2 / Ni (excess)": [
        "[C:1]#[C:2] >> [CH2:1]-[CH2:2]" #[cite: 5]
    ],

    # 4. Kucherov Reaction (Hydration of Alkynes)[cite: 5]
    "HgSO4 / dil. H2SO4": [
        "[C:1]#[C:2] >> [C:1](=O)-[CH2:2]" #[cite: 5]
    ],

    # 5. Terminal Alkyne Test: Ammoniacal AgNO3[cite: 5]
    "Ammoniacal AgNO3": [
        "[CH:1]#[C:2] >> [Ag]-[C:1]#[C:2]" #[cite: 5]
    ],
    
    # 6. Complete Halogenation[cite: 5]
    "Br2 / CCl4 (excess)": [
        "[C:1]#[C:2] >> [C:1]([Br])([Br])-[C:2]([Br])([Br])" #[cite: 5]
    ],

    # ==========================================
    # OLYMPIAD LEVEL ADDITIONS
    # ==========================================

    # 7. Hydroboration-Oxidation of Terminal Alkynes
    # Yields aldehydes instead of ketones (Anti-Markovnikov hydration).
    "Sia2BH then H2O2, OH-": [
        "[CH:1]#[C:2]-[#6:3] >> [CH:1](=O)-[CH2:2]-[#6:3]"
    ],

    # 8. Alkyne Alkylation (Homologation)
    # Deprotonates the terminal alkyne and attaches a methyl group.
    "NaNH2 then CH3I": [
        "[CH:1]#[C:2]-[#6:3] >> [CH3]-[C:1]#[C:2]-[#6:3]"
    ]
}