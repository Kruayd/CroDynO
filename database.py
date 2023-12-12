import fitclasses as ftc

Hp_from_H2_target = {
    'H + H2 -> total fast H+':
    ftc.TabataFit2((5.62e1, 1.12e5), 'Total H+ production from H + H2.\n'
                   'Reference: The Collected Works of Tatsuo Tabata, Volume'
                   ' 17, Atomic and Molecular Collision Cross Section (2). T.'
                   ' Tabata.\n'
                   'Notes: none.'
                   'RMS: 4.7%.',
                   (2.0e1, 2.53e-4, 1.728, 2.164, 7.74e-1, 1.639, 1.43e1)),

    'H- + H2 -> total fast H+':
    ftc.TabataFit6((1.00e3, 3.00e5), 'Total H+ production from H- + H2.\n'
                   'Reference: The Collected Works of Tatsuo Tabata, Volume'
                   ' 17, Atomic and Molecular Collision Cross Section (2). T.'
                   ' Tabata.\n'
                   'Notes: none.'
                   'RMS: 9.0%.',
                   (0.0, 1.75e-8, 3.88, 9.06e-1, -2.74e-1, 3.19, 1.19)),

    'H2+ + H2 -> total fast H+ low energy':
    ftc.BarnettChebFit((1.6, 5.0), 'Total H+ production from H2+ + H2 at low'
                       ' energies.\n'
                       'Reference: ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS'
                       ' OF H, H2, He and Li ATOMS and IONS with ATOMS and'
                       ' MOLECULES. C. F. Barnett.\n'
                       'Notes: No attempt has been made to interpolate between'
                       ' the low-energy data and the data taken at higher'
                       ' energiesi.\n'
                       'Accuracy: 25%.',
                       2,
                       (-74.4493, .351878, -.249279, .0781924, -.0295527,
                        .00853617, -.00490330)),

    'H2+ + H2 -> total fast H+ high energy':
    ftc.BarnettChebFit((1.5e3, 1.0e7), 'Total H+ production from H2+ + H2 at'
                       ' high energies.\n'
                       'Reference: ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS'
                       ' OF H, H2, He and Li ATOMS and IONS with ATOMS and'
                       ' MOLECULES. C. F. Barnett.\n'
                       'Notes: No attempt has been made to interpolate between'
                       ' the low-energy data and the data taken at higher'
                       ' energies.\n'
                       'Accuracy: 25%.',
                       2,
                       (-74.9261, -2.19443, -.855834, .0421307, .216227,
                        .0921147, -.0893079)),

    'H2 + H2 -> total fast H+ low energy':
    ftc.BarnettChebFit((2.5e3, 5.0e4), 'Total H+ production from H2 + H2 at'
                       ' low energies.\n'
                       'Reference: ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS'
                       ' OF H, H2, He and Li ATOMS and IONS with ATOMS and'
                       ' MOLECULES. C. F. Barnett.\n'
                       'Notes: This data involves the sum of the cross'
                       ' sections for the products: σ(H+ + H)proj + 2σ(H+ +'
                       ' H+)proj + σ(H+ + H-). No attempt has been made to'
                       ' join the high and low energy data sets.\n'
                       'Accuracy: Unknown.',
                       2,
                       (-75.7161, .371301, -.373363, -.209805, -.0677263,
                        -.00389719, .0259767)),

    'H2 + H2 -> total fast H+ high energy':
    ftc.BarnettChebFit((1.5e5, 6.0e5), 'Total H+ production from H2 + H2 at'
                       ' high energies.\n'
                       'Reference: ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS'
                       ' OF H, H2, He and Li ATOMS and IONS with ATOMS and'
                       ' MOLECULES. C. F. Barnett.\n'
                       'Notes: This data involves the sum of the cross'
                       ' sections for the products: σ(H+ + H)proj + 2σ(H+ +'
                       ' H+)proj + σ(H+ + H-). No attempt has been made to'
                       ' join the high and low energy data sets.\n'
                       'Accuracy: Unknown.',
                       2,
                       (-75.8616, -.542987, .0642733, .0118753, -.00148111,
                        .000221649, .00636358)),

    'H3+ + H2 -> total fast H+':
    ftc.BarnettChebFit((4.0e1, 6.0e5), 'Total H+ production from H3+ + H2.\n'
                       'Reference: ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS'
                       ' OF H, H2, He and Li ATOMS and IONS with ATOMS and'
                       ' MOLECULES. C. F. Barnett.\n'
                       'Notes: Large variations in measured dissociation cross'
                       ' sections have been ascribed to the influence of H3+'
                       ' ions formed in ion sources with varying degree of'
                       ' vibrational excitation.\n'
                       'Accuracy: 30%.',
                       3,
                       (-75.3369, 1.74367, -.759749, -.559135, .0918355,
                        .0438106, -.0940811)),
}

