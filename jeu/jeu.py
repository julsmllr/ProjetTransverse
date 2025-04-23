# ---------------------- IMPORTATIONS ---------------------- # 

import pygame
import sys
import os
import random

# Pour avoir le script Physique (Essayer de simplifier ça)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from scriptPhysique.physique import calculate_trajectory


# ---------------------- PROGRAMME ---------------------- # 

# Initialisation de Pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 640, 800 
MAX_ESSAIS = 5
# Variables de tir prédéfinies
POWER = 100  
THETA = 80  

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
BROWN = (139, 69, 19)

# Fenetre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Basket 2D")

# images (bg, ball, panier)
background = pygame.image.load("assets/img/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
ball_img = pygame.image.load("assets/img/basketball.png")
ball_img = pygame.transform.scale(ball_img, (50, 50))
hoop_img = pygame.image.load("assets/img/hoop.png")
hoop_img = pygame.transform.scale(hoop_img, (100, 50))


# Position joueur + panier
pos_joueur = (320, HEIGHT - 100)
pos_panier = [random.randint(100, WIDTH - 100), random.randint(200, HEIGHT - 250)]


# Variables de jeu
global ball_pos, ball_launched, trajectory_points, current_point_index, essais, score, hoop_radius

# Liste de position de la balle
pos_balle = list(pos_joueur)




def reset_ball(pos_balle, pos_joueur, essais, pos_panier):
    pos_balle = list(pos_joueur)
    essais = 0
    pos_panier = [random.randint(100, WIDTH - 100), random.randint(200, HEIGHT - 250)]




def draw_trajectory_preview(pos_x, pos_y):
    pygame.draw.circle(screen, RED, (pos_x[0], pos_y[0]), 50)
    pygame.draw.circle(screen, RED, (pos_x[1], pos_y[1]), 50)
    pygame.draw.circle(screen, RED, (pos_x[2], pos_y[2]), 50)


def draw_game(essais, score, pos_balle, pos_panier):
    screen.blit(background, (0, 0))

    screen.blit(hoop_img, (pos_panier[0], pos_panier[1]))
    screen.blit(ball_img, (pos_balle[0]-25, pos_balle[1]-25))

    # Dessiner la hitbox du panier
    pygame.draw.rect(screen, RED, (pos_panier[0], pos_panier[1]-50, 100, 50), 2)
    pygame.draw.circle(screen, BLACK, (pos_balle[0], pos_balle[1]), 5)


    # Afficher le score et les tentatives
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, BLACK)
    essais_text = font.render(f'Tentatives: {essais}/{MAX_ESSAIS}', True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(essais_text, (10, 50))
    pygame.display.flip() #MAJ Fenetre


def verif_coordonate(pos_balle_x, pos_balle_y, pos_panier, essais, score):
    indice_position = 0
    panier_touche = False
    while indice_position < len(pos_balle_x) and not panier_touche:
        if pos_panier[0]+25 < pos_balle_x[indice_position] <pos_panier[0]+75:
            print("Dans x")
            if (pos_panier[1]-50 < pos_balle_y[indice_position] <pos_panier[1]) and (pos_balle_y[indice_position-1] > pos_balle_y[indice_position]):
                
                panier_touche = True
                score += 1  
                reset_ball(pos_balle, pos_joueur, essais, pos_panier)

            else:
                draw_game(essais, score, (pos_balle_x[indice_position], pos_balle_y[indice_position]), pos_panier)
                print("Panier Raté")
                indice_position += 1
        else: 
            draw_game(essais, score, (pos_balle_x[indice_position], pos_balle_y[indice_position]), pos_panier)
            print("Panier Raté")
            indice_position += 1

    if not panier_touche:
        essais += 1 

def main():
    clock = pygame.time.Clock()
    essais = 0
    score = 0
    print(pos_joueur, pos_panier)

    while essais < MAX_ESSAIS:  
        print("Score :", score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Calcul de la trajectoire complète
                    verif_coordonate(pos_balle_x, pos_balle_y, pos_panier, essais, score)



        draw_game(essais, score, pos_joueur, pos_panier)
        pos_balle_x, pos_balle_y = calculate_trajectory(POWER, THETA, pos_joueur)
        draw_trajectory_preview(pos_balle_x[:2], pos_balle_y[:2])



        clock.tick(60) #Max fps

    pygame.quit()

if __name__ == "__main__":
    main()
