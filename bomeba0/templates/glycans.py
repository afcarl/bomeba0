from collections import namedtuple
import numpy as np
"""
Templates for glycan residues
"""

AA_info = namedtuple('AA_info', 'coords atom_names bonds bb sc offset')

BDP_info = AA_info(coords=np.array([[-14.69,  10.15, -18.15],
                                    [-15.46,  11.47, -18.33],
                                    [-16.33,  11.35, -19.46],
                                    [-14.45,  12.62, -18.54],
                                    [-15.15,  13.88, -18.62],
                                    [-13.41,  12.66, -17.39],
                                    [-12.36,  13.57, -17.75],
                                    [-12.76,  11.28, -17.17],
                                    [-11.74,  11.28, -16.03],
                                    [-10.58,  11.62, -16.19],
                                    [-12.26,  11.06, -14.85],
                                    [-13.8,  10.27, -17.01],
                                    [-14.09,   9.95, -19.04],
                                    [-16.06,  11.66, -17.43],
                                    [-13.92,  12.44, -19.49],
                                    [-13.9,  12.98, -16.46],
                                    [-12.19,  11.01, -18.07],
                                    [-16.99,  10.64, -19.31],
                                    [-14.59,  14.56, -19.03]]),
                   atom_names=['C1', 'C2', 'O2', 'C3', 'O3', 'C4', 'O4', 'C5',
                               'C6', 'O6A', 'O6B', 'OR', 'H1', 'H2', 'H3',
                               'H4', 'H5', 'H2o', 'H3o'],
                   bb=[],
                   sc=[],
                   bonds=[(0, 1), (0, 11), (0, 12), (1, 2), (1, 3), (1, 13),
                          (2, 17), (3, 4), (3, 5), (3, 14), (4, 18), (5, 6),
                          (5, 7), (5, 15), (7, 8), (7, 11), (7, 16), (8, 9),
                          (8, 10)],
                   offset=19)

NGA_info = AA_info(coords=np.array([[-15.,   5.88, -16.15],
                                    [-15.3,   7.39, -16.33],
                                    [-16.63,   7.71, -15.78],
                                    [-15.24,   7.7, -17.85],
                                    [-15.52,   9.08, -18.1],
                                    [-13.87,   7.26, -18.45],
                                    [-12.73,   7.93, -17.9],
                                    [-13.71,   5.74, -18.23],
                                    [-12.4,   5.17, -18.83],
                                    [-12.36,   3.77, -18.58],
                                    [-17.03,   8.94, -15.35],
                                    [-16.27,   9.85, -15.15],
                                    [-18.54,   9.06, -15.17],
                                    [-13.75,   5.49, -16.79],
                                    [-17.3,   6.97, -15.77],
                                    [-15.8,   5.34, -16.66],
                                    [-14.56,   7.98, -15.81],
                                    [-16.02,   7.14, -18.36],
                                    [-13.91,   7.52, -19.51],
                                    [-14.54,   5.23, -18.71],
                                    [-19.05,   8.97, -16.13],
                                    [-18.78,  10.05, -14.75],
                                    [-18.91,   8.29, -14.49],
                                    [-12.37,   5.36, -19.91],
                                    [-11.52,   5.64, -18.37],
                                    [-12.52,   7.65, -16.98],
                                    [-12.35,   3.64, -17.61]]),
                   atom_names=['C1', 'C2', 'N2', 'C3', 'O3', 'C4', 'O4', 'C5',
                               'C6', 'O6', 'C7', 'O7', 'C8', 'OR', 'HN2', 'H1',
                               'H2', 'H3', 'H4', 'H5', 'H81', 'H82', 'H83',
                               'H6R', 'H6S', 'H4o', 'H6o'],
                   bb=[],
                   sc=[],
                   bonds=[(0, 1), (0, 13), (0, 15), (1, 2), (1, 3), (1, 16),
                          (2, 10), (2, 14), (3, 4), (3, 5), (3, 17), (5, 6),
                          (5, 7), (5, 18), (6, 25), (7, 8), (7, 13), (7, 19),
                          (8, 9), (8, 23), (8, 24), (9, 26), (10, 11), (10, 12),
                          (12, 20), (12, 21), (12, 22)],
                   offset=27)

