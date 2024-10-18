from sys import setrecursionlimit

setrecursionlimit(10 * 10000)


# def f(n):
#     if n == 1: return 1
#     return (n - 1) * f(n - 1)
#
#
# print((f(2024) // 7 - f(2023)) // f(2022))


# def f(n):
#     if n == 1: return 1
#     return (n + 1) * f(n - 1)
#
#     s.replace("0")
#
# print((f(2024) - 3 * f(2023)) // f(2022))


# def f(n):
#     if n == 1: return 1
#     return 2 * n * f(n - 1)
#
# print((f(2024) // 16 - f(2023)) // f(2022))


# def f(n):
#     if n <= 3: return 2025
#     return 3 * (n - 1) * f(n - 2)
#
# print(f(2027) // f(2023))


# def f(n):
#     if n == 1: return 1
#     return n * f(n - 1)
#
# print((f(2024) - f(2023)) // f(2022))


# def f(n):
#     if n < 7: return 7
#     if n >= 7 and n % 3 != 0: return 5 - f(n - 1)
#     if n >= 7 and n % 3 == 0: return 3 + f(n - 1)
#
#
# print(f(3015))


# def f(n):
#     if n <= 7: return 1
#     return n + 2 + f(n - 1)
#
#
# print(f(2024) - f(2020))


# def f(n):
#     if n == 1: return 1
#     return (n + 1) * f(n - 1)
#
#
# print(f(5037) // f(5034))


# def f(n):
#     if n >= 7777: return n
#     return n + 5 + f(n + 5)
#
#
# print(f(1101) - f(1111))


# def f(n):
#     if n <= 3: return 1
#     if n % 3 == 0 and n > 3: return f(n // 3) + 4 * n
#     return n * n * n - 26
#
#
# print(next(x for x in range(1000, 1, -1) if f(x) < 300))


# def g(n):
#     if n == 3:
#         return 1
#     if n > 3:
#         return 6 * f(n - 1) + 5 * g(n - 1) + 3
#
#
# def f(n):
#     if n == 3:
#         return 1
#     if n > 3:
#         return 5 * f(n - 1) + 6 * g(n - 1) - 3 * n + 8
#
#
# print(f(9) + g(9))


# def f(n):
#     if n < 10:
#         return n
#     if 10 <= n < 1000:
#         return f(n // 10) + f(n % 10)
#     if n >= 1000:
#         return f(n // 1000) - f(n % 1000)
#
#
# res = 0
#
# for n in range(10**6):
#     if f(n) == 0:
#         res += 1
#
# print(res)


# def f(n):
#     if n == 1: return 1
#     if n > 1: return 2 * n * f(n - 1)
#
# print((f(2024) // 16 - f(2023)) // f(2022))


# def f(n):
#     if n == 1: return 1
#     if n > 1: return (n + 1) * f(n - 1)
#
#
# print((f(2024) + 3 * (f(2023))) // f(2022))


# def f(n):
#     if n == 1: return 1
#     if n > 1: return (n + 1) * f(n - 1)
#
#
# print((f(2024) - 3 * (f(2023))) // f(2022))


# def f(n):
#     if n == 1: return 1
#     if n > 1: return (n - 1) * f(n - 1)
#
# print((f(2024) // 7 - f(2023)) // f(2022))


# def f(n):
#     if n < 2: return 7
#     if n > 1: return 7 * f(n - 2)
#
# print(f(12950) // 7**6473)


# def f(n):
#     if n == 1: return 1
#     if n > 1: return n * f(n - 1)
#
# print((f(2024) - f(2023)) // f(2022))


# def f(n):
#     if n == 0:
#         return 0
#     elif n % 2 == 0:
#         return f(n // 2) + 1
#     else:
#         return f(n - 1) + 1
#
# k = 0
# for i in range(1000000001):
#     if f(3) < i:
#         k += 1
#
# print(k)


# def f(n):
#     if n == 1: return 1
#     if n > 1: return n * f(n - 1)
#
#
# print((f(2024) - f(2023)) // f(2022))


# def f(n):
#     if n > 400: return n ** n
#     if n <= 400: return n + 6 + f(n + 12)
#
#
# print(f(72) - f(108))


# def f(n):
#     if n < 7: return 7
#     if n >= 7: return n + 1 + f(n - 2)
#
#
# print(f(2024) - f(2020))


# def f(n):
#     if n <= 3: return 2025
#     if n > 3: return 3 * (n - 1) * f(n - 2)
#
#
# print(f(2027) // f(2023))
