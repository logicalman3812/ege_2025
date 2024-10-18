from itertools import permutations, product

# print("x y z w")
#
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 if (not(w) or z) and ((not(y) or x) == (not(z) or y)):
#                     print(x, y, z, w)


# def f(w, x, y, z):
#     return (z <= (not y <= x)) or w
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (i[0], 1, i[1], i[2]),
#         (i[3], i[4], 0, 0),
#         (i[5], 0, 1, i[6])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return not(x <= z) or (y == w) or y
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (1, 0, i[0], i[1]),
#         (i[2], 1, 0, i[3]),
#         (0, i[4], i[5], i[6])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r)) for r in t] == [0, 0, 0]:
#                 print(*p)


# print("x y z w")
#
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((z <= x) == (w <= y) or (x and w)) == 0:
#                     print(x, y, z, w)


# def f(x, y, z, w):
#     return ((z <= x) == (w <= y) or (x and w))
#
#
# for i in product([1, 0], repeat=6):
#     t = (
#         (i[0], i[1], i[2], 1),
#         (i[3], i[4], 1, 1),
#         (i[5], 1, 1, 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x or (not(z) and w) or w) == (y and not(x) and w)
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (1, i[0], i[1], 0),
#         (1, i[2], 0, 0),
#         (0, 1, i[3], 1)
#     )
#
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(u, w, x, y, z):
#     return ((z <= w) and (y == (not x))) <= (u == (y or z))
#
#
# for i in product([1, 0], repeat=8):
#     t = (
#         (0, i[0], 0, 0, 0),
#         (0, i[1], i[2], 0, 0),
#         (i[3], 0, 0, 0, i[4]),
#         (0, 0, i[5], i[6], i[7])
#     )
#
#     if len(set(t)) == len(t):
#         for p in permutations("uwxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0, 0]:
#                 print(*p)


# def f1(w, x, y, z):
#     return (w == x) and (y <= z)
#
#
# def f2(w, x, y, z):
#     return (w <= x) <= (y == z)
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (1, i[0], 1, 1),
#         (i[1], 1, 0, 0),
#         (i[2], 0, 0, i[3])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f1(**dict(zip(p, r))) for r in t] == [1, 1, 0] and \
#                 [f2(**dict(zip(p, r))) for r in t] == [0, i[4], 0]:
#                 print(*p)


# def f(u, w, x, y, z):
#     return (((z <= w ) and (y == (not x))) <= (u == (y or z)))
#
#
# for i in product([1, 0], repeat=8):
#     t = (
#         (0, i[0], 0, 0, 0),
#         (0, i[1], i[2], 0, 0),
#         (i[3], 0, 0, 0, i[4]),
#         (0, 0, i[5], i[6], i[7])
#     )
#
#     if len(set(t)) == len(t):
#         for p in permutations("uwxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0, 0]:
#                 print(*p)

#
# def f1(w, x, y, z):
#     return (w == x) and (y <= z)
#
#
# def f2(w, x, y, z):
#     return (w <= x) <= (y == z)
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (1, i[0], 1, 1),
#         (i[1], 1, 0, 0),
#         (i[2], 0, 0, i[3])
#     )
#
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f1(**dict(zip(p, r))) for r in t] == [1, 1, 0] and \
#                 [f2(**dict(zip(p, r))) for r in t] == [0, i[4], 0]:
#                 print(*p)
#

