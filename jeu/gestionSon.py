import pygame



pygame.mixer.init()

# --- Initialisation des sons ---
# Les variables des sons seront initialisées par la fonction initialiser_sons()
son_lancer = None
son_rebond = None
son_panier = None

# Variable pour gérer le volume général (par défaut : 0.7)
volume_general = 0.7


# --- Fonctions d'initialisation ---
# Charge tous les sons et règle le volume initial
def initialiser_sons():
    global son_lancer, son_rebond, son_panier

    #son_lancer = pygame.mixer.Sound("")
    #son_rebond = pygame.mixer.Sound("")
    son_panier = pygame.mixer.Sound("swish.mp3")

    # Réglage du volume pour chaque son



# --- Fonctions pour jouer les sons ---
# Joue le son du lancer
def jouer_son_lancer():
    if son_lancer:
        son_lancer.play()


# Joue le son du rebond
def jouer_son_rebond():
    if son_rebond:
        son_rebond.play()


# Joue le son du panier marqué
def jouer_son_panier():
    if son_panier:
        son_panier.play()


# --- Musique de fond ---
# Joue la musique de fond en boucle
def jouer_musique_fond(volume=0.5):
    pygame.mixer.music.load("Bit_Adventure.wav")
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)  # -1 pour une boucle infinie


# Arrête la musique de fond
def arreter_musique_fond():
    pygame.mixer.music.stop()


# Met la musique de fond en pause
def pause_musique_fond():
    pygame.mixer.music.pause()


# Reprend la musique de fond après une pause
def reprendre_musique_fond():
    pygame.mixer.music.unpause()


# Coupe tous les sons et la musique (volume à 0)
def couper_son():
    global volume_general
    volume_general = 0.0
    pygame.mixer.music.set_volume(volume_general)
    for son in [son_lancer, son_rebond, son_panier]:
        if son:
            son.set_volume(volume_general)


# Remet le volume des sons et de la musique (volume à 0.7)
def remettre_son():
    global volume_general
    volume_general = 0.7
    pygame.mixer.music.set_volume(volume_general)
    for son in [son_lancer, son_rebond, son_panier]:
        if son:
            son.set_volume(volume_general)