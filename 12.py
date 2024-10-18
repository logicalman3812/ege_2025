# s = "9" * 136
#
# while "22222" in s or "9999" in s:
#     if "22222" in s:
#         s = s.replace("22222", "99", 1)
#     else:
#         s = s.replace("9999", "2", 1)
#
# print(s)


# s = 83 * "8"
#
# while "111" in s or "88888" in s:
#     if "111" in s:
#         s = s.replace("111", "88", 1)
#     else:
#         s = s.replace("88888", "8", 1)
#
# print(s)


# s = 100 * "9"
#
# while "33333" in s or "999" in s:
#     if "33333" in s:
#         s = s.replace("33333", "99", 1)
#     else:
#         s = s.replace("999", "3", 1)
#
# print(s)


# s = 82 * "8"
#
# while "1111" in s or "8888" in s:
#     if "1111" in s:
#         s = s.replace("1111", "8", 1)
#     else:
#         s = s.replace("8888", "11", 1)
#
# print(s)


# for n in range(4, 1000):
#     s = "2" + "5" * n
#
#     while "25" in s or "355" in s or "555" in s:
#         s = s.replace("25", "5", 1)
#         s = s.replace("355", "52", 1)
#         s = s.replace("555", "3", 1)
#
#     if s.count("3") == 3:
#         print(n)
#         break


# for n in range(4, 10000):
#     s = "5" + "2" * n
#
#     while "52" in s or "2222" in s or "1122" in s:
#         if "52" in s:
#             s = s.replace("52", "11")
#         if "2222" in s:
#             s = s.replace("2222", "5")
#         if "1122" in s:
#             s = s.replace("1122", "25")
#
#     if sum(map(int, s)) == 64:
#         print(n)


# res = 0
#
# for n in range(4, 10000):
#     s = "5" + "7" * n
#
#     while "57" in s or "877" in s or "777" in s:
#         s = s.replace("57", "7", 1)
#         s = s.replace("877", "75", 1)
#         s = s.replace("777", "8", 1)
#
#     res = max(res, sum(map(int, s)))
#
#
# print(res)


# res = 0
#
# for n in range(210, 300):
#     s = "3" + n * "7"
#
#     while "27" in s or "377" in s or "777" in s:
#         s = s.replace("27", "32", 1)
#         s = s.replace("377", "27", 1)
#         s = s.replace("777", "3", 1)
#
#     if sum(map(int, s)) % 15 == 0:
#         print(n)


# res = 0
#
# for n in range(4, 2000):
#     s = "3" * n + "5"
#
#     while "23" in s or "5333" in s or "33333" in s:
#         s = s.replace("23", "3", 1)
#         s = s.replace("5333", "32", 1)
#         s = s.replace("33333", "55", 1)
#
#     res = min(res, sum(map(int, s)))
#
# print(res)


# m = 0
# s = "3" + "4" * 40 + 25 * "2" + "3"
#
# while "3" in s:
#     if "342" in s:
#         s = s.replace("342", "4123", 1)
#     elif "34" in s:
#         s = s.replace("34", "413", 1)
#     elif "32" in s:
#         s = s.replace("32", "13", 1)
#     elif "33" in s:
#         s = s.replace("33", "424", 1)
#
#     m = max(m, sum(map(int, s)))
#
# print(m)


# for n in range(108, 1000, 9):
#     s = "5" * n
#
#     while "555" in s or "11" in s or "2" in s:
#         s = s.replace("555", "5", 1)
#         s = s.replace("11", "25", 1)
#         s = s.replace("2", "5", 1)
#
#     print(n, s)


# for n in range(108, 1000, 9):
#     s = "5" * n
#
#     while "555" in s or "11" in s or "2" in s:
#         s = s.replace("555", "5", 1)
#         s = s.replace("11", "25", 1)
#         s = s.replace("2", "5", 1)
#
#     print(n, s)


# for n in range(3, 1000):
#     s = "2" + "5" * n
#
#     while "25" in s or "35" in s or "555" in s:
#         s = s.replace("25", "53", 1)
#         s = s.replace("35", "2", 1)
#         s = s.replace("555", "23", 1)
#
#     if sum(map(int, s)) % 7 == 0:
#         print(n)


# res = 0
#
# for n in range(1000, 2001):
#     s = "7" + "8" * n
#
#     while "78" in s or "888" in s:
#         s = s.replace("78", "8", 1)
#         s = s.replace("888", "7", 1)
#
#     if sum(map(int, s)) == 16:
#         res += 1
#
# print(res)


