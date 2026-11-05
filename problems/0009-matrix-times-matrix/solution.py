def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]|int:

    if(len(a[0]) != len(b)):
        return -1
    else:
        c: list[list[int|float]] = []
        for i in range(len(a)):
            row = a[i]
            c_row = []
            for j in range(len(b[0])):
                column = [x[j] for x in b]
                cur_sum = sum([row[l] * column[l] for l in range(len(b))])
                c_row.append(cur_sum)
            c.append(c_row)

        return c
