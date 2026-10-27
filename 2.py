rsrp_list = [-91.5, -108.1, -86.2, -103.3, -110.4]
weak = 0
for v in rsrp_list:
    if v < -105:
        print(v, "zeif")
        weak = weak + 1
    else:
        print(v, "normal")
    print("zeif olcme sayi:", weak)
