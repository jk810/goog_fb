def answer(M, F):
    M = int(M)
    F = int(F)
    n_gens = 0

    while M > 0 and F > 0:
        if M == F:
            break
        elif M > F:
            mod = M / F
            M -= F * mod
            n_gens += mod
        else:
            mod = F / M
            F -= M * mod
            n_gens += mod

    # Possible results will end in [M, F] = [1, 0] or [0, 1]
    if M > 1 or F > 1:
        return "impossible"
    else:
        return str(n_gens - 1)

print answer(2, 4)