# def f(k, l, m, n):
#     return (not(k <= m)) and (k or n) or (l <= n)
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (1, i[0], i[1], 0),
#         (i[2], i[3], i[4], 1),
#         (0, 1, i[5], i[6])
#     )
#
#     if len(set(t)) == len(t):
#         for p in permutations("klmn"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     left = ((x and not y) <= (z and w))
#     right = ((y <= z) or (w <= x))
#     return left and right
#
#
# for i in product([1, 0], repeat=6):
#     t = (
#         (i[0], i[1], 1, 1),
#         (1, i[2], 1, i[3]),
#         (i[4], 0, i[5], 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     left = not(y <= (x == w))
#     right = (z <= x)
#     return left and right
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (i[0], 1, 1, i[1]),
#         (0, i[2], i[3], 0),
#         (i[4], 0, 1, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     left = y and (x or z)
#     right = (not(y or z) or w)
#     return left or right
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (1, i[0], 0, 1),
#         (i[1], 1, 0, i[2]),
#         (0, 0, i[3], 1)
#     )
#
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     left = ((y and not(x == z)) <= w)
#     right = (z <= y)
#     return left and right
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (0, 0, i[0], i[1]),
#         (0, i[2], 0, 0),
#         (1, i[3], i[4], 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (not x or y) and (y or z) and w
#
#
# for i in product([1, 0], repeat=6):
#     t = (
#         (i[0], i[1], 0, 0),
#         (0, 1, 0, i[2]),
#         (0, i[3], i[4], i[5])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return (not x or y) and z and not w
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (0, 1, i[0], 1),
#         (i[1], 1, i[2], i[3]),
#         (0, 1, 1, 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x or not y) and not(x == z) and w
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (i[0], 0, 0, 1),
#         (0, 0, 1, 1),
#         (0, i[1], i[2], i[3])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**(dict(zip(p, r)))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     left = (x <= (z == w))
#     right = not(y <= w)
#     return left or right
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (i[0], 1, i[1], i[2]),
#         (0, i[3], 0, i[4]),
#         (i[5], 0, 0, i[6])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                print(*p)


# def f(w, x, y, z):
#     return ((x or y) == (not y or z)) or w
#
#
# for i in product([1, 0], repeat=8):
#     t = (
#         (i[0], 1, i[1], i[2]),
#         (i[3], i[4], i[5], 1),
#         (1, i[6], i[7], 1)
#     )
#
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(x, y, z, w):
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
#         for p in permutations("xyzw"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(x, y, z, w):
#     return (not x or y or not z or w) and not (not x or w)
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (i[0], 0, i[1], 1),
#         (0, i[2], 0, i[3]),
#         (1, 0, 0, i[4])
#     )
#
#     if len(set(t)) == len(t):
#         for p in permutations("xyzw"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(x, y, z, w):
#     return ((x == z) or not(x == w)) and ((not y or x) or not z)
#
#
# for i in product([1, 0], repeat=9):
#     t = (
#         (1, i[0], 1, 1),
#         (i[1], 1, i[2], 1),
#         (i[3], 1, 1, 1),
#         (1, i[4], 1, i[5]),
#         (i[6], 1, i[7], i[8])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("xyzw"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0, 0, 0]:
#                 print(*p)


# def f(x, y, z, w):
#     return (not z == (not y)) or (not x and y) or w
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (i[0], 1, i[1], 1),
#         (1, 1, i[2], i[3]),
#         (1, i[4], i[5], i[6])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("xyzw"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(y, x, z, w):
#     return not y and (x <= (not z == w)) or z
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (0, i[0], 0, 0),
#         (i[1], 0, 1, 0),
#         (i[2], 0, 0, i[3])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("yxzw"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return ((w <= y) <= x) or not z
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (i[0], i[1], 1, i[2]),
#         (i[3], 0, i[4], i[5]),
#         (i[6], 1, 0, 0)
#     )
#
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(a, b, c, d):
#     return (a <= b) and (b <= (not c)) and (c == (not d))
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (1, 1, 0, i[0]),
#         (i[1], 0, 1, 0),
#         (1, 0, i[2], 1),
#         (0, i[3], 0, 1)
#     )
#
#     if len(set(t)) == len(t):
#         for p in permutations("abcd"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return ((1 == w) == (not((w and x) or y))) <= z
#
# for i in product([1, 0], repeat=10):
#     t = (
#         (i[0], i[1], 1, i[2]),
#         (1, i[3], 1, i[4]),
#         (0, 1, 0, 0),
#         (1, i[5], 1, i[6]),
#         (i[7], i[8], 1, i[9])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return not x or y or (not z and w)
#
#
# for i in product([1, 0], repeat=0):
#     t = (
#         (0, 1, 0, 0),
#         (0, 1, 1, 0),
#         (1, 1, 1, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x or y) and (not x or not z) and not w
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (i[0], 1, i[1], 0),
#         (1, i[2], 1, i[3]),
#         (1, 1, 0, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(u, w, x, y):
#     return (not((y <= w) == x)) and u
#
#
# for i in product([1, 0], repeat=3):
#     t = (
#         (0, 1, 0, i[0]),
#         (0, 1, 1, 1),
#         (1, 0, 1, i[1]),
#         (1, i[2], 1, 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("uwxy"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 1, 1]:
#                 print(*p)


