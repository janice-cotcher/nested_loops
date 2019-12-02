size(100, 200)


def booth_status(row, col):
    a = "Unavailable"
    return a


def twoc(row, col):
    for row in range(row):
        for column in range(col):
            if booth_status(row, col) == "Occupied":
                fill(255, 0, 0)
            elif booth_status(row, col) == "Open":
                fill(0, 255, 0)
            elif booth_status(row, col) == "Unavailable":
                fill(200, 200, 200)
            x = 20 * col + 10
            y = 20 * row + 10
            rect(x, y, 15, 15)


twoc(8, 4)
