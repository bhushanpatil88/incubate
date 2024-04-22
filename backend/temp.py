import random
import igraph as ig
import json

profile_ceo = './Profile/ceo'
profile_cto = './Profile/cto'
profile_cmo = './Profile/cmo'




edges = []
for i in range(0,1001):
    for j in range(0,1001):
        ran_num = random.choice([1,2,3,4,5,6,7,8,9,10])
        if ran_num == 5:
            ran_wt = random.choice([1,2,3,4,5,6,7,8,9,10])
            edges.append((f'cto_{i}',f'cmo_{j}',ran_wt))

for i in range(0,1001):
    for j in range(0,1001):
        ran_num = random.choice([1,2,3,4,5,6,7,8,9,10])
        if ran_num == 5:
            ran_wt = random.choice([1,2,3,4,5,6,7,8,9,10])
            edges.append((f'cto_{i}',f'ceo_{j}',ran_wt))

for i in range(0,1001):
    for j in range(0,1001):
        ran_num = random.choice([1,2,3,4,5,6,7,8,9,10])
        if ran_num == 5:
            ran_wt = random.choice([1,2,3,4,5,6,7,8,9,10])
            edges.append((f'ceo_{i}',f'cmo_{j}',ran_wt))


G = ig.Graph.TupleList(edges, weights=True)
partition = G.community_multilevel(weights='weight')
print(partition)
communities = {}

# Iterate over each vertex and its corresponding community
# for vertex, community_id in enumerate(partition.membership):
#     if community_id not in communities:
#         # If the community is not yet in the dictionary, add it
#         communities[community_id] = [vertex]
#     else:
#         # If the community is already in the dictionary, append the vertex to its list
#         communities[community_id].append(vertex)



# json_obj = json.dumps(G_dict)

