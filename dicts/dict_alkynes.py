# ==========================================
# ALKYNE ENGINE (EXHAUSTIVE OLYMPIAD & GRADUATE LEVEL)
# ==========================================

def generate_kucherov_hydration():
    """
    Acid and Mercury(II)-catalyzed Markovnikov hydration of alkynes.
    Proceeds via mercurinium ion formation followed by water attack and tautomerization.
    """
    return [
        # Terminal alkynes -> Methyl ketones (Markovnikov orientation via stable secondary oxonium intermediates)
        "[C:1]#[CH1:2] >> [C:1](=O)-[C:2]",
        
        # Internal unsymmetrical alkynes -> Constitutional ketone mixtures based on electronic stabilization
        "[CH0:1]#[CH0:2] >> [C:1](=O)-[C:2]"
    ]

def generate_hydroboration_oxidation():
    """
    Regioselective Anti-Markovnikov Hydration via sterically hindered organoboranes (Sia2BH or Borane).
    Terminal alkynes yield aldehydes following oxidation.
    """
    return [
        # Terminal alkynes -> Aldehydes (Anti-Markovnikov regioselectivity)
        "[C:1]#[CH1:2] >> [C:1]-[C:2]=O",
        
        # Internal alkynes -> Ketones
        "[CH0:1]#[CH0:2] >> [C:1](=O)-[C:2]"
    ]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
ALKYNE_RULES = {
    
    # ==========================================
    # 1. HYDRATION & TAUTOMERIC CONTROL
    # ==========================================
    
    "HgSO4 / Aqueous H2SO4 (Kucherov Markovnikov Hydration to Ketones)": {
        "rules": generate_kucherov_hydration()
    },
    
    "Sterically Hindered Hydroboration followed by Alkaline H2O2 (Anti-Markovnikov Hydration)": {
        "rules": generate_hydroboration_oxidation()
    },

    "HBr (1 Equivalent) / Ionic Addition (Markovnikov Vinyl Bromide Synthesis)": {
        "rules": [
            # Electrophilic addition across triple bonds following Markovnikov regioselectivity
            "[C:1]#[CH1:2] >> [C:1](-[Br])=[CH2:2]"
        ]
    },
    
    "Excess HBr / Ionic Addition (Geminal Dihalide Formation)": {
        "rules": [
            # Exhaustive hydrohalogenation yielding geminal dihalides via sequential Markovnikov additions
            "[C:1]#[C:2] >> [C:1]([Br])([Br])-[CH2:2]"
        ]
    },
    
    # ==========================================
    # 2. STEREOSPECIFIC REDUCTION PATHWAYS
    # ==========================================
    
    "H2 / Poisoned Palladium - Lindlar Catalyst (Stereospecific Syn-Hydrogenation to Z-Alkenes)": {
        "rules": [
            # Internal Alkynes -> CIS (Z) Alkenes via concerted heterogeneous metal-surface syn-addition
            "[#6:1]-[C:2]#[C:3]-[#6:4] >> [#6:1]/[CH1:2]=[CH1:3]\[#6:4]",
            
            # Terminal Alkynes -> Unsubstituted Terminal Alkenes
            "[#6:1]-[C:2]#[CH1:3] >> [#6:1]-[CH1:2]=[CH2:3]"
        ]
    },
    
    "Na / Liquid NH3 (Dissolving Metal Birch Reduction to E-Alkenes)": {
        "rules": [
            # Internal Alkynes -> TRANS (E) Alkenes via stepwise single-electron transfer (SET) and vinyl anion inversion
            "[#6:1]-[C:2]#[C:3]-[#6:4] >> [#6:1]/[CH1:2]=[CH1:3]/[#6:4]"
        ],
        "poisons": ["[CH1]#[C]"], 
        "poison_message": "Birch reduction intervention: Terminal alkynes possess an activated acidic sp-hybridized C-H proton (pKa ~ 25). Dissolving metals act as strong Brønsted bases, abstracting the proton to generate an unreactive sodium acetylide salt instead of performing reduction."
    },
    
    "H2 / Excess Raney Ni or Pt Catalyst (Exhaustive Hydrogenation to Alkanes)": {
        "rules": [
            # Complete saturation of triple bonds down to fully saturated saturated alkanes
            "[C:1]#[C:2] >> [C:1]-[C:2]"
        ]
    },

    # ==========================================
    # 3. HALOGENATION & OXIDATIVE CLEAVAGE
    # ==========================================

    "Br2 (1 Equivalent) / CCl4 (Stereospecific Anti-Addition Dihalogenation)": {
        "rules": [
            # Halogenation proceeding via cyclic halonium intermediates, yielding trans-dihaloalkenes
            "[#6:1]-[C:2]#[C:3]-[#6:4] >> [#6:1]/[C:2](-[Br])=[C:3](-[Br])/[#6:4]"
        ]
    },

    "O3 followed by Aqueous Workup or KMnO4 (Oxidative Cleavage of Alkynes)": {
        "rules": [
            # Oxidative cleavage breaking triple bonds to yield corresponding carboxylic acids
            "[C:1]#[C:2] >> [C:1](=O)[OH].[C:2](=O)[OH]"
        ]
    },

    # ==========================================
    # 4. TERMINAL ALKYNE ACIDITY & METAL ACETYLIDES
    # ==========================================

    "NaNH2 / Liquid Ammonia (Strong Base Terminal Deprotonation)": {
        "rules": [
            # Deprotonation of terminal alkyne to synthesize nucleophilic sodium acetylides for chain homologation
            "[C:1]#[CH1:2] >> [C:1]#[C:2]-[Na]"
        ]
    },
    
    "Ammoniacal AgNO3 / Aqueous NH3 (Tollens Qualitative Detection of Terminal Alkynes)": {
        "rules": [
            # Precipitation of white/off-white silver acetylide complexes confirming terminal triple bonds
            "[C:1]#[CH1:2] >> [C:1]#[C:2]-[Ag]" 
        ]
    },

    "Ammoniacal CuCl / Aqueous NH3 (Cuprous Acetylide Precipitation Test)": {
        "rules": [
            # Formation of characteristic red/brown copper(I) acetylide precipitates
            "[C:1]#[CH1:2] >> [C:1]#[C:2]-[Cu]"
        ]
    }
}