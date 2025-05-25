# ---------------------- IMPORTATIONS ---------------------- # 

import pygame
import sys
import os
import random
from gestionSon import *


# Pour avoir le script Physique (Essayer de simplifier ça)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from scriptPhysique.physique import calculate_trajectory


# ---------------------- PROGRAMME ---------------------- # 

class JeuBasket:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        initialiser_sons()
        jouer_musique_fond(volume=0.1 )
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("../assets/fonts/Helvetica.ttf", 36)


        self.changes = True

        # Variables
        self.width = 1920
        self.height = 1080
        self.power = 90
        self.angle = 90
        self.essais = 0
        self.max_essais = 15
        self.score = 0
        self.pos_joueur = (self.width/2, self.height - 100)
        self.pos_panier = [random.randint(100, self.width - 100), random.randint(200, self.height - 250)]
        self.ballonStatus = False

        # Ecrans 
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)      
        pygame.display.set_caption("Jeu de Basket 2D")

    def chargementTextureJeu(self):
        self.background = pygame.image.load("../assets/img/background.png")
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.ball_img = pygame.image.load("../assets/img/basketball.png")
        self.ball_img = pygame.transform.scale(self.ball_img, (50, 50))
        self.hoop_img = pygame.image.load("../assets/img/hoop.png")
        self.hoop_img = pygame.transform.scale(self.hoop_img, (150, 250))

    # Set et Get
    def setPower(self, power):
        self.power = power
    
    def getPower(self):
        return self.power
    
    def setAnglePlus(self ):
        if self.angle < 180:
            self.angle += 0.5

    def setAngleMoins(self):
        if self.angle > 0:
            self.angle -= 0.5

    def getAngle(self):
        return self.angle
    
    # Méthodes liées aux coordonnées
    def dessinerLancer(self, pos_balle_x, pos_balle_y, pos_panier, pos_rebond):
        indice_position = 0
        panier_touche = False 
        while indice_position < len(pos_balle_x) and not panier_touche:
            if len(pos_rebond) > 0:
                if (pos_rebond[0][0]-5, pos_rebond[0][1]-5) <= (pos_balle_x[indice_position], pos_balle_y[indice_position]) <= (pos_rebond[0][0]+5, pos_rebond[0][1]+5):
                    jouer_son_rebond()
                    if len(pos_rebond) > 0:
                        pos_rebond.pop(0)

            if self.verifCoordonnes(pos_balle_x, pos_balle_y, pos_panier, indice_position):
                    panier_touche = True
                    jouer_son_panier()
                    self.score += 1
                    pos_panier = self.resetBall(pos_panier)


            else:
                    self.drawGame((pos_balle_x[indice_position], pos_balle_y[indice_position]), pos_panier)
                    indice_position += 1

        if not panier_touche:
            self.essais += 1
            pos_panier = self.resetBall(pos_panier)
        return pos_panier

    def verifCoordonnes(self, pos_balle_x, pos_balle_y, pos_panier, indice_position):
        if pos_panier[0]+25 < pos_balle_x[indice_position] <pos_panier[0]+125:
            if (pos_panier[1]+75 < pos_balle_y[indice_position] <pos_panier[1]+100) and (pos_balle_y[indice_position-10] < pos_balle_y[indice_position]):
                return True
            else: return False
        else: return False

    # Méthodes pour jeu

    def resetBall(self, pos_panier):
        pos_panier = [random.randint(100, self.width - 100), random.randint(200, self.height - 350)]
        return pos_panier


    def drawTrajectoryPreview(self, pos_x, pos_y):
        index = 1
        while index < len(pos_x) and pos_y[index-1] > pos_y[index]:
            if (pos_x[index] > 0):
                pygame.draw.circle(self.screen, ORANGE, (pos_x[index], pos_y[index]), 5)
                index += 20
        pygame.display.flip()

    def drawGame(self, pos_ball, pos_panier):
        
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.hoop_img, (pos_panier[0], pos_panier[1]))
        self.screen.blit(self.ball_img, (pos_ball[0]-25, pos_ball[1]-25))

        pygame.draw.rect(self.screen, RED, (pos_panier[0]+25, pos_panier[1]+75, 100, 25), 2)
        pygame.draw.rect(self.screen, WHITE, (0, 0, 300, 150))
        titre_text = self.font.render(f"Score : {self.score}", True, BLACK)
        self.screen.blit(titre_text, (30, 30))
        pygame.display.flip()

    def jeuLancer(self):
        self.chargementTextureJeu()
        while self.essais < self.max_essais:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        self.changes = True
                        self.ballonLancer()
                        jouer_son_lancer(volume=0.1)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.setPower(self.getPower()+0.5)
                self.changes = True
            elif keys[pygame.K_DOWN]:
                self.setPower(self.getPower()-0.5)
                self.changes = True
            elif keys[pygame.K_LEFT]:
                self.setAnglePlus()
                self.changes = True
            elif keys[pygame.K_RIGHT]:
                self.setAngleMoins()
                self.changes = True

            if self.changes :
                if self.ballonStatus:
                    self.dessinBallonLancer()
                    self.changes = True
                else:
                    self.dessinBallonNonLancer()
                    self.changes = False
        pygame.quit()

    def ballonLancer(self):
        self.ballonStatus = True

    def dessinBallonNonLancer(self):
        posBalleX, posBalleY, posRebond = calculate_trajectory(self.power, self.angle,(self.width, self.height), position_initiale=self.pos_joueur)
        self.drawGame(self.pos_joueur, self.pos_panier)
        self.drawTrajectoryPreview(posBalleX, posBalleY)
        self.clock.tick(60) #Max fps
        pygame.display.flip()

    def dessinBallonLancer(self):
        posBalleX, posBalleY, posRebond= calculate_trajectory(self.power, self.angle, (self.width, self.height), position_initiale=self.pos_joueur)
        self.pos_panier = self.dessinerLancer(posBalleX, posBalleY, self.pos_panier, posRebond)
        self.clock.tick(60) #Max fps
        pygame.display.flip()
        self.ballonStatus = False
    


    def jeuQuit(self):

        pygame.quit()
        sys.exit()

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
BROWN = (139, 69, 19)

if __name__ == "__main__":
    jeu = JeuBasket()
    jeu.jeuLancer()    
