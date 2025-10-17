def finobachchi(n=10, m=1):
    a, b = 0, 1
    list_finobachchi = []
    for x in range(n):
        a, b = b, a + b
        list_finobachchi.append(a)
    if m in list_finobachchi:
        return True
    else:
        return False
