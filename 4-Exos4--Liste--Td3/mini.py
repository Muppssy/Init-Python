def mini():
    l = [1, 5, 4, 7, 87, 9, 6, 5, 4]
    m = l[0]
    for i in l:
        if(m > i):
            m = i
    print("le min est: ", m)


mini()
