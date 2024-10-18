import math
from itertools import permutations, product

# for n in range(65, 1000):
#     s = f"{n:b}"
#
#     for i in range(2):
#         if s.count('1') == s.count('0'):
#             s += s[-1]
#         else:
#             s += '0' if s.count('0') < s.count('1') else '1'
#
#     k = int(s, 2)
#     if k % 4 == 0:
#         print(k)
#         break
#

# a = '4' * 31
#
# while '444' in a or '222' in a:
#     a = a.replace('444', '2', 1)
#     a = a.replace('222', '4', 1)
#
# print(a)

# a = 8 ** 1014 - 2 ** 530 - 12
# a = str(a)
# print(a.count('1'))


# import sys
# sys.setrecursionlimit(10 ** 6)


# def F(n):
#     if n <= 3:
#         return 1
#     if n > 3:
#         return (n + 3) * F(n - 2)

# print(F(2028) / F(2024))


# from sys import setrecursionlimit


# setrecursionlimit(10 ** 6)

# def f(n):
#     if n <= 7:
#         return 1
#     if n > 7:
#         return n + 2 + f(n - 1)


# print(f(2024) - f(2020))

# for n in range(1, 1000):
#     s = f"{n:b}"
#     if len(s) % 2 == 0:
#         s += "1"
#     else:
#         s += "0"
#     if s.count("1") % 2 == 0:
#         s += "1"
#     else:
#         s += "0"
#
#     k = int(s, 2)
#
#     if k > 228:
#         print(n)
#         break
#


# for k1 in range(50):
#     for k2 in range(50):
#         for k3 in range(50):
#             a = '0' + k1 * '1' + k2 * '2' + k3 * '3'
#
#             while '01' in a or '02' in a or '03' in a:
#                 a = a.replace('01', '2302', 1)
#                 a = a.replace('02', '10', 1)
#                 a = a.replace('03', '201', 1)
#             if a.count('1') == 40 and a.count('2') == 10 and a.count('3') == 8:
#                 print(k1)


# a = 49 ** 6 + 7 ** 18 - 21
# s = ''
#
# while a != 0:
#     s += str(a % 7)
#     a //= 7
#
# print(s.count('6'))


# def F(n):
#     if n == 1:
#         return 3
#     if n > 1:
#         return F(n - 1) * (n - 1)
#
#
# print(F(6))


# for i in range(1000, 10000):
#     s = str(i)
#     k1 = int(s[0]) + int(s[1])
#     k2 = int(s[1]) + int(s[2])
#     k3 = int(s[2]) + int(s[3])
#
#     first = str(k1 + k2 + k3 - max(k1, k2, k3) - min(k1, k2, k3))
#     second = str(max(k1, k2, k3))
#
#     s1 = first + second
#     if s1 == '1418':
#         print(i)
#         break


# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if s.count('1') % 2 == 0:
#         s += '00'
#     else:
#         s += '10'
#
#     r = int(s, 2)
#     if r > 43:
#         print(r)
#         break


# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if s.count('1') % 2 == 0:
#         s += '00'
#     else:
#         s += '11'
#
#     r = int(s, 2)
#
#     if r > 114:
#         print(r)
#         break


# print("x y z w")
#
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 if ((not(not(x) or z) or (y == w) or y)) == 0:
#                     print(x, y, z, w)


# table = "12 15 16 21 23 24 32 36 37 42 47 51 56 61 63 65 73 74"
# graph = "ab ba af fa fe ef bf fb bd db ed de ec ce gd dg cg gc"
#
# for per in permutations("abcdefg"):
#     new_graph = table
#     for i in range(1, 8):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#     if set(graph.split()) == set(new_graph.split()):
#         print(*per)


# table = "12 14 21 24 26 35 36 37 41 42 46 47 53 56 62 63 64 65 67 73 74 76"
# graph = "аб ба ав ва бв вб бд дб вд дв ве ев вг гв де ед ге ег ек ке кг гк"
#
# for per in permutations("абвгдек"):
#     new_graph = table
#     for i in range(1, 8):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#     if set(graph.split()) == set(new_graph.split()):
#         print(*per)


