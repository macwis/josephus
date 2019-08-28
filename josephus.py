def msb(n):
    p = 0
    while n != 0:
        p += 1
        n = n >> 1
    return p


def sit2survive(n):
    p = msb(n)
    print("msb = ", bin(p), p)
    j = 1 << (p - 1)
    print("j = ", bin(j), j)
    n = n ^ j
    print("n XOR j = ", bin(n), n)
    n = n << 1
    print("n shifted by 1 right = ", bin(n), n)
    n = n | 1
    print("n OR 1 = ", bin(n), n)
    return n


n = 41
print("n = ", bin(n))

print("safe bet = ", sit2survive(n))