H_from_H2_target = {
    'H+ + H2 -> total fast H':
    ftc.TabataFit8((3.16, 1.00e5), 'Total H production from H+ + H2.\n'
                   'Reference: The Collected Works of Tatsuo Tabata, Volume'
                   ' 17, Atomic and Molecular Collision Cross Section (2). T.'
                   ' Tabata.\n'
                   'Notes: none.'
                   'RMS: 1.3%.',
                   (2.5, 2.12e2, 1.721, 6.7e-4, 3.239e-1, 4.34e-3, 1.296,
                    1.42e-1, 9.34, 2.997)),

    'H- + H2 -> total fast H':
    ftc.TabataFit11((2.37, 5.00e4), 'Total H production from H- + H2.\n'
                    'Reference: The Collected Works of Tatsuo Tabata, Volume'
                    ' 17, Atomic and Molecular Collision Cross Section (2). T.'
                    ' Tabata.\n'
                    'Notes: none.'
                    'RMS: 6.4%.',
                    (2.25, 4.19e-2, 1.89, 1.78e-1, -2.3e-1, 1.04, 8.7e-1,
                     1.65e1, 1.088, 5.33e-3, 1.66e-1)),

    'H2+ + H2 -> total fast H':
    ftc.BarnettChebFit((2.0e3, 1.0e5), 'Total H production from H2+ + H2.\n'
                       'Reference: ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS'
                       ' OF H, H2, He and Li ATOMS and IONS with ATOMS and'
                       ' MOLECULES. C. F. Barnett.\n'
                       'Notes: The data refer to the sum of the cross section'
                       ' for H2+ + H2 -> (H+ + H)proj  and H2+ + H2 -> (H +'
                       ' H)proj.\n'
                       'Accuracy: 20%.',
                       2,
                       (-70.6702, -.632612, -.606521, -.0915143, -.0121710,
                        .0168179, .0104797)),

    'H2 + H2 -> total fast H':
    ftc.BarnettChebFit((2.5e3, 5.0e4), 'Total H production from H2 + H2.\n'
                       'Reference: ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS'
                       ' OF H, H2, He and Li ATOMS and IONS with ATOMS and'
                       ' MOLECULES. C. F. Barnett.\n'
                       'Notes: This data involves the sum of the cross'
                       ' sections for the products: σ(H+ + H)proj + 2σ(H +'
                       ' H)proj. Variations in ion source conditions produce'
                       ' changes up to 10% in the measured values.\n'
                       'Accuracy: 40%.',
                       2,
                       (-71.7329, -.200109, -.223241, -.0773361, -.0140887,
                        .0563185, -.00955263)),

    'H3+ + H2 -> total fast H':
    ftc.BarnettChebFit((1.5e3, 6.0e5), 'Total H production from H3+ + H2.\n'
                       'Reference: ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS'
                       ' OF H, H2, He and Li ATOMS and IONS with ATOMS and'
                       ' MOLECULES. C. F. Barnett.\n'
                       'Notes: Large variations in measured dissociation cross'
                       ' sections have been ascribed to the influence of H3+'
                       ' ion sources with varying degree of vibrational'
                       ' excitation.\n'
                       'Accuracy: 30%.',
                       3,
                       (-71.5391, -1.05347, -.826342, .203507, .0536140,
                        -.0425785, -.0185315)),
}

Hm_from_H2_target = {
    'H+ + H2 -> total fast H-':
    ftc.BarnettChebFit((2.0e2, 1.0e6), 'Total H- production from H+ + H2.\n'
                       'Reference: ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS'
                       ' OF H, H2, He and Li ATOMS and IONS with ATOMS and'
                       ' MOLECULES. C. F. Barnett.\n'
                       'Notes: none.\n'
                       'Accuracy: 25% for energy < 1e4, 15% for energy < 1e5,'
                       ' 40% for energy > 1e5.',
                       1,
                       (-95.8165, -7.17049, -7.48288, -1.93034, .761153,
                        .556689, -.0542859, -.270184, -.0147551)),

    'H + H2 -> total fast H-':
    ftc.TabataFit13((2.37e1, 9.11e4), 'Total H- production from H + H2.\n'
                    'Reference: The Collected Works of Tatsuo Tabata, Volume'
                    ' 17, Atomic and Molecular Collision Cross Section (2). T.'
                    ' Tabata.\n'
                    'Notes: none'
                    'RMS: 3.6%.',
                    (2.1e1, 9.73e-3, 2.38, 1.39e-2, -5.51e-1, 7.7e-2, 2.12,
                     1.97e-6, 2.051, 5.5, 6.62e-1, 2.02e1, 3.62)),
}

