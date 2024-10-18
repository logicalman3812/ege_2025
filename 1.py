from itertools import permutations

# table = "12 14 18 21 25 27 34 35 36 41 43 46 51 53 63 64 72 78 81 87"
# graph = "ab ba ae ea eb be bh hb hd dh dg gd cg gc ch hc cf fc fa af"
#
# for per in permutations("abcdefgh"):
#     new_graph = table
#
#     for i in range(1, 9):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(graph.split()):
#         print(*per)


# t = "12 15 16 21 23 24 32 36 37 42 47 51 56 61 63 65 73 74"
# g = "af fa ab ba fb bf fe ef ec ce cg gc gd dg db bd ed de"
#
# for per in permutations("abcdefg"):
#     new_graph = t
#     for i in range(1, 8):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#     if set(new_graph.split()) == set(g.split()):
#         print(*per)


# t = "13 16 17 25 26 28 31 38 45 48 52 54 57 61 62 67 71 75 76 82 83 84"
# g = "ae ea eh he hg gh gc cg cf fc fa af ed de df fd db bd bh hb bg gb"
#
# for per in permutations("abcdefgh"):
#     new_graph = t
#
#     for i in range(1, 9):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(g.split()):
#         print(*per)


# table = "12 14 18 21 25 27 34 35 36 41 43 46 52 53 63 64 72 78 81 87"
# group = "ae ea ab ba eb be bh hb hd dh dg gd gc cg hc ch cf fc fa af"
#
#
# for per in permutations("abcdefgh"):
#     new_graph = table
#
#     for i in range(1, 9):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(group.split()):
#         print(*per)


# table = "13 18 25 28 31 34 36 43 46 52 57 63 64 67 75 76 78 81 82 87"
# group = "de ed db bd eb be ea ae ah ha hc ch cf fc fg gf hg gh gb bg"
#
#
# for per in permutations("abcdefgh"):
#     new_graph = table
#
#     for i in range(1, 9):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(group.split()):
#         print(*per)


# table = "12 13 14 21 25 26 31 37 41 46 52 54 56 62 65 67 73 76"
# group = "fe ef ed de dc cd cb bc gb bg gf fg da ad ag ga ab ba"
#
#
# for per in permutations("abcdefg"):
#     new_graph = table
#
#     for i in range(1, 8):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(group.split()):
#         print(*per)


# table = "14 16 23 24 27 32 37 38 41 42 45 54 56 58 61 65 72 73 83 85"
# group = "ae ea eb be bf fb fa af bc cb ch hc hd dh dg gd gf fg dc cd"
#
#
# for per in permutations("abcdefgh"):
#     new_graph = table
#
#     for i in range(1, 9):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#     if set(new_graph.split()) == set(group.split()):
#         print(*per)


# table = "13 14 16 24 25 31 36 41 42 45 46 47 52 54 61 63 64 67 74 76"
# group = "аб ба бв вб ва ав вг гв гк кг ге ег ке ек ев ве вд дв де ед"
#
#
# for per in permutations("абвгдек"):
#     new_graph = table
#
#     for i in range(1, 8):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#     if set(new_graph.split()) == set(group.split()):
#         print(*per)


# table = "15 16 18 23 26 32 34 37 43 46 48 51 57 58 61 62 64 73 75 81 84 85"
# group = "cd dc de ed eh he ha ah ab ba bc cb cf fc fg gf fe ef gh hg ga ag"
#
#
# for per in permutations("abcdefgh"):
#     new_graph = table
#
#     for i in range(1, 9):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(group.split()):
#         print(*per)


# table = "12 15 16 21 23 25 32 34 35 37 43 47 51 52 53 56 61 65 67 73 74 76"
# group = "ав ва вг гв гд дг дб бд жб бж жа аж аз за зв вз зг гз зд дз жд дж"
#
# for per in permutations("абвгджз"):
#     new_graph = table
#
#     for i in range(1, 8):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(group.split()):
#         print(*per)


# table = "12 16 17 21 24 25 27 35 38 42 45 52 53 54 56 61 65 71 72 78 83 87"
# group = "вг гв гд дг дж жд же еж ев ве да ад аж жа жз зж зе ез бе еб аб ба"
#
#
# for per in permutations("абвгдезж"):
#     new_graph = table
#
#     for i in range(1, 9):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(group.split()):
#         print(*per)