# res = []
#
# for n in range(1, 1000):
#     s = "4" + "6" * n
#
#     while "46" in s or "666" in s:
#         s = s.replace("46", "5", 1)
#         s = s.replace("666", "4", 1)
#
#     if sum(map(int, s)) > 1000:
#         res.append(n)
#
# print(min(res))


# res = []
#
# for n in range(10, 101):
#     s = "3" + n * "7"
#
#     while "27" in s or "377" in s or "777" in s:
#         s = s.replace("27", "32", 1)
#         s = s.replace("377", "27", 1)
#         s = s.replace("777", "3", 1)
#
#     if sum(map(int, s)) % 22 == 0:
#         res.append(n)
#
# print(max(res))


# res = []
#
#
# for n in range(1, 100):
#     s = "13" * n
#
#     while "13" in s or "31" in s or "11" in s:
#         s = s.replace("13", "4", 1)
#         s = s.replace("31", "1", 1)
#         s = s.replace("11", "2", 1)
#         s = s.replace("44", "1", 1)
#
#     if 10 <= sum(map(int, s)) <= 99:
#         res.append(n)
#
#
# print(res)


# for n in range(1, 1000):
#     s = "2" + n * "5"
#
#     while "25" in s or "355" in s or "555" in s:
#         s = s.replace("25", "5", 1)
#         s = s.replace("355", "52", 1)
#         s = s.replace("555", "3", 1)
#
#     if s.count("3") == 2:
#         print(n, s)


# res = []
#
# for n in range(6, 1500):
#     s = "1" + "5" * n + "2" + "5" * n
#
#     while "15" in s or "255" in s or "555" in s:
#         s = s.replace("15", "2", 1)
#         s = s.replace("255", "1", 1)
#         s = s.replace("555", "12", 1)
#
#     if 100 <= sum(map(int, s)) <= 999:
#         res.append(n)
#
# print(max(res))


# res = []
#
# for n in range(6, 1000):
#     s = "1" + "3" * n
#
#     while "12" in s or "233" in s or "3333" in s:
#         s = s.replace("12", "332", 1)
#         s = s.replace("233", "23", 1)
#         s = s.replace("3333", "32", 1)
#
#     if sum(map(int, s)) % 6 == 0:
#         res.append(n)
#
# print(min(res))


# def prime(x):
#     for j in range(2, x):
#         if x % j == 0:
#             return 0
#     return 1
#
#
# for n in range(1, 1000):
#     s = ">" + "0" * 39 + "2" * 39
#
#     while ">1" in s or ">2" in s or ">0" in s:
#         s = s.replace(">1", "22>", 1)
#         s = s.replace(">2", "2>", 1)
#         s = s.replace(">0", "1>", 1)
#
#     sum_ = sum(map(int, s))
#
#     print(n, s, prime(sum_))


# s = 104 * "7"
#
# while "33333" in s or "777" in s:
#     if "33333" in s:
#         s = s.replace("33333", "7", 1)
#     else:
#         s = s.replace("777", "3", 1)
#
# print(s)


# for n in range(1, 500):
#     s = "1" * (n // 2) + "2" * (n // 2)
#
#     while "12" in s or "21" in s:
#         if "12" in s:
#             s = s.replace("12", "21", 1)
#         else:
#             s = s.replace("21", "111", 1)
#
#     if s.count("1") > 100:
#         print(n)
#         break


# for n in range(101, 200):
#     s = "3" * n
#
#     while "111" in s or "333" in s:
#         if "111" in s:
#             s = s.replace("111", "3", 1)
#         else:
#             s = s.replace("333", "1", 1)
#


# for n in range(4, 1000):
#     s = "4" * 20 + n * "5" + "7" * 15
#
#     while "74" in s or "75" in s:
#         if "75" in s:
#             s = s.replace("75", "744", 1)
#         else:
#             s = s.replace("74", "44", 1)
#
#     print(n, s)


# for n in range(4, 1000):
#     s = "2" + "5" * n
#
#     while "25" in s or "355" in s or "555" in s:
#         s = s.replace("25", "5", 1)
#         s = s.replace("355", "52", 1)
#         s = s.replace("555", "3", 1)
#
#     if s.count("3") == 3:
#         print(n)
#         break


# for x in range(50):
#     for y in range(50):
#         for z in range(50):
#             s = "0" + "1" * x + "2" * y + "3" * z
#
#             while "01" in s or "02" in s or "03" in s:
#                 s = s.replace("01", "30", 1)
#                 s = s.replace("02", "3103", 1)
#                 s = s.replace("03", "1201", 1)
#             if s.count("1") == 31 and s.count("2") == 24 and s.count("3") == 46:
#                 print(z)


