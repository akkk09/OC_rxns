# ==========================================
# ALKENE ADDITION ENGINE (EXHAUSTIVE OLYMPIAD LEVEL)
# ==========================================

def generate_markovnikov(nu_smarts):
    """
    Advanced Markovnikov Addition (Carbocation Pathway via Electrophilic Attack).
    Proton adds to the less substituted carbon to generate the most stable intermediate carbocation.
    """
    return [
        # Asymmetric terminal alkenes: Proton goes to terminal CH2, nucleophile to substituted carbon
        f"[CH2:1]=[CH1,CH0:2] >> [C:1]-[C:2]-{nu_smarts}",
        
        # Asymmetric trisubstituted alkenes
        f"[CH1:1]=[CH0:2] >> [C:1]-[C:2]-{nu_smarts}",
        
        # Symmetric matrices
        f"[CH2:1]=[CH2:2] >> [C:1]-[C:2]-{nu_smarts}",
        f"[CH1:1]=[CH1:2] >> [C:1]-[C:2]-{nu_smarts}",
        f"[CH0:1]=[CH0:2] >> [C:1]-[C:2]-{nu_smarts}"
    ]

def generate_anti_markovnikov(nu_smarts):
    """
    Anti-Markovnikov Addition (Radical Chain Mechanism or Concerted Boron Addition).
    """
    return [
        f"[CH2:1]=[CH1,CH0:2] >> [C:1](-{nu_smarts})-[C:2]",
        f"[CH1:1]=[CH0:2] >> [C:1](-{nu_smarts})-[C:2]",
        f"[CH2:1]=[CH2:2] >> [C:1](-{nu_smarts})-[C:2]",
        f"[CH1:1]=[CH1:2] >> [C:1](-{nu_smarts})-[C:2]",
        f"[CH0:1]=[CH0:2] >> [C:1](-{nu_smarts})-[C:2]"
    ]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
ALKENE_RULES = {
    
    # ==========================================
    # 1. HYDROHALOGENATION & ELECTROPHILIC ADDITIONS
    # ==========================================
    
    "HBr / Ionic Addition (Markovnikov Hydrobromination)": {
        "rules": generate_markovnikov("[Br]"),
        "poisons": ["[O]-[O]"],
        "poison_message": "Peroxide effect intervention: The presence of alkyl peroxides alters the mechanism from ionic electrophilic addition to a radical chain pathway, shifting product formation to anti-Markovnikov addition."
    },
    
    "HCl / Anhydrous Conditions (Ionic Hydrochlorination)": {
        "rules": generate_markovnikov("[Cl]") # Radical addition of HCl is thermodynamically unfavorable
    },
    
    "HBr / Organic Peroxides, UV Light (Kharasch Radical Anti-Markovnikov Addition)": {
        "rules": generate_anti_markovnikov("[Br]")
    },

    # ==========================================
    # 2. HYDRATION PATHWAYS (MARKOVNIKOV VS. ANTI-MARKOVNIKOV)
    # ==========================================

    "H2O / Catalytic H2SO4 (Acid-Catalyzed Hydration with Carbocation Shifts)": {
        "rules": generate_markovnikov("[OH]")
    },
    
    "Hg(OAc)2 / H2O followed by NaBH4 Reduction (Oxymercuration-Demercuration)": {
        "rules": generate_markovnikov("[OH]"),
        "poisons": ["[CX4](C)(C)(C)-C=C"], # Extremely hindered sterics
        "poison_message": "Oxymercuration failure: Highly hindered alkenes obstruct mercurinium ion formation."
    },

    "B2H6 / THF followed by Alkaline H2O2 (Stereospecific Syn-Hydroboration-Oxidation)": {
        "rules": generate_anti_markovnikov("[OH]")
    },

    # ==========================================
    # 3. STEREOSPECIFIC HALOGENATION & PSEUDOHALOGENATION
    # ==========================================

    "Br2 / CCl4 Dark Conditions (Stereospecific Anti-Dihydrohalogenation via Halonium Ion)": {
        "rules": [
            # Halogenation proceeds via a cyclic bromonium intermediate followed by back-side attack,
            # ensuring rigorous anti-addition stereochemistry across internal double bonds.
            "[#6:1]-[C:2]=[C:3]-[#6:4] >> [#6:1]/[C:2](-[Br])-[C:3](-[Br])/[#6:4]"
        ]
    },
    
    "Cl2 / CCl4 (Chlorination via Cyclic Chloronium Intermediate)": {
        "rules": [
            "[#6:1]-[C:2]=[C:3]-[#6:4] >> [#6:1]/[C:2](-[Cl])-[C:3](-[Cl])/[#6:4]"
        ]
    },

    "ICl / CH2Cl2 (Regioselective Halogen Iodination)": {
        "rules": [
            # Electrophilic iodine monochloride addition placing iodine at the less substituted 
            # and chlorine at the more substituted carbon position.
            "[CH2:1]=[CH1,CH0:2] >> [C:1](-[I])-[C:2]-[Cl]"
        ]
    },

    # ==========================================
    # 4. EPOXIDATION, DIHYDROXYLATION & CYCLOPROPANATION
    # ==========================================

    "mCPBA / CH2Cl2 (Concerted Stereospecific Epoxidation)": {
        "rules": [
            # Peroxyacid epoxidation transfers oxygen in a concerted syn-addition fashion, 
            # preserving cis/trans alkene geometry inside an oxirane ring.
            "[C:1]=[C:2] >> [C:1]1-[C:2]-O1"
        ]
    },
    
    "OsO4 / Catalytic NMO, Aqueous Acetone (Stereospecific Syn-Dihydroxylation)": {
        "rules": [
            # Concerted [3+2] cycloaddition yielding a cyclic osmate ester intermediate, 
            # hydrolyzing with retention to form a cis-1,2-diol (syn-addition).
            "[C:1]=[C:2] >> [C:1](-[OH])-[C:2](-[OH])"
        ]
    },

    "CH2I2 / Zn-Cu Couple (Simmons-Smith Syn-Cyclopropanation)": {
        "rules": [
            # Carbenoid generation transferring a methylene unit directly across the alkene pi-bond 
            # in a concerted, stereospecific syn-addition to yield cyclopropane rings.
            "[C:1]=[C:2] >> [C:1]1-[C:2]-[CH2]-1"
        ]
    },

    # ==========================================
    # 5. CATALYTIC REDUCTION & OXIDATIVE CLEAVAGE
    # ==========================================

    "H2 / Pt or Pd/C Catalyst, Ethanol (Catalytic Syn-Hydrogenation)": {
        "rules": [
            # Heterogeneous catalytic reduction delivering hydrogen atoms from the catalyst surface 
            # in a stereospecific syn-addition fashion across the alkene bond.
            "[C:1]=[C:2] >> [C:1](-H)-[C:2](-H)"
        ]
    },

    "O3 followed by Dimethyl Sulfide (Reductive Ozonolysis Cleavage)": {
        "rules": [
            # Cleavage of alkene carbon-carbon double bonds into independent aldehyde or ketone components 
            # without over-oxidation to carboxylic acids.
            "[C:1]=[C:2] >> [C:1]=O.[C:2]=O"
        ]
    },

    "Hot Concentrated KMnO4 / H3O+ (Oxidative Cleavage to Acids/Ketones)": {
        "rules": [
            # Vigorous oxidative cleavage converting terminal and internal alkenes 
            # into respective carboxylic acids or ketones.
            "[C:1]=[C:2] >> [C:1](=O)[OH].[C:2](=O)[OH]"
        ]
    }
}