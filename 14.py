from string import digits, ascii_uppercase


# def f(n):
#     s = ""
#
#     while n > 0:
#         s = str(n % 7) + s
#         n //= 7
#
#     return s
#
#
# for x in range(2030, 0, -1):
#     s = f(7 ** 170 + 7 ** 100 - x)
#
#     if s.count("0") == 71:
#         print(x)
#         break

# def f(n):
#     s = ''
#
#     while n > 0:
#         s = str(n % 25) + s
#         n //= 25
#
#     return s
#
#
# s = f(3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2025)
# print(s.count("0"))


# def f(n):
#     s = ''
#
#     while n > 0:
#         s = str(n % 6) + s
#         n //= 6
#
#     return s
#
#
# for x in range(2031):
#     s = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
#
#     if f(s).count("0") == 202:
#         print(x)
#         break


# def f(n):
#     s = ""
#
#     while n > 0:
#         s = str(n % 7) + s
#         n //= 7
#
#     return s
#
#
# for x in range(2030, 0, -1):
#     s = 7 ** 91 + 7 ** 160 - x
#
#     if f(s).count("0") == 70:
#         print(x)
#         break


# def f(n):
#     s = ""
#
#     while n > 0:
#         s = str(n % 3) + s
#         n //= 3
#
#     return s
#
#
# for x in range(2030, 0, -1):
#     s = 3 ** 100 - x
#
#     if f(s).count("0") == 5:
#         print(x)
#         break


# n = 3 * 2187 ** 2020 + 3 * 729 ** 2021 - 2 * 81 ** 2022 + 27 ** 2023 - 4 * 3 ** 2024 - 2029
# res = 0
#
# while n > 0:
#     if n % 27 > 9:
#         res += 1
#
#     n //= 27
#
# print(res)


# for x in "0123456789abcdefghijlmnopq":
#     a = int(f"123{x}24", 27) + int(f"135{x}78", 27)
#
#     if a % 26 == 0:
#         print(x, a // 26)


# for x in "012345678":
#     a = int(f"{x}1{x}", 16) + int(f"{x}3{x}3", 8)
#
#     if a % 2 == 0:
#         print(x)


# for x in "0123456789abcde":
#     s = int(f"99658{x}29", 15) + int(f"102{x}023", 15)
#
#     if s % 14 == 0:
#         print(x, s // 14)


# for x in "0123456789abcdef":
#     s = n = int(f"b7a{x}9", 16) + int(f"54{x}ed", 16)
#     a = 0
#
#     while s > 0:
#         a = s % 6 + a
#         s //= 6
#
#     if a == 25:
#         print(x, n)


# for x in range(111):
#     n1 = 1 * 111 ** 0 + 2 * 111 ** 1 + 3 * 111 ** 2 + x * 111 ** 3
#     n2 = 4 * 211 ** 0 + x * 211 ** 1 + 7 * 211 ** 2 + 1 * 211 ** 3
#     n = n1 + n2
#
#     if n % 111 == 0:
#         print(n // 111)

# for x in range(98): n1 = 5 * 98 ** 0 + 4 * 98 ** 1 + x * 98 ** 2 + 2 * 98 ** 3 + 1 * 98 ** 4 n2 = 8 * 123 ** 0 + 9 * 123 ** 1 + x * 123 ** 2 + 1 * 123 ** 3 n = n1 + n2 if n % 123 == 0: print(n // 123) for p in range(2, 100): for x in range(p): for y in range(p): n1 = 7 * p ** 0 + 7 * p ** 1 + x * p ** 2 + 1 * p ** 3 n2 = 7 * p ** 0 + 7 * p ** 1 + x * p ** 2 + x * p ** 3 r = y * p ** 0 + y * p ** 1 + 0 + y * p ** 3 n = n1 + n2 if n == r: print(x * p ** 0 + y * p ** 1 + x * p ** 2 + y * p ** 3)


# for p in range(2, 100):
#     for x in range(p):
#         for y in range(p):
#             n1 = 3 * p ** 0 + 8 * p ** 1 + x * p ** 2 + 5 * p ** 3
#             n2 = 9 * p ** 0 + x * p ** 1 + 9 * p ** 2 + x * p ** 3
#             n = n1 + n2
#
#             r = y * p ** 0 + 0 + 2 * p ** 2 + y * p ** 3
#
#             if n == r:
#                 print(x * p ** 0 + y * p ** 1 + y * p ** 2 + x * p ** 3)