# def f(a, b, c, d):
#     return (a <= b) and (b <= c) and (c <= d)
#
#
# for i in product([1, 0], repeat=2):
#     t = (
#         (0, i[0], 1, 0),
#         (0, i[1], 1, 0),
#         (0, 1, 1, 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("abcd"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return not(w <= x) or (y <= z) or not y
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (i[0], 0, i[1], i[2]),
#         (i[3], 1, 0, i[4]),
#         (i[5], i[6], 1, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return ((y and not(x == z)) <= w) and (z <= y)
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (0, 0, i[0], i[1]),
#         (0, i[2], 0, 0),
#         (1, i[3], i[4], 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x <= y) and ((not y) <= z) and w
#
#
# for i in product([1, 0], repeat=6):
#     t = (
#         (i[0], i[1], 0, 0),
#         (0, 1, 0, i[2]),
#         (0, i[3], i[4], i[5])
#     )
#
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x <= y) and z and not w
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (0, 1, i[0], 1),
#         (i[1], 1, i[2], i[3]),
#         (0, 1, 1, 1)
#     )
#
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return (not x and not y) or (x == z) or w
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (i[0], 0, 1, 1),
#         (1, 0, 0, i[1]),
#         (1, i[2], i[3], 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(a, b, c, d):
#     return ((a <= b) == c) or not d and (d <= (not a))
#
#
# for i in product([1, 0], repeat=9):
#     t = (
#         (0, i[0], i[1], i[2]),
#         (i[3], i[4], 0, i[5]),
#         (0, i[6], i[7], 0),
#         (0, i[8], 0, 0)
#     )
#
#     if len(set(t)) == len(t):
#         for p in permutations("abcd"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0, 0]:
#                 print(*p)


# def f(a, b, c, d):
#     return (a and b == (not c)) and (b <= d)
#
# for i in product([1, 0], repeat=0):
#     t = (
#         (1, 0, 0, 0),
#         (1, 0, 1, 0),
#         (1, 0, 1, 1),
#         (1, 1, 0, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("abcd"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return ((x or y) == (y <= z)) or w
#
#
# for i in product([1, 0], repeat=8):
#     t = (
#         (i[0], 1, i[1], i[2]),
#         (i[3], i[4], i[5], 1),
#         (1, i[6], i[7], 1)
#     )
#
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(x, y, z, w):
#     return (x or (not y)) and z and not w
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (1, 1, i[0], i[1]),
#         (i[2], 1, 0, 0),
#         (1, i[3], 1, 0,)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("xyzw"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(x, y, z, w):
#     return (not x or y or not z or w) and not(not x or w)
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (i[0], 0, i[1], 1),
#         (0, i[2], 0, i[3]),
#         (1, 0, 0, i[4])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("xyzw"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(x, y, z, w):
#     return ((x and y) <= (not z)) and (x <= y) or w
#
#
# for i in product([1, 0], repeat=6):
#     t = (
#         (i[0], 0, i[1], i[2]),
#         (1, i[3], i[4], 1),
#         (i[5], 1, 0, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("xyzw"):
#             if [f(**dict((zip(p, r)))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f1(w, x, y, z):
#     return (x <= y) or (not w == z)
#
#
# def f2(w, x, y, z):
#     return (x <= y) == (w and (not z))
#
#
# for i in product([1, 0], repeat=6):
#     t = (
#         (i[0], i[1], i[2], 0),
#         (i[3], i[4], 0, 0),
#         (i[5], 0, 0, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f1(**dict(zip(p, r))) for r in t] \
#                  == [f2(**dict(zip(p, r))) for r in t]:
#                 print(*p)


