rsrp_list = [-91.5, -108.1, -86.2, -103.3, -97.4]
print(rsrp_list[0])
print(rsrp_list[1])
print(rsrp_list[-1])
print(len(rsrp_list))
avg = sum(rsrp_list) / len(rsrp_list)
print(round(avg, 1))
r =int(input())
print(rsrp_list[r])

