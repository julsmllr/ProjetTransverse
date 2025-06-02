# ===================================================== #
#                                                       #
#                   Projet Transverse                   #
#                     INTERFACE.PY                      #
#                                                       #
# ===================================================== #



# ===================================================== #
#                       IMPORTATIONS                    #
# ===================================================== #

from customtkinter import *
from PIL import Image


# ===================================================== #
#                       FONCTIONS                       #
# ===================================================== #

def afficher_interface():

    # Apparence et fenêtre
    set_appearance_mode("Dark")
    fenetre = CTk()
    fenetre.bind('<Escape>', lambda e: fenetre.destroy())
    fenetre.title("EFREI BALLERS :) - Écran d'accueil")
    fenetre.geometry("1920x1080")
    fenetre.attributes("-fullscreen", True)


    img_path = "assets/buttonImg/fond_regle_projet_tranverse.png"
    bg_image = CTkImage(Image.open(img_path), size=(1920, 1080))

    background_label = CTkLabel(fenetre, image=bg_image, text="")  # customtkinter version
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    # Widgets
    CTkLabel(fenetre, text="EFREI BALLERS", font=("Arial", 40, "bold"),
             text_color="orange", bg_color="white").pack(pady=20)

    regles = """
         Quelques informations pour que tu passes une bonne expérience... 
    
            • Utilise tes talents de tireur pour viser et tirer la balle sur l'arceau.
            • Vise le panier pour accéder au niveau suivant.
            • Dans ce jeu , tu peux te déplacer grâce à chacune des flèches de ton clavier.
            • Le chronomètre te permet de pouvoir suivre ta progression en temps réel.
            • A toi de te surpasser pour réaliser le meilleur temps de jeu possible.
            • Conseil : utilise les rebonds sur les murs pour t'aider :) !
        """
    CTkLabel(fenetre, text=regles, font=("Arial", 20), text_color="black",
             justify="left", bg_color="white").pack(padx=20, pady=10)

    CTkButton(fenetre, text="Démarrer l'expérience", font=("Arial", 40),
              fg_color="#61afef", text_color="white", command=fenetre.destroy).place(relx=0.5, rely=0.5, anchor="center")

    fenetre.mainloop()
