from math import cos, sin, radians

def calculate_trajectory(vitesse_initiale, angle_degres, size,  position_initiale=(0, 0)):

    # Constantes
    g = 9.81
    dt = 0.1  # Intervalle de temps entre chaque point
    SCREEN_WIDTH = size[0]
    SCREEN_HEIGHT = size[1]
    
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

    while calcul_positions:
        x = x0 + vx * t
        y = y0 + vy * t + (g * t **2) / 2
        
        
        # Vérifier si le point est dans l'écran
        if x < 0 or x > SCREEN_WIDTH or y < 0 or y > SCREEN_HEIGHT:
            calcul_positions = False
        else: 
            positions_x.append(x)
            positions_y.append(y)
            t += dt
        
        
    
    return positions_x, positions_y