# def f1(w, x, y, z):
#     return () == (x and z)
#
#
# def f2(w, x, y, z):
#     return not x or not y or not z or w
#
#
# def f3(w, x, y, z):
#     return (z or w) and y and x
#
#
# t = ((1, 0, 1, 0), (0, 1, 1, 1), (1, 1, 1, 0))
#
# if len(t) == len(set(t)):
#     for p in permutations("wxyz"):
#         if (
#             [f1(**dict(zip(p, t[0])))] == [1]
#             and [f2(**dict(zip(p, t[1])))] == [0]
#             and [f3(**dict(zip(p, t[2])))] == [1]
#         ):
#             print(*p)


# def f1(w, x, y, z):
#     return (w <= y) == (x and z)
#
#
# def f2(w, x, y, z):
#     return (not (x)) or (not (y)) or (not (z)) or w
#
#
# def f3(w, x, y, z):
#     return (z or w) and y and x
#
#
# table = [(1, 0, 1, 0), (0, 1, 1, 1), (1, 1, 1, 0)]
#
# if len(table) == len(set(table)):
#     for p in permutations("wxyz"):
#         if (
#             [f1(**dict(zip(p, table[0])))] == [1]
#             and [f2(**dict(zip(p, table[1])))] == [0]
#             and [f3(**dict(zip(p, table[2])))] == [1]
#         ):
#             print(p)


# def f(w, x, y, z):
#     return not(not(x <= (not w) and z)) and not(w <= z) and (x <= (not z))
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (1, 0, i[0], 0),
#         (1, 0, i[1], i[2]),
#         (i[3], 1, i[4], 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 0, 0]:
#                 print(*p)


# def f1(w, x, y, z):
#     return (w == x) and (y <= z)
#
#
# def f2(w, x, y, z):
#     return (w <= x) <= (y == z)
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (1, i[0], 1, 1),
#         (i[1], 1, 0, 0),
#         (i[2], 0, 0, i[3])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f1(**dict(zip(p, r))) for r in t] == [1, 1, 0] \
#                 and [f2(**dict(zip(p, r))) for r in t] == [0, i[4], 0]:
#                 print(*p)


# def f1(w, x, y, z):
#     return (x <= y) or (not w == z)
#
#
# def f2(w, x, y, z):
#     return (x <= y) == (w and (not z))
#
#
# for i in product([1, 0], repeat=6):
#     t = (
#         (i[0], i[1], i[2], 0),
#         (i[3], i[4], 0, 0),
#         (i[5], 0, 0, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f1(**dict(zip(p, r))) for r in t] \
#                 == [f2(**dict(zip(p, r))) for r in t]:
#                 print(*p)