AFL_info = AA_info(coords=np.array([[  3.54,  -4.94,  -9.76],
       [  3.83,  -3.48, -10.16],
       [  3.92,  -2.65,  -9.01],
       [  5.17,  -3.41, -10.92],
       [  5.41,  -2.05, -11.31],
       [  5.13,  -4.33, -12.16],
       [  4.22,  -3.76, -13.11],
       [  4.71,  -5.76, -11.76],
       [  4.44,  -6.66, -12.99],
       [  3.49,  -5.74, -10.97],
       [  2.58,  -5.  ,  -9.26],
       [  3.03,  -3.12, -10.81],
       [  5.98,  -3.74, -10.26],
       [  6.13,  -4.36, -12.61],
       [  5.5 ,  -6.22, -11.15],
       [  5.32,  -6.68, -13.65],
       [  4.23,  -7.68, -12.67],
       [  3.59,  -6.29, -13.56],
       [  4.24,  -1.79,  -9.36],
       [  6.3 ,  -2.01, -11.67],
       [  4.27,  -2.8 , -13.  ]]),
             atom_names = ['C1', 'C2', 'O2', 'C3', 'O3', 'C4', 'O4', 'C5',
                           'C6', 'OR', 'H1', 'H2', 'H3', 'H4', 'H5', 'H61',
                           'H62', 'H63', 'H2o', 'H3o', 'H4o'],
             bb = [],
             sc = [],
             bonds = [(0, 1), (0, 9), (0, 10), (1, 2), (1, 3), (1, 11),
                      (2, 18), (3, 4), (3, 5), (3, 12), (4, 19), (5, 6),
                      (5, 7), (5, 13), (6, 20), (7, 8), (7, 9), (7, 14),
                      (8, 15), (8, 16), (8, 17)],
             offset = 21)

NAG_info = AA_info(coords=np.array([[  0.7 ,  -7.06,  -8.68],
       [ -0.47,  -6.53,  -7.82],
       [ -0.6 ,  -7.33,  -6.59],
       [ -1.77,  -6.52,  -8.68],
       [ -2.86,  -5.83,  -8.05],
       [ -1.54,  -5.79, -10.02],
       [ -2.72,  -5.91, -10.8 ],
       [ -0.32,  -6.38, -10.77],
       [ -0.01,  -5.62, -12.08],
       [  0.03,  -4.21, -11.88],
       [ -1.35,  -6.97,  -5.53],
       [ -2.06,  -6.  ,  -5.51],
       [ -1.26,  -7.89,  -4.34],
       [  0.83,  -6.29,  -9.9 ],
       [  0.53,  -8.1 ,  -8.97],
       [ -0.24,  -5.51,  -7.51],
       [ -2.09,  -7.55,  -8.86],
       [ -1.37,  -4.73,  -9.8 ],
       [ -0.5 ,  -7.43, -11.  ],
       [ -0.35,  -8.49,  -4.36],
       [  0.04,  -8.12,  -6.49],
       [ -2.13,  -8.56,  -4.33],
       [ -1.25,  -7.3 ,  -3.42],
       [ -2.7 ,  -5.79,  -7.09],
       [ -0.78,  -5.86, -12.82],
       [  0.96,  -5.95, -12.45],
       [ -3.45,  -5.7 , -10.19],
       [ -0.89,  -3.9 , -11.9 ]]),
             atom_names = ['C1', 'C2', 'N2', 'C3', 'O3', 'C4', 'O4', 'C5',
                           'C6', 'O6', 'C7', 'O7', 'C8', 'OR', 'H1', 'H2',
                           'H3', 'H4', 'H5', 'H81', 'H2n', 'H82', 'H83',
                           'H3o', 'H6R', 'H6S', 'H4o', 'H6o'],
             bb = [],
             sc = [],
             bonds = [(0, 1), (0, 13), (0, 14), (1, 2), (1, 3), (1, 15),
                      (2, 10), (2, 20), (3, 4), (3, 5), (3, 16), (4, 23),
                      (5, 6), (5, 7), (5, 17), (6, 26), (7, 8), (7, 13),
                      (7, 18), (8, 9), (8, 24), (8, 25), (9, 27), (10, 11),
                      (10, 12), (12, 19), (12, 21), (12, 22)],
             offset = 28)

