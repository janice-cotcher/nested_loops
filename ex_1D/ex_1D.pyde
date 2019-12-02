size(600, 600)


def oned(n_squares, square_size, gap_square):
    for square in range(n_squares):
        if square != gap_square:
            square_x = square * square_size
            rect(square_x, 0, square_size, square_size)


oned(10, 50, 5)