# table = "15 16 24 25 26 28 37 38 42 45 47 48 51 52 54 56 61 62 65 73 74 78 82 83 84 87"
# group = "ае еа аг га ег ге аб ба бг гб гж жг бж жб бд дб дж жд жи иж ид ди дв вд ви ив"
#
#
# for per in permutations("абвгдежи"):
#     new_graph = table
#     for i in range(1, 9):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(group.split()):
#         print(*per)


# table = "14 15 18 23 27 32 36 41 47 48 51 56 58 63 65 67 72 74 76 81 84 85"
# group = "ab ba bf fb fg gf gh hg hc ch ce ec ae ea fe ef gd dg dh hd cd dc"
#
#
# for per in permutations("abcdefgh"):
#     new_graph = table
#
#     for i in range(1, 9):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(group.split()):
#         print(*per)


# table = "14 15 17 24 26 35 36 37 41 42 51 53 56 62 63 65 71 73"
# group = "ec ce ca ac ab ba db bd df fd fe ef cg gc fg gf gd dg"
#
#
# for per in permutations("abcdefg"):
#     new_graph = table
#
#     for i in range(1, 8):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(group.split()):
#         print(*per)


# table = "12 14 15 21 23 25 26 32 34 41 43 45 46 51 52 54 62 64"
# group = "ae ea ef fe fb bf ba ab ad da ac ca cd dc cf fc fd df"
#
#
# for per in permutations("abcdef"):
#     new_graph = table
#
#     for i in range(1, 7):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(group.split()):
#         print(*per)


# table = "13 18 23 24 26 31 32 38 42 47 57 62 74 75 78 81 83 87"
# group = "ae ea ed de df fd dc cd cf fc cg gc gb bg eb be gh hg"
#
#
# for per in permutations("abcdefgh"):
#     new_graph = table
#
#     for i in range(1, 9):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(group.split()):
#         print(*per)


# table = "15 16 17 23 24 25 27 32 34 36 37 42 43 47 51 52 57 61 63 67 71 72 73 74 75 76"
# group = "сл лс лк кл кр рк рм мр мс см ст тс тм мт тп пт сп пс мп пм пл лп пк кп рп пр"
#
#
# for per in permutations("слкрмтп"):
#     new_graph = table
#
#     for i in range(1, 8):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(group.split()):
#         print(*per)


# t = "12 14 21 24 26 35 36 41 42 46 47 53 56 62 63 64 65 67 74 76"
# g = "аб ба бв вб ва ав вд дв де ед ве ев вг гв ге ег ек ке гк кг"
#
#
# for per in permutations("абвгдек"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "13 14 15 16 18 19 24 29 31 34 35 41 42 43 51 53 58 61 67 68 76 79 81 85 86 91 92 97"
# g = "аб ба бв вб ве ев еи ие из зи зж жз жг гж га аг гд дг дб бд де ед дж жд дз зд ид ди"
#
#
# for per in permutations("абвгдежзи"):
#     ng = t
#
#     for i in range(1, 10):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "15 16 24 26 27 28 34 36 37 38 42 43 45 47 51 54 61 62 63 68 72 73 74 78 82 83 86 87"
# g = "df fd fc cf cb bc ba ab ad da de ed dg gd ef fe eh he ge eg ga ag gh hg hf fh ah ha"
#
#
# for per in permutations("dfcbaghe"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "14 16 17 18 23 24 27 28 32 37 41 42 45 48 54 56 58 61 65 68 71 72 73 78 81 82 84 85 86 87"
# g = "ве ев ез зе зг гз гж жг жв вж ва ав вд дв ад да аб ба бе еб бд дб де ед дз зд дж жд зж жз"
#
# for per in permutations("ебавдзгж"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "14 17 18 23 28 32 35 36 41 45 53 54 63 67 71 76 78 81 82 87"
# g = "fe ef ed de dg gd ga ag ah ha fh hf fb bf bc cb cg gc bh hb"
#
#
# for per in permutations("abcdefgh"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 16 17 21 26 36 47 57 61 62 63 67 71 74 75 76"
# g = "бв вб ве ев ва ав вг гв аг га ад да дг гд гк кг"
#
#
# for per in permutations("абвгдек"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 14 18 21 24 27 34 35 36 41 42 43 45 46 53 54 57 58 63 64 72 75 81 85"
# g = "аб ба бв вб ве ев ед де дг гд аг га аж жа жб бж жз зж зд дз бе еб дб бд"
#
#
# for per in permutations("абведгжз"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 13 21 23 24 25 26 27 31 32 35 42 46 52 53 57 62 64 67 72 75 76"
# g = "ак ка ае еа ад да аг га ав ва аб ба бв вб вг гв гд дг де ед ке ек"
#
#
# for per in permutations("акедгвб"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "13 17 25 27 31 34 37 43 47 52 56 65 67 71 72 73 74 76"
# g = "ac ca cd dc ad da ag ga dg gd db bd bf fb fe ef de ed"
#
#
# for per in permutations("acdgbfe"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "14 15 17 24 26 35 36 37 41 42 51 53 56 62 63 65 71 73"
# g = "ec ce ca ac ab ba db bd df fd fe ef fg gf gc cg gd dg"
#
#
# for p in permutations("ecabdfg"):
#     ng = t
#
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), p[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*p)


