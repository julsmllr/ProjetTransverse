from math import cos, sin, radians, atan, degrees, sqrt

def calculate_trajectory(vitesse_initiale, angle_degres, size, position_initiale=(0, 0)):
    # Constantes
    g = 9.81
    dt = 0.05  # Intervalle de temps entre chaque point
    SCREEN_WIDTH = size[0]
    SCREEN_HEIGHT = size[1]
    REBONDS_MAX = 1
    POURCENTS_REBOND = 0.7
    POSITION_REBOND = []
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
    rebond = True

    while calcul_positions:
        x = x0 + vx * t
        y = y0 + vy * t + (g * t ** 2) / 2

        # Vérifier si le point est dans l'écran
        if not (y <= SCREEN_HEIGHT):
            calcul_positions = False
        elif not (0 <= x <= SCREEN_WIDTH) and rebond:
            rebond = False
            POSITION_REBOND.append((x, y))
            dx = vx
            dy = g*t+vy
            new_angle = calculNouvelAngle(dx, dy)

            new_vitesse = sqrt((positions_x[-1]- positions_x[-10])**2 + (positions_y[-1]- positions_y[-10])**2)
            new_angle = -radians(180 - new_angle)
            vx = new_vitesse*POURCENTS_REBOND * cos(new_angle)
            vy = -new_vitesse*POURCENTS_REBOND * sin(new_angle)

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
            if (rebond == False):
                rebond = True

    return positions_x, positions_y, POSITION_REBOND


def calculNouvelAngle(dx, dy):
    if dx == 0:
        if dy > 0:
            new_angle = 90
        else:
            new_angle = -90
    else:
        new_angle = degrees(atan(dy / dx))


        if dx < 0:
            if dy >= 0:
                new_angle += 180
            else:
                new_angle -= 180
    return new_angle
