ADVANCED_REARRANGEMENT_RULES = {
    # 1. Favorskii Rearrangement
    # Alpha-halo ketones react with base to form a highly strained cyclopropanone intermediate, 
    # which then opens to form a carboxylic acid or ester (shown here forming an acid).
    "NaOH / H2O (Favorskii)": [
        "[C:1]-[C:2](=O)-[CH:3]-[Cl,Br:4] >> [C:1]-[CH:3]-[C:2](=O)[OH]"
    ],

    # 2. Benzilic Acid Rearrangement
    # A 1,2-diketone undergoes a 1,2-alkyl shift in the presence of strong base.
    "KOH / Heat, then H3O+ (Benzilic Acid)": [
        "[c:1]-[C:2](=O)-[C:3](=O)-[c:4] >> [c:1]-[C:2](-[OH])(-[c:4])-[C:3](=O)[OH]"
    ],

    # 3. Aliphatic Claisen Rearrangement
    # A [3,3]-sigmatropic rearrangement of an allyl vinyl ether, triggered entirely by heat.
    "Heat / 200°C (Claisen)": [
        # Allyl vinyl ether -> gamma,delta-unsaturated ketone
        "[O:1](-[C:2]=[C:3])-[CH2:4]-[CH:5]=[CH2:6] >> [O:1]=[C:2]-[C:3]-[CH2:6]-[CH:5]=[CH2:4]"
    ],
    
    # 4. Beckmann Fragmentation
    # If an oxime has an alpha-quaternary carbon, it fragments into a nitrile and a carbocation 
    # (which gets trapped by water to form an alcohol) instead of normal rearrangement.
    "H2SO4 / Heat (Beckmann Fragmentation)": [
        "[C:1](=[N:2]-[OH])-[C:3](-[C])(-[C])(-[C]) >> [C:1]#[N:2].[C:3]-[OH]"
    ]
}