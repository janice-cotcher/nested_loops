def twoa(portal_activated, portal_visible, draw_effects):
    if portal_activated:
        if portal_visible:
            if draw_effects:
                fill(225, 255, 255)
            else:
                fill(0, 0, 0)
            ellipse(50, 50, 25, 50)


twoa(True, True, True)
                 