# t = "12 14 18 21 25 27 34 35 36 41 43 46 52 53 63 64 72 78 81 87"
# g = "fc cf ch hc hb bh be eb ae ea af fa cg gc gd dg dh hd ab ba"
#
#
# for per in permutations("abcdefgh"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "14 17 25 27 34 35 41 43 46 52 53 56 64 65 67 71 72 76"
# g = "bd db de ed ea ae ag ga gf fg fb bf bc cb ce ec cg gc"
#
#
# for per in permutations("abcdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 14 15 16 21 23 24 26 32 34 35 36 41 42 43 45 51 53 54 56 61 62 63 65"
# g = "ад да де ед еа ае ав ва аг га вг гв вб бв гб бг ве ев еб бе бд дб гд дг"
#
#
# for per in permutations("адевгб"):
#     ng = t
#
#     for i in range(1, 7):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "14 16 23 24 27 32 37 38 41 42 45 54 56 58 61 65 72 73 83 85"
# g = "eb be bc cb ch hc hd dh dg gd gf fg fa af ae ea bf fb cd dc"
#
#
# for per in permutations("abcdefgh"):
#     ng = t
#
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "14 15 16 23 27 32 35 41 46 51 53 57 61 64 67 72 75 76"
# g = "gb bg bf fb fd df dc cd ce ec ae ea ag ga be eb fc cf"
#
#
# for per in permutations("abcdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "13 14 16 24 25 31 36 41 42 45 46 47 52 54 61 63 64 67 74 76"
# g = "гв вг ав ва аб ба бв вб вд дв де ед ке ек кг гк ге ег ве ев"
#
#
# for per in permutations("абвгдек"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "13 17 18 28 31 34 37 43 56 57 65 71 73 75 78 81 82 87"
# g = "ac ca cf fc fg gf gh hg cd dc df fd fe ef de ed be eb"
#
#
# for per in permutations("abcdefgh"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 13 16 21 24 26 31 37 42 45 46 54 57 61 62 64 67 73 75 76"
# g = "аб ба вб бв вг гв гд дг де ед еа ае аж жа еж же жб бж жг гж"
#
#
# for per in permutations("абвгдеж"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 14 21 24 26 35 36 41 42 46 47 53 56 62 63 64 65 67 74 76"
# g = "аб ба ав ва бв вб вд дв ве ев ед де вг гв ге ег гк кг ек ке"
#
#
# for per in permutations("абвгдек"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 14 15 21 23 25 32 36 41 45 46 51 52 54 63 64"
# g = "ab ba bc cb cd dc de ed ea ae af fa fe ef fd df"
#
#
# for per in permutations("abcdef"):
#     ng = t
#
#     for i in range(1, 7):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 14 21 24 26 35 36 41 42 46 47 53 56 62 63 64 65 67 74 76"
# g = "аб ба ав ва вб бв вг гв вд дв ве ев ге ег де ед гк кг ек ке"
#
#
# for per in permutations("абвгдек"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "16 17 23 24 26 32 34 42 43 45 54 57 61 62 67 71 75 76"
# g = "ба аб аг га гд дг дж жд же еж ев ве вб бв ав ва де ед"
#
#
# for per in permutations("абвгдеж"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "13 14 17 23 25 26 31 32 34 35 36 37 41 43 52 53 62 63 67 71 73 76"
# g = "ав ва вг гв гж жг жд дж де ед еб бе ба аб аг га бг гб ег ге гд дг"
#
#
# for per in permutations("абвгдеж"):
#     ng = t
#
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "15 16 17 23 25 27 32 34 36 43 46 51 52 57 61 63 64 71 72 75"
# g = "ба аб ав ва вб бв бд дб дк кд ке ек ев ве гд дг кг гк ге ег"
#
#
# for per in permutations("абвгдек"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "16 18 24 27 34 35 42 43 47 53 56 58 61 65 72 74 78 81 85 87"
# g = "gf fg fe ef ed de db bd ab ba ac ca ch hc hg gh he eh cb bc"
#
#
# for per in permutations("abcdefgh"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "13 18 25 28 31 34 36 43 46 52 57 63 64 67 75 76 78 81 82 87"
# g = "de ed ea ae ah ha hc ch cf fc fg gf gb bg db bd eb be hg gh"
#
#
# for per in permutations("abcdefgh"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "13 16 25 26 27 31 34 43 46 47 52 57 61 62 64 72 74 75"
# g = "ae ea ef fe fb bf db bd dc cd ca ac ab ba cg gc gd dg"
#
#
# for per in permutations("abcdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 15 16 21 23 24 32 36 37 42 47 51 56 61 63 65 73 74"
# g = "af fa fe ef ec ce cg gc gd dg db bd ab ba fb bf ed de"
#
#
# for per in permutations("abcdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 14 18 21 25 27 34 35 36 41 43 46 52 53 63 64 72 78 81 87"
# g = "ch hc bh hb be eb ae ea af fa fc cf cg gc gd dg dh hd ab ba"
#
#
# for per in permutations("abcdefgh"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 13 14 21 24 28 31 34 35 38 41 42 43 45 46 47 49 53 54 64 67 68 74 76 78 82 83 84 86 87"
# g = "qr rq rc cr cp pc pa ap ak ka kb bk bq qb ra ar ca ac qa aq ab ba al la bc cb bl lb lk kl"
#
#
# for per in permutations("qrcpalkb"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "14 15 18 25 26 28 35 36 37 41 47 51 52 53 58 62 63 67 68 73 74 76 81 82 85 86"
# g = "fg gf ge eg eh he hc ch fc cf fa af ac ca ad da de ed db bd dh hd bc cb bh hb"
#
#
# for per in permutations("fgedabhc"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "15 17 25 26 28 34 38 43 46 47 51 52 62 64 67 68 71 74 76 82 83 86"
# g = "ба аб ав ва ве ев зе ез зж жз дж жд дб бд аг га гж жг гз зг гв вг"
#
# for per in permutations("абвгдежз"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "15 17 26 27 35 47 51 53 56 62 65 67 71 72 74 76"
# g = "за аз аб ба бв вб вд дв дг гд га аг гв вг вж жв"
#
#
# for per in permutations("абвгджз"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 14 15 16 17 21 24 26 35 41 42 51 53 56 57 61 62 65 71 75"
# g = "ав ва вб бв бг гб гд дг дж жд же еж ве ев вг гв ге ег гж жг"
#
#
# for per in permutations("абвгдеж"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "13 15 16 24 27 28 31 36 37 38 42 45 47 51 54 57 61 63 68 72 73 74 75 82 83 86"
# g = "ad da de ed eg ge gh hg bh hb ab ba ac ca dc cd bc cb cf fc fe ef fg gf fh hf"
#
#
# for per in permutations("abcdefgh"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):ouuuuuu
#         print(*per)


