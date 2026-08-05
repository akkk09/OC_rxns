# ==========================================
# AMINES & NITROGEN COMPOUNDS ENGINE (EXHAUSTIVE OLYMPIAD & GRADUATE LEVEL)
# ==========================================

# --- NITROGEN TRAPS & POISONS ---
SECONDARY_TERTIARY_AMINES = ["[NX3H1]", "[NX3H0]"]
ARYL_HALIDES = ["[c]-[F,Cl,Br,I]"]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
NITROGEN_RULES = {

    # ==========================================
    # 1. QUALITATIVE IDENTIFICATION (CARBYLAMINE TEST)
    # ==========================================

    "CHCl3 / KOH, Thermal Flash (Carbylamine Reaction for Primary Amines)": {
        "rules": [
            # Converts ONLY Primary Amines (Aliphatic and Aromatic) to Isocyanides
            # Formal charges explicitly mapped: Nitrogen is positive (+), Carbon is negative (-)
            "[#6,c:1]-[NX3H2:2] >> [#6,c:1]-[N+:2]#[C-]"
        ],
        "poisons": SECONDARY_TERTIARY_AMINES,
        "poison_message": "The Carbylamine test strictly requires a primary amine! Secondary and tertiary amines cannot provide the two necessary protons required to form the triple bond of the foul-smelling isocyanide network."
    },

    # ==========================================
    # 2. DIAZOTIZATION & BIFURCATION PATHWAYS
    # ==========================================

    "NaNO2 / Aqueous HCl, 0-5°C (Diazotization Cascade)": {
        "rules": [
            # 1. Aromatic Primary Amines -> Stable Aromatic Diazonium Salt
            # Resonance stabilization allows the N2+ leaving group to persist at low temperatures.
            "[c:1]-[NX3H2:2] >> [c:1]-[N+:2]#[N]",
            
            # 2. Aliphatic Primary Amines -> Carbocation Intermediates -> Alcohols / Alkenes
            # The aliphatic diazonium ion is highly unstable, instantly ejecting N2 gas 
            # to form a reactive carbocation trapped by solvent water.
            "[CX4:1]-[NX3H2:2] >> [C:1]-[OH]"
        ],
        "poisons": SECONDARY_TERTIARY_AMINES,
        "poison_message": "Diazotization bifurcation failure: Secondary amines form yellow oily N-nitrosamines. Tertiary amines undergo protonation or ring nitrosation. Only primary amines generate the diazonium species."
    },

    # ==========================================
    # 3. GABRIEL PHTHALIMIDE SYNTHESIS
    # ==========================================

    "Gabriel Phthalimide Sequence (Base-Mediated Primary Amine Synthesis)": {
        "rules": [
            # Strictly converts accessible primary and secondary alkyl halides into primary amines via SN2 substitution
            "[CX4:1]-[Cl,Br,I] >> [C:1]-[NH2]"
        ],
        "poisons": ARYL_HALIDES + ["[CX4H0]-[Cl,Br,I]"], 
        "poison_message": "Gabriel Phthalimide failure: Relies on a clean SN2 nucleophilic attack by the bulky phthalimide anion. Aryl halides cannot undergo SN2 due to sp2 partial double-bond character (aniline synthesis is impossible here), and tertiary halides strictly undergo quantitative E2 elimination."
    },

    # ==========================================
    # 4. EXHAUSTIVE METHYLATION & HOFMANN ELIMINATION
    # ==========================================

    "CH3I (Excess) followed by Ag2O / Heat (Exhaustive Hofmann Elimination)": {
        "rules": [
            # E2 Beta-Elimination yielding the LEAST substituted alkene (Anti-Zaitsev / Hofmann Product)
            # The bulky quaternary ammonium leaving group controls the transition state geometry.
            "[CH3,CH2,CH1:1]-[CX4:2]-[NX3,NX4+] >> [C:1]=[C:2]"
        ]
    },

    # ==========================================
    # 5. REDUCTION OF NITRO COMPOUNDS
    # ==========================================

    "Sn / Concentrated HCl or Fe / HCl (Chemoselective Acidic Nitro Reduction)": {
        "rules": [
            # The standard laboratory and industrial protocol for reducing aromatic and aliphatic nitro groups to primary amines
            "[#6,c:1]-[N+](=O)[O-] >> [#6,c:1]-[NH2]"
        ]
    },
    
    # ==========================================
    # 6. SANDMEYER & GATTERMANN TRANSFORMATIONS
    # ==========================================

    "CuCl / Aqueous HCl (Sandmeyer Chlorination)": {
        "rules": [
            # Replaces the aromatic diazonium group with a chloride atom via a copper-mediated radical mechanism
            "[c:1]-[N+]#[N] >> [c:1]-[Cl]"
        ],
        "poisons": ["[CX4]-[N+]#[N]"],
        "poison_message": "Sandmeyer failure: Aliphatic diazonium salts decompose spontaneously into nitrogen gas. The reaction requires the transient low-temperature stability of an AROMATIC diazonium salt."
    }
}