MAG_info = AA_info(coords=np.array([[  5.63,  -8.87,  -7.81],
       [  6.82,  -9.65,  -8.03],
       [  5.68,  -7.48,  -8.46],
       [  6.84,  -6.71,  -7.97],
       [  4.37,  -6.71,  -8.2 ],
       [  4.45,  -5.46,  -8.88],
       [  3.1 ,  -7.58,  -8.52],
       [  1.94,  -6.96,  -7.95],
       [  3.26,  -8.98,  -7.84],
       [  2.14, -10.01,  -8.14],
       [  1.97, -10.17,  -9.54],
       [  7.69,  -6.03,  -8.75],
       [  7.65,  -6.05,  -9.98],
       [  8.75,  -5.26,  -8.01],
       [  7.14,  -9.94,  -9.4 ],
       [  4.48,  -9.59,  -8.28],
       [  7.47,  -9.03,  -9.9 ],
       [  6.26, -10.36,  -9.91],
       [  7.95, -10.67,  -9.41],
       [  5.54,  -8.78,  -6.72],
       [  5.79,  -7.59,  -9.54],
       [  4.3 ,  -6.47,  -7.13],
       [  2.96,  -7.7 ,  -9.6 ],
       [  3.31,  -8.86,  -6.76],
       [  9.47,  -5.95,  -7.57],
       [  6.93,  -6.62,  -6.96],
       [  8.29,  -4.67,  -7.22],
       [  9.27,  -4.58,  -8.69],
       [  1.21,  -9.7 ,  -7.67],
       [  2.44, -10.98,  -7.71],
       [  2.82, -10.46,  -9.9 ]]),
             atom_names = ['C1', 'O1', 'C2', 'N2', 'C3', 'O3', 'C4', 'O4',
                           'C5', 'C6', 'O6', 'C7', 'O7', 'C8', 'CO1', 'OR',
                           'HCO1', 'HCO2', 'HCO3', 'H1', 'H2', 'H3', 'H4',
                           'H5', 'H81', 'H2n', 'H82', 'H83', 'H6R', 'H6S',
                           'H6o'],
             bb = [],
             sc = [],
             bonds = [(0, 1), (0, 2), (0, 15), (0, 19), (1, 14), (2, 3),
                      (2, 4), (2, 20), (3, 11), (3, 25), (4, 5), (4, 6),
                      (4, 21), (6, 7), (6, 8), (6, 22), (8, 9), (8, 15),
                      (8, 23), (9, 10), (9, 28), (9, 29), (10, 30), (11, 12),
                      (11, 13), (13, 24), (13, 26), (13, 27), (14, 16),
                      (14, 17), (14, 18)],
             offset = 31)

