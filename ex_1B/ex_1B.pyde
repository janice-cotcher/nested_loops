def oneb(n_rows, n_columns, diameter):
    for row in range(n_rows):
        for col in range(n_columns):
            # current circle's centre coordinates
            circle_x = row * diameter + diameter/2
            circle_y = col * diameter + diameter/2
            # draw circle
            ellipse(circle_x, circle_y, diameter, diameter)


oneb(3, 6, 15)