# t = "14 16 23 24 27 32 37 38 41 42 45 54 56 58 61 65 72 73 83 85"
# g = "ae ea eb be bc cb ch hc hd dh dg gd gf fg fa af fb bf cd dc"
#
#
# for per in permutations("abcdefgh"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "14 15 16 23 27 32 35 41 46 51 53 57 61 64 67 72 75 76"
# g = "gb bg bf fb fd df dc cd ce ec ae ea ag ga be eb cf fc"
#
#
# for per in permutations("abcdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "13 14 16 24 25 31 36 41 42 45 46 47 52 54 61 63 64 67 74 76"
# g = "гв вг ва ав аб ба бв вб вд дв де ед ке ек кг гк ге ег ве ев"
#
#
# for per in permutations("абвгдек"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "13 17 25 27 31 34 37 43 47 52 56 65 67 71 72 73 74 76"
# g = "ac ca cd dc ad da ag ga gd dg db bd bf fb fe ef de ed"
#
#
# for per in permutations("acbdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "13 17 23 26 27 31 32 35 45 46 53 54 62 64 67 71 72 76"
# g = "ad da de ed eg ge gc cg cf fc af fa ab ba bf fb be eb"
#
# for per in permutations("abcdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 21 23 25 26 32 34 35 43 45 52 53 54 57 62 75"
# g = "бв вб ве ев ва ав ад да аг га вг гв гд дг гк кг"
#
#
# for per in permutations("абвгдек"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 13 15 21 24 31 37 42 45 46 51 54 57 64 67 73 75 76"
# g = "bd db de ed ea ae ga ag gf fg fb bf bc cb ce ec cg gc"
#
#
# for per in permutations("abcdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# g = "bd de ea ag fg bf bc ce gc "
# g += g[-2::-1]
# t = "12 13 15 21 24 31 37 42 45 46 51 54 57 64 67 73 75 76"
#
# for per in permutations("abcdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "14 15 17 24 26 35 36 37 41 42 51 53 56 62 63 65 71 73"
# g = "ec ca ab db fd fe fg gc gd "
# g += g[-2::-1]
#
# for per in permutations("abcdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 14 16 18 21 23 25 27 32 35 37 41 48 52 53 56 57 61 65 68 72 73 75 81 84 86"
# g = "аб бв вг ги жи еж де ад дб бе ев вж ви"
# g += g[-2::-1]
#
# for per in permutations("абвгдеиж"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "16 17 23 24 26 32 34 42 43 45 54 57 61 62 67 71 75 76"
# g = "аб ба бв вб ав ва аг га ве ев гд дг де ед дж жд еж же"
#
#
# for per in permutations("абвгдеж"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "13 17 25 27 31 34 37 43 47 52 56 65 67 71 72 73 74 76"
# g = "ac ca cd dc ad da ag ga gd dg db bd bf fb de ed ef fe"
#
#
# for per in permutations("abcdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 21 23 26 27 32 35 45 47 53 54 57 62 72 74 75"
# g = "бв вб ве ев ва ав аг га гд дг дк кд кв вк гк кг"
#
#
# for per in permutations("абвгдек"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 21 23 25 26 32 34 35 43 45 52 53 54 57 62 75"
# g = "бв вб ве ев ва ав вг гв аг га гк кг ад да гд дг"
#
#
# for per in permutations("абвгдек"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 14 21 24 26 35 36 41 42 46 47 53 56 62 63 64 65 67 74 76"
# g = "аб ба ав ва бв вб вд дв ве ев де ед вг гв ге ег гк кг ек ке"
#
#
# for p in permutations("абвгдек"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), p[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*p)


