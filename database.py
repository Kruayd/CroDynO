import fitclasses as ftc

Hp_from_H2_target = {
    'H2 + H2 -> fast H+ low energy':
        ftc.BarnettChebFit((2.5e3, 5.0e4), 'H+ production from H2 + H2 at low'
                           ' energies.\n'
                           'Reference: ATOMIC DATA FOR FUSION VOLUME 1'
                           ' COLLISIONS OF H, H2, He and Li ATOMS and IONS'
                           ' with ATOMS and MOLECULES. C. F. Barnett.\n'
                           'Notes: This data involves the sum of the cross'
                           ' sections for the products: σ(H+ + H)proj + 2σ(H+'
                           ' + H+)proj + σ(H+ + H-). No attempt has been made'
                           ' to join the high and low energy data sets.\n'
                           'Accuracy: Unknown',
                           2,
                           (-75.7161, .371301, -.373363, -.209805, -.0677263,
                            -.00389719, .0259767)),
    'H2 + H2 -> fast H+ high energy':
        ftc.BarnettChebFit((1.5e5, 6.0e5), 'H+ production from H2 + H2 at high'
                           ' energies\n'
                           'Reference: ATOMIC DATA FOR FUSION VOLUME 1'
                           ' COLLISIONS OF H, H2, He and Li ATOMS and IONS'
                           ' with ATOMS and MOLECULES. C. F. Barnett.\n'
                           'Notes: This data involves the sum of the cross'
                           ' sections for the products: σ(H+ + H)proj + 2σ(H+'
                           ' + H+)proj + σ(H+ + H-). No attempt has been made'
                           ' to join the high and low energy data sets.\n'
                           'Accuracy: Unknown',
                           2,
                           (-75.8616, -.542987, .0642733, .0118753, -.00148111,
                            .000221649, .00636358))
}

H_from_H2_target = {
    'H2 + H2 -> fast H':
        ftc.BarnettChebFit((2.5e3, 5.0e4), 'H production from H2 + H2\n'
                           'Reference: ATOMIC DATA FOR FUSION VOLUME 1'
                           ' COLLISIONS OF H, H2, He and Li ATOMS and IONS'
                           ' with ATOMS and MOLECULES. C. F. Barnett.\n'
                           'Notes: This data involves the sum of the cross'
                           ' sections for the products: σ(H+ + H)proj + 2σ(H +'
                           ' H)proj. Variations in ion source conditions'
                           ' produce changes up to 10% in the measured'
                           ' values.\n'
                           'Accuracy: 40%',
                           2,
                           (-71.7329, -.200109, -.223241, -.0773361, -.0140887,
                            .0563185, -.00955263)),
}

H2p_from_H2_target = {
}

H2_from_H2_target = {
    'H2 + H2 -> H2 destruction':
        ftc.BarnettChebFit((1.3e3, 5.0e4), 'Total H2 destruction from H2 +'
                           ' H2\n'
                           'Reference: ATOMIC DATA FOR FUSION VOLUME 1'
                           ' COLLISIONS OF H, H2, He and Li ATOMS and IONS'
                           ' with ATOMS and MOLECULES. C. F. Barnett.\n'
                           'Notes: This cross section is the sum of cross'
                           ' sections for all reactions that destroy the fast'
                           ' H2 molecule in passage through H2, i.e. those'
                           ' producing fast H2+, (H + H), (H + H+) and (H+ +'
                           ' H+) products. Large variations in ion source'
                           ' operating conditions were  found to produce'
                           ' changes up to 10% in the measured cross section\n'
                           'Accuracy: 20%',
                           2,
                           (-71.8671, .380700, -.137630, -.0886297, -.00459765,
                            .0134628, .00197498)),
}

H3p_from_H2_target = {
}

H3_from_H2_target = {
}
