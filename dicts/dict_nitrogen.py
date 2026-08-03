NITROGEN_RULES = {
    # 1. Carbylamine Reaction (Isocyanide Test)[cite: 8]
    "CHCl3 / KOH (Carbylamine Test)": [
        "[#6:1]-[NX3H2] >> [#6:1]-[N+]#[C-]" #[cite: 8]
    ],

    # 2. Hofmann Bromamide Degradation[cite: 8]
    "Br2 / KOH (Hofmann Bromamide)": [
        "[#6:1]-[C](=O)-[NH2] >> [#6:1]-[NH2]" #[cite: 8]
    ],

    # 3. Diazotization[cite: 8]
    "NaNO2 / HCl, 0-5°C": [
        "[c:1]-[NH2] >> [c:1]-[N+]#[N]" #[cite: 8]
    ],

    # 4. Sandmeyer Reaction (Chlorination)[cite: 8]
    "Cu2Cl2 / HCl (Sandmeyer)": [
        "[c:1]-[N+]#[N] >> [c:1]-[Cl]" #[cite: 8]
    ],

    # 5. Balz-Schiemann Reaction (Fluorination)[cite: 8]
    "HBF4 / Heat": [
        "[c:1]-[N+]#[N] >> [c:1]-[F]" #[cite: 8]
    ],

    # 6. Diazonium Hydrolysis (Phenol Formation)[cite: 8]
    "H2O / Warm": [
        "[c:1]-[N+]#[N] >> [c:1]-[OH]" #[cite: 8]
    ],

    # 7. Mild Reduction (Deamination)[cite: 8]
    "H3PO2 / H2O": [
        "[c:1]-[N+]#[N] >> [c:1]-[H]" #[cite: 8]
    ],

    # ==========================================
    # OLYMPIAD LEVEL ADDITIONS
    # ==========================================

    # 8. Curtius Rearrangement (Simplified from Acyl Azide)
    # Converts an acid chloride (via azide) to an isocyanate, which hydrolyzes to a primary amine.
    "NaN3 then Heat / H2O (Curtius)": [
        "[#6:1]-[C](=O)[Cl] >> [#6:1]-[NH2]"
    ],

    # 9. Beckmann Rearrangement
    # Acid-catalyzed rearrangement of an oxime to an amide.
    "H2SO4 / Heat (Beckmann)": [
        "[C:1](=[N:2]-[OH])-[C:3] >> [C:1](=O)-[NH:2]-[C:3]"
    ]
}