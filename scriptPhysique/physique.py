from math import cos, sin, radians

def calculate_trajectory(vitesse_initiale, angle_degres, position_initiale=(0, 0)):
    """
    Calcule les points de la trajectoire d'un projectile jusqu'à ce qu'il sorte de l'écran.
    
    Args:
        vitesse_initiale (float): Vitesse initiale en m/s
        angle_degres (float): Angle de tir en degrés
        position_initiale (tuple): Position initiale (x0, y0)
    
    Returns:
        list, list: Listes des coordonnées x et y de la trajectoire
    """
    # Constantes
    g = 9.81
    dt = 0.1  # Intervalle de temps entre chaque point
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 1080
    
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
        y = y0 + vy * t + (g * t * t) / 2
        
        
        # Vérifier si le point est dans l'écran
        if x < 0 or x > SCREEN_WIDTH or y < 0 or y > SCREEN_HEIGHT:
            calcul_positions = False
        else: 
            positions_x.append(x)
            positions_y.append(y)
            t += dt
        
        
    
    return positions_x, positions_y
