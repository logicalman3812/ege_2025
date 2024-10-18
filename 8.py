from itertools import permutations, product


# a = list(product("БЕНРСТЬЯ", repeat=5))
# k = 0
#
# for x in a:
#     k += 1
#
#     if k % 2 == 0 and x[0] == "Р" and not "Ь" in x:
#         print(k)


# a = list(product("АЙЛМ", repeat=5))
# k = 0
#
# for x in a:
#     k += 1
#     x = "".join(x)
#
#     if x.count("М") == 0 and x.count("Л") == 0 and "ЙЙ" not in x:
#         print(k)


# k = 0
#
# for x in product("КОСУФ", repeat=5):
#     k += 1
#     x = "".join(x)
#
#     if x.count("Ф") == 0 and x.count("У") == 2:
#         print(k)


# k = 0
#
# for x in product("АПРСУ", repeat=5):
#     k += 1
#     x = "".join(x)
#
#     if x.count("У") == 1 and "АА" not in x:
#         print(k)


# k = 0
#
# for x in product("АПРСУ", repeat=5):
#     k += 1
#     x = "".join(x)
#
#     if x.count("У") <= 1 and "АА" not in x:
#         print(k)
#         break


# k = 0
#
# for x in product(sorted("МИЗАНТРОП"), repeat=5):
#     k += 1
#     x = "".join(x)
#
#     if k % 2 == 0 and x[0] == "Н" and x.count("Р") == 2:
#         print(k)


# k = 0
#
# for x in product(sorted(set("КАЛЕЙДОСКОП"), reverse=1), repeat=6):
#     x = "".join(x)
#
#     if k % 2 == 0 and x[0] == "К" and x.count("Й") >= 2 and "С" not in x and "Е" not in x:
#         print(k)
#
#     k += 1


# k = 0
#
# for x in product(sorted("ГИРЛЯНДА"), repeat=6):
#     k += 1
#     
#     if k % 2 == 0 and x[0] != "Я" and x.count("Д") == 3:
#         print(k)


# k = 0
#
# for x in product(sorted(set("ГОНДУБШ")), repeat=6):
#     k += 1
#
#     if k % 2 != 0 and x[0] != "Б" and x.count("Н") >= 2 and "У" not in x:
#         print(k)


# k = 0
#
# for x in product(sorted("БМЮРН"), repeat=6):
#     k += 1
#
#     if k % 2 != 0 and x[0] != "М" and x.count("Р") >= 2 and "Ю" not in x:
#         print(k)


# k = a = 0
#
# for x in product(sorted("АОЖПЮЗ"), repeat=6):
#     k += 1
#
#     if k % 2 == 0 and x[0] == "А" and x.count("З") >= 2:
#         a += 1
#         print(a)


# k = 0
#
# for x in product(sorted("ЩРЮИ"), repeat=5):
#     k += 1
#
#     if x[0] == "Щ" and x[-1] == "И":
#         print(k)


# k = 0
#
# for x in product(sorted("ДОСЖ"), repeat=6):
#     k += 1
#
#     if x[0] == "Ж" and x[1] == "С":
#         print(k)
#         break


# k = 0
#
# for x in product(sorted("ЩЭДСР"), repeat=4):
#     k += 1
#     x = "".join(x)
#
#     if x == "ЩДЩД":
#         print(k)


# k = 0
#
# for x in product(sorted("ПАРУС"), repeat=5):
#     k += 1
#     x = "".join(x)
#
#     if x.count("У") >= 1 and "АА" not in x:
#         print(k)

# k = 0
#
# for x in product(sorted("СЕНТЯБРЬ"), repeat=5):
#     k += 1
#
#     if k % 2 == 0 and x[0] == "Р" and "Ь" not in x:
#         print(k)


# k = 0
#
# for x in product(sorted("КОМПЬЮТЕР"), repeat=5):
#     k += 1
#
#     if k % 2 != 0 and x[0] != "Ь" and x.count("К") == 2:
#         print(k)


# k = 0
#
# for i, x in enumerate(product(sorted("КЕГЭ2023"), repeat=4), start=1):
#
#     if x[0].isdigit() and all(x[i] != x[i + 1]):
#         print(k)
