# 
#         cork
#                   www.fabiocrameri.ch/colourmaps
from matplotlib.colors import LinearSegmentedColormap      
      
cm_data = [[0.1709, 0.099347, 0.29895],      
           [0.17083, 0.10606, 0.30528],      
           [0.17066, 0.11263, 0.31159],      
           [0.17041, 0.11908, 0.31789],      
           [0.17008, 0.12545, 0.32416],      
           [0.1697, 0.13175, 0.3304],      
           [0.16925, 0.13799, 0.3366],      
           [0.16872, 0.14414, 0.34279],      
           [0.16814, 0.15025, 0.34892],      
           [0.16757, 0.15632, 0.35505],      
           [0.16696, 0.16234, 0.36112],      
           [0.16629, 0.16831, 0.36719],      
           [0.16559, 0.17429, 0.37324],      
           [0.16491, 0.18023, 0.37928],      
           [0.16425, 0.18619, 0.38529],      
           [0.16354, 0.19211, 0.39132],      
           [0.16282, 0.19804, 0.39731],      
           [0.16212, 0.20399, 0.40331],      
           [0.16142, 0.2099, 0.4093],      
           [0.16068, 0.21586, 0.41529],      
           [0.15998, 0.22179, 0.42127],      
           [0.15934, 0.22776, 0.42728],      
           [0.15874, 0.23372, 0.43326],      
           [0.15814, 0.23973, 0.43926],      
           [0.15759, 0.24574, 0.44527],      
           [0.15712, 0.25181, 0.45129],      
           [0.15676, 0.25786, 0.4573],      
           [0.1565, 0.264, 0.46333],      
           [0.15636, 0.27014, 0.46938],      
           [0.15637, 0.27633, 0.47541],      
           [0.15656, 0.28256, 0.48144],      
           [0.15696, 0.28883, 0.48748],      
           [0.15763, 0.29514, 0.49349],      
           [0.15862, 0.30151, 0.4995],      
           [0.15986, 0.30792, 0.5055],      
           [0.16156, 0.31439, 0.51147],      
           [0.16358, 0.32091, 0.51741],      
           [0.16599, 0.32744, 0.52329],      
           [0.16889, 0.33402, 0.52912],      
           [0.17217, 0.34062, 0.53488],      
           [0.17591, 0.34724, 0.54058],      
           [0.18011, 0.35385, 0.5462],      
           [0.18474, 0.36048, 0.55173],      
           [0.18975, 0.3671, 0.55716],      
           [0.19515, 0.37371, 0.5625],      
           [0.20087, 0.38029, 0.56772],      
           [0.20696, 0.38683, 0.57286],      
           [0.21327, 0.39334, 0.57787],      
           [0.21986, 0.3998, 0.5828],      
           [0.22664, 0.40623, 0.58762],      
           [0.23356, 0.4126, 0.59236],      
           [0.24064, 0.41889, 0.59699],      
           [0.24786, 0.42515, 0.60154],      
           [0.25514, 0.43135, 0.606],      
           [0.26247, 0.43749, 0.6104],      
           [0.26987, 0.44357, 0.61472],      
           [0.27729, 0.4496, 0.619],      
           [0.28472, 0.45558, 0.62321],      
           [0.29219, 0.46153, 0.62738],      
           [0.29967, 0.46744, 0.63152],      
           [0.30716, 0.47332, 0.63562],      
           [0.31467, 0.4792, 0.63971],      
           [0.32223, 0.48506, 0.64378],      
           [0.32982, 0.49095, 0.64786],      
           [0.33744, 0.49682, 0.65195],      
           [0.34511, 0.50273, 0.65604],      
           [0.35284, 0.50868, 0.66015],      
           [0.36062, 0.51466, 0.66429],      
           [0.36849, 0.52067, 0.66846],      
           [0.37642, 0.52674, 0.67266],      
           [0.38441, 0.53285, 0.67689],      
           [0.39249, 0.53901, 0.68115],      
           [0.40065, 0.54523, 0.68546],      
           [0.40886, 0.5515, 0.6898],      
           [0.41717, 0.55782, 0.69417],      
           [0.42553, 0.5642, 0.69859],      
           [0.43397, 0.57062, 0.70304],      
           [0.44251, 0.57711, 0.70753],      
           [0.4511, 0.58365, 0.71206],      
           [0.45977, 0.59024, 0.71663],      
           [0.46851, 0.5969, 0.72122],      
           [0.47733, 0.6036, 0.72587],      
           [0.48621, 0.61035, 0.73054],      
           [0.49518, 0.61716, 0.73526],      
           [0.50422, 0.62403, 0.74001],      
           [0.51332, 0.63095, 0.74479],      
           [0.52249, 0.63791, 0.74961],      
           [0.53174, 0.64493, 0.75448],      
           [0.54105, 0.65201, 0.75937],      
           [0.55045, 0.65914, 0.76431],      
           [0.55991, 0.66631, 0.76928],      
           [0.56942, 0.67355, 0.77428],      
           [0.57903, 0.68082, 0.77932],      
           [0.58868, 0.68816, 0.7844],      
           [0.59841, 0.69555, 0.78951],      
           [0.60822, 0.70298, 0.79465],      
           [0.61808, 0.71046, 0.79983],      
           [0.62801, 0.71799, 0.80504],      
           [0.63799, 0.72557, 0.81028],      
           [0.64804, 0.73319, 0.81556],      
           [0.65816, 0.74085, 0.82086],      
           [0.66833, 0.74857, 0.82619],      
           [0.67856, 0.75632, 0.83156],      
           [0.68885, 0.76412, 0.83695],      
           [0.69917, 0.77195, 0.84236],      
           [0.70957, 0.77983, 0.84779],      
           [0.72, 0.78773, 0.85323],      
           [0.73047, 0.79568, 0.85869],      
           [0.74097, 0.80365, 0.86416],      
           [0.75152, 0.81164, 0.86962],      
           [0.76207, 0.81965, 0.87507],      
           [0.77263, 0.82768, 0.88049],      
           [0.78319, 0.83571, 0.88586],      
           [0.79373, 0.84372, 0.89116],      
           [0.8042, 0.85171, 0.89637],      
           [0.81458, 0.85965, 0.90143],      
           [0.82483, 0.8675, 0.90632],      
           [0.83489, 0.87523, 0.91097],      
           [0.84468, 0.88278, 0.91532],      
           [0.85411, 0.89011, 0.9193],      
           [0.86308, 0.89713, 0.92282],      
           [0.87146, 0.90374, 0.9258],      
           [0.87912, 0.90987, 0.92813],      
           [0.88593, 0.9154, 0.92975],      
           [0.89175, 0.92024, 0.93056],      
           [0.89648, 0.92432, 0.9305],      
           [0.90002, 0.92755, 0.92953],      
           [0.9023, 0.92989, 0.92762],      
           [0.90331, 0.93131, 0.92477],      
           [0.90304, 0.93182, 0.92102],      
           [0.90154, 0.93143, 0.91641],      
           [0.89887, 0.93019, 0.91101],      
           [0.89513, 0.92816, 0.90491],      
           [0.89043, 0.92543, 0.89819],      
           [0.88488, 0.92207, 0.89095],      
           [0.87861, 0.91817, 0.88329],      
           [0.87172, 0.9138, 0.87526],      
           [0.86432, 0.90905, 0.86695],      
           [0.85649, 0.90398, 0.85841],      
           [0.84833, 0.89865, 0.84969],      
           [0.83989, 0.8931, 0.84081],      
           [0.83122, 0.88739, 0.83181],      
           [0.82237, 0.88154, 0.8227],      
           [0.81337, 0.87558, 0.81351],      
           [0.80425, 0.86952, 0.80425],      
           [0.79503, 0.86339, 0.79491],      
           [0.78573, 0.8572, 0.78553],      
           [0.77636, 0.85095, 0.77609],      
           [0.76692, 0.84467, 0.76661],      
           [0.75744, 0.83835, 0.75709],      
           [0.74792, 0.832, 0.74754],      
           [0.73835, 0.82562, 0.73794],      
           [0.72875, 0.81922, 0.72832],      
           [0.71913, 0.8128, 0.71868],      
           [0.70949, 0.80637, 0.70902],      
           [0.69982, 0.79992, 0.69932],      
           [0.69014, 0.79346, 0.68963],      
           [0.68045, 0.78699, 0.67991],      
           [0.67076, 0.78051, 0.6702],      
           [0.66105, 0.77403, 0.66047],      
           [0.65136, 0.76755, 0.65075],      
           [0.64165, 0.76108, 0.64102],      
           [0.63196, 0.75461, 0.63131],      
           [0.62228, 0.74814, 0.6216],      
           [0.61261, 0.74168, 0.61191],      
           [0.60296, 0.73523, 0.60223],      
           [0.59333, 0.72879, 0.59258],      
           [0.58372, 0.72237, 0.58294],      
           [0.57413, 0.71597, 0.57334],      
           [0.56459, 0.70958, 0.56376],      
           [0.55507, 0.70322, 0.55421],      
           [0.54559, 0.69687, 0.5447],      
           [0.53615, 0.69055, 0.53523],      
           [0.52675, 0.68426, 0.5258],      
           [0.51739, 0.67801, 0.5164],      
           [0.50808, 0.67177, 0.50706],      
           [0.49881, 0.66557, 0.49777],      
           [0.48958, 0.65939, 0.48851],      
           [0.48042, 0.65325, 0.47931],      
           [0.47132, 0.64715, 0.47017],      
           [0.46225, 0.64107, 0.46106],      
           [0.45325, 0.63504, 0.45203],      
           [0.44431, 0.62904, 0.44304],      
           [0.43542, 0.62308, 0.4341],      
           [0.42658, 0.61715, 0.42524],      
           [0.41781, 0.61126, 0.41642],      
           [0.40909, 0.6054, 0.40766],      
           [0.40045, 0.59959, 0.39896],      
           [0.39185, 0.59382, 0.39032],      
           [0.38333, 0.58807, 0.38175],      
           [0.37486, 0.58238, 0.37323],      
           [0.36646, 0.57673, 0.36477],      
           [0.35812, 0.5711, 0.35639],      
           [0.34985, 0.56551, 0.34805],      
           [0.34163, 0.55997, 0.33978],      
           [0.33348, 0.55445, 0.33154],      
           [0.32537, 0.54897, 0.32338],      
           [0.31734, 0.5435, 0.31527],      
           [0.30936, 0.53807, 0.30719],      
           [0.30139, 0.53264, 0.29917],      
           [0.29348, 0.52723, 0.29117],      
           [0.2856, 0.5218, 0.28319],      
           [0.27776, 0.51637, 0.27523],      
           [0.26992, 0.51092, 0.26726],      
           [0.26208, 0.50544, 0.25934],      
           [0.25426, 0.49992, 0.25139],      
           [0.24641, 0.49436, 0.2434],      
           [0.23859, 0.48873, 0.23547],      
           [0.23078, 0.48303, 0.2275],      
           [0.22299, 0.47726, 0.21955],      
           [0.21519, 0.47141, 0.21162],      
           [0.20746, 0.46546, 0.20371],      
           [0.19975, 0.45944, 0.19583],      
           [0.19216, 0.45332, 0.18805],      
           [0.18466, 0.44709, 0.18029],      
           [0.17728, 0.44077, 0.17267],      
           [0.17004, 0.43436, 0.16516],      
           [0.16299, 0.42785, 0.15783],      
           [0.15615, 0.42122, 0.15065],      
           [0.14954, 0.41452, 0.14367],      
           [0.14319, 0.40772, 0.13688],      
           [0.13715, 0.40086, 0.13037],      
           [0.13142, 0.39388, 0.12401],      
           [0.12604, 0.38685, 0.118],      
           [0.12094, 0.37977, 0.11224],      
           [0.11631, 0.37262, 0.10676],      
           [0.11197, 0.36544, 0.10148],      
           [0.10795, 0.35822, 0.096498],      
           [0.1043, 0.35097, 0.091908],      
           [0.10099, 0.34368, 0.087495],      
           [0.09801, 0.33639, 0.083276],      
           [0.09526, 0.3291, 0.079326],      
           [0.092688, 0.32178, 0.075628],      
           [0.09043, 0.31448, 0.072139],      
           [0.088312, 0.30718, 0.068912],      
           [0.086311, 0.29989, 0.065708],      
           [0.084528, 0.29261, 0.062804],      
           [0.082751, 0.28534, 0.059986],      
           [0.081097, 0.27811, 0.057227],      
           [0.079445, 0.2709, 0.054671],      
           [0.077857, 0.2637, 0.052231],      
           [0.076319, 0.25652, 0.049974],      
           [0.074814, 0.24938, 0.047724],      
           [0.073376, 0.24228, 0.045555],      
           [0.071888, 0.23523, 0.043204],      
           [0.070497, 0.2282, 0.040881],      
           [0.069269, 0.22122, 0.03829],      
           [0.06795, 0.21428, 0.035663],      
           [0.066717, 0.20739, 0.032729],      
           [0.065546, 0.20053, 0.029942],      
           [0.064438, 0.19379, 0.027099],      
           [0.063398, 0.18707, 0.024191],      
           [0.062387, 0.18039, 0.021213],      
           [0.061326, 0.1738, 0.01816],      
           [0.060486, 0.16728, 0.015026],      
           [0.05968, 0.16077, 0.011816]]      
      
cork_map = LinearSegmentedColormap.from_list('cork', cm_data)      
# For use of "viscm view"      
test_cm = cork_map      
      
if __name__ == "__main__":      
    import matplotlib.pyplot as plt      
    import numpy as np      
      
    try:      
        from viscm import viscm      
        viscm(cork_map)      
    except ImportError:      
        print("viscm not found, falling back on simple display")      
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',      
                   cmap=cork_map)      
    plt.show()      