# table = "12 14 21 24 26 35 36 41 42 46 47 53 56 62 63 64 65 67 74 76"
# graph = "аб ба ва ав бв вб дв вд де ед вг гв ве ев ег ге ек ке кг гк"
#
# for per in permutations("абвгдек"):
#     new_graph = table
#     for i in range(1, 8):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#     if set(graph.split()) == set(new_graph.split()):
#         print(*per)


# table = "16 17 23 24 26 32 34 42 43 45 54 57 61 62 67 71 75 76"
# graph = "аб ба ак ка кб бк ке ек ед де дв вд гд дг гв вг вб бв"
#
# for per in permutations("абвгдек"):
#     new_graph = table
#
#     for i in range(1, 8):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#     if set(new_graph.split()) == set(graph.split()):
#         print(*per)


# table = "15 16 23 24 27 32 35 37 42 46 51 53 56 61 64 65 72 73"
# graph = "ab ba af fa bf fb bd db dc cd ce ec cg gc ge eg gf fg"
#
# for per in permutations("abcdefg"):
#     new_graph = table
#     for i in range(1, 8):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#     if set(graph.split()) == set(new_graph.split()):
#         print(*per)


# table = "13 14 15 23 26 27 31 32 36 37 41 45 46 51 54 57 62 63 64 72 73 75"
# graph = "аб ба бд дб дг гд га аг ав ва вг гв ве ев ед де еж же дж жд бж жб"
#
# for per in permutations("абвгдеж"):
#     new_graph = table
#
#     for i in range(1, 8):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(graph.split()):
#         print(*per)


# table = "13 14 15 24 25 27 31 36 37 41 42 45 46 51 52 54 63 64 67 72 73 76"
# graph = "аб ба бж жб же еж ев ве ва ав вг гв аг га гд дг де ед дб бд дж жд"
#
# for per in permutations("абвгдеж"):
#     new_graph = table
#
#     for i in range(1, 8):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(graph.split()):
#         print(*per)


# table = "15 16 17 23 25 27 32 34 36 43 46 51 52 57 61 63 64 71 72 75"
# graph = "аб ба ав ва бд дб дк кд дг гд кг гк ге ег ке ек ев ве вб бв"
#
# for per in permutations("абвгдек"):
#     new_graph = table
#
#     for i in range(1, 8):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#     if set(new_graph.split()) == set(graph.split()):
#         print(*per)


# table = "12 15 16 21 24 25 35 38 42 45 51 52 53 54 56 57 58 61 65 75 78 83 85 87"
# graph = "аб ба бв вб ад да дб бд дв вд дг гд дж жд гж жг жи иж ди ид ие еи де ед"
#
# for per in permutations("абвгдежи"):
#     new_graph = table
#
#     for i in range(1, 9):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#     if set(new_graph.split()) == set(graph.split()):
#         print(*per)


# t = "12 15 16 21 23 24 32 36 37 42 47 51 56 61 63 65 73 74"
# g = "af fa ab ba bf fb fe ef bd db ed de ec ce cg gc dg gd"
#
# for per in permutations("abcdefg"):
#     new_graph = t
#     for i in range(1, 8):
#         new_graph = new_graph.replace(str(i), per[i - 1])
#
#     if set(new_graph.split()) == set(g.split()):
#         print(*per)


# t = "15 16 23 27 28 32 36 46 48 51 57 61 63 64 72 75 78 82 84 87"
# g = "ac ca cf fc fd df dh hd gh hg ga ag ab ba cb bc be eb ed de"
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


# def f(w, x, y, z):
#     return (x or not y) and z and not w
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (1, 1, i[0], i[1]),
#         (i[2], 1, 0, 0),
#         (1, i[3], 1, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(a, b, c, t):
#     return (not a or not b) and (c <= (not a)) and (t and not a or c or not b)
#
#
# for i in product([1, 0]):
#     t = (
#         (1, 0, 0, 1),
#         (1, 1, 0, 1),
#         (0, 0, 0, 1),
#         (1, 0, 0, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("abct"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 1, 0, 1]:
#                 print(*p)
