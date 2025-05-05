from math import cos, sin, radians, atan2, degrees

def calculate_trajectory(vitesse_initiale, angle_degres, size, position_initiale=(0, 0)):
    # Constantes
    g = 9.81
    dt = 0.15  # Intervalle de temps entre chaque point
    SCREEN_WIDTH = size[0]
    SCREEN_HEIGHT = size[1]
    REBONDS_MAX = 1
    POURCENTS_REBOND = 0.5
    # Conversion en radians
    angle_rad = radians(angle_degres)

    # Position initiale
    x0, y0 = position_initiale

    # Composantes de la vitesse initiale
    vx = vitesse_initiale * cos(angle_rad)
    vy = -vitesse_initiale * sin(angle_rad)  # Négatif car l'axe y est inversé dans Pygame

    positions_x = []
    positions_y = []

    # Calcul des positions
    t = 0
    calcul_positions = True
    rebond = 0

    while calcul_positions:
        x = x0 + vx * t
        y = y0 + vy * t + (g * t ** 2) / 2

        # Vérifier si le point est dans l'écran
        if not (0 <= y <= SCREEN_HEIGHT):
            calcul_positions = False
        elif not (0 <= x <= SCREEN_WIDTH) and rebond < REBONDS_MAX:
            rebond += 1
            dx = vx
            dy = g*t+vy
            new_angle = degrees(atan2(dy,dx))
            new_vitesse = 0

            new_angle = -radians(180 - new_angle)
            vx = vitesse_initiale*POURCENTS_REBOND * cos(new_angle)
            vy = -vitesse_initiale*POURCENTS_REBOND * sin(new_angle)

            if x > SCREEN_WIDTH:
                x0 = SCREEN_WIDTH
            elif x < 0:
                x0 = 0

            y0 = positions_y[-1]
            t = 0
        else:
            positions_x.append(x)
            positions_y.append(y)
            t += dt
        if len(positions_x) > 10000:
            print("Trop Lourd")
            return positions_x, positions_y

    return positions_x, positions_y
