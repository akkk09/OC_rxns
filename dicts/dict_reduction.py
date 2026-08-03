REDUCTION_RULES = {
    # 1. Sodium Borohydride (Mild)[cite: 10]
    "NaBH4": [
        "[C,CH:1]=[O:2] >> [C,CH:1][OH:2]" #[cite: 10]
    ],
    
    # 2. Lithium Aluminum Hydride (Strong)[cite: 10]
    "LiAlH4": [
        "[C,CH:1]=[O:2] >> [C,CH:1][OH:2]", #[cite: 10]
        "[C:1](=[O:2])[OH] >> [CH2:1][OH:2]" #[cite: 10]
    ],

    # ==========================================
    # OLYMPIAD LEVEL ADDITIONS
    # ==========================================

    # 3. DIBAL-H (Partial Reduction of Esters)
    # Crucially stops at the aldehyde when run at -78°C.
    "DIBAL-H / -78°C (Ester Reduction)": [
        "[#6:1]-[C:2](=O)-[O]-[#6] >> [#6:1]-[C:2](=O)[H]"
    ],

    # 4. DIBAL-H (Partial Reduction of Nitriles)
    # Reduces nitriles to imines, which hydrolyze to aldehydes.
    "DIBAL-H then H3O+ (Nitrile Reduction)": [
        "[#6:1]-[C:2]#[N] >> [#6:1]-[C:2](=O)[H]"
    ],

    # 5. Luche Reduction
    # Completely regioselective 1,2-reduction of alpha,beta-unsaturated ketones (avoids 1,4-reduction).
    "NaBH4 / CeCl3": [
        "[C:1]=[C:2]-[C:3](=O)-[#6:4] >> [C:1]=[C:2]-[C:3](-[OH])-[#6:4]"
    ],

    # 6. Rosenmund Reduction
    # Reduces acid chlorides to aldehydes using a poisoned palladium catalyst.
    "H2 / Pd-BaSO4, Quinoline (Rosenmund)": [
        "[#6:1]-[C:2](=O)[Cl] >> [#6:1]-[C:2](=O)[H]"
    ],

    # 7. Stephen Reaction
    # Reduces nitriles to aldehydes using tin(II) chloride.
    "SnCl2 / HCl, then H3O+ (Stephen)": [
        "[#6:1]-[C:2]#[N] >> [#6:1]-[C:2](=O)[H]"
    ]
}