H2p_from_H2_target = {
    'H2+ + H2 -> total H2+ destruction':
    ftc.BarnettChebFit((1.3e3, 5.0e4), 'Total H2+ destruction from H2+ + H2.\n'
                       'Reference: ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS'
                       ' OF H, H2, He and Li ATOMS and IONS with ATOMS and'
                       ' MOLECULES. C. F. Barnett.\n'
                       'Notes: This cross section is the sum of cross sections'
                       ' for all reactions that destroy the fast H2+ molecular'
                       ' ion in passage through H2. Large variations in ion'
                       ' source operating conditions were found to produce'
                       ' changes up to 10% in the measured cross section\n'
                       'Accuracy: 20%.',
                       2,
                       (-69.7995, -.288081, -.216489, -.102343, -.0344599,
                        .0155290, .0223268)),

    'H2 + H2 -> total fast H2+':
    ftc.TabataFit10((4.21e1, 9.90e4), 'Total H2+ production from H2 + H2.\n'
                    'Reference: The Collected Works of Tatsuo Tabata, Volume'
                    ' 17, Atomic and Molecular Collision Cross Section (2). T.'
                    ' Tabata.\n'
                    'Notes: none.'
                    'RMS: 3.4%.',
                    (3.2e1, 1.879e-3, 2.497, 6.62e-2, -4.67e-1, 3.58e-1,
                     5.0e-1, 7.67, 2.01e+2)),

    'H3+ + H2 -> total fast H2+':
    ftc.BarnettChebFit((1.1e2, 6.0e5), 'Total H2+ production from H3+ + H2.\n'
                       'Reference: ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS'
                       ' OF H, H2, He and Li ATOMS and IONS with ATOMS and'
                       ' MOLECULES. C. F. Barnett.\n'
                       'Notes: Large variations in measured dissociation cross'
                       ' sections have been ascribed to the influence of H3+'
                       ' ion sources with varying degree of vibrational'
                       ' excitation.\n'
                       'Accuracy: 30%.',
                       3,
                       (-75.4231, .295854, -.985779, -.0762360, .0980699,
                        -.0248092, -.0512818)),
}