# def f(w, x, y, z):
#     return (z <= w) and y and not x
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (0, 1, i[0], 0),
#         (i[1], 0, i[2], i[3]),
#         (0, 1, 1, i[4])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return w and ((z or y) == (z and x))
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (1, i[0], 1, 0),
#         (0, i[1], i[2], i[3]),
#         (1, 1, 1, i[4])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return w and ((y <= x) <= z)
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (i[0], i[1], 0, 1),
#         (0, i[2], i[3], 0),
#         (0, 1, i[4], 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return not x or z or not w and y
#
#
# for i in product([1, 0], repeat=6):
#     t = (
#         (i[0], 1, i[1], i[2]),
#         (i[3], 1, 1, i[4]),
#         (1, 1, 1, [5])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x or (not y)) and not(y == z) and w
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (0, 1, i[0], 0),
#         (i[1], 1, 1, 0),
#         (1, i[2], 0, i[3])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(a, b, c):
#     return (a and (not c)) and ((not b) and (not c))
#
#
# for i in product([1, 0]):
#     t = (
#         (0, 0, 0),
#         (0, 0, 1),
#         (0, 1, 0),
#         (0, 1, 1),
#         (1, 0, 0),
#         (1, 0, 1),
#         (1, 1, 0),
#         (1, 1, 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("abc"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 0, 0, 0, 1, 0, 1, 0]:
#                 print(*p)


# def f(x, y, z):
#     return (not x and y and z) and (not z and not y and z) and (not z and not y and not z)
#
#
# for i in product([1, 0], repeat=0):
#     t = (
#         (0, 0, 0),
#         (1, 0, 0),
#         (1, 0, 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("xyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return not(y <= w) or (x <= z) or not x
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (i[0], i[1], 0, 0),
#         (i[2], 1, i[3], i[4]),
#         (i[5], 0, 1, i[6])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return not(y <= x) or (z <= w) or not z
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (i[0], 0, i[1], i[2]),
#         (0, 1, i[3], i[4]),
#         (1, i[5], i[6], 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (y <= (not (x <= z))) or w
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (i[0], 0, i[1], i[2]),
#         (0, 1, i[3], i[4]),
#         (1, i[5], i[6], 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (not x and y and z and not w) or (not x and y and not z and not w) or (x and y and z and not w)
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (1, i[0], i[1], i[2]),
#         (0, i[3], 1, i[4]),
#         (i[5], 0, 0, i[6])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return not(x <= z) or (y == w) or y
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (1, 0, i[0], i[1]),
#         (i[2], 1, 0, i[3]),
#         (0, i[4], i[5], i[6])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (z <= (not(y <= x))) or w
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (i[0], 1, i[1], i[2]),
#         (i[3], i[4], 0, 0),
#         (i[5], 0, 1, i[6])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return w and (y == (z <= (x or y)))
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (i[0], 0, 0, i[1]),
#         (1, i[2], 1, 0),
#         (i[3], i[4], 1, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return ((y <= w) and (w <= z)) == ((z and x) or (x and y))
#
#
# for i in product([1, 0], repeat=2):
#     t = (
#         (0, 1, i[0], 0),
#         (0, 1, 1, 1),
#         (0, 1, i[1], 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1,  1]:
#                 print(*p)


# def f(x, y, z):
#     return x <= y and z
#
#
# for i in product([1, 0]):
#     t = (
#         (0, 1, 0),
#         (1, 1, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("xyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (w or y) and (x <= (not z)) and not w
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (i[0], 0, i[1], 0),
#         (1, i[2], i[3], i[4]),
#         (1, 1, 0, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return ((w <= y) <= x) or not z
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (i[0], i[1], 1, i[2]),
#         (i[3], 0, i[4], i[5]),
#         (i[6], 1, 0, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return not(x <= z) or (y == w) or y
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (1, 0, i[0], i[1]),
#         (i[2], 1, 0, i[3]),
#         (0, i[4], i[5], i[6])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return not (y <= (x == w)) and (z <= x)
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (i[0], 1, 1, i[1]),
#         (0, i[2], i[3], 0),
#         (i[4], 0, 1, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x == (w or y)) or ((w <= z) and (y <= w))
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (1, i[0], i[1], 1),
#         (i[2], i[3], i[4], 1),
#         (1, i[5], 1, i[6])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x or not y) and not(x == z) and w
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (i[0], 0, 0, 1),
#         (0, 0, 1, 1),
#         (0, i[1], i[2], i[3])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return not(not(x <= (not w)) and z) and not(w <= z) and (x <= (not z))
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (1, 0, i[0], 0),
#         (1, 0, i[1], i[2]),
#         (i[3], 1, i[4], 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (w or y) and (x <= (not z)) and not w
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (i[0], 0, i[1], 0),
#         (1, i[2], i[3], i[4]),
#         (1, 1, 0, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f1(w, x, y, z):
#     return (w == x) and (y <= z)
#
#
# def f2(w, x, y, z):
#     return (w <= x) <= (y == z)
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (1, i[0], 1, 1),
#         (i[1], 1, 0, 0),
#         (i[2], 0, 0, i[3])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f1(**dict(zip(p, r))) for r in t] == [1, 1, 0] and \
#                [f2(**dict(zip(p, r))) for r in t] == [0, i[4], 0]:
#                print(*p)


