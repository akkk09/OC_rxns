# ==========================================
# ALDEHYDE & KETONE ENGINE (EXHAUSTIVE OLYMPIAD LEVEL)
# ==========================================

# --- ADVANCED STRUCTURAL POISONS & CLASSIFICATIONS ---
HAS_ALPHA_H = ["[CX4H1,CX4H2,CX4H3]-[CX3]=O"]
STERICALLY_HINDERED_ENOLATE = ["[CX4](C)(C)(C)-[CX3]=O"] # Highly branched alpha carbons inhibit aldol addition rates
ENOLIZABLE_ALDEHYDE_KETONE = [
    "[CX4H1,CX4H2,CX4H3]-[CX3]=O", 
    "[cH1]1[cH][cH][cH][cH][c]1-[CX3]=O" # Includes aromatic systems with ortho/para enolizable sites
]
STABLE_AMIDE_ESTER = ["[CX3](=O)-[OX2,NX3]"]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
ALDEHYDE_KETONE_RULES = {

    # ==========================================
    # 1. NUCLEOPHILIC ADDITION & EQUILIBRIA
    # ==========================================

    "HCN / KCN, pH 9-10 (Cyanohydrin Addition Equilibrium)": {
        "rules": [
            # Base-catalyzed nucleophilic addition of cyanide ion to carbonyl electrophiles,
            # thermodynamically controlled by ring strain and steric environment.
            "[CX3:1]=O >> [C:1](-[OH])-[C]#N"
        ],
        "poisons": STABLE_AMIDE_ESTER,
        "poison_message": "Cyanohydrin addition failure: Amides, esters, and carboxylates possess excessive resonance stabilization, shutting down nucleophilic addition by cyanide."
    },

    "Sodium Bisulfite / Aqueous Buffer (Alpha-Hydroxysulfonate Adduct Formation)": {
        "rules": [
            # Reversible bisulfite addition used for the selective separation and purification 
            # of unhindered aldehydes and methyl ketones as crystalline salts.
            "[CX3:1]=O >> [C:1](-[OH])-[SX4](=O)(=O)[O-]"
        ],
        "poisons": ["[CX4](C)(C)-[CX3]=O", "[CX4](C)(C)(C)-[CX3]=O"],
        "poison_message": "Bisulfite addition failure: Sterically hindered ketones block the formation of bulky alpha-hydroxysulfonate tetrahedral adducts."
    },

    # ==========================================
    # 2. ACETAL PROTECTIVE & DEPROTECTIVE PROTOCOLS
    # ==========================================

    "Ethylene Glycol / Anhydrous TsOH, Dean-Stark Trapping (Cyclic Acetal Synthesis)": {
        "rules": [
            # Acid-catalyzed formation of 1,3-dioxolane protective groups driven forward 
            # by continuous physical removal of water vapor.
            "[CX3:1]=O >> [C:1]1-[O]-[CH2]-[CH2]-[O]-1"
        ]
    },

    "Aqueous HCl / Acetone, Room Temp (Acetal Deprotection & Regeneration)": {
        "rules": [
            # Oxonium-ion mediated hydrolysis restoring the parent carbonyl moiety.
            "[C:1]1-[O]-[CH2]-[CH2]-[O]-1 >> [C:1]=O"
        ]
    },

    "1,2-Ethanedithiol / BF3·OEt2 (Thioacetal / Thioketal Formation)": {
        "rules": [
            # Conversion of carbonyl functionalities into 1,3-dithiolanes, 
            # a prerequisite for subsequent Mozingo reduction (Raney Ni desulfurization).
            "[CX3:1]=O >> [C:1]1-[S]-[CH2]-[CH2]-[S]-1"
        ]
    },

    # ==========================================
    # 3. ALDOL ADDITION, CONDENSATION, & CROSSLINKING
    # ==========================================

    "Dilute NaOH / Low Temp (Base-Catalyzed Aldol Addition)": {
        "rules": [
            # Reversible carbon-carbon bond forming reaction between enolizable carbonyl donors 
            # and electrophilic acceptors to yield beta-hydroxy carbonyl structures.
            "[CX4H2,CX4H3:1]-[CX3:2]=O.[CX3:3]=O >> [C:1](-[OH])-[C:2](=O)-[C:3]=O"
        ],
        "poisons": STERICALLY_HINDERED_ENOLATE,
        "poison_message": "Aldol addition failure: Sterically encumbered enolizable systems experience prohibitive steric congestion during tetrahedral carbon-carbon coupling."
    },

    "Dilute NaOH / Thermal Conditions (Aldol Condensation & E1cB Elimination)": {
        "rules": [
            # Dehydration of beta-hydroxy carbonyl intermediates via an E1cB pathway 
            # to generate stable, conjugated alpha,beta-unsaturated systems.
            "[CX4H2,CX4H3:1]-[CX3:2]=O.[CX3:3]=O >> [C:3]=[C:1]-[C:2]=O"
        ],
        "poisons": STERICALLY_HINDERED_ENOLATE,
        "poison_message": "Aldol condensation failure: Requires accessible alpha-hydrogens and structural geometry conducive to base-promoted water elimination."
    },

    "Ba(OH)2 / Warm Aqueous Conditions (Directed Cross-Aldol / Claisen-Schmidt Condensation)": {
        "rules": [
            # Condensation between aromatic aldehydes (lacking alpha-protons) and enolizable aliphatic ketones 
            # to yield single-product alpha,beta-unsaturated enones (e.g., dibenzalacetone).
            "[cH1]1[cH][cH][cH][cH][c]1-[CX3:1]=O.[CX4H3]-[CX3:2]=O >> [c]1[cH][cH][cH][cH][c]1-[C:1]=[C]-[CX3:2]=O"
        ]
    },

    # ==========================================
    # 4. DISPROPORTIONATION & REDOX PATHWAYS
    # ==========================================

    "Concentrated KOH / Room Temp (Cannizzaro Disproportionation)": {
        "rules": [
            # Base-mediated hydride transfer between two non-enolizable aldehyde molecules, 
            # yielding equivalent quantities of primary alcohol and carboxylate salt.
            "[CX3H1:1]=O.[CX3H1:2]=O >> [C:1]-[OH].[O-]-[C:2]=O"
        ],
        "poisons": HAS_ALPHA_H,
        "poison_message": "Cannizzaro reaction failure: Presence of acidic alpha-hydrogens triggers rapid base-mediated aldol polymerization instead of redox disproportionation."
    },

    "I2 / Aqueous NaOH (Iodoform Cleavage Assay)": {
        "rules": [
            # Sequential base-promoted alpha-iodination followed by hydroxide-mediated cleavage 
            # of methyl ketones to form carboxylates and iodoform.
            "[CH3:1]-[C:2](=O)-[#6,#1:3] >> [O-]-[C:2](=O)-[#6,#1:3].[C:1](I)(I)I"
        ],
        "poisons": ["[CH2]-[CX3]=O", "[CH1]-[CX3]=O", "[CH0]-[CX3]=O"],
        "poison_message": "Iodoform test failure: Requires an active terminal methyl ketone architecture. Non-methyl ketones fail to form triiodo reaction intermediates."
    },

    # ==========================================
    # 5. NITROGEN DERIVATIVE CONDENSATIONS & QUALITATIVE TESTS
    # ==========================================

    "Hydroxylamine Hydrochloride / Sodium Acetate Buffer (Oxime Derivatization)": {
        "rules": [
            # Nucleophilic addition of hydroxylamine followed by rapid dehydration 
            # to yield crystalline oximes (existing as geometric E/Z isomer mixtures).
            "[CX3:1]=O >> [C:1]=[N]-[OH]"
        ]
    },

    "Phenylhydrazine / Acetic Acid Catalyst (Phenylhydrazone Synthesis)": {
        "rules": [
            # Condensation yielding crystalline phenylhydrazone derivatives for physical melting-point characterization.
            "[CX3:1]=O >> [C:1]=[N]-[NH]-[c]1[cH][cH][cH][cH][cH]1"
        ]
    },

    "2,4-DNP / Sulfuric Acid / Ethanol (Brady's Reagent - Qualitative Carbonyl Test)": {
        "rules": [
            # Acid-catalyzed condensation using electron-deficient 2,4-dinitrophenylhydrazine 
            # to generate intensely colored red/yellow crystalline precipitates.
            "[CX3:1]=O >> [C:1]=[N]-[NH]-[c]1[cH][c](-[N+](=O)[O-])[cH][c](-[N+](=O)[O-])[cH]1"
        ],
        "poisons": ["[CX3](=O)-[OH]", "[CX3](=O)-[O]-[#6]", "[CX3](=O)-[NX3]"],
        "poison_message": "Brady's test failure: Carboxylic acids and carboxylic acid derivatives are resonance-stabilized and unreactive toward 2,4-DNP nucleophilic addition."
    }
}