B6D_info = AA_info(coords=np.array([[  1.95e+01,   3.45e+01,   1.77e+00],
       [  1.85e+01,   3.49e+01,   2.70e+00],
       [  1.99e+01,   3.57e+01,   8.50e-01],
       [  1.88e+01,   3.62e+01,   1.03e-01],
       [  2.11e+01,   3.53e+01,  -5.60e-02],
       [  2.16e+01,   3.64e+01,  -7.50e-01],
       [  2.23e+01,   3.47e+01,   7.93e-01],
       [  2.35e+01,   3.43e+01,  -1.70e-02],
       [  2.18e+01,   3.35e+01,   1.71e+00],
       [  2.29e+01,   3.30e+01,   2.67e+00],
       [  1.80e+01,   3.55e+01,  -7.76e-01],
       [  1.82e+01,   3.44e+01,  -1.05e+00],
       [  1.69e+01,   3.63e+01,  -1.37e+00],
       [  2.48e+01,   3.32e+01,  -1.65e+00],
       [  2.35e+01,   3.33e+01,  -9.47e-01],
       [  2.25e+01,   3.26e+01,  -1.18e+00],
       [  2.07e+01,   3.40e+01,   2.52e+00],
       [  1.91e+01,   3.36e+01,   1.20e+00],
       [  2.03e+01,   3.65e+01,   1.51e+00],
       [  2.08e+01,   3.45e+01,  -7.86e-01],
       [  2.26e+01,   3.55e+01,   1.46e+00],
       [  2.14e+01,   3.27e+01,   1.11e+00],
       [  1.86e+01,   3.72e+01,   2.98e-01],
       [  2.24e+01,   3.23e+01,   3.35e+00],
       [  2.37e+01,   3.26e+01,   2.12e+00],
       [  2.33e+01,   3.38e+01,   3.27e+00],
       [  2.43e+01,   3.49e+01,   1.15e-01],
       [  1.84e+01,   3.42e+01,   3.32e+00],
       [  1.73e+01,   3.73e+01,  -1.75e+00],
       [  1.61e+01,   3.65e+01,  -6.10e-01],
       [  1.64e+01,   3.58e+01,  -2.20e+00],
       [  2.55e+01,   3.27e+01,  -9.86e-01],
       [  2.47e+01,   3.25e+01,  -2.54e+00],
       [  2.52e+01,   3.41e+01,  -1.96e+00]]),
             atom_names = ['C1', 'O1', 'C2', 'N2', 'C3', 'O3', 'C4', 'N4', 'C5', 'C6', 'C7', 'O7', 'C8', 'C9', 'C10', 'O10', 'OR', 'H1', 'H2', 'H3', 'H4', 'H5', 'H2N', 'H61', 'H62', 'H63', 'H4N', 'H1o', 'H81', 'H82', 'H83', 'H91', 'H92', 'H93'],
             bb = [],
             sc = [],
             bonds = [(0, 1), (0, 2), (0, 16), (0, 17), (1, 27), (2, 3), (2, 4), (2, 18), (3, 10), (3, 22), (4, 5), (4, 6), (4, 19), (6, 7), (6, 8), (6, 20), (7, 14), (7, 26), (8, 9), (8, 16), (8, 21), (9, 23), (9, 24), (9, 25), (10, 11), (10, 12), (12, 28), (12, 29), (12, 30), (13, 14), (13, 31), (13, 32), (13, 33), (14, 15)],
             offset = 34)