# def f1(w, x, y, z):
#     return (x <= y) or (not w == z)
#
#
# def f2(w, x, y, z):
#     return (x <= y) == (w and (not z))
#
#
# for i in product([1, 0], repeat=6):
#     t = (
#         (i[0], i[1], i[2], 0),
#         (i[3], i[4], 0, 0),
#         (i[5], 0, 0, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f1(**dict(zip(p, r))) for r in t] == \
#                [f2(**dict(zip(p, r))) for r in t]:
#                print(*p)


# def f(x, y, z):
#     return x <= y and z
#
#
# for i in product([1, 0]):
#     t = (
#         (0, 1, 0),
#         (1, 1, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("xyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (z <= w) and y and not x
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (0, 1, i[0], 0),
#         (i[1], 0, i[2], i[3]),
#         (0, 1, 1, i[4])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 0]:
#                 print(*p)


# def f(x, y, z):
#     return (x or y) <= (z == x)
#
#
# for i in product([1, 0], repeat=3):
#     t = (
#         (i[0], 0, 0),
#         (i[1], 0, i[2])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("zyx"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0]:
#                 print(*p)


# def f(x, y, z):
#     return (x == y) or ((y or z) <= x)
#
#
# for i in product([1, 0], repeat=3):
#     t = (
#         (i[0], 1, 1),
#         (i[1], i[2], 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("zyx"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x and not y) or (y == z) or not w
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (i[0], 0, i[1], i[2]),
#         (1, 0, i[3], 0),
#         (1, i[4], 0, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x == (w or y)) or ((w <= z) and (y <= w))
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (1, i[0], i[1], 1),
#         (i[2], i[3], i[4], 1),
#         (1, i[5], 1, i[6])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] ==[0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (z and y) or ((x <= z) == (y <= w))
#
#
# for i in product([1, 0], repeat=6):
#     t = (
#         (i[0], i[1], i[2], 1),
#         (1, i[3], i[4], 1),
#         (1, i[5], 1, 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (not x and not y) or (y == z) or not w
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (0, i[0], 0, 1),
#         (i[1], 0, i[2], 1),
#         (0, 1, 1, i[3])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return ((x <= y) == (y <= z)) and (y or w)
#
#
# for i in product([1, 0], repeat=6):
#     t = (
#         (0, i[0], 0, i[1]),
#         (0, 0, i[2], 0),
#         (i[3], i[4], i[5], 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [ 1, 1, 1 ]:
#                 print(*p)


