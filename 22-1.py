for i in range(1000):
    x = i
    a = 0 
    b = 1
    while x > 0: 
        a = a + 1
        b = b*(x % 10)
        x = x // 10
    #print(a)
    #print(b)
    if a == 3 and b == 15:
        print(i)