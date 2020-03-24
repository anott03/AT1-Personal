def generate_triangle(degree, prev_row=None):
    if prev_row is None:
        row = [0 for _ in range(degree)]
        row.insert(0, 1)
        if degree > 1:
            return [row] + generate_triangle(degree-1, row)
        return [row]
    # will only happen if prev_row is not None
    row = []
    row.insert(0, 1)
    for i in range(len(prev_row)-1):
        row.append(prev_row[i] + prev_row[i + 1])
    row.append(prev_row[len(prev_row)-2])

    if degree > 1:
        return [row] + generate_triangle(degree-1, row)
    return [row]

def triangle(degree):
    for row in generate_triangle(degree):
        out = ""
        for num in row:
            if num != 0:
                out += str(num) + " "
            else:
                out += "  "
        print(out)

triangle(5)
