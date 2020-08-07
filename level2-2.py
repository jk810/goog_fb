def answer(total_lambs):

    def generous(total_lambs):
        rem_lambs = 0

        if total_lambs == 1:
            gen = [1]
        elif total_lambs == 2:
            gen = [1, 1]
        else:
            gen = [1, 2]
            sum_previous_two = sum(gen[-2:])
            rem_lambs = total_lambs - sum_previous_two

            while 2*gen[-1] < rem_lambs:

                if 2*gen[-1] < rem_lambs:
                    gen.append(2*gen[-1])
                    rem_lambs -= gen[-1]
                sum_previous_two = sum(gen[-2:])

            if  sum_previous_two <= rem_lambs:
                gen.append(rem_lambs)
                rem_lambs -= rem_lambs

        return len(gen)

    def stingy(total_lambs):
        rem_lambs = 0

        if total_lambs == 1:
            stingy = [1]
        elif total_lambs == 2:
            stingy = [1, 1]
        else:
            stingy = [1, 1]
            sum_previous_two = sum(stingy[-2:])
            rem_lambs = total_lambs - sum_previous_two

            while sum_previous_two <= rem_lambs:
                sum_previous_two = sum(stingy[-2:])

                if sum_previous_two <= rem_lambs:
                    stingy.append(sum_previous_two)
                    rem_lambs -= sum_previous_two
        return len(stingy)

    return abs(generous(total_lambs) - stingy(total_lambs))

print answer(143)
