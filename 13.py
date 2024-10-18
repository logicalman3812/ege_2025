from ipaddress import *


# k = 0
# net = ip_network("192.168.32.160/255.255.255.240", 0)
#
# for ip in net:
#     if format(ip, "b").count("1") % 2 == 0:
#         k += 1
#
# print(k)


# for i in range(0, 33):
#     net = ip_network(f"145.192.94.230/{i}", 0)
#     
#     if str(net.network_address) == "145.192.80.0":
#         print(net.netmask)


# k = 0
# net = ip_network("172.16.168.0/255.255.248.0")
#
# for ip in net:
#     b = f"{ip:b}"
#
#     if b.count("1") % 5 != 0:
#         k += 1
#
# print(k)
