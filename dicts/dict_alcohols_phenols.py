# ==========================================
# ALCOHOLS, PHENOLS, & ETHERS ENGINE (EXHAUSTIVE OLYMPIAD LEVEL)
# ==========================================

# --- ADVANCED STRUCTURAL POISONS & CLASSIFICATIONS ---
PRIMARY_ALCOHOLS = ["[CX4H2,CX4H3]-[OH]"]
ALIPHATIC_ALCOHOLS = ["[CX4]-[OH]"]
PHENOLS_ONLY = ["[CX4]-[OH]"] 

# Bredt's Rule Violation: Bridgehead carbons cannot host double bonds in small/medium rings
BREDT_VIOLATION_SYSTEMS = ["[CX4H0]1-[#6]-[#6]-[CX4H0]2-[#6]-[#6]-1-[#6]-2"] 

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
ALCOHOL_PHENOL_RULES = {

    # ==========================================
    # 1. QUALITATIVE ALCOHOL IDENTIFICATION
    # ==========================================

    "ZnCl2 / conc. HCl (Lucas Reagent - SN1 Carbocation Pathway)": {
        "rules": [
            # Tertiary Alcohols -> Immediate turbidity via stable tertiary carbocation SN1 transition states
            "[CX4H0:1]-[OH] >> [C:1]-[Cl]",
            
            # Secondary Alcohols -> Turbidity manifest upon mild heating or extended time profiles
            "[CX4H1:1]-[OH] >> [C:1]-[Cl]"
        ],
        "poisons": PRIMARY_ALCOHOLS + ["[c]-[OH]"],
        "poison_message": "Lucas Test failure: Primary alcohols and phenolic matrices cannot form the high-energy primary carbocations or resonance-stabilized oxonium species necessary for SN1 displacement at ambient conditions."
    },

    "I2 / NaOH / Heat (Iodoform Test for Methyl Carbinols)": {
        "rules": [
            # Oxidation of secondary methyl carbinols to methyl ketones followed by exhaustive alpha-iodination 
            # and hydroxide-mediated carbon-carbon cleavage to yield iodoform precipitate.
            "[CH3:1]-[CH1:2](-[OH])-[#6:3] >> [O-]-[C:2](=O)-[#6:3].[C:1](I)(I)I",
            
            # Special primary alcohol case: Ethanol undergoes rapid oxidation and cleavage to iodoform.
            "[CH3:1]-[CH2:2]-[OH] >> [H]-[C:2](=O)[O-].[C:1](I)(I)I"
        ],
        "poisons": ["[CX4](C)(C)(C)-[OH]"],
        "poison_message": "Iodoform test failure: Requires a terminal methyl carbinol structural unit (CH3-CH(OH)-R or ethanol). Other secondary or tertiary alcohols yield negative results."
    },

    # ==========================================
    # 2. ACID-CATALYZED DEHYDRATION & SKELETAL REARRANGEMENTS
    # ==========================================

    "Conc. H2SO4 / Thermal Conditions (E1 Dehydration & Zaitsev Elimination)": {
        "rules": [
            # Acid-catalyzed protonation of hydroxyl group yielding a good leaving group (H2O), 
            # forming an intermediate carbocation followed by Zaitsev-preferred elimination.
            "[CH3,CH2,CH1:1]-[CX4:2]-[OH] >> [C:1]=[C:2]"
        ],
        "poisons": BREDT_VIOLATION_SYSTEMS + ["[c]-[OH]"],
        "poison_message": "Dehydration failure: Phenols are completely unreactive toward acid dehydration due to partial double-bond character of the C-O bond. Bridgehead matrices are locked by Bredt's rule."
    },

    "H2SO4 / Thermal Reflux (Pinacol-Pinacolone Rearrangement)": {
        "rules": [
            # Acid-catalyzed dehydration of 1,2-diols to yield stabilized carbonyl frameworks 
            # driven by concerted 1,2-alkyl or aryl shifts and carbocation stabilization relief.
            "[C:1](-[OH])-[CX4:2](-[OH])(-[#6])-[#6] >> [C:1](=O)-[CH:2](-[#6])-[#6]"
        ]
    },

    # ==========================================
    # 3. CLASSIC NAME REACTIONS OF PHENOLS
    # ==========================================

    "CHCl3 / Aqueous NaOH, 70°C (Reimer-Tiemann Ortho-Formylation)": {
        "rules": [
            # Base-mediated alpha-elimination of chloroform generating electrophilic dichlorocarbene (:CCl2),
            # which intercepts the in-situ generated phenoxide ion to form ortho-hydroxybenzaldehyde (salicylaldehyde).
            "[c:1](-[OH])[cH1:2] >> [c:1](-[OH])[c:2]-[C](=O)[H]"
        ],
        "poisons": PHENOLS_ONLY,
        "poison_message": "Reimer-Tiemann reaction failure: Strictly requires an acidic phenolic hydroxyl group to generate the ambient phenoxide nucleophile required for carbene attack."
    },
    
    "CO2 / NaOH, 125°C, High Pressure (Kolbe-Schmitt Ortho-Carboxylation)": {
        "rules": [
            # Reversible thermal carboxylation of dry sodium phenoxide using carbon dioxide 
            # to synthesize ortho-hydroxybenzoic acid (salicylic acid).
            "[c:1](-[OH])[cH1:2] >> [c:1](-[OH])[c:2]-[C](=O)[OH]"
        ],
        "poisons": PHENOLS_ONLY,
        "poison_message": "Kolbe-Schmitt reaction failure: Requires a dry phenoxide salt under elevated barometric pressure to force electrophilic addition of carbon dioxide to the ring."
    },

    "NaOH / High Temp & Pressure followed by Acidification (Industrial Dow Process for Phenols)": {
        "rules": [
            # Nucleophilic aromatic substitution (SNAr via benzyne intermediate pathways under extreme conditions) 
            # converting chlorobenzenes directly into phenol derivatives.
            "[c:1]-[Cl] >> [c:1]-[OH]"
        ]
    },

    # ==========================================
    # 4. STEREOMIS-MECHANISTIC ETHER CLEAVAGE (ZEISEL METHOD)
    # ==========================================

    "Cold HI (1 Equivalent - Mechanistic SN1 vs SN2 Ether Cleavage)": {
        "rules": [
            # 1. Alkyl-Aryl Ethers (Anisole matrices): Phenolic C-O-C bond resists cleavage due to resonance; yields Phenol + Alkyl Iodide
            "[c:1]-[O:2]-[CX4:3] >> [c:1]-[OH:2].[C:3]-[I]",
            
            # 2. Dialkyl Ethers featuring Tertiary/Benzyl groups: Rapid SN1 ionization yielding tertiary alkyl iodides + alcohols
            "[CX4H0:1]-[O:2]-[CX4:3] >> [C:1]-[I].[OH:2]-[C:3]",
            
            # 3. Primary/Secondary Dialkyl Ethers: Nucleophilic SN2 attack of iodide on the less sterically hindered carbon center
            "[CX4H2,CX4H1:1]-[O:2]-[CX4H3,CX4H2:3] >> [C:1]-[OH:2].[C:3]-[I]"
        ]
    },
    
    "Excess Concentrated HI / Reflux (Exhaustive Ether Cleavage)": {
        "rules": [
            # 1. Alkyl-Aryl Ethers: Aryl oxygen bond remains completely intact; forms Phenol + Alkyl Iodide
            "[c:1]-[O:2]-[CX4:3] >> [c:1]-[OH:2].[C:3]-[I]",
            
            # 2. Dialkyl Ethers: Exhaustive transformation of both hydrocarbon fragments into respective alkyl iodides
            "[CX4:1]-[O]-[CX4:2] >> [C:1]-[I].[C:2]-[I]"
        ]
    }
}