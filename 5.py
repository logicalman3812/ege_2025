# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if n % 2 == 0:
#         s += "01"
#     else:
#         s = "1" + s + "1"
#
#     r = int(s, 2)
#
#     if r > 156:
#         print(n)


# def f(n):
#     if n == 0:
#         return 0
#
#     result = np.base_repr(n, base=4)
#
#     return result


# for n in range(1, 1000, 2):
#     s = f(n)
#
#     if n % 3 == 0:
#         n = s[0] + s[1:-1] + "1"
#     else:
#         n = str(n % 3)
#
#     r = int(s, 2)
#     if r < 340:
#         print(r)

# res = []
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if n % 3 == 0:
#         s = s.replace('0', '11')
#     else:
#         s = s.replace('1', '10')
#
#     r = int(s, 2)
#     if r < 161:
#         res.append(r)
#
# print(max(res))


# res = []
#
# for n in range(1, 1000):
#     s = oct(n)[2:]
#
#     if (s.count('0') + s.count('2') + s.count('4') + s.count('6')) % 2 != 0:
#         s = s[-3:] + '46'
#     else:
#         s = oct((n % 8) * 5)[2:] + s
#
#     r = int(s, 8)
#
#     if n >= 80:
#         res.append(r)
#
# print(min(res))


# res = []
#
# for n in range(1, 50):
#     b = f"{n:b}"
#
#     if b.count('1') % 2 == 0:
#         b = '11' + b[2:] + '0'
#     else:
#         b = '10' + b[2:] + '1'
#
#     r = int(b, 2)
#
#     res.append(r)
#
# print(max(res))


# res = []
#
# for n in range(1000):
#     b = f"{n:b}"
#     b += f"{n % 4:b}"
#     r = int(b, 2)
#     res.append(r)


# res = []
#
#
# def f(n):
#     s = ''
#     while n > 0:
#         s = str(n % 7) + s
#         n //= 7
#     return s
#
#
# for n in range(1, 10000):
#     s = f(n)
#
#     if s.count("2") % 2 == 0:
#         s += "555"
#     else:
#         s = "1" + s
#     r = int(s, 7)
#     if r < 3799:
#         res.append(n)
#
# print(max(res))


# def f(n):
#     s = ''
#     while n > 0:
#         s += str(n % 3) + s
#         n //= 3
#     return s
#
#
# for n in range(1, 1000):
#     s = f(n)
#     if n % 2 == 0:
#         s = "1" + s + "00"
#     else:
#         # sum_digit = sum([int(symb) for symb in s])
#         sum_digits = sum(map(int, s))
#         s += f(sum_digit)
#
#     r = int(s, 3)
#     if r > 168:
#         print(n, r)


# res = []
#
# for n in range(1, 13):
#     b = f"{n:b}"
#
#     if n % 2 == 0:
#         b = "10" + b
#     else:
#         b = "1" + b + "01"
#
#     r = int(b, 2)
#     res.append(r)
#
#
# print(max(res))


# res = []
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if s.count('1') % 2 == 0:
#         s = "10" + s[2:] + "0"
#     else:
#         s = "11" + s[2:] + "1"
#     r = int(s, 2)
#
#     if n > 27:
#         res.append(r)
#
# print(min(res))


# res = []
#
# for n in range(1, 100):
#     s = f"{n:b}"
#     for i in range(2):
#         s += str(s.count("1") % 2)
#
#     r = int(s, 2)
#     if r > 75:
#         res.append(r)
#
# print(min(res))


# res = []
#
#
# for n in range(1, 13):
#     s = f"{n:b}"
#
#     if n % 2 == 0:
#         s = "10" + s
#     else:
#         s = "1" + s + "01"
#
#     r = int(s, 2)
#     res.append(r)
#
# print(max(res))


# res = []
#
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if s.count("1") % 2 == 0:
#         s = "10" + s[2:] + "0"
#     else:
#         s = "11" + s[2:] + "1"
#     r = int(s, 2)
#
#     if r > 50:
#         res.append(n)
#
#
# print(min(res))


# def f(n):
#     s = ''
#     while n > 0:
#         s = str(n % 3) + s
#         n //= 3
#     return s


# res = []
#
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if n % 3 == 0:
#         s += s[-2:]
#     else:
#         last = (n % 3)
#         s += bin(last * 3)[2:]
#
#     r = int(s, 2)
#
#     if r >= 195:
#         res.append(r)
#
#
# print(min(res))