A2G_info = AA_info(coords=np.array([[  2.25e+01,   3.67e+01,  -2.07e+00],
       [  2.33e+01,   3.80e+01,  -2.32e+00],
       [  2.43e+01,   3.82e+01,  -1.26e+00],
       [  2.23e+01,   3.92e+01,  -2.39e+00],
       [  2.30e+01,   4.04e+01,  -2.61e+00],
       [  2.12e+01,   3.90e+01,  -3.45e+00],
       [  2.18e+01,   3.89e+01,  -4.76e+00],
       [  2.05e+01,   3.76e+01,  -3.14e+00],
       [  1.94e+01,   3.73e+01,  -4.19e+00],
       [  1.87e+01,   3.61e+01,  -3.81e+00],
       [  2.54e+01,   3.75e+01,  -1.15e+00],
       [  2.57e+01,   3.65e+01,  -1.90e+00],
       [  2.63e+01,   3.79e+01,  -2.70e-02],
       [  2.14e+01,   3.66e+01,  -3.09e+00],
       [  2.31e+01,   3.58e+01,  -2.09e+00],
       [  2.38e+01,   3.79e+01,  -3.28e+00],
       [  2.05e+01,   3.98e+01,  -3.38e+00],
       [  2.00e+01,   3.77e+01,  -2.16e+00],
       [  2.41e+01,   3.89e+01,  -6.34e-01],
       [  1.99e+01,   3.72e+01,  -5.17e+00],
       [  1.87e+01,   3.81e+01,  -4.26e+00],
       [  2.58e+01,   3.78e+01,   9.29e-01],
       [  2.67e+01,   3.89e+01,  -1.90e-01],
       [  2.72e+01,   3.72e+01,   2.90e-02],
       [  1.94e+01,   3.54e+01,  -3.68e+00]]),
             atom_names = ['C1', 'C2', 'N2', 'C3', 'O3', 'C4', 'O4', 'C5', 'C6', 'O6', 'C7', 'O7', 'C8', 'OR', 'H1', 'H2', 'H4', 'H5', 'H2N', 'H61', 'H62', 'H81', 'H82', 'H83', 'H6o'],
             bb = [],
             sc = [],
             bonds = [(0, 1), (0, 13), (0, 14), (1, 2), (1, 3), (1, 15), (2, 10), (2, 18), (3, 4), (3, 5), (5, 6), (5, 7), (5, 16), (7, 8), (7, 13), (7, 17), (8, 9), (8, 19), (8, 20), (9, 24), (10, 11), (10, 12), (12, 21), (12, 22), (12, 23)],
             offset = 25)


BGC_info = AA_info(coords=np.array([[ 20.45,  43.74, -11.36],
       [ 19.72,  45.09, -11.42],
       [ 19.65,  45.66, -10.11],
       [ 18.29,  44.89, -11.94],
       [ 17.63,  46.15, -12.08],
       [ 18.32,  44.19, -13.32],
       [ 16.97,  43.96, -13.73],
       [ 19.11,  42.86, -13.22],
       [ 19.33,  42.2 , -14.6 ],
       [ 18.08,  41.74, -15.13],
       [ 20.43,  43.13, -12.67],
       [ 19.97,  43.07, -10.64],
       [ 20.27,  45.77, -12.08],
       [ 17.73,  44.27, -11.24],
       [ 18.81,  44.85, -14.05],
       [ 18.59,  42.16, -12.55],
       [ 18.22,  41.54, -16.07],
       [ 18.99,  46.38, -10.17],
       [ 16.82,  45.99, -12.59],
       [ 19.77,  42.93, -15.28],
       [ 20.01,  41.36, -14.49],
       [ 17.  ,  43.31, -14.46]]),
             atom_names = ['C1', 'C2', 'O2', 'C3', 'O3', 'C4', 'O4', 'C5', 'C6', 'O6', 'OR', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H2o', 'H3o', 'H6R', 'H6S', 'H4o'],
             bb = [],
             sc = [],
             bonds = [(0, 1), (0, 10), (0, 11), (1, 2), (1, 3), (1, 12), (2, 17), (3, 4), (3, 5), (3, 13), (4, 18), (5, 6), (5, 7), (5, 14), (6, 21), (7, 8), (7, 10), (7, 15), (8, 9), (8, 19), (8, 20), (9, 16)],
             offset = 22)


templates_gl = {'B': BDP_info, 'N': NGA_info,
                'A':AFL_info, 'G':NAG_info, 'M':MAG_info,
                'D':B6D_info, 'C':A2G_info, 'F':BGC_info}

one_to_three_gl = {'B': 'BDP', 'N': 'NGA',
                   'A':'AFL', 'G':'NAG', 'M':'MAG',
                   'D':'B6D', 'C':'A2G', 'F':'BGC'}

three_to_one_gl = {val: key for key, val in one_to_three_gl.items()}
