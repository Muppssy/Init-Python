def tchin(t):
    if t == 2:
        return 1
    else:
        return tchin(t-1)+t-1


print(tchin(7))

# nombre de tchin
# 1+2+3+4+5+6+7
# 2 = 1 n-1
# 3 = 3
# 4 = 6
# 5 = 10
# 6 = 15
# 7 = 21
