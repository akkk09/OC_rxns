HETEROCYCLE_RULES = {
    # 1. Electrophilic Aromatic Substitution on Pyrrole/Furan/Thiophene
    # These 5-membered rings direct incoming electrophiles exclusively to the 2-position (alpha).
    "Br2 / Acetic Acid (Heterocycle)": [
        "[o,s,nH:1]1[cH:2][cH][cH][cH:3]1 >> [o,s,nH:1]1[c:2](-[Br])[cH][cH][cH:3]1"
    ],
    
    # 2. Vilsmeier-Haack on Furan/Pyrrole
    # Formylates specifically at the 2-position.
    "POCl3 / DMF (Heterocycle Formylation)": [
        "[o,s,nH:1]1[cH:2][cH][cH][cH:3]1 >> [o,s,nH:1]1[c:2](-[C](=O)[H])[cH][cH][cH:3]1"
    ],

    # 3. Electrophilic Aromatic Substitution on Pyridine
    # Pyridine is electron-poor and resists reaction, but forcing conditions direct to the 3-position (meta).
    "Fuming HNO3 / H2SO4 / 300°C": [
        "[n:1]1[cH:2][cH:3][cH:4][cH:5][cH:6]1 >> [n:1]1[cH:2][c:3](-[N+](=[O])[O-])[cH:4][cH:5][cH:6]1"
    ],

    # 4. Pyridine N-Oxide Formation
    # Makes pyridine more reactive to both electrophiles and nucleophiles.
    "mCPBA (Pyridine N-Oxidation)": [
        "[n:1]1[cH:2][cH:3][cH:4][cH:5][cH:6]1 >> [n+:1]1(-[O-])[cH:2][cH:3][cH:4][cH:5][cH:6]1"
    ]
}