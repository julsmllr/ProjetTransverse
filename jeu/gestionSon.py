import pygame



pygame.mixer.init()

# --- Initialisation des sons ---
# Les variables des sons seront initialisées par la fonction initialiser_sons()
son_lancer = None
son_rebond = None
son_panier = None


volume_general = 0.5



def initialiser_sons():
    global son_lancer, son_rebond, son_panier

    son_lancer = pygame.mixer.Sound("../assets/soundEffect/Slingshot1.mp3")
    son_rebond = pygame.mixer.Sound("../assets/soundEffect/Dribble1.mp3")
    son_panier = pygame.mixer.Sound("../assets/soundEffect/swish.mp3")

def jouer_son_lancer(volume=0.1):
    if son_lancer:
        son_lancer.play()



def jouer_son_rebond():
    if son_rebond:
        son_rebond.play()



def jouer_son_panier():
    if son_panier:
        son_panier.play()



def jouer_musique_fond(volume=0.1):
    pygame.mixer.music.load("../assets/soundEffect/EuSentu.mp3")
    #pygame.mixer.music.load("WiiMusic.mp3")
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)