# a = 68
# for x in range(68):
#     n1 = 5 * a**0 + x * a**1 + 3 * a**2 + 2 * a**3 + 1 * a**4
#     n2 = 3 * a**0 + 3 * a**1 + 2 * a**2 + x * a**3 + 1 * a**4
#
#     n = n1 + n2
#
#     if n % 12 == 0:
#         print(n // 12)


# def f(n):
#     s = ""
#
#     while n > 0:
#         s += str(n % 3)
#         n //= 3
#
#     return s
#
#
# s = 2 * 729**1021 - 2 * 243**1022 + 81**1023 - 2 * 27**1024 - 1025
# print(f(s).count("0"))


# for x in "012345679abc":
#     s = int(f"753{x}2", 13) + int(f"2{x}173", 13)
#
#     if s % 12 == 0:
#         print(x, s // 12)


# for p in range(2, 100):
#     for x in range(p):
#         for y in range(p):
#             n1 = 8 * p ** 0 + x * p ** 1 + x * p ** 2 + x * p ** 3
#             n2 = 9 * p ** 0 + x * p ** 1 + 3 * p ** 2 + 4 * p ** 3
#
#             r = 4 * p ** 0 + 0 + y * p ** 2 + y * p ** 3
#
#             if n1 + n2 == r:
#                 print(x * p ** 0 + y * p ** 1 + y * p ** 2)


# def f(n):
#     zeros_count = 0
#
#     while n > 0:
#         if n % 32 == 0:
#             zeros_count += 1
#         n //= 32
#
#     return zeros_count
#
#
# s = 3 * 1024**75 + 2 * 256**76 - 16**77 - 2023
# print(f(s))


# def f(n):
#     zeros_count = 0
#
#     while n > 0:
#         if n % 6 == 0:
#             zeros_count += 1
#         n //= 6
#
#     return zeros_count
#
#
# s = 5 * 216**155 + 4 * 36**156 - 4 * 6**157 - 2023
#
# print(f(s))


# for x in "012345679abcdef":
#     s = int(f"10{x}A", 16) + int(f"FF{x}78", 16)
#
#     if s % 19 == 0:
#         print(x, s // 19)


# m = 0
#
# for x in range(20):
#     for y in range(5):
#         s1 = 4 * 20**0 + x * 20**1 + 3 * 20**2 + x * 20**3 + 2 * 20**4 + x * 20**5 + 1 * 20**6
#         s2 = y * 5**0 + 4 * 5**1 + y * 5**2 + 3 * 5**3 + y * 5**4 + 2 * 5**5 + y * 5**6 + 1 * 5**7
#         s = s1 - s2
#         a = 0
#
#         while s > 0:
#             a += s % 7
#             s //= 7
#
#         m = max(m, s)
#
# print(m)


# for x in range(1, 1000):
#     s = int(f"9{x}AB", 13) + int(f"{x}46C", 16) - int(f"B7{x}", 15)
#
#     if s % 14 == 0:
#         print(x, s // 14)
#         break


# def f(n):
#     s = ""
#
#     while n > 0:
#         s += str(n % 9)
#         n //= 9
#
#     return s
#
#
# s = 2 * 729**333 + 2 * 243**334 - 81**335 + 2 * 27**336 - 2 * 9**337 - 338
# print(len(f(s)) - f(s).count("0"))


# def f(n):
#     s = ""
#
#     while n > 0:
#         s += str(n % 9)
#         n //= 9
#
#     return s
#
#
# s = 361 * 2349**84 - 89**192 + 1953**481 * 4843**151
# print(f(s).count("5"))


# for x in range(1, 1000):
#     k1 = 4 * 32 ** 0 + 6 * 32 ** 1 + 9 * 32 ** 2 + x * 32 ** 3 + 1 * 32 ** 4 + 3 * 32 ** 5 + 9 * 32**6
#     k2 = 1 * 32**0 + x * 32**1 + 1 * 32**2 + 5 * 32**3 + x * 32**4 + 4 * 32**5
#     k3 = 7 * 32**0 + 3 * 32**1 + 6 * 32**2 + x * 32**3 + 1 * 32**4 + 6 * 32**5 + 8 * 32** 6 + 2 * 32**7
#
#     k = k1 + k2 + k3
#
#     if k % 31 == 0:
#         print(x, k // 31)
#         break