# s = ">" + "1" * 50 + "2" * 30 + "3" * 10 + "4" * 10
#
# while ">12" in s or ">13" in s or ">41" in s or ">31" in s:
#     s = s.replace(">12", "32>", 1)
#     s = s.replace(">31", "21>", 1)
#     s = s.replace(">13", "41>", 1)
#     s = s.replace(">41", "23>", 1)
#
# print(sum(map(int, s[:-1])))


# for x1 in range(100):
#     for x2 in range(100):
#         for x3 in range(100):
#             s = "0" + "1" * x1 + "2" * x2 + "3" * x3 + "0"
#
#             while "00" not in s:
#                 s = s.replace("01", "210", 1)
#                 s = s.replace("02", "3101", 1)
#                 s = s.replace("03", "2012", 1)
#
#             print(s)


# s = "9" * 100 + "1" * 14 + "2" * 48
#
# while "999" in s or "22" in s:
#     if "999" in s:
#         s = s.replace("999", "12", )
#     else:
#         s = s.replace("22", "1", 1)
#
#     print(s.count("1"))


# s = "1" * 81
#
# while "11111" in s or "888" in s:
#     if "11111" in s:
#         s = s.replace("11111", "88", 1)
#     else:
#         s = s.replace("888", "8", 1)
#
#     print(s)


# s = "3" + "4" * 40 + "2" * 25 + "3"
#
# while "3" in s:
#     if "342" in s:
#         s = s.replace("342", "4123", 1)
#     elif "34" in s:
#         s = s.replace("34", "413", 1)
#     elif "32" in s:
#         s = s.replace("32", "13", 1)
#     elif "33" in s:
#         s = s.replace("33", "424", 1)
#
#
# print(sum(map(int, s)))


# s = "7" * 333
#
# while "66" in s or "77777" in s:
#     if "66" in s:
#         s = s.replace("66", "7", 1)
#     else:
#         s = s.replace("77777", "676676", 1)
#
# print(sum(map(int, s)))


# s = "8" * 83
#
# while "111" in s or "88888" in s:
#     if "111" in s:
#         s = s.replace("111", "88", 1)
#     else:
#         s = s.replace("88888", "8", 1)
#
# print(s)


# s = "9" * 81
#
# while "33333" in s or "999" in s:
#     if "33333" in s:
#         s = s.replace("33333", "99", 1)
#     else:
#         s = s.replace("999", "3", 1)
#
# print(s)


# s = "9" * 136
#
# while "22222" in s or "9999" in s:
#     if "22222" in s:
#         s = s.replace("22222", "99", 1)
#     else:
#         s = s.replace("9999", "2", 1)
#
# print(s)


# s = "9" * 134
#
# while "22222" in s or "9999" in s:
#     if "22222" in s:
#         s = s.replace("22222", "99", 1)
#     else:
#         s = s.replace("9999", "2", 1)
#
# print(s)


# s = 512 * "7"
#
# while "7777" in s or "1111" in s:
#     if "7777" in s:
#         s = s.replace("7777", "1", 1)
#     else:
#         s = s.replace("1111", "7", 1)
#
# print(s)


# s = "8" * 82
#
# while "1111" in s or "8888" in s:
#     if "1111" in s:
#         s = s.replace("1111", "8", 1)
#     else:
#         s = s.replace("8888", "11", 1)
#
# print(s)


# s = "1" * 84
#
# while "11111" in s:
#     s = s.replace("222", "1", 1)
#     s = s.replace("111", "2", 1)
#
# print(s)


# s = "8" * 82
#
# while "1111" in s or "8888" in s:
#     if "1111" in s:
#         s = s.replace("1111", "8", 1)
#     else:
#         s = s.replace("8888", "11", 1)
#
# print(s)


# s = "9" * 68
#
# while "22222" in s or "9999" in s:
#     if "22222" in s:
#         s = s.replace("22222", "99", 1)
#     else:
#         s = s.replace("9999", "29", 1)
#
# print(s)

# ms = 0
#
# for n in range(4, 10000):
#     s = "8" + "4" * n
#
#     if "11" in s or "444" in s or "8888" in s:
#         s = s.replace("11", "4", 1)
#         s = s.replace("444", "88", 1)
#         s = s.replace("8888", "1", 1)
#
#     sm = sum(map(int, s))
#     ms = max(ms, sm)
#
# print(ms)
