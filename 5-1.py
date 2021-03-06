def decto(x, base):
    s = ''
    while x > 0:
        s = str(x % base) + s
        x //= base
    return s

def change(n):
    s = decto(n, 2)
    if n % 2 == 0:
        s = s + '01'
    else:
        s = s + '10'
    n = int(s, base=2)
    return n

# print(s)
# print(change(n))

for i in range(2, 1000):
    if change(i) >= 81:
        print(change(i))
