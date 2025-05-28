# =============================================================================
# IMPORTATIONS
# =============================================================================
import pygame
import sys
import os
import random
from jeu.gestionSon import *


# Pour avoir le script Physique (Essayer de simplifier ça)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from scriptPhysique.physique import calculate_trajectory

# =============================================================================
# PROGRAMME
# =============================================================================

class JeuBasket:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        initialiser_sons()
        jouer_musique_fond(volume=0.1 )
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("assets/fonts/Helvetica.ttf", 36)


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
        self.clock.tick(60)  # Max fps

        # Bonus
        self.bonus = Bonus()
        self.BonusState = True
        self.bonusCoord = (-1, -1)
        self.bonus_actif = False
        bonusLances = 0

    def chargementTextureJeu(self):
        self.background = pygame.image.load("assets/img/background.png")
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.ball_img = pygame.image.load("assets/img/basketball.png")
        self.ball_img = pygame.transform.scale(self.ball_img, (50, 50))
        self.hoop_img = pygame.image.load("assets/img/hoop.png")
        self.hoop_img = pygame.transform.scale(self.hoop_img, (150, 250))

    # Set et Get
    def setPower(self, power):
        self.power = power
    
    def getPower(self):
        return self.power
    
    def setAnglePlus(self ):
        if self.angle < 180:
            self.angle += 0.2

    def setAngleMoins(self):
        if self.angle > 0:
            self.angle -= 0.2

    def getAngle(self):
        return self.angle
    
    # Méthodes liées aux coordonnées
    def dessinerLancer(self, pos_balle_x, pos_balle_y, pos_panier, pos_rebond):
        indice_position = 0
        panier_touche = False
        rebond = False
        while indice_position < len(pos_balle_x) and not panier_touche:
            if len(pos_rebond) > 0:
                if (pos_rebond[0][0]-5, pos_rebond[0][1]-5) <= (pos_balle_x[indice_position], pos_balle_y[indice_position]) <= (pos_rebond[0][0]+5, pos_rebond[0][1]+5):
                    jouer_son_rebond()
                    rebond = True
                    if len(pos_rebond) > 0:
                        pos_rebond.pop(0)

            if self.verifCoordonnes(pos_balle_x, pos_balle_y, pos_panier, indice_position):
                    panier_touche = True
                    jouer_son_panier()
                    self.score += 1
                    if rebond:
                        self.score += 1
                    pos_panier = self.resetBall(pos_panier)


            else:
                    self.drawGame((pos_balle_x[indice_position], pos_balle_y[indice_position]), pos_panier)

                    if (self.bonus_actif and self.bonusCoord[0]<= pos_balle_x[indice_position] <= self.bonusCoord[0] + 50 and self.bonusCoord[1] <= pos_balle_y[indice_position] <= self.bonusCoord[1] + 50):
                        self.essais, self.score = self.bonus.pointsBonus(self.essais, self.score)
                        self.bonus_actif = False
                        self.bonusCoord = (-1, -1)
                    indice_position += 1


        if not panier_touche:
            self.essais += 1
            pos_panier = self.resetBall(pos_panier)

        if (not self.bonus_actif and random.randint(1, 3) == 1):
            self.bonusCoord = self.bonus.nouveauBonus(self.width, self.height)
            self.bonus_actif = True
            pygame.display.flip()

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

    def drawGame(self, pos_ball, pos_panier):

        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.hoop_img, (pos_panier[0], pos_panier[1]))
        self.screen.blit(self.ball_img, (pos_ball[0]-25, pos_ball[1]-25))

        self.showScore()

        if self.bonus_actif and self.bonusCoord != (-1, -1):
            self.bonus.dessinerBonus(self.bonusCoord, self.screen)
        pygame.display.flip()

    def showScore(self):
        score_text = self.font.render(f"Score : {self.score}", True, WHITE)
        self.screen.blit(score_text, (30, 30))
        essai_text = self.font.render(f"Erreurs : {self.essais}/{self.max_essais}", True, WHITE)
        self.screen.blit(essai_text, (30, 80))

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
            if keys[pygame.K_UP] and self.power < 400:
                self.setPower(self.getPower()+0.5)
                self.changes = True
            elif keys[pygame.K_DOWN] and self.power > 0:
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
            pygame.display.flip()
        pygame.quit()

    def ballonLancer(self):
        self.ballonStatus = True

    def dessinBallonNonLancer(self):
        posBalleX, posBalleY, posRebond = calculate_trajectory(self.power, self.angle,(self.width, self.height), position_initiale=self.pos_joueur)
        self.drawGame(self.pos_joueur, self.pos_panier)
        self.drawTrajectoryPreview(posBalleX, posBalleY)

    def dessinBallonLancer(self):
        posBalleX, posBalleY, posRebond= calculate_trajectory(self.power, self.angle, (self.width, self.height), position_initiale=self.pos_joueur)
        self.pos_panier = self.dessinerLancer(posBalleX, posBalleY, self.pos_panier, posRebond)
        self.ballonStatus = False

    def jeuQuit(self):
        pygame.quit()
        sys.exit()


class Bonus:
    def __init__(self):
        self.images = {
            "coeur": "assets/img/coeur_bonus.png",
            "bonus_1": "assets/img/bonus1.png",
            "bonus_2": "assets/img/bonus2.png"
        }
        self.bonus_actuel = ""

    def choixBonus(self):
        keys = list(self.images.keys())
        self.bonus_actuel = keys[random.randint(0, len(keys)-1)]

    def nouveauBonus(self, width, height):
        self.choixBonus()
        coordX = random.randint(100, width - 100)
        coordY = random.randint(200, height - 350)
        return (coordX, coordY)

    def pointsBonus(self, erreurs_actuelles, score_actuel):
        if self.bonus_actuel == "coeur":
            return erreurs_actuelles-1, score_actuel
        elif self.bonus_actuel == "bonus_1":
            return erreurs_actuelles, score_actuel + 1
        else:
            return erreurs_actuelles, score_actuel + 2

    def dessinerBonus(self, coordonnees, screen):
        image = pygame.image.load(self.images[self.bonus_actuel])
        image = pygame.transform.scale(image, (50, 50))
        screen.blit(image, coordonnees)
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