# res = []
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if n % 2 == 0:
#         s = "10" + s
#     else:
#         s = "1" + s + "01"
#
#     r = int(s, 2)
#
#     if r > 516:
#         res.append(n)
#
#
# print(min(res))


# res = []
#
# def f(n):
#     s = ''
#
#     while n > 0:
#         s = str(n % 3) + s
#         n //= 3
#
#     return s
#
#
# for n in range(1, 1000):
#     s = f(n)
#
#     if n % 2 == 0:
#         s = "2" + s + f(int(s[-1]) * 2)
#     else:
#         s = f(int(s[0]) * 2) + s + "2"
#
#     r = int(s, 3)
#
#     if r > 100:
#         res.append(r)
#
#
# print(min(res))


# res = []
#
#
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
# for n in range(1, 1000):
#     s = f(n)
#
#     if n % 7 == 0:
#         s += s[-2:]
#     else:
#         s += f(int((n % 7) * 3))
#
#     r = int(s, 3)
#
#     if r > 369:
#         res.append(r)
#
# print(min(res))


# res = []
#
# for n in range(1, 13500):
#     s = f"{n:b}"
#
#     s += s[-1]
#     s += str(s.count("1") % 2)
#
#     r = int(s, 2)
#
#     if r < 13500:
#         res.append(r)
#
# print(max(res))


# res = []
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#     if s.count("1") % 2 == 0:
#         s += "1"
#     else:
#         s += "0"
#
#     if s.count("1") % 2 == 0:
#         s += "10"
#     else:
#         s += "01"
#
#     r = int(s, 2)
#
#     if r < 1000:
#         res.append(r)
#
#
# print(max(res))


# res = []
#
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if n % 3 == 0:
#         s = s.replace("0", "11")
#     else:
#         s = s.replace("1", "10")
#
#     r = int(s, 2)
#
#     if r < 161:
#         res.append(r)
#
#
# print(max(res))


# res = []
#
# for n in range(1, 1000):
#     s = oct(n)[2:]
#
#     if (s.count("0") + s.count("2") + s.count("4") + s.count("6")) % 2 != 0:
#         s = s[:-3] + "46"
#     else:
#         s = oct((n % 8) * 5)[2:] + s
#
#     r = int(s, 8)
#
#     if n > 80:
#         res.append(r)
#
# print(min(res))


# res = []
#
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if s.count("1") % 2 == 0:
#         s = "11" + s[2:] + "0"
#     else:
#         s = "10" + s[2:] + "1"
#     r = int(s, 2)
#
#     if n < 50:
#         res.append(r)
#
#
# print(max(res))


# def f(n):
#     s = ''
#
#     while n > 0:
#         s = str(n % 5) + s
#         n //= 5
#
#     return s
#
#
# res = []
#
# for n in range(1, 1000):
#     s = f(n)
#
#     if int(s[-1]) % 2 == 0:
#         s += "2"
#     else:
#         s = "2" + s + "3"
#
#     r = int(s, 5)
#
#     if r < 1000:
#         res.append(n)
#
#
# print(max(res))


# res = []
#
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     for i in range(2):
#         if n % 2 != 0 and s.count("1") % 2 != 0:
#             s = "1" + s
#         if n % 2 == 0 or s.count("1") % 2 == 0:
#             s += "0"
#         else:
#             s += "1"
#
#     if int(s, 2) < 100:
#         res.append(n)
#
#
# print(max(res))


# res = []
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if s.count("1") % 3 == 0:
#         s += s[2:]
#     else:
#         s = bin(s.count("1") * 3) + s
#
#     r = int(s, 2)
#
#     if r < 60:
#         res.append(n)
#
#
# print(max(res))


# res = []
#
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if n % 5 == 0:
#         s += s[:-3]
#     else:
#         s = bin((n % 5) * 5)[2:] + s
#
#     r = int(s, 2)
#
#     if r > 512:
#         res.append(n)
#
#
# print(min(res))


# def f(n):
#     s = ''
#
#     while n > 0:
#         s = str(n % 4) + s
#         n //= 4
#
#     return s
#
#
# res = []
#
# for n in range(1, 100):
#     s = f(n)
#     s = str(n % 2) + s + str(n % 3)
#     r = int(s, 4)
#
#     if r < 100:
#         print(r)


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
# res = []
#
# for n in range(1, 1000):
#     s = f(n)
#
#     if n % 7 == 0:
#         s += s[-2:]
#
#     else:
#         s += f((n % 7) * 2)
#
#     r = int(s, 7)
#
#     if r < 220:
#         res.append(n)
#
# print(max(res))


