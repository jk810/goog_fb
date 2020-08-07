def answer(x, y):

    x_id = 0            # x_id is the x value at y = 1
    for i in range(1, x + 1):
        x_id += i

    n_ysteps = y - 1    # number of steps to go vertically

    ID = x_id
    for j in range(x, x + n_ysteps):
        ID += j

    return str(ID)
