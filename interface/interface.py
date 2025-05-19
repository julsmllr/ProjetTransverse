# =============================================================================
# IMPORTATIONS
# =============================================================================

#import tkinter as tk
#from tkinter import messagebox #j'ai full trust Chat GPT askip ce module il est souvent utilisé pour les graphismes

import customtkinter
from customtkinter import *
from tkinter import messagebox, Label  # <-- on importe Label ici
from PIL import Image, ImageTk

def lancer_jeu():
    messagebox.showinfo("Démarrage", "Prépare-toi, la partie va bientôt commencer (Big J, il me faut ton aide pour co au jeu)")


set_appearance_mode("Dark")
fenetre = CTk()
fenetre.title("EFREI BALLERS :) - Écran d'accueil")
fenetre.geometry("%dx%d+0+0" % (fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()))
fenetre.attributes("-fullscreen", True)


try:
    image_path = "../assets/buttonImg/fond_regle_projet_tranverse.png"
    img = Image.open(image_path)
    img = img.resize((fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(img)


    background_label = Label(fenetre, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"Erreur lors du chargement de l'image de fond : {e}")

#widgets plutot styles je trouve

titre = CTkLabel(fenetre, text="EFREI BALLERS (donnez titre svp)", font=("Arial", 40, "bold"),
                 text_color="orange", bg_color="transparent")
titre.pack(pady=20)

regles = """
• Utilise ta souris pour viser et tirer la balle sur l'arceau.
• Vise le panier pour accéder au niveau suivant.
• Attention : plus tu marques, plus le niveau devient difficile !
• Conseil : utilise les rebonds sur les murs pour t'aider :) !
"""
label_regles = CTkLabel(fenetre, text=regles, font=("Arial", 30),
                        text_color="black", justify="left", bg_color="transparent")
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