# with open("Graph.json",'w') as f:
#     f.write(json_obj)
G_dict = {
    "Community_1": [ "cto_0, cmo_0, cmo_41, cmo_85, cmo_231, cmo_262, cmo_293, cmo_310, cmo_342,
    cmo_410, cmo_446, cmo_490, cmo_497, cmo_509, cmo_578, cmo_711, cmo_735,
    cmo_858, cmo_885, cmo_973, cmo_974, cmo_123, cmo_131, cmo_215, cmo_222,
    cmo_343, cmo_391, cmo_439, cmo_494, cmo_545, cmo_794, cmo_798, cmo_810,
    cmo_942, cmo_171, cmo_244, cmo_291, cmo_369, cmo_382, cmo_485, cmo_530,
    cmo_543, cmo_608, cmo_760, cmo_768, cmo_948, cmo_166, cmo_176, cmo_230,
    cmo_502, cmo_697, cmo_995, cmo_73, cmo_307, cmo_756, cmo_954, cmo_960,
    cmo_80, cmo_179, cmo_187, cmo_472, cmo_488, cmo_774, cmo_874, cmo_128,
    cmo_329, cmo_334, cmo_629, cmo_636, cmo_82, cmo_152, cmo_246, cmo_322,
    cmo_938, cmo_966, cmo_664, cmo_746, cmo_825, cmo_944, cmo_76, cmo_180,
    cmo_407, cmo_484, cmo_799, cmo_39, cmo_136, cmo_653, cmo_581, cmo_705,
    cmo_872, cmo_383, cmo_737, cmo_772, cmo_124, cmo_216, cmo_450, cmo_596,
    cmo_169, cmo_242, cmo_440, cmo_481, cmo_226, cmo_824, cmo_851, cmo_247,
    cmo_767, cmo_538, cmo_998, cmo_397, cmo_888, cmo_153, cmo_738, cmo_129,
    cmo_96, cmo_658, cmo_327, cmo_715, cmo_464, cmo_994, cto_28, cmo_224,
    cmo_572, cmo_448, cmo_546, cmo_186, cmo_820, cmo_78, cmo_207, cmo_892,
    cto_56, cmo_287, cto_62, cto_64, cto_70, cto_75, cto_78, cto_84, cto_101,
    cto_103, cto_106, cto_115, cto_119, cto_142, cto_143, cto_149, cto_154,
    cto_156, cto_162, cto_182, cto_194, cto_209, cto_215, cto_234, cto_251,
    cto_253, cto_255, cto_260, cto_267, cto_296, cto_308, cto_311, cto_325,
    cto_327, cto_329, cto_332, cto_350, cto_353, cto_355, cto_382, cto_384,
    cto_390, cto_391, cto_413, cto_418, cto_440, cto_454, cto_461, cto_463,
    cto_465, cto_473, cto_475, cto_482, cto_485, cto_505, cto_508, cto_515,
    cto_517, cto_519, cto_521, cto_523, cto_527, cto_536, cto_540, cto_541,
    cto_552, cto_565, cto_580, cto_583, cto_584, cto_600, cto_617, cto_620,
    cto_659, cto_670, cto_671, cto_679, cto_695, cto_701, cto_704, cto_709,
    cto_710, cto_711, cto_722, cto_723, cto_726, cto_734, cto_754, cto_765,
    cto_769, cto_778, cto_779, cto_785, cto_786, cto_792, cto_796, cto_797,
    cto_800, cto_802, cto_809, cto_810, cto_813, cto_819, cto_831, cto_842,
    cto_843, cto_846, cto_852, cto_853, cto_855, cto_858, cto_872, cto_885,
    cto_890, cto_923, cto_927, cto_932, cto_934, cto_936, cto_941, cto_953,
    cto_960, cto_970, cto_979, cto_980, cto_990, cto_998, cto_1000, ceo_3,
    ceo_63, ceo_84, ceo_85, ceo_152, ceo_215, ceo_253, ceo_309, ceo_430,
    ceo_435, ceo_558, ceo_639, ceo_669, ceo_743, ceo_922, ceo_15, ceo_92,
    ceo_213, ceo_583, ceo_656, ceo_695, ceo_718, ceo_788, ceo_818, ceo_24,
    ceo_178, ceo_240, ceo_325, ceo_346, ceo_501, ceo_516, ceo_527, ceo_569,
    ceo_663, ceo_689, ceo_748, ceo_822, ceo_872, ceo_906, ceo_140, ceo_198,
    ceo_229, ceo_377, ceo_530, ceo_773, ceo_69, ceo_125, ceo_159, ceo_398,
    ceo_405, ceo_478, ceo_559, ceo_611, ceo_756, ceo_94, ceo_291, ceo_358,
    ceo_378, ceo_737, ceo_32, ceo_444, ceo_764, ceo_857, ceo_564, ceo_699,
    ceo_949, ceo_217, ceo_554, ceo_565, ceo_578, ceo_753, ceo_987, ceo_997,
    ceo_553, ceo_815, ceo_894, ceo_121, ceo_414, ceo_173, ceo_562, ceo_724,
    ceo_759, ceo_877, ceo_109, ceo_582, ceo_826, ceo_998, ceo_70, ceo_483,
    ceo_524, ceo_871, ceo_962, ceo_90, ceo_334, ceo_745, ceo_741, ceo_366,
    ceo_468, ceo_744, ceo_763, ceo_786, ceo_630, ceo_641, ceo_655, ceo_54,
    ceo_222, ceo_960, ceo_970, ceo_486, ceo_781, ceo_953, ceo_41, ceo_6,
    ceo_338, ceo_62, ceo_155, ceo_757, ceo_782, ceo_804, ceo_266, ceo_219,
    ceo_397, ceo_923"],
"Community_2" : [ "cmo_7, cmo_111, cmo_467, cmo_519, cmo_532, cmo_604, cmo_688, cmo_831,
    cmo_922, cmo_931, cmo_135, cmo_160, cmo_255, cmo_304, cmo_337, cmo_452,
    cmo_471, cmo_703, cmo_718, cmo_4, cmo_75, cmo_119, cmo_275, cmo_332,
    cmo_341, cmo_521, cmo_587, cmo_666, cmo_712, cmo_785, cmo_807, cmo_813,
    cmo_914, cmo_941, cmo_87, cmo_249, cmo_346, cmo_710, cmo_803, cmo_350,
    cmo_406, cmo_491, cmo_634, cmo_721, cmo_870, cmo_970, cmo_65, cmo_190,
    cmo_234, cmo_292, cmo_808, cmo_829, cto_6, cmo_162, cmo_194, cmo_286,
    cmo_328, cmo_434, cmo_603, cmo_612, cmo_987, cmo_56, cmo_432, cmo_477,
    cmo_489, cmo_702, cmo_822, cmo_880, cmo_228, cmo_232, cmo_513, cmo_741,
    cmo_795, cto_9, cmo_396, cmo_447, cmo_466, cmo_708, cmo_732, cmo_31,
    cmo_250, cmo_267, cmo_367, cmo_478, cmo_681, cmo_217, cmo_374, cmo_480,
    cmo_740, cmo_919, cmo_551, cmo_583, cmo_9, cmo_621, cmo_727, cmo_733,
    cmo_351, cmo_510, cmo_716, cmo_937, cmo_38, cmo_229, cmo_832, cmo_853,
    cto_16, cmo_206, cmo_924, cmo_264, cmo_418, cmo_114, cmo_796, cmo_977,
    cmo_278, cmo_110, cmo_827, cmo_443, cto_27, cto_30, cmo_175, cto_37,
    cmo_220, cto_40, cto_42, cmo_515, cto_48, cto_51, cto_60, cto_69, cto_79,
    cto_97, cto_102, cto_105, cto_108, cto_127, cto_137, cto_160, cto_169,
    cto_172, cto_178, cto_185, cto_186, cto_191, cto_197, cto_210, cto_214,
    cto_224, cto_250, cto_258, cto_266, cto_268, cto_280, cto_282, cto_288,
    cto_293, cto_300, cto_315, cto_333, cto_344, cto_357, cto_367, cto_372,
    cto_378, cto_380, cto_393, cto_394, cto_396, cto_401, cto_406, cto_436,
    cto_472, cto_479, cto_492, cto_498, cto_499, cto_506, cto_514, cto_520,
    cto_526, cto_549, cto_570, cto_572, cto_577, cto_587, cto_597, cto_602,
    cto_606, cto_614, cto_618, cto_619, cto_624, cto_632, cto_634, cto_636,
    cto_641, cto_642, cto_648, cto_665, cto_669, cto_676, cto_681, cto_683,
    cto_688, cto_693, cto_721, cto_725, cto_733, cto_741, cto_742, cto_749,
    cto_783, cto_794, cto_812, cto_837, cto_841, cto_845, cto_863, cto_868,
    cto_869, cto_902, cto_909, cto_914, cto_925, cto_946, cto_948, cto_951,
    cto_956, cto_972, cto_973, cto_974, cto_977, cto_991, cto_997, ceo_31,
    ceo_44, ceo_56, ceo_67, ceo_131, ceo_238, ceo_251, ceo_255, ceo_593,
    ceo_605, ceo_624, ceo_635, ceo_665, ceo_941, ceo_964, ceo_980, ceo_986,
    ceo_58, ceo_176, ceo_297, ceo_359, ceo_423, ceo_471, ceo_475, ceo_1,
    ceo_23, ceo_991, ceo_503, ceo_518, ceo_610, ceo_880, ceo_110, ceo_263,
    ceo_485, ceo_585, ceo_708, ceo_785, ceo_813, ceo_907, ceo_8, ceo_118,
    ceo_151, ceo_205, ceo_526, ceo_540, ceo_618, ceo_647, ceo_676, ceo_808,
    ceo_985, ceo_231, ceo_315, ceo_408, ceo_453, ceo_499, ceo_563, ceo_774,
    ceo_827, ceo_248, ceo_464, ceo_617, ceo_643, ceo_698, ceo_859, ceo_919,
    ceo_167, ceo_185, ceo_313, ceo_547, ceo_638, ceo_855, ceo_268, ceo_300,
    ceo_424, ceo_469, ceo_784, ceo_912, ceo_932, ceo_648, ceo_89, ceo_134,
    ceo_212, ceo_714, ceo_51, ceo_869, ceo_460, ceo_210, ceo_441, ceo_581,
    ceo_700, ceo_705, ceo_910, ceo_992, ceo_382, ceo_701, ceo_806, ceo_819,
    ceo_487, ceo_586, ceo_958, ceo_170, ceo_621, ceo_86, ceo_664, ceo_679,
    ceo_968, ceo_401, ceo_861, ceo_165, ceo_627, ceo_78"],
    "Community_3" : [ "cmo_74, cmo_84, cmo_240, cmo_252, cmo_852, cmo_855, cmo_104, cmo_185,
    cmo_421, cmo_475, cmo_623, cmo_672, cmo_876, cmo_22, cmo_165, cmo_221,
    cmo_479, cmo_655, cmo_657, cmo_983, cmo_986, cmo_44, cmo_182, cmo_499,
    cmo_674, cmo_689, cmo_817, cmo_830, cmo_864, cmo_227, cmo_442, cmo_615,
    cmo_678, cmo_828, cmo_58, cmo_627, cmo_920, cmo_97, cmo_358, cmo_463,
    cmo_961, cmo_203, cmo_801, cmo_899, cmo_527, cmo_297, cmo_373, cmo_745,
    cmo_413, cmo_419, cmo_43, cmo_701, cmo_945, cmo_192, cmo_667, cmo_579,
    cmo_786, cmo_574, cmo_857, cmo_909, cmo_151, cmo_901, cmo_750, cmo_923,
    cmo_619, cmo_838, cmo_425, cmo_896, cto_29, cmo_506, cmo_595, cmo_132,
    cto_36, cmo_561, cmo_771, cto_74, cto_81, cto_83, cto_87, cto_90, cto_94,
    cto_100, cto_109, cto_120, cto_147, cto_165, cto_174, cto_175, cto_188,
    cto_216, cto_220, cto_236, cto_276, cto_283, cto_284, cto_303, cto_319,
    cto_326, cto_330, cto_352, cto_373, cto_381, cto_399, cto_405, cto_408,
    cto_414, cto_424, cto_425, cto_512, cto_581, cto_595, cto_596, cto_615,
    cto_621, cto_639, cto_656, cto_664, cto_667, cto_678, cto_715, cto_719,
    cto_727, cto_731, cto_737, cto_763, cto_807, cto_815, cto_817, cto_830,
    cto_838, cto_839, cto_864, cto_867, cto_871, cto_879, cto_881, cto_884,
    cto_892, cto_898, cto_922, cto_930, cto_937, cto_944, cto_994, cto_996,
    ceo_19, ceo_116, ceo_305, ceo_357, ceo_626, ceo_651, ceo_654, ceo_659,
    ceo_687, ceo_844, ceo_420, ceo_513, ceo_905, ceo_926, ceo_39, ceo_201,
    ceo_561, ceo_682, ceo_223, ceo_354, ceo_418, ceo_731, ceo_879, ceo_71,
    ceo_311, ceo_733, ceo_909, ceo_940, ceo_146, ceo_323, ceo_380, ceo_433,
    ceo_546, ceo_767, ceo_166, ceo_412, ceo_645, ceo_157, ceo_249, ceo_292,
    ceo_337, ceo_227, ceo_712, ceo_839, ceo_963, ceo_988, ceo_20, ceo_271,
    ceo_326, ceo_403, ceo_494, ceo_599, ceo_856, ceo_437, ceo_488, ceo_777,
    ceo_53, ceo_427, ceo_467, ceo_73, ceo_911, ceo_666, ceo_814, ceo_449,
    ceo_938, ceo_981, ceo_144, ceo_811, ceo_228, ceo_261, ceo_214, ceo_707,
    ceo_989"],
"Community_4" : ["cmo_77, cmo_163, cmo_239, cmo_354, cmo_355, cmo_564, cmo_725, cmo_754,
    cmo_804, cmo_811, cmo_844, cmo_61, cmo_143, cmo_243, cmo_251, cmo_430,
    cmo_465, cmo_470, cmo_537, cmo_540, cmo_597, cmo_698, cmo_773, cmo_877,
    cto_2, cmo_24, cmo_34, cmo_69, cmo_86, cmo_102, cmo_158, cmo_177, cmo_427,
    cmo_500, cmo_592, cmo_640, cmo_677, cmo_739, cmo_752, cmo_758, cmo_791,
    cmo_841, cmo_895, cmo_903, cmo_908, cmo_927, cmo_936, cmo_997, cmo_64,
    cmo_93, cmo_140, cmo_209, cmo_256, cmo_305, cmo_408, cmo_415, cmo_445,
    cmo_469, cmo_605, cmo_747, cmo_145, cmo_204, cmo_347, cmo_400, cmo_498,
    cmo_673, cmo_675, cmo_720, cmo_19, cmo_37, cmo_172, cmo_184, cmo_214,
    cmo_261, cmo_360, cmo_695, cmo_730, cmo_989, cmo_47, cmo_138, cmo_201,
    cmo_210, cmo_692, cmo_769, cmo_887, cmo_999, cmo_52, cmo_117, cmo_238,
    cmo_272, cmo_340, cmo_384, cmo_411, cmo_555, cmo_609, cmo_647, cmo_676,
    cmo_957, cmo_167, cmo_361, cmo_704, cmo_107, cmo_161, cmo_196, cmo_386,
    cmo_569, cmo_775, cmo_793, cmo_46, cmo_103, cmo_257, cmo_526, cto_11,
    cmo_271, cmo_508, cmo_582, cmo_873, cmo_126, cmo_326, cmo_375, cmo_809,
    cmo_26, cmo_669, cto_14, cmo_288, cmo_364, cmo_380, cmo_453, cmo_925,
    cmo_962, cmo_263, cmo_805, cmo_23, cmo_72, cmo_837, cto_17, cmo_27,
    cmo_55, cmo_116, cmo_181, cmo_381, cmo_590, cmo_94, cmo_390, cmo_897,
    cmo_294, cmo_483, cmo_766, cto_21, cmo_66, cmo_200, cmo_816, cmo_270,
    cmo_356, cmo_525, cmo_133, cmo_353, cmo_650, cmo_731, cto_24, cmo_573,
    cmo_35, cmo_779, cto_31, cmo_800, cmo_348, cto_35, cmo_985, cto_39,
    cto_41, cmo_571, cmo_435, cto_46, cto_53, cto_55, cto_58, cto_63, cto_68,
    cto_71, cto_72, cto_77, cto_85, cto_89, cto_104, cto_122, cto_125,
    cto_128, cto_130, cto_131, cto_138, cto_140, cto_151, cto_152, cto_155,
    cto_159, cto_168, cto_173, cto_176, cto_180, cto_181, cto_189, cto_198,
    cto_201, cto_204, cto_212, cto_219, cto_225, cto_230, cto_231, cto_235,
    cto_239, cto_244, cto_246, cto_257, cto_262, cto_265, cto_272, cto_274,
    cto_277, cto_278, cto_285, cto_290, cto_291, cto_301, cto_328, cto_336,
    cto_338, cto_348, cto_349, cto_360, cto_361, cto_365, cto_377, cto_395,
    cto_407, cto_415, cto_420, cto_426, cto_433, cto_437, cto_446, cto_449,
    cto_453, cto_455, cto_464, cto_471, cto_476, cto_478, cto_481, cto_493,
    cto_500, cto_538, cto_546, cto_557, cto_562, cto_564, cto_569, cto_571,
    cto_576, cto_588, cto_591, cto_592, cto_598, cto_599, cto_608, cto_609,
    cto_612, cto_625, cto_626, cto_627, cto_633, cto_635, cto_637, cto_647,
    cto_652, cto_653, cto_655, cto_658, cto_666, cto_668, cto_687, cto_698,
    cto_702, cto_705, cto_706, cto_713, cto_732, cto_744, cto_745, cto_761,
    cto_764, cto_768, cto_774, cto_775, cto_776, cto_780, cto_781, cto_787,
    cto_803, cto_804, cto_806, cto_824, cto_828, cto_829, cto_832, cto_840,
    cto_848, cto_850, cto_854, cto_865, cto_875, cto_880, cto_883, cto_896,
    cto_905, cto_911, cto_913, cto_919, cto_929, cto_950, cto_954, cto_955,
    cto_967, cto_971, cto_984, cto_986, cto_987, cto_999, ceo_179, ceo_206,
    ceo_216, ceo_270, ceo_332, ceo_340, ceo_391, ceo_416, ceo_419, ceo_457,
    ceo_571, ceo_580, ceo_596, ceo_736, ceo_755, ceo_830, ceo_849, ceo_947,
    ceo_11, ceo_43, ceo_133, ceo_172, ceo_225, ceo_246, ceo_272, ceo_301,
    ceo_327, ceo_333, ceo_349, ceo_570, ceo_600, ceo_615, ceo_721, ceo_842,
    ceo_873, ceo_990, ceo_103, ceo_145, ceo_290, ceo_320, ceo_387, ceo_470,
    ceo_509, ceo_512, ceo_595, ceo_670, ceo_691, ceo_709, ceo_833, ceo_920,
    ceo_934, ceo_994, ceo_274, ceo_304, ceo_308, ceo_411, ceo_548, ceo_616,
    ceo_650, ceo_776, ceo_885, ceo_40, ceo_141, ceo_149, ceo_150, ceo_283,
    ceo_374, ceo_399, ceo_445, ceo_495, ceo_572, ceo_750, ceo_893, ceo_975,
    ceo_100, ceo_186, ceo_199, ceo_243, ceo_413, ceo_440, ceo_704, ceo_716,
    ceo_68, ceo_439, ceo_493, ceo_535, ceo_694, ceo_841, ceo_863, ceo_881,
    ceo_995, ceo_511, ceo_532, ceo_598, ceo_732, ceo_889, ceo_944, ceo_952,
    ceo_984, ceo_142, ceo_171, ceo_237, ceo_336, ceo_395, ceo_101, ceo_376,
    ceo_389, ceo_489, ceo_577, ceo_607, ceo_730, ceo_812, ceo_42, ceo_111,
    ceo_668, ceo_30, ceo_75, ceo_83, ceo_285, ceo_451, ceo_456, ceo_461,
    ceo_865, ceo_816, ceo_977, ceo_66, ceo_295, ceo_302, ceo_480, ceo_104,
    ceo_328, ceo_407, ceo_678, ceo_942, ceo_393, ceo_510, ceo_128, ceo_720,
    ceo_273, ceo_862, ceo_584, ceo_603, ceo_829, ceo_983, ceo_77, ceo_182,
    ceo_696, ceo_681, ceo_845, ceo_312, ceo_706, ceo_738, ceo_843, ceo_925,
    ceo_180, ceo_352, ceo_652, ceo_908, ceo_772, ceo_202, ceo_369, ceo_417,
    ceo_588, ceo_860, ceo_798"],
"Commnity_5":["cmo_90, cmo_120, cmo_147, cmo_638, cmo_649, cmo_690, cmo_792, cmo_818,
    cmo_862, cmo_912, cmo_980, cmo_50, cmo_362, cmo_637, cmo_784, cmo_869,
    cmo_883, cmo_13, cmo_283, cmo_507, cmo_878, cmo_991, cmo_258, cmo_273,
    cmo_486, cmo_535, cmo_622, cmo_821, cmo_91, cmo_495, cmo_585, cmo_755,
    cmo_871, cmo_389, cmo_462, cmo_552, cmo_867, cmo_921, cmo_279, cmo_444,
    cmo_474, cmo_645, cmo_788, cmo_982, cmo_276, cmo_339, cmo_376, cmo_492,
    cmo_496, cmo_654, cmo_324, cmo_557, cmo_379, cmo_743, cmo_902, cmo_420,
    cmo_624, cmo_707, cmo_969, cto_12, cmo_144, cmo_235, cmo_562, cmo_683,
    cto_13, cmo_20, cmo_108, cmo_344, cmo_518, cmo_780, cmo_848, cmo_976,
    cto_15, cmo_115, cmo_797, cmo_197, cmo_847, cmo_763, cmo_25, cmo_137,
    cmo_449, cto_38, cmo_943, cto_44, cto_65, cto_80, cto_91, cto_95, cto_112,
    cto_113, cto_116, cto_126, cto_129, cto_133, cto_192, cto_200, cto_221,
    cto_229, cto_238, cto_243, cto_248, cto_269, cto_271, cto_294, cto_304,
    cto_307, cto_310, cto_322, cto_323, cto_324, cto_340, cto_345, cto_346,
    cto_358, cto_371, cto_392, cto_398, cto_403, cto_435, cto_444, cto_452,
    cto_484, cto_491, cto_495, cto_530, cto_537, cto_543, cto_545, cto_547,
    cto_548, cto_554, cto_563, cto_567, cto_575, cto_582, cto_594, cto_613,
    cto_616, cto_643, cto_649, cto_662, cto_694, cto_736, cto_739, cto_747,
    cto_750, cto_752, cto_755, cto_758, cto_767, cto_771, cto_798, cto_801,
    cto_811, cto_814, cto_820, cto_825, cto_844, cto_849, cto_882, cto_893,
    cto_904, cto_921, cto_924, cto_935, cto_943, ceo_120, ceo_143, ceo_211,
    ceo_306, ceo_335, ceo_481, ceo_683, ceo_800, ceo_996, ceo_5, ceo_236,
    ceo_775, ceo_875, ceo_930, ceo_957, ceo_29, ceo_97, ceo_568, ceo_824,
    ceo_902, ceo_978, ceo_160, ceo_232, ceo_351, ceo_454, ceo_463, ceo_589,
    ceo_899, ceo_931, ceo_976, ceo_130, ceo_168, ceo_169, ceo_343, ceo_428,
    ceo_579, ceo_609, ceo_810, ceo_993, ceo_48, ceo_208, ceo_314, ceo_496,
    ceo_742, ceo_900, ceo_914, ceo_915, ceo_28, ceo_91, ceo_218, ceo_259,
    ceo_522, ceo_739, ceo_34, ceo_135, ceo_138, ceo_14, ceo_316, ceo_360,
    ceo_404, ceo_350, ceo_508, ceo_276, ceo_400, ceo_686, ceo_740, ceo_797,
    ceo_956, ceo_114, ceo_355, ceo_884, ceo_749, ceo_766, ceo_383, ceo_840,
    ceo_9, ceo_933, ceo_793, ceo_821, ceo_883, ceo_341, ceo_390, ceo_719,
    ceo_99, ceo_254, ceo_267, ceo_61"],
"Communtiy_6" :["cmo_105, cmo_125, cmo_146, cmo_199, cmo_223, cmo_241, cmo_254, cmo_363,
    cmo_422, cmo_473, cmo_520, cmo_523, cmo_533, cmo_633, cmo_713, cmo_789,
    cmo_842, cmo_898, cmo_940, cto_1, cmo_10, cmo_49, cmo_59, cmo_83, cmo_274,
    cmo_301, cmo_308, cmo_403, cmo_644, cmo_646, cmo_765, cmo_953, cmo_150,
    cmo_323, cmo_405, cmo_428, cmo_454, cmo_461, cmo_684, cmo_964, cmo_11,
    cmo_112, cmo_277, cmo_302, cmo_316, cmo_599, cmo_648, cmo_724, cmo_866,
    cmo_868, cto_4, cmo_48, cmo_159, cmo_173, cmo_438, cmo_544, cmo_567,
    cmo_584, cmo_641, cmo_933, cmo_972, cmo_2, cmo_67, cmo_79, cmo_349,
    cmo_424, cmo_455, cmo_563, cmo_594, cmo_694, cmo_935, cmo_118, cmo_370,
    cmo_517, cmo_71, cmo_157, cmo_628, cmo_696, cmo_846, cto_8, cmo_285,\
    cmo_321, cmo_401, cmo_685, cmo_782, cmo_33, cmo_416, cmo_660, cmo_860,\
    cmo_306, cmo_542, cmo_812, cmo_17, cmo_570, cmo_661, cmo_682, cmo_823,\
    cmo_963, cmo_539, cmo_749, cmo_843, cmo_178, cmo_884, cmo_1, cmo_387,\
    cmo_516, cmo_524, cmo_534, cmo_53, cmo_748, cto_20, cmo_881, cmo_967,\
    cmo_211, cmo_437, cmo_441, cmo_744, cmo_894, cmo_14, cmo_759, cmo_92,\
    cmo_237, cmo_662, cto_26, cmo_536, cmo_198, cmo_971, cto_34, cmo_130,\
    cmo_134, cmo_882, cmo_836, cmo_141, cto_45, cmo_318, cmo_993, cmo_642,\
    cto_88, cto_98, cto_124, cto_136, cto_148, cto_153, cto_170, cto_177,\
    cto_179, cto_193, cto_207, cto_211, cto_223, cto_226, cto_227, cto_242,\
    cto_247, cto_249, cto_270, cto_281, cto_289, cto_295, cto_297, cto_298,\
    cto_299, cto_305, cto_306, cto_312, cto_313, cto_321, cto_331, cto_337,\
    cto_343, cto_354, cto_356, cto_366, cto_369, cto_386, cto_411, cto_416,\
    cto_422, cto_423, cto_429, cto_430, cto_434, cto_442, cto_443, cto_456,\
    cto_457, cto_459, cto_460, cto_466, cto_469, cto_470, cto_483, cto_494,\
    cto_507, cto_509, cto_510, cto_513, cto_531, cto_533, cto_535, cto_550,\
    cto_551, cto_574, cto_601, cto_607, cto_610, cto_611, cto_629, cto_630,\
    cto_644, cto_645, cto_657, cto_660, cto_663, cto_690, cto_697, cto_716,\
    cto_724, cto_729, cto_735, cto_738, cto_762, cto_766, cto_770, cto_782,\
    cto_789, cto_818, cto_835, cto_847, cto_851, cto_861, cto_870, cto_874,\
    cto_876, cto_878, cto_887, cto_895, cto_897, cto_907, cto_908, cto_910,\
    cto_920, cto_926, cto_928, cto_931, cto_939, cto_945, cto_947, cto_949,\
    cto_957, cto_961, cto_964, cto_965, cto_969, cto_982, cto_983, cto_985,\
    cto_992, cto_995, ceo_4, ceo_74, ceo_187, ceo_371, ceo_384, ceo_386,\
    ceo_628, ceo_684, ceo_903, ceo_47, ceo_88, ceo_244, ceo_250, ceo_361,\
    ceo_476, ceo_500, ceo_506, ceo_515, ceo_612, ceo_623, ceo_690, ceo_838,\
    ceo_895, ceo_918, ceo_971, ceo_108, ceo_147, ceo_161, ceo_299, ceo_347,\
    ceo_394, ceo_504, ceo_557, ceo_636, ceo_662, ceo_847, ceo_929, ceo_50,\
    ceo_289, ceo_294, ceo_409, ceo_436, ceo_619, ceo_792, ceo_999, ceo_2,\
    ceo_37, ceo_45, ceo_113, ceo_188, ceo_192, ceo_194, ceo_296, ceo_426,\
    ceo_479, ceo_590, ceo_591, ceo_677, ceo_787, ceo_891, ceo_897, ceo_917,\
    ceo_935, ceo_124, ceo_136, ceo_280, ceo_286, ceo_318, ceo_342, ceo_434,\
    ceo_549, ceo_608, ceo_779, ceo_868, ceo_132, ceo_637, ceo_717, ceo_954,\
    ceo_979, ceo_177, ceo_497, ceo_520, ceo_573, ceo_592, ceo_974, ceo_107,\
    ceo_345, ceo_432, ceo_556, ceo_613, ceo_834, ceo_870, ceo_943, ceo_55,\
    ceo_448, ceo_727, ceo_801, ceo_303, ceo_809, ceo_356, ceo_458, ceo_693,\
    ceo_233, ceo_455, ceo_928, ceo_604, ceo_646, ceo_322, ceo_0, ceo_887,\
    ceo_425, ceo_892, ceo_711, ceo_452, ceo_466, ceo_622, ceo_770, ceo_204,\
    ceo_858, ceo_831, ceo_846, ceo_898, ceo_951, ceo_587, ceo_293, ceo_631,\
    ceo_778, ceo_789, ceo_531"],
"Communtiy_7":[ "cmo_208, cmo_219, cmo_456, cmo_457, cmo_753, cmo_762, cmo_835, cmo_904,\
    cmo_905, cmo_926, cmo_949, cmo_965, cmo_101, cmo_295, cmo_468, cmo_589,\
    cmo_665, cmo_918, cmo_981, cmo_5, cmo_29, cmo_99, cmo_290, cmo_359,\
    cmo_504, cmo_693, cmo_958, cto_3, cmo_88, cmo_109, cmo_312, cmo_330,\
    cmo_365, cmo_522, cmo_548, cmo_588, cmo_686, cmo_913, cmo_928, cmo_3,\
    cmo_51, cmo_296, cmo_372, cmo_576, cmo_601, cmo_719, cmo_861, cmo_193,\
    cmo_433, cmo_459, cmo_610, cmo_975, cmo_988, cmo_188, cmo_268, cmo_591,\
    cmo_593, cmo_651, cmo_764, cmo_776, cmo_282, cmo_388, cmo_394, cmo_565,\
    cmo_875, cmo_36, cmo_156, cmo_213, cmo_266, cmo_815, cmo_996, cmo_568,\
    cmo_616, cmo_57, cmo_122, cmo_814, cmo_183, cmo_742, cmo_992, cmo_121,\
    cmo_174, cmo_336, cmo_429, cmo_850, cmo_30, cmo_501, cmo_680, cmo_127,\
    cmo_303, cmo_338, cmo_787, cmo_947, cmo_630, cmo_700, cmo_952, cmo_691,\
    cto_19, cmo_12, cmo_728, cmo_393, cmo_139, cmo_212, cmo_618, cto_23,\
    cto_25, cmo_652, cmo_893, cto_32, cto_33, cmo_300, cmo_431, cmo_505,\
    cto_43, cmo_460, cto_47, cto_49, cto_50, cto_54, cto_66, cto_92, cto_93,\
    cto_96, cto_114, cto_132, cto_134, cto_135, cto_141, cto_163, cto_166,\
    cto_171, cto_199, cto_213, cto_228, cto_241, cto_252, cto_254, cto_256,\
    cto_263, cto_309, cto_320, cto_335, cto_339, cto_342, cto_347, cto_359,\
    cto_363, cto_370, cto_375, cto_379, cto_397, cto_412, cto_417, cto_421,\
    cto_428, cto_432, cto_438, cto_441, cto_451, cto_462, cto_467, cto_468,\
    cto_488, cto_489, cto_511, cto_516, cto_522, cto_534, cto_539, cto_542,\
    cto_579, cto_590, cto_603, cto_605, cto_631, cto_640, cto_646, cto_651,\
    cto_654, cto_674, cto_677, cto_684, cto_692, cto_696, cto_703, cto_728,\
    cto_730, cto_760, cto_772, cto_773, cto_790, cto_816, cto_821, cto_826,\
    cto_827, cto_834, cto_836, cto_857, cto_862, cto_866, cto_891, cto_894,\
    cto_900, cto_916, cto_917, cto_940, cto_942, cto_952, cto_959, cto_962,\
    cto_976, cto_988, ceo_21, ceo_137, ceo_197, ceo_284, ceo_287, ceo_364,\
    ceo_450, ceo_538, ceo_601, ceo_632, ceo_754, ceo_848, ceo_972, ceo_33,\
    ceo_35, ceo_36, ceo_129, ceo_158, ceo_242, ceo_275, ceo_523, ceo_594,\
    ceo_597, ceo_794, ceo_927, ceo_59, ceo_117, ceo_431, ceo_642, ceo_660,\
    ceo_697, ceo_890, ceo_916, ceo_76, ceo_235, ceo_252, ceo_410, ceo_551,\
    ceo_634, ceo_713, ceo_758, ceo_973, ceo_492, ceo_505, ceo_543, ceo_791,\
    ceo_950, ceo_961, ceo_87, ceo_331, ceo_421, ceo_525, ceo_735, ceo_780,\
    ceo_955, ceo_12, ceo_321, ceo_367, ceo_771, ceo_837, ceo_886, ceo_196,\
    ceo_298, ceo_344, ceo_368, ceo_534, ceo_567, ceo_657, ceo_680, ceo_747,\
    ceo_825, ceo_190, ceo_239, ceo_576, ceo_614, ceo_969, ceo_200, ceo_536,\
    ceo_575, ceo_661, ceo_16, ceo_692, ceo_402, ceo_429, ceo_112, ceo_465,\
    ceo_674, ceo_703, ceo_555, ceo_658, ceo_710, ceo_783, ceo_307, ceo_765,\
    ceo_667, ceo_820, ceo_282, ceo_462, ceo_139, ceo_224, ceo_790, ceo_126,\
    ceo_162, ceo_256, ceo_533, ceo_220, ceo_802, ceo_119, ceo_13"],
"Community_8": ["cmo_233, cmo_319, cmo_335, cmo_409, cmo_600, cmo_668, cmo_723, cmo_819,\
    cmo_32, cmo_40, cmo_89, cmo_100, cmo_106, cmo_260, cmo_385, cmo_528,\
    cmo_709, cmo_932, cmo_939, cmo_45, cmo_315, cmo_357, cmo_503, cmo_639,\
    cmo_726, cmo_915, cmo_930, cmo_62, cmo_68, cmo_164, cmo_189, cmo_412,\
    cmo_625, cmo_916, cmo_1000, cmo_314, cmo_352, cmo_487, cmo_511, cmo_577,\
    cmo_729, cmo_751, cmo_840, cmo_859, cmo_863, cmo_889, cto_5, cmo_15,\
    cmo_42, cmo_265, cmo_298, cmo_514, cmo_575, cmo_865, cmo_917, cmo_6,\
    cmo_345, cmo_366, cmo_556, cmo_613, cmo_706, cmo_890, cmo_280, cmo_331,\
    cmo_371, cmo_529, cmo_781, cmo_849, cmo_984, cmo_98, cmo_325, cmo_395,\
    cmo_191, cmo_320, cmo_398, cmo_458, cmo_541, cmo_679, cmo_155, cmo_560,\
    cmo_886, cmo_253, cmo_482, cmo_929, cmo_990, cmo_309, cmo_512, cmo_476,\
    cmo_611, cmo_956, cmo_317, cmo_18, cmo_632, cto_22, cmo_368, cmo_598,\
    cmo_154, cmo_631, cmo_333, cmo_757, cmo_402, cmo_656, cmo_826, cmo_911,\
    cmo_968, cmo_734, cmo_580, cmo_856, cto_52, cto_57, cto_67, cto_73,\
    cto_76, cto_107, cto_110, cto_111, cto_118, cto_123, cto_139, cto_144,\
    cto_145, cto_150, cto_167, cto_184, cto_190, cto_195, cto_202, cto_203,\
    cto_206, cto_218, cto_233, cto_240, cto_245, cto_264, cto_279, cto_286,\
    cto_287, cto_314, cto_316, cto_318, cto_334, cto_341, cto_351, cto_374,\
    cto_385, cto_387, cto_389, cto_404, cto_410, cto_427, cto_431, cto_439,\
    cto_447, cto_450, cto_477, cto_480, cto_487, cto_490, cto_497, cto_502,\
    cto_504, cto_518, cto_528, cto_532, cto_544, cto_553, cto_558, cto_559,\
    cto_561, cto_566, cto_585, cto_593, cto_604, cto_623, cto_628, cto_638,\
    cto_661, cto_672, cto_673, cto_675, cto_682, cto_685, cto_686, cto_689,\
    cto_708, cto_718, cto_743, cto_753, cto_756, cto_759, cto_777, cto_791,\
    cto_793, cto_795, cto_799, cto_823, cto_833, cto_859, cto_877, cto_886,\
    cto_899, cto_901, cto_903, cto_912, cto_938, cto_958, cto_963, cto_968,\
    cto_981, ceo_18, ceo_164, ceo_281, ceo_406, ceo_491, ceo_529, ceo_606,\
    ceo_629, ceo_653, ceo_725, ceo_761, ceo_796, ceo_876, ceo_888, ceo_945,\
    ceo_106, ceo_234, ceo_362, ceo_365, ceo_422, ceo_472, ceo_715, ceo_769,\
    ceo_851, ceo_60, ceo_373, ceo_625, ceo_26, ceo_115, ceo_258, ceo_264,\
    ceo_673, ceo_752, ceo_966, ceo_49, ceo_82, ceo_193, ceo_372, ceo_447,\
    ceo_473, ceo_528, ceo_671, ceo_57, ceo_81, ceo_96, ceo_175, ceo_379,\
    ceo_385, ceo_807, ceo_817, ceo_948, ceo_965, ceo_521, ceo_123, ceo_230,\
    ceo_269, ceo_728, ceo_122, ceo_443, ceo_602, ceo_245, ceo_442, ceo_853,\
    ceo_288, ceo_7, ceo_339, ceo_507, ceo_25, ceo_79, ceo_156, ceo_241,\
    ceo_519, ceo_644, ceo_864, ceo_874, ceo_163, ceo_415, ceo_675, ceo_746,\
    ceo_904, ceo_924, ceo_27, ceo_649, ceo_854, ceo_852, ceo_38, ceo_127,\
    ceo_729, ceo_560, ceo_823, ceo_72, ceo_541, ceo_805, ceo_836, ceo_514,\
    ceo_498, ceo_502, ceo_633, ceo_762, ceo_207, ceo_363, ceo_330, ceo_93,\
    ceo_348"],
"Community_9" :["cmo_311, cmo_423, cmo_531, cmo_586, cmo_617, cmo_790, cmo_950, cmo_978,\
    cmo_16, cmo_21, cmo_205, cmo_245, cmo_248, cmo_299, cmo_554, cmo_620,\
    cmo_722, cmo_879, cmo_95, cmo_377, cmo_547, cmo_663, cmo_770, cmo_934,\
    cmo_289, cmo_378, cmo_392, cmo_404, cmo_553, cmo_614, cmo_626, cmo_671,\
    cmo_202, cmo_259, cmo_558, cmo_761, cmo_778, cmo_854, cmo_63, cmo_70,\
    cmo_218, cmo_399, cmo_414, cmo_417, cmo_806, cmo_891, cmo_946, cmo_959,\
    cmo_81, cmo_149, cmo_436, cmo_687, cmo_699, cmo_839, cmo_900, cto_7,\
    cmo_113, cmo_148, cmo_168, cmo_195, cmo_284, cmo_714, cmo_845, cmo_906,\
    cmo_979, cmo_54, cmo_606, cmo_907, cto_10, cmo_8, cmo_236, cmo_313,\
    cmo_493, cmo_777, cmo_834, cmo_955, cmo_717, cmo_802, cmo_549, cmo_602,\
    cmo_170, cmo_225, cmo_281, cmo_566, cmo_643, cmo_910, cmo_607, cmo_635,\
    cmo_60, cmo_550, cto_18, cmo_142, cmo_269, cmo_783, cmo_659, cmo_451,\
    cmo_736, cmo_951, cmo_28, cmo_426, cmo_833, cmo_559, cmo_670, cto_59,\
    cto_61, cto_82, cto_86, cto_99, cto_117, cto_121, cto_146, cto_157,\
    cto_158, cto_161, cto_164, cto_183, cto_187, cto_196, cto_205, cto_208,\
    cto_217, cto_222, cto_232, cto_237, cto_259, cto_261, cto_273, cto_275,\
    cto_292, cto_302, cto_317, cto_362, cto_364, cto_368, cto_376, cto_383,\
    cto_388, cto_400, cto_402, cto_409, cto_419, cto_445, cto_448, cto_458,\
    cto_474, cto_486, cto_496, cto_501, cto_503, cto_524, cto_525, cto_529,\
    cto_555, cto_556, cto_560, cto_568, cto_573, cto_578, cto_586, cto_589,\
    cto_622, cto_650, cto_680, cto_691, cto_699, cto_700, cto_707, cto_712,\
    cto_714, cto_717, cto_720, cto_740, cto_746, cto_748, cto_751, cto_757,\
    cto_784, cto_788, cto_805, cto_808, cto_822, cto_856, cto_860, cto_873,\
    cto_888, cto_889, cto_906, cto_915, cto_918, cto_933, cto_966, cto_975,\
    cto_978, cto_989, cto_993, ceo_95, ceo_98, ceo_174, ceo_542, ceo_702,\
    ceo_734, ceo_17, ceo_52, ceo_181, ceo_195, ceo_279, ceo_438, ceo_768,\
    ceo_799, ceo_835, ceo_921, ceo_22, ceo_153, ceo_392, ceo_474, ceo_544,\
    ceo_620, ceo_726, ceo_795, ceo_832, ceo_1000, ceo_189, ceo_257, ceo_375,\
    ceo_446, ceo_545, ceo_640, ceo_65, ceo_80, ceo_278, ceo_317, ceo_751,\
    ceo_760, ceo_221, ceo_388, ceo_396, ceo_484, ceo_574, ceo_672, ceo_937,\
    ceo_10, ceo_324, ceo_329, ceo_517, ceo_539, ceo_459, ceo_482, ceo_685,\
    ceo_850, ceo_939, ceo_64, ceo_154, ceo_265, ceo_310, ceo_490, ceo_566,\
    ceo_688, ceo_722, ceo_878, ceo_46, ceo_183, ceo_191, ceo_353, ceo_370,\
    ceo_936, ceo_946, ceo_959, ceo_803, ceo_913, ceo_262, ceo_866, ceo_537,\
    ceo_381, ceo_901, ceo_967, ceo_550, ceo_723, ceo_102, ceo_260, ceo_105,\
    ceo_477, ceo_867, ceo_896, ceo_226, ceo_247, ceo_319, ceo_277, ceo_828,\
    ceo_148, ceo_882, ceo_184, ceo_982, ceo_209, ceo_203, ceo_552"]

}


