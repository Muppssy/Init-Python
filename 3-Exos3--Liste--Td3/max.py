def maxi():
    l = [1, 5, 4, 7, 87, 9, 6, 5, 4]
    m = 0
    for i in l:
        if(m < i):
            m = i
    print("le max est: ", m)

maxi()