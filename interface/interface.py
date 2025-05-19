# =============================================================================
# IMPORTATIONS
# =============================================================================

#import tkinter as tk
#from tkinter import messagebox #j'ai full trust Chat GPT askip ce module il est souvent utilisé pour les graphismes

import customtkinter
from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def lancer_jeu():
    messagebox.showinfo("Démarrage", "Prépare-toi, la partie va bientôt commencer (Big J, il me faut ton aide pour co au jeu)")

# Apparence et fenêtre
set_appearance_mode("Dark")
fenetre = CTk()
fenetre.title("EFREI BALLERS :) - Écran d'accueil")
fenetre.geometry(f"{fenetre.winfo_screenwidth()}x{fenetre.winfo_screenheight()}+0+0")
fenetre.attributes("-fullscreen", True)

# Image de fond
try:
    image_path = os.path.join("..", "assets", "buttonImg", "fond_regle_projet_tranverse.png")
    img = Image.open(image_path)
    img = img.resize((fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(img)

    background_label = CTkLabel(fenetre, image=bg_image, text="")  # customtkinter version
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"Erreur lors du chargement de l'image de fond : {e}")

# Widgets
titre = CTkLabel(
    master=fenetre,
    text="EFREI BALLERS (donnez titre svp)",
    font=("Arial", 40, "bold"),
    text_color="#DA741C",
    bg_color="white"
)
titre.pack(pady=20)

regles = """
• Utilise ta souris pour viser et tirer la balle sur l'arceau.
• Vise le panier pour accéder au niveau suivant.
• Attention : plus tu marques, plus le niveau devient difficile !
• Conseil : utilise les rebonds sur les murs pour t'aider :) !
"""
label_regles = CTkLabel(
    master=fenetre,
    text=regles,
    font=("Arial", 30),
    text_color="black",
    justify="left",
    bg_color="white"
)
label_regles.pack(padx=20, pady=10)

bouton_commencer = CTkButton(
    master=fenetre,
    text="Démarrer l'expérience",
    font=("Arial", 40),
    fg_color="#61afef",
    text_color="white",
    command=lancer_jeu
)
bouton_commencer.place(relx=0.5, rely=0.5, anchor="center")

# Boucle principale
if __name__ == "__main__":
    fenetre.mainloop()

# Commentaires :
"""le messagebox il sert quand tu vas avoir des erreurs, des demandes de confirmations ou quoi... donc en soit nous pas besoins. 

- Il faut qu'on mette la fenetre en fullscreen (plus esthetic)
- se mettre d'accord sur quel écran on met, (est-ce qu'on met tout sur un seul écran ou bien on a genre un écran d'accueil, un écran règle, etc...
- On va se mettre d'accord sur des couleurs etc... pour avoir quelque chose d'harmonieux 

SINON C'EST BIEN BOSS(merci bibou)
"""

if __name__ == "__main__":
    fenetre.mainloop()
