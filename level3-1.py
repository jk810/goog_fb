def answer(n):
    n = int(n)

    n_steps = 0

    while n != 1:
        if n & 1 == 0:  # if its divisible by 2, divide by 2
            n >>= 1
        #
        elif n == 3  or ((n + 1) & n) > ((n - 1) & (n - 2)):
            n -= 1
        else:
            n += 1
        n_steps += 1

    return n_steps

print answer(10)
