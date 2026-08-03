AROMATIC_RULES = {
    # 1. Halogenation[cite: 6]
    "Cl2 / AlCl3": [
        "[cH:1] >> [c:1]-[Cl]" #[cite: 6]
    ],
    "Br2 / FeBr3": [
        "[cH:1] >> [c:1]-[Br]" #[cite: 6]
    ],
    
    # 2. Nitration (Conc. HNO3 + Conc. H2SO4)[cite: 6]
    "Conc. HNO3 + H2SO4": [
        "[cH:1] >> [c:1]-[N+](=[O])[O-]" #[cite: 6]
    ],
    
    # 3. Sulfonation (Fuming H2SO4 / Oleum)[cite: 6]
    "Fuming H2SO4": [
        "[cH:1] >> [c:1]-[S](=O)(=O)[OH]" #[cite: 6]
    ],
    
    # 4. Friedel-Crafts Alkylation[cite: 6]
    "CH3Cl / AlCl3": [
        "[cH:1] >> [c:1]-[CH3]" #[cite: 6]
    ],
    
    # 5. Friedel-Crafts Acylation[cite: 6]
    "CH3COCl / AlCl3": [
        "[cH:1] >> [c:1]-[C](=O)[CH3]" #[cite: 6]
    ],

    # ==========================================
    # OLYMPIAD LEVEL ADDITIONS
    # ==========================================

    # 6. Gattermann-Koch Formylation
    # Formylates an aromatic ring using CO and HCl.
    "CO / HCl / AlCl3 / CuCl (Gattermann-Koch)": [
        "[cH:1] >> [c:1]-[C](=O)[H]"
    ],

    # 7. Vilsmeier-Haack Reaction
    # Formylates activated aromatic rings (like phenols or anilines).
    "POCl3 / DMF (Vilsmeier-Haack)": [
        "[cH:1] >> [c:1]-[C](=O)[H]"
    ],

    # 8. Birch Reduction (Aromatics)
    # Reduces benzene to 1,4-cyclohexadiene.
    "Na / Liq. NH3 / EtOH (Birch Reduction)": [
        "[c:1]1[c:2][c:3][c:4][c:5][c:6]1 >> [C:1]1=[C:2][CH2:3][C:4]=[C:5][CH2:6]1"
    ]
}