# def f(w, x, y, z):
#     return ((y <= x) == (x <= w)) and (z or x)
#
#
# for i in product([1, 0], repeat=6):
#     t = (
#         (0, i[0], i[1], 0),
#         (0, 0, 0, i[2]),
#         (i[3], i[4], 0, i[5])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x == (not y)) <= (z == (y or w))
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (0, i[0], 0, i[1]),
#         (0, 0, i[2], 0),
#         (0, i[3], i[4], 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f1(w, x, y, z):
#     return (x or not y) <= (w == z)
#
#
# def f2(w, x, y, z):
#     return (x or not y) == (w <= z)
#
#
# for i in product([1, 0], repeat=6):
#     t = (
#         (0, i[0], 0, 0),
#         (i[1], 1, 1, i[2]),
#         (i[3], 0, 0, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f1(**dict(zip(p, r))) for r in t] == [0, 0, i[4]] and \
#                [f2(**dict(zip(p, r))) for r in t] == [0, i[5], 0]:
#                 print(*p)


# def f1(w, x, y, z):
#     return (w or not y) <= (z == x)
#
#
# def f2(w, x, y, z):
#     return (w or not y) == (x <= z)
#
#
# for i in product([1, 0], repeat=6):
#     t = (
#         (i[0], 1, i[1], 1),
#         (i[2], 0, 0, 0),
#         (0, 0, 0, i[3])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations('wxyz'):
#             if [f1(**dict(zip(p, r))) for r in t] == [0, i[4], 0] and \
#                 [f2(**dict(zip(p, r))) for r in t] == [i[5], 0, 0,]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x and not y) or (x == z) or w
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (i[0], i[1], 0, 1),
#         (1, 0, i[2], 1),
#         (1, 1, 0, i[3])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x or (not y)) and not(y == z) and not w
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


# def f(w, x, y, z):
#     return (x and (not y)) or (x == z) or w
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (0, 0, i[0], 1),
#         (0, i[1], 1, i[2]),
#         (i[3], 1, 1, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x or y) and not(y == z) and not w
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (i[0], 1, i[1], 1),
#         (0, 0, 1, i[2]),
#         (0, i[3], 1, 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f1(w, x, y, z):
#     return (x == y) and (w <= z)
#
#
# def f2(w, x, y, z):
#     return (x <= y) <= (w == z)
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (1, i[0], 1, 1),
#         (0, 1, 0, i[1]),
#         (i[2], 0, 0, i[3])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f1(**dict(zip(p, r))) for r in t] == [1, 1, 0] and \
#                [f2(**dict(zip(p, r))) for r in t] == [0, i[4], 0]:
#                 print(*p)


# def f1(w, x, y, z):
#     return (w == x) and (y <= z)
#
#
# def f2(w, x, y, z):
#     return (w <= x) <= (y == z)
#
#
# for i in product([1, 0], repeat=5):
#     t = (
#         (1, i[0], 1, 1),
#         (i[1], 1, 0, 0),
#         (i[2], 0, 0, i[3])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f1(**dict(zip(p, r))) for r in t] ==[1, 1, 0] and \
#                [f2(**dict(zip(p, r))) for r in t] ==[0, i[4], 0]:
#                 print(*p)


# def f(u, w, x, y, z):
#     return ((x <= y) and (z == (not w))) <= (u == (x or z))
#
#
# for i in product([1, 0], repeat=8):
#     t = (
#         (0, i[0], 0, 0, 0),
#         (0, i[1], i[2], 0, 0),
#         (i[3], 0, 0, 0, i[4]),
#         (i[5], 0, i[6], i[7], 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("uwxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return not (x <= z) or (y == w) or y
#
#
# for i in product([1, 0], repeat=7):
#     t = (
#         (1, 0, i[0], i[1]),
#         (i[2], 1, 0, i[3]),
#         (0, i[4], i[5], i[6])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return not(not x or not (not z or w)) and (not z or (not w == y))
#
#
# for i in product([1, 0], repeat=5):
#     t = ((1, i[0], 1, 1), (i[1], i[2], 0, 0), (i[3], 0, 0, i[4]))
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 1, 1]:
#                 print(*p)


# print("x y z f")
#
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             f = (not z) and x or x and y
#             print(x, y, z, int(f))


# def f(w, x, y, z):
#     return (y <= x) and not w and z
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (1, 0, 1, 1),
#         (1, 0, i[0], 1),
#         (i[1], i[2], i[3], 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] ==[1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return (y <= x) and not z and w
#
#
# for i in product([1, 0], repeat=6):
#     t = (
#         (1, 0, i[0], i[1]),
#         (1, 1, i[2], i[3]),
#         (i[4], 1, 1, i[5])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] ==[1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return ((x and w) or (w and z)) == ((z <= y) and (y <= x))
#
#
# for i in product([1, 0], repeat=2):
#     t = (
#         (1, 0, 1, 1),
#         (1, 0, i[0], 0),
#         (1, 0, i[1], 0),
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] ==[1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x and (not y)) or (y == z) or not w
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (0, i[0], i[1], 0),
#         (0, 1, 0, 1),
#         (i[2], 1, 0, i[3])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] ==[0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x and y) or (y == z) or w
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (i[0], 1, 0, 0),
#         (0, i[1], 1, i[2]),
#         (0, 1, i[3], 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return ((y <= w) == (x <= (not z))) and ( x or w )
#
#
# for i in product([1, 0], repeat=2):
#     t = (
#         (0, 1, 1, 1),
#         (1, 0, 1, 0),
#         (i[0], 0, 0, i[1])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return ((y <= z) or (not x and w)) == (w == z)
#
#
# for i in product([1, 0], repeat=3):
#     t = (
#         (i[0], 1, 0, 0),
#         (0, 0, 0, 1),
#         (0, 1, i[1], i[2])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] ==[1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return ((x and (not y)) or (w <= z)) == (z == x)
#     
#
# for i in product([1, 0], repeat=3):
#     t = (
#         (i[0], 0, 0, 1),
#         (0, 1, 0, 0),
#         (0, i[1], i[2], 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return ((w <= (not x)) == (z <= y)) and (y or w)
#
#
# for i in product([1, 0], repeat=2):
#     t = (
#         (1, 1, 1, 0),
#         (0, 0, 1, 1),
#         (0, i[0], 0, i[1])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] ==[0, 1, 1]:
#                 print(*p)


# def f(w, x, y, z):
#     return (x or (not y)) and not(w == z) and w
#
#
# for i in product([1, 0], repeat=3):
#     t = (
#         (1, i[0], 0, 0),
#         (1, 0, 0, 1),
#         (1, 0, i[1], i[2])
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1 ,1]:
#                 print(*p)


# def f(w, x, y, z):
#     return not(x or y) and not w or not(z or w) and y
#
#
# for i in product([1, 0], repeat=8):
#     t = (
#         (i[0], 1, i[1], i[2]),
#         (i[3], i[4], 1, i[5]),
#         (i[6], 1, i[7], 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1 ,1 ,1]:
#                 print(*p)


# def f(w, x, y, z):
#     return not(x or y) and not w or not(z or w) and y
#
#
# for i in product([1, 0], repeat=8):
#     t = [
#         (i[0], 1, i[1], i[2]),
#         (i[3], i[4], 1, i[5]),
#         (i[6], 1, i[7], 1)
#     ]
#
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(*p)


# def f(a, b, c, d):
#     return ((a <= b) == c) or d
#
#
# for i in product([1, 0], repeat=4):
#     t = (
#         (1, 0, 1, i[0]),
#         (1, 0, i[1], 1),
#         (i[2], i[3], 1, 0)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("abcd"):
#             if [f(**dict(zip(p, r))) for r in t] ==[0, 0, 0]:
#                 print(*p)


# def f(w, x, y, z):
#     return ((z == x) <= w) and (w <= (y and x))
#
#
# for i in product([1, 0], repeat=3):
#     t = (
#         (1, 1, i[0], 0),
#         (1, i[1], i[2], 0),
#         (1, 0, 1, 1)
#     )
#     if len(set(t)) == len(t):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p,r ))) for r in t] == [1, 1, 1]:
#                 print(*p)
