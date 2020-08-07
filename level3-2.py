def xor_zerorange(c):       # compute the xor of all integers in range(c)
    if c % 4 == 0:
        return 0
    elif c % 4 == 1:
        return c - 1
    elif c % 4 == 2:
        return 1
    else:
        return c

def xor_range(a, b):        # compute the xor of integers in range (a, b)
    aa = xor_zerorange(a)
    bb = xor_zerorange(b)
    return aa^bb

def answer(start, length):
    xor_rows = []

    for i in range(length):
        a = start + i*length
        b = start + i*length + length - i
        xor_rows.append(xor_range(a, b))

    return reduce(lambda i, j: i^j, xor_rows)

print answer(17, 4)
