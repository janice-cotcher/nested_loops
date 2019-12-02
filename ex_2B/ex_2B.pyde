size(600, 600)


def twob(n_rows, n_columns, n_inner):
    for row in range(n_rows):
        for column in range(n_columns):
            for d in range(n_inner):
                x = column * 30 + 15
                y = row * 30 + 15
                diameter = 30 - d * 8
                ellipse(x, y, diameter, diameter)


twob(5, 6, 3)