# res = []
#
# for n in range(1, 10000):
#     s = oct(n)[2:]
#
#     if n % 2 != 0:
#         s += "00"
#     else:
#         s += "10"
#
#     r = int(s, 8)
#
#     if r >= 100:
#         res.append(r)
#
# print(len(res))


# res = []
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if n % 2 == 0:
#         s = "1" + s + "0"
#     else:
#         s = "11" + s + "11"
#
#     r = int(s, 2)
#
#     if r > 225:
#         res.append(r)
#
# print(min(res))


# res = []
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     for i in range(2):
#         s += str(s.count("1") % 2)
#
#     if int(s, 2) > 77:
#         res.append(n)
#
# print(min(res))


# res = []
#
# for b in range(1, 1000):
#     s = f"{b:b}"
#     for i in range(2):
#         if s.count("1") % 2 == 0:
#             s += "0"
#         else:
#             s += "1"
#
#     if int(s, 2) > 80:
#         res.append(int(s, 2))
#
# print(min(res))


# for n in range(100, 2, -1):
#     s = f"{n:b}"
#
#     for i in range(2):
#         if s.count("0") == s.count("1"):
#             s += s[-1]
#         else:
#             if s.count("1") < s.count("0"):
#                 s += "1"
#             else:
#                 s += "0"
#
#     r = int(s, 2)
#
#     if r % 4 == 0 and r % 8 != 0:
#         print(r)
#         break


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
# for n in range(1, 1000):
#     s = f(n)
#
#     if n % 2 == 0:
#         s = "1" + s + "00"
#     else:
#         s += f(sum(map(int, s)))
#
#     r = int(s, 3)
#
#     if r > 168:
#         print(n)
#         break


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
# for n in range(1, 1000):
#     s = f(n)
#
#     digits_sum = sum(map(int, s))
#
#     print(type(digits_sum))
#
#     if digits_sum % 4 == 0:
#         s = "1" + s
#         s = s[:-2]
#     else:
#         s += f(digits_sum) % 4 * 3
#
#     r = int(s, 3)
#
#     if r > 353:
#         print(r)
#         break


# for n in range(1, 10000):
#     s = f"{n:b}"
#
#     k1 = sum(s[x] == "1" for x in range(1, len(s), 2))
#     k2 = sum(s[x] == "0" for x in range(0, len(s), 2))
#
#     if abs(k1 - k2) == 5:
#         print(n)
#         break


# for n in range(1000, 1, -1):
#     s = f"{n:b}"
#
#     if n % 2 == 0:
#         s = "10" + s
#     else:
#         s = "1" + s + "01"
#
#     r = int(s, 2)
#
#     if n < 12:
#         print(r)


# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     for i in range(2):
#         s += str(s.count("1") % 2)
#
#     r = int(s, 2)
#
#     if r > 123:
#         print(r)
#         break


# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     for i in range(2):
#         s += str(s.count("1") % 2)
#
#     r = int(s, 2)
#
#     if r > 75:
#         print(r)
#         break


# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if s.count("1") % 2 == 0:
#         s = "10" + s[2:] + "0"
#     else:
#         s = "11" + s[2:] + "1"
#
#     r = int(s, 2)
#
#     print(r, n)


# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if len(s) % 2 == 0:
#         s = s[:len(s) // 2] + "000" + s[len(s) // 2:]
#     else:
#         s = "1" + s + "01"
#
#     r = int(s, 2)
#
#     if r > 100:
#         print(n)
#         break


# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if n % 2 == 0:
#         s = "10" + s
#     else:
#         s = "1" + s + "01"
#
#     r = int(s, 2)
#     if r > 516:
#         print(n)
#         break


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
# for n in range(1000, 1, -1):
#     s = f(n)
#
#     if s[-1] in "024":
#         s += "2"
#     else:
#         s = "2" + s + "3"
#
#     r = int(s, 5)
#
#     if r < 1000:
#         print(n)
#         break


# def f(n):
#     s = ""
#
#     while n > 0:
#         s = str(n % 6) + s
#         n //= 6
#
#     return s
#     
#
# for n in range(1, 1000):
#     s = f(n)
#     
#     if n % 3 == 0:
#         s += f(s)[:2]
#     else:
#
#
#     r = int(s, 2)
#
#     if r > 680:
#         print(r)
#         break


# for n in range(1000, 1, -1):
#     s = f"{n:b}"
#
#     if n % 2 == 0:
#         s = "10" + s
#     else:
#         s = "1" + s + "01"
#
#     r = int(s, 2)
#
#     if n < 12:
#         print(r)
#         break


# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if s.count("1") % 2 == 0:
#         s += "11"
#     else:
#         s += "01"
#
#     r = int(s, 2)
#
#     if r > 61:
#         print(r)
#         break


# res = []
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if s.count("1") % 2 == 0:
#         s = "10" + s[2:] + "0"
#     else:
#         s = "11" + s[2:] + "1"
#
#     r = int(s, 2)
#
#     if n > 27:
#         res.append(r)
#
# print(min(res))


# res = []
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     for i in range(2):
#         if s.count("1") % 2 == 0:
#             s += "0"
#         else:
#             s += "1"
#
#     r = int(s, 2)
#
#     if r > 75:
#         res.append(r)
#     
# print(min(res))


# for n in range(1000, 1, -1):
#     s = f"{n:b}"
#
#     if n % 2 != 0:
#         s = "1" + s + "01"
#     else:
#         s = "10" + s
#
#     r = int(s, 2)
#
#     if n < 12:
#         print(r)
#         break


# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if s.count("1") % 2 == 0:
#         s = "10" + s[2:] + "0"
#     else:
#         s = "11" + s[2:] + "1"
#
#     r = int(s, 2)
#
#     if r > 50:
#         print(n)
#         break


# res = []
#
# for n in range(1, 1010):
#     s = f"{n:b}"
#
#     if n % 3 == 0:
#         s += s[-2:]
#     else:
#         s += bin((n % 3) * 3)[2:]
#
#     r = int(s, 2)
#
#     if r >= 195:
#         res.append(r)
#
# print(min(res))


# res = []
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if n % 2 == 0:
#         s = "10" + s
#     else:
#         s = "1" + s + "01"
#
#     r = int(s, 2)
#
#     if r > 516:
#         print(n)
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
# res = []
#
# for n in range(1, 1000):
#     s = f(n)
#
#     if n % 2 == 0:
#         s += "2" + s + f(int(s[-1]) * 2)
#     else:
#         s = f(int(s[0]) * 2) + s + "2" 
#
#     r = int(s, 3)
#
#     if r > 100:
#         res.append(r)
#
# print(min(res))


# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if n % 2 == 0:
#         s = "10" + s
#     else:
#         s = "1" + s + "01"
#
#     r = int(s, 2)
#
#     if r > 516:
#         print(n)
#         break


# res = []
#
# for n in range(1000, 1, -1):
#     s = f"{n:b}"
#
#     if n % 3 == 0:
#         s = s.replace("0", "11")
#     else:
#         s = s.replace("1", "10")
#
#     r = int(s, 2)
#
#     if r < 161:
#         print(r)


# res = []
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if s.count("1") % 2 == 0:
#         s += "11"
#     else:
#         s += "01"
#
#     r = int(s, 2)
#
#     if r > 61:
#         res.append(r)
#
# print(min(res))


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
# res = []
#
# for n in range(1, 1000):
#     s = f(n)
#
#     if n % 3 == 0:
#         s += s[-2:]
#     else:
#         s += f((n % 3) * 5)
#
#     r = int(s, 3)
#
#     if r > 133:
#         res.append(r)
#
# print(min(res))


# res = []
#
# for n in range(1, 1000):
#     s = f"{n:b}"
#
#     if n % 3 == 0:
#         s += s[:2]
#     else:
#         s += bin((n % 3) * 3)[2:]
#
#     r = int(s, 2)
#
#     if r < 195:
#         res.append(r)
#
# print(min(res))


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
# for n in range(1, 1000):
#     s = f(n)
#
#     if s[-1] in "24":
#         s += "2"
#     else:
#         s = "2" + s + "3"
#
#     r = int(s, 5)
#
#     if r < 1000:
#         print(n)


# def f(n):
#     s = ""
#
#     while n > 0:
#         s = str(n % 9) + s
#         n //= 9
#     return s
#
#
# for n in range(1, 10000):
#     s = f(n)
#
#     for i in range(4):
#         if s.count("5") == s.count("7"):
#             s += s[-1]
#         else:
#             if s.count("5") > s.count("7"):
#                 s += "5"
#             else:
#                 s += "7"
#
#     r = hex(int(s, 9))[2:].upper()
#
#     if "BAC" in r:
#         print(n, r)


def f(n):
    s = ""

    while n > 0:
        s = str(n % 3) + s
        n //= 3

    return s
#
#
# for n in range(1, 1000):
#     s = f(n)
#
    # if sum(map(int(s, 2))) % 2 == 0:


s = f(123)
print(sum(map(int(s, 2))))
