"""
Results for Markov Autoregression Models.

References
----------

Datasets produced using GAUSS code described in Kim and Nelson (1999) and
found at http://econ.korea.ac.kr/~cjkim/SSMARKOV.htm
Accessed 2013-09-17
Code was run using OxGauss 7.

Kim, Chang-Jin, and Charles R. Nelson. 1999.
"State-Space Models with Regime Switching:
Classical and Gibbs-Sampling Approaches with Applications".
MIT Press Books. The MIT Press.

"""

"""
Hamilton's (1989) Markov Switching Model of GNP

See http://econ.korea.ac.kr/~cjkim/MARKOV/prgmlist.htm#chapter4

Gauss Code: hmt4_kim.opt
Dataset:    gdp4795.prn

So that the test also replicates the findings in Table 4.1  of Kim and Nelson
(1999), the following changes were made to hmt4_kim.opt

Line 35 of hmt4_kim.opt must be changed from:
    yy_d=(ln(data[21:152,1])-ln(data[20:151,1]))*100;
(which uses the data range 1952.2 - 1985.1), to
    yy_d=(ln(data[20:151,1])-ln(data[19:150,1]))*100;
(which uses the data range 1952.1 - 1984.4).
(this may only be necessary when running the program in OxGauss)

The results below were then generated by the following code, inserted just
before "@ Maximum Likelihood Estimation @"

PRM_FNL=TRANS(PRMTR_IN);
LIK_FCN(PRMTR_IN);
{pr_tt0,pr_tl0}=FILTER(PRMTR_IN);
"PR_TT0";
pr_tt0;
"PR_TL0";
pr_tl0;
smooth0=SMOOTH(pr_tt0,pr_tl0);
"SMOOTH0"
smooth0;

Note: LIK_FCN returns the negative of the log likelihood (fout), so the value
below is -1*fout.
"""
htm4_kim = {
    'data':    [
        1239.5, 1247.19995117, 1255, 1269.5, 1284, 1295.69995117,
        1303.80004883, 1316.40002441, 1305.30004883, 1302, 1312.59997559,
        1301.90002441, 1350.90002441, 1393.5, 1445.19995117, 1484.5,
        1504.09997559, 1548.30004883, 1585.40002441, 1596, 1607.69995117,
        1612.09997559, 1621.90002441, 1657.80004883, 1687.30004883,
        1695.30004883, 1687.90002441, 1671.19995117, 1660.80004883,
        1658.40002441, 1677.69995117, 1698.30004883, 1742.5,
        1758.59997559, 1778.19995117, 1793.90002441, 1787, 1798.5,
        1802.19995117, 1826.59997559, 1836.40002441, 1834.80004883,
        1851.19995117, 1830.5, 1790.09997559, 1804.40002441,
        1840.90002441, 1880.90002441, 1904.90002441, 1937.5,
        1930.80004883, 1941.90002441, 1976.90002441, 1971.69995117,
        1973.69995117, 1961.09997559, 1977.40002441, 2006, 2035.19995117,
        2076.5, 2103.80004883, 2125.69995117, 2142.60009766,
        2140.19995117, 2170.89990234, 2199.5, 2237.60009766, 2254.5,
        2311.10009766, 2329.89990234, 2357.39990234, 2364, 2410.10009766,
        2442.80004883, 2485.5, 2543.80004883, 2596.80004883,
        2601.39990234, 2626.10009766, 2640.5, 2657.19995117, 2669, 2699.5,
        2715.10009766, 2752.10009766, 2796.89990234, 2816.80004883,
        2821.69995117, 2864.60009766, 2867.80004883, 2884.5,
        2875.10009766, 2867.80004883, 2859.5, 2895, 2873.30004883,
        2939.89990234, 2944.19995117, 2962.30004883, 2977.30004883,
        3037.30004883, 3089.69995117, 3125.80004883, 3175.5,
        3253.30004883, 3267.60009766, 3264.30004883, 3289.10009766,
        3259.39990234, 3267.60009766, 3239.10009766, 3226.39990234, 3154,
        3190.39990234, 3249.89990234, 3292.5, 3356.69995117,
        3369.19995117, 3381, 3416.30004883, 3466.39990234, 3525,
        3574.39990234, 3567.19995117, 3591.80004883, 3707, 3735.60009766,
        3779.60009766, 3780.80004883, 3784.30004883, 3807.5,
        3814.60009766, 3830.80004883, 3732.60009766, 3733.5, 3808.5,
        3860.5, 3844.39990234, 3864.5, 3803.10009766, 3756.10009766,
        3771.10009766, 3754.39990234, 3759.60009766, 3783.5, 3886.5,
        3944.39990234, 4012.10009766, 4089.5, 4144, 4166.39990234,
        4194.20019531, 4221.79980469, 4254.79980469, 4309, 4333.5, 4390.5,
        4387.70019531, 4412.60009766, 4427.10009766, 4460, 4515.29980469,
        4559.29980469, 4625.5, 4655.29980469, 4704.79980469, 4734.5,
        4779.70019531, 4817.60009766, 4839, 4839, 4856.70019531,
        4898.29980469, 4917.10009766, 4906.5, 4867.20019531, 4842,
        4867.89990234, 4879.89990234, 4880.79980469, 4918.5, 4947.5,
        4990.5, 5060.70019531, 5075.29980469, 5105.39990234,
        5139.39990234, 5218, 5261.10009766, 5314.10009766, 5367,
        5433.79980469, 5470.10009766, 5487.79980469, 5544.60009766
    ],
    '-1*fout': -175.24343,
    'pr_tt0':  [
        0.04085, 0.15908, 0.48877, 0.87628, 0.93508, 0.90305, 0.43708,
        0.17632, 0.00463, 0.05226, 0.03378, 0.03314, 0.39209, 0.25374,
        0.39891, 0.11032, 0.20268, 0.51911, 0.21696, 0.89537, 0.99789,
        0.45628, 0.04412, 0.01310, 0.03696, 0.00813, 0.29297, 0.17911,
        0.01512, 0.48045, 0.63426, 0.88696, 0.47185, 0.10301, 0.03803,
        0.00718, 0.02017, 0.03125, 0.04454, 0.27190, 0.04683, 0.03138,
        0.01606, 0.07515, 0.00241, 0.05142, 0.03240, 0.11887, 0.00863,
        0.02193, 0.01213, 0.00234, 0.00369, 0.15213, 0.04668, 0.06912,
        0.11398, 0.20684, 0.08370, 0.15944, 0.04843, 0.01589, 0.08624,
        0.23830, 0.03037, 0.24528, 0.25474, 0.63568, 0.82075, 0.88378,
        0.30312, 0.85974, 0.04145, 0.22351, 0.20173, 0.17288, 0.01120,
        0.01400, 0.03891, 0.01142, 0.00147, 0.11418, 0.33116, 0.12084,
        0.78288, 0.72975, 0.95452, 0.94391, 0.99859, 0.37254, 0.04679,
        0.06218, 0.01061, 0.10886, 0.15894, 0.05205, 0.02159, 0.01568,
        0.02203, 0.32272, 0.16240, 0.00092, 0.11061, 0.05965, 0.17350,
        0.27868, 0.21040, 0.41857, 0.46229, 0.99741, 0.80569, 0.06983,
        0.06918, 0.63705, 0.37328, 0.96007, 0.98630, 0.72253, 0.92944,
        0.89171, 0.61464, 0.01222, 0.02061, 0.01056, 0.00364, 0.01357,
        0.07333, 0.06761
    ],
    'pr_tl0':  [
        0.29288, 0.12618, 0.20438, 0.42245, 0.67875, 0.71765, 0.69646,
        0.38826, 0.21579, 0.10222, 0.13373, 0.12151, 0.12108, 0.35850,
        0.26699, 0.36301, 0.17213, 0.23322, 0.44251, 0.24266, 0.69138,
        0.75919, 0.40095, 0.12834, 0.10783, 0.12361, 0.10454, 0.29294,
        0.21763, 0.10917, 0.41694, 0.51867, 0.68582, 0.41125, 0.16730,
        0.12432, 0.10391, 0.11250, 0.11983, 0.12862, 0.27900, 0.13014,
        0.11992, 0.10978, 0.14887, 0.10076, 0.13317, 0.12059, 0.17778,
        0.10487, 0.11366, 0.10718, 0.10071, 0.10160, 0.19978, 0.13004,
        0.14488, 0.17455, 0.23597, 0.15452, 0.20462, 0.13119, 0.10967,
        0.15621, 0.25678, 0.11925, 0.26140, 0.26765, 0.51962, 0.64203,
        0.68371, 0.29965, 0.66781, 0.12658, 0.24700, 0.23259, 0.21351,
        0.10657, 0.10842, 0.12490, 0.10672, 0.10014, 0.17469, 0.31820,
        0.17909, 0.61698, 0.58184, 0.73050, 0.72349, 0.75966, 0.34557,
        0.13011, 0.14029, 0.10618, 0.17117, 0.20429, 0.13359, 0.11344,
        0.10953, 0.11374, 0.31262, 0.20657, 0.09977, 0.17232, 0.13861,
        0.21392, 0.28349, 0.23833, 0.37601, 0.40493, 0.75888, 0.63206,
        0.14535, 0.14492, 0.52053, 0.34606, 0.73418, 0.75153, 0.57706,
        0.71392, 0.68896, 0.50570, 0.10724, 0.11280, 0.10615, 0.10157,
        0.10814, 0.14767
    ],
    'smooth0': [
        0.13186, 0.51341, 0.85558, 0.96395, 0.94534, 0.76944, 0.20870,
        0.05493, 0.00195, 0.02146, 0.02481, 0.07717, 0.34218, 0.28570,
        0.31693, 0.24349, 0.46444, 0.67116, 0.66970, 0.98312, 0.99356,
        0.19142, 0.01327, 0.00464, 0.01261, 0.01156, 0.16460, 0.09887,
        0.07714, 0.72132, 0.77160, 0.74215, 0.21530, 0.03440, 0.01091,
        0.00230, 0.00749, 0.01561, 0.03744, 0.10034, 0.01545, 0.00980,
        0.00662, 0.02149, 0.00097, 0.01863, 0.01584, 0.03589, 0.00269,
        0.00639, 0.00331, 0.00067, 0.00254, 0.05868, 0.02466, 0.04542,
        0.07591, 0.09242, 0.04588, 0.05711, 0.01673, 0.01267, 0.07930,
        0.13865, 0.09837, 0.48595, 0.64089, 0.87044, 0.90216, 0.83431,
        0.52627, 0.63483, 0.04226, 0.12999, 0.09547, 0.05453, 0.00337,
        0.00484, 0.01139, 0.00329, 0.00297, 0.23910, 0.44389, 0.48514,
        0.94130, 0.94997, 0.99259, 0.99152, 0.99548, 0.14858, 0.01798,
        0.01956, 0.00702, 0.05709, 0.05669, 0.01630, 0.00680, 0.00699,
        0.02655, 0.14566, 0.04944, 0.00080, 0.08185, 0.10928, 0.29836,
        0.43530, 0.52275, 0.75433, 0.86541, 0.99574, 0.57926, 0.12352,
        0.30061, 0.81825, 0.81623, 0.99388, 0.99442, 0.92113, 0.94258,
        0.77581, 0.30006, 0.00377, 0.00595, 0.00291, 0.00117, 0.00775,
        0.04474, 0.06761
    ]
}