H2_from_H2_target = {
    'H2 + H2 -> total H2 destruction':
    ftc.BarnettChebFit((1.3e3, 5.0e4), 'Total H2 destruction from H2 + H2.\n'
                       'Reference: ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS'
                       ' OF H, H2, He and Li ATOMS and IONS with ATOMS and'
                       ' MOLECULES. C. F. Barnett.\n'
                       'Notes: This cross section is the sum of cross sections'
                       ' for all reactions that destroy the fast H2 molecule'
                       ' in passage through H2, i.e. those producing fast H2+,'
                       ' (H + H), (H + H+) and (H+ + H+) products. Large'
                       ' variations in ion source operating conditions were'
                       ' found to produce changes up to 10% in the measured'
                       ' cross section.\n'
                       'Accuracy: 20%.',
                       2,
                       (-71.8671, .380700, -.137630, -.0886297, -.00459765,
                        .0134628, .00197498)),

    'H+ + H2 -> H2 momentum transfer':
    ftc.TabataFit1((1.00e-1, 1.00e4), 'H2 production from H+ + H2 due to'
                   ' momentum transfer.\n'
                   'Reference: The Collected Works of Tatsuo Tabata, Volume'
                   ' 17, Atomic and Molecular Collision Cross Section (2). T.'
                   ' Tabata.\n'
                   'Notes: none.'
                   'RMS: 4.9%.',
                   (0.0, 5.74, -5.765e-1, 2.79e-2, 1.737)),

    'H + H2 -> H2 momentum transfer':
    ftc.TabataFit6((1.00e-1, 1.00e4), 'H2 production from H- + H2 due to'
                   ' momentum transfer.\n'
                   'Reference: The Collected Works of Tatsuo Tabata, Volume'
                   ' 17, Atomic and Molecular Collision Cross Section (2). T.'
                   ' Tabata.\n'
                   'Notes: none.'
                   'RMS: 2.6%.',
                   (0.0, 6.36, -3.37e-1, 5.5e-3, 8.3e-1, 2.6e-2, 1.766)),

    'H- + H2 -> H2 momentum transfer':
    ftc.TabataFit6((1.00e-1, 1.00e4), 'H2 production from H + H2 due to'
                   ' momentum transfer.\n'
                   'Reference: The Collected Works of Tatsuo Tabata, Volume'
                   ' 17, Atomic and Molecular Collision Cross Section (2). T.'
                   ' Tabata.\n'
                   'Notes: none.'
                   'RMS: 1.5%.',
                   (0.0, 2.97e1, 4.095e-3, 1.11e-4, 5.55e-1, 6.0e-3, 1.607)),

    'H2+ + H2 -> fast H2 charge exchange':
    ftc.BarnettChebFit((2.0, 1.0e5), 'H2 production from H2+ + H2 due to'
                       ' charge exchange.\n'
                       'Reference: ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS'
                       ' OF H, H2, He and Li ATOMS and IONS with ATOMS and'
                       ' MOLECULES. C. F. Barnett.\n'
                       'Notes: It is well known that the H2+ electron capture'
                       ' cross sections are dependent on the vibrational'
                       ' levels of the H2+ ion. The effect increases as the'
                       ' energy decreases.\n'
                       'Accuracy: 30% for energy < 2e3, 20% for energy > 2e3.',
                       2,
                       (-71.4572, -1.88878, -.906965, -.676593, -.388666,
                        -.0528444, .0283239, -.0386419, .00767518)),

    'H3+ + H2 -> H2 momentum transfer':
    ftc.TabataFit14((1.00e-1, 1.00e4), 'H2 production from H3+ + H2 due to'
                    ' momentum transfer.\n'
                    'Reference: The Collected Works of Tatsuo Tabata, Volume'
                    ' 17, Atomic and Molecular Collision Cross Section (2). T.'
                    ' Tabata.\n'
                    'Notes: none.'
                    'RMS: 5.6%.',
                    (0.0, 1.16, -8.12e-1, 4.29e-4, -1.38e-1, 1.28e-2, 1.33,
                     8.67e-2, 2.18)),

    'H3+ + H2 -> total fast H2':
    ftc.BarnettChebFit((3.0e1, 6.0e5), 'Total H2 production from H3+ + H2.\n'
                       'Reference: ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS'
                       ' OF H, H2, He and Li ATOMS and IONS with ATOMS and'
                       ' MOLECULES. C. F. Barnett.\n'
                       'Notes: Large variations in measured dissociation cross'
                       ' sections have been ascribed to the influence of H3+'
                       ' ion sources with varying degree of vibrational'
                       ' excitation.\n'
                       'Accuracy: 30%.',
                       3,
                       (-74.8168, -.899995, -1.57067, -.379862, .384429,
                        .264557, .0263143)),
}

H3p_from_H2_target = {
    'H3+ + H2 -> total H3+ destruction':
    ftc.BarnettChebFit((1.6e3, 3.5e4), 'Total H3+ destruction from H3+ + H2.\n'
                       'Reference: ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS'
                       ' OF H, H2, He and Li ATOMS and IONS with ATOMS and'
                       ' MOLECULES. C. F. Barnett.\n'
                       'Notes: This corss section is the sum of cross sections'
                       ' for all reactions that destroy the H3+ molecular ion'
                       ' in passage through H2. Large variations in ion source'
                       ' operating conditions were found to produce changes up'
                       ' to 10% in the measured cross sections.\n'
                       'Accuracy: 20%.',
                       3,
                       (-70.3701, .284601, -.184305, -.0425670, -.00921848,
                        .00921848, .00698594, .00725332)),

    'H2+ + H2 -> H3+ + H':
    ftc.TabataFit6((1.00e-1, 1.78e1), 'H3+ production from H2+ + H2.\n'
                   'Reference: The Collected Works of Tatsuo Tabata, Volume'
                   ' 17, Atomic and Molecular Collision Cross Section (2). T.'
                   ' Tabata.\n'
                   'Notes: none.'
                   'RMS: 1.2%.',
                   (0.00, 6.05, -5.247e-1, 4.088e-3, 2.872, 7.3e-3, 6.99)),
}

H3_from_H2_target = {
}