# t = "15 16 23 27 28 32 36 46 48 51 57 61 63 64 72 75 78 82 84 87"
# g = "ac ca cf fc fd df dh hd hg gh ag ga ab ba cb bc be eb ed de"
#
#
# for per in permutations("abcdefgh"):
#     ng = t
#
#     for i in range(1, 9):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "12 14 16 21 26 35 37 41 45 53 54 57 61 62 67 73 75 76"
# g = "be eb ef fe fd df dc cd fc cf ac ca ag ga ab ba gb bg"
#
#
# for per in permutations("abcdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "13 14 24 25 26 27 31 34 41 42 43 46 52 62 64 72"
# g = "ab ac bc ce ef cd ed eg"
# g += g[-2::-1]
#
#
# for per in permutations("abcdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "13 17 25 27 31 34 37 43 47 52 56 65 67 71 72 73 74 76"
# g = "ac ca cd dc ad da ag ga gd dg db bd bf fb fe ef de ed"
#
#
# for per in permutations("abcdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "13 15 16 17 23 27 31 32 36 45 47 51 54 56 61 63 65 71 72 74"
# g = "ab ba bc cb cd dc de ed fe ef fa af gf fg gb bg gd dg ge eg"
#
#
# for per in permutations("abcdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)


# t = "14 15 17 24 26 35 36 37 41 42 51 53 56 62 63 65 71 73"
# g = "ec ce ca ac ab ba bd db df fd fe ef fg gf dg gd gc cg"
#
#
# for per in permutations("abcdefg"):
#     ng = t
#
#     for i in range(1, 8):
#         ng = ng.replace(str(i), per[i - 1])
#
#     if set(ng.split()) == set(g.split()):
#         print(*per)