# for x in (digits + ascii_uppercase)[:32]:
#     s = int(f"931{x}964", 32) + int(f"4{x}51{x}1", 32) + int(f"2861{x}637", 32)
#
#     if s % 31 == 0:
#         print(, s // 31)

# symbols = digits + ascii_uppercase
#
# for x in symbols[:27]:
#     s = int(f"17{x}35", 27) + int(f"{x}742M", 27) + int(x, 27) ** 3
#
#     if s % 23 == 0:
#         print(s // 23)


# symbols = digits + ascii_uppercase
#
# for x in symbols[:17][::-1]:
#     s = int(f"7AC{x}53D", 17) + int(f"83BG94{x}D", 17) + int(f"C5{x}D", 17) + int(f"C4BBF{x}4", 17) + int(f"7{x}79", 17)
#
#     if s % 16 == 0:
#         print(s // 16)
#         break


# def f(n):
#     s = ""
#
#     while n > 0:
#         s += str(n % 7)
#         n //= 7
#
#     return s
#
#
# for x in range(2030, 1, -1):
#     s = f(7**91 + 7**160 - x)
#
#     if s.count("0") == 70:
#         print(x)
#         break


# def f(n):
#     s = ""
#
#     while n > 0:
#         s += str(n % 6)
#         n //= 6
#
#     return s
#
# res = []
#
# for x in range(2030, 1, -1):
#     s = f(6**2030 + 6**100 - x)
#
#     res.append(s.count("0"))
#
# print(max(res))


# def f(n):
#     s = ""
#
#     while n > 0:
#         s += str(n % 6)
#         n //= 6
#
#     return s
#
#
# for x in range(1, 2031):
#     s = f(6**260 + 6**160 + 6**60 - x)
#
#     if s.count("0") == 202:
#         print(x)


# def f(n):
#     s = ""
#
#     while n > 0:
#         s += str(n % 6)
#         n //= 6
#
#     return s
#
#
# for x in range(2030, 1, -1):
#     s = f(6**260 + 6**160 + 6**60 - x)
#
#     if s.count("0") == 202:
#         print(x)
#         break


# symbols = digits + ascii_uppercase
#
# for x in range(1000, 1, -1):
#     s = int(f"12{x}34", 33) + int(f"49{x}9", 33)
#
#     if s % 19 == 0:
#         print(x, s // 19)
#         break


# s = 2 * 729**2014 + 2 * 243**2016 - 2 * 81**2018 + 2 * 27**2020 - 2 * 9**2022 - 2024
#
# k = 0
#
# while s > 0:
#     if s % 27 > 9:
#         k += 1
#     s //= 27
#
# print(k)


# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if n % 2 == 0:
#         s = "1" + s + "0"
#     else:
#         s = "11" + s + "11"
#
#         r = int(s, 2)
#
#         if r > 52:
#             print(n)
#             break


# def f(n):
#     s = ""
#
#     while n > 0:
#         s = str(n % 5) + s
#         n //= 5
#
#     return s
#
#
# s = f(125 + 25**3 + 5**9)
# print(s.count("0"))


# s = 2 * 729**2014 + 2 * 243**2016 - 2 * 81**2018 + 2 * 27**2020 - 2 * 9**2022 - 2024
#
# k = 0
#
# while s > 0:
#     if s % 27 > 9:
#         k += 1
#     s //= 27
#
# print(k)


# def f(n):
#     s = ""
#
#     while n > 0:
#         s = str(n % 4) + s
#         n //= 4
#
#     return s
#
#
# s = 4**644 + 4**322 + 16**35 - 64**3
#
# print(f(s).count("3"))


# symbols = digits + ascii_uppercase
#
# for x in symbols:
#     s = int(f"18{x}89957", 22) + int(f"80{x}33", 22) + int(f"521{x}6", 22)
#
#     if s % 21 == 0:
#         print(s // 21)
#         break


# s = 4 * 3125**2019 + 3 * 625**2020 - 2 * 125**2021 + 25**2022 - 4 * 5**2023 - 2024
# n = 0
#
# while s > 0:
#     a = ""
#
#     if s % 25 > 10:
#         n += 1
#     s //= 25
#
# print(n)
