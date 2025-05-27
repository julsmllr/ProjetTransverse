# =============================================================================
# IMPORTATIONS
# =============================================================================
import tkinter as t
from tkinter import font
import os
import threading

from customtkinter import *

from tkinter import messagebox

from PIL import Image, ImageTk



os.sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from jeu.jeu import JeuBasket

# =============================================================================
# CONSTANTES ET VARIABLES GLOBALES
# =============================================================================
pygameGame = JeuBasket()

# Couleurs
bg_color = "#F8F8F8"
primary_color = "#FCA311"
text_color = "#14213D"
dark_bg_color = "#213241"
dark_primary_color = "#FC8E11"
dark_text_color = "#F8F8F8"

# Polices
primaryFont = "Helvetica"

# =============================================================================
# GESTIONNAIRES D'ÉVÉNEMENTS
# =============================================================================

def RightButtonClicked(event):
    gestionSettingsEntriesDirectionButtonPlus.config(image=GameSettingDirectionRightClicked)

def RightButtonNotClicked(event):
    gestionSettingsEntriesDirectionButtonPlus.config(image=GameSettingDirectionRight)

def LeftButtonClicked(event):
    gestionSettingsEntriesDirectionButtonMinus.config(image=GameSettingDirectionLeftClicked)

def LeftButtonNotClicked(event):
    gestionSettingsEntriesDirectionButtonMinus.config(image=GameSettingDirectionLeft)

def LaunchButtonNotClicked(event):
    gestionSettingsConfirmationButton.config(image=BoutonLancer)

def LaunchButtonClicked(event):
    gestionSettingsConfirmationButton.config(image=BoutonLancerClicked)

def GameClose(event):
    jeu.destroy()
    pygameGame.jeuQuit()

# =============================================================================
# CONFIGURATION INITIALE
# =============================================================================

# Création de la fenêtre principale
jeu = t.Tk()
jeu.title("Simulation de projectile")
jeu.geometry("960x1080+0+0")
jeu.bind('<Escape>', lambda e: GameClose(e))




# Configuration de la police
font_path = os.path.join("../assets/fonts/Helvetica.ttf")
font.nametofont("Helvetica").configure(size=10)
jeu.tk.call("font", "create", "Helvetica", "-family", "Helvetica", "-size", "12")

# Chargement des images
GameSettingDirectionLeft = t.PhotoImage(file="../assets/buttonImg/GameSettingDirectionLeft.png")
GameSettingDirectionRight = t.PhotoImage(file="../assets/buttonImg/GameSettingDirectionRight.png")
GameSettingDirectionLeftClicked = t.PhotoImage(file="../assets/buttonImg/GameSettingsDirectionLeftClicked.png")
GameSettingDirectionRightClicked = t.PhotoImage(file="../assets/buttonImg/GameSettingsDirectionRightClicked.png")
BoutonLancer = t.PhotoImage(file="../assets/buttonImg/LancerBouton.png")
BoutonLancerClicked = t.PhotoImage(file="../assets/buttonImg/LancerBoutonClicked.png")

# =============================================================================
# CRÉATION DE L'INTERFACE
# =============================================================================

# Frame principale
gameInterface = t.Frame(jeu, bg=dark_bg_color)
gameInterface.pack(expand=True, fill="both")

# Sections principales
gameGestionSettings = t.Frame(gameInterface, bg=bg_color, width=480)
gameInformations = t.Frame(gameInterface, bg='purple', width=480)

gameGestionSettings.pack_propagate(False)
gameInformations.pack_propagate(False)

gameGestionSettings.pack(side="left", fill="both", expand=True)
gameInformations.pack(side="left", fill="both", expand=True)

# =============================== SECTION GESTION DES PARAMÈTRES =============================== #

# Frames principaux des paramètres
gestionSettingsFrame = t.Frame(gameGestionSettings, bg=bg_color)
gestionSettingsFrame.pack(expand=True, fill="both", padx=20, pady=20)

gestionSettingsEntriesFrame = t.Frame(gestionSettingsFrame, bg=bg_color, borderwidth=2, relief="groove")
gestionSettingsConfirmationFrame = t.Frame(gestionSettingsFrame, bg=bg_color)
gestionSettingsEntriesFrame.pack(expand=True, fill="both")
gestionSettingsConfirmationFrame.pack(fill="both", ipady=100, pady=10, padx=10)

# Entrées des settings du jeu
gestionSettingsEntriesTitle = t.Frame(gestionSettingsEntriesFrame, bg=bg_color)
gestionSettingsEntriesDirection = t.Frame(gestionSettingsEntriesFrame, bg=bg_color)
gestionSettingsEntriesPower = t.Frame(gestionSettingsEntriesFrame, bg=bg_color)

gestionSettingsEntriesTitle.pack(fill="both", padx=20, pady=20)
gestionSettingsEntriesDirection.pack(expand=True, fill="both", padx=20, pady=20)
gestionSettingsEntriesPower.pack(expand=True, fill="both", padx=20, pady=20)

# Titre
gestionSettingsEntriesTitleLabel = t.Label(
    gestionSettingsEntriesTitle,
    text="Ajustez votre tir :",
    fg=text_color,
    font=primaryFont
)
gestionSettingsEntriesTitleLabel.pack(expand=True)

# Section Direction
gestionSettingsEntriesDirectionLabel = t.Label(
    gestionSettingsEntriesDirection,
    text="Angle de tir :",
    fg=text_color,
    font=primaryFont
)
gestionSettingsEntriesDirectionLabel.pack(side="top", pady=50)

gestionSettingsEntriesDirectionButtonFrame = t.Frame(gestionSettingsEntriesDirection, bg=bg_color)
gestionSettingsEntriesDirectionButtonFrame.pack(expand=True, fill="both", side="bottom")

gestionSettingsEntriesDirectionButtonPlus = t.Button(
    gestionSettingsEntriesDirectionButtonFrame,
    image=GameSettingDirectionRight,
    bd=0,
    highlightthickness=0,
    relief="flat",
    bg=bg_color,
    activebackground=bg_color,
    cursor="hand2",
    command= pygameGame.setAngleMoins  
)

gestionSettingsEntriesDirectionButtonMinus = t.Button(gestionSettingsEntriesDirectionButtonFrame,
    image=GameSettingDirectionLeft,
    bd=0,
    highlightthickness=0,
    relief="flat",
    bg=bg_color,
    activebackground=bg_color,
    cursor="hand2",
    command= pygameGame.setAnglePlus
)

# Configuration des événements des boutons
gestionSettingsEntriesDirectionButtonPlus.bind("<Button-1>", RightButtonClicked)
gestionSettingsEntriesDirectionButtonPlus.bind("<ButtonRelease-1>", RightButtonNotClicked)
gestionSettingsEntriesDirectionButtonMinus.bind("<Button-1>", LeftButtonClicked)
gestionSettingsEntriesDirectionButtonMinus.bind("<ButtonRelease-1>", LeftButtonNotClicked)

# Positionnement des boutons
gestionSettingsEntriesDirectionButtonPlus.pack(side="right", expand=True)
gestionSettingsEntriesDirectionButtonMinus.pack(side="left", expand=True)

# =============================== SECTION PUISSANCE =============================== #

gestionSettingsEntriesPowerLabel = t.Label(
    gestionSettingsEntriesPower,
    text="Puissance de tir :",
    fg=text_color,
    font=primaryFont
)
gestionSettingsEntriesPowerLabel.pack(side="top", pady=50)

powerScale = t.Scale(gestionSettingsEntriesPower, from_=10, to=200, orient='horizontal')
powerScale.bind("<Motion>", lambda event: pygameGame.setPower(powerScale.get()))

powerScale.pack(expand=True, side="bottom")

# =============================== CONFIRMATION BUTTON =============================== #

gestionSettingsConfirmationButton = t.Button(
    gestionSettingsConfirmationFrame,
    image=BoutonLancer,
    bd=0,
    highlightthickness=0,
    relief="flat",
    bg=bg_color,
    activebackground=bg_color,
    cursor="hand2",
    command=pygameGame.ballonLancer
)
gestionSettingsConfirmationButton.pack(expand=True, ipady=20)


gestionSettingsConfirmationButton.bind("<Button-1>", LaunchButtonClicked)
gestionSettingsConfirmationButton.bind("<ButtonRelease-1>", LaunchButtonNotClicked)



# =============================================================================
# SECTION INFORMATIONS
# =============================================================================

def misAJourScoreErreurs():
    scoreLabel.config(text="Score : " + str(pygameGame.score))
    erreurLabel.config(text="Erreurs : " + str(pygameGame.essais) + "/" + str(pygameGame.max_essais))
    jeu.after(1000, misAJourScoreErreurs)


scoreLabel = t.Label(
    gameInformations,
    text="Score : " + str(pygameGame.score),
    bg=bg_color,
    fg=text_color,
    font=primaryFont
)
scoreLabel.pack(expand=True)

erreurLabel = t.Label(
    gameInformations,
    text="Erreurs : " + str(pygameGame.essais) + "/" + str(pygameGame.max_essais),
    bg=bg_color,
    fg=text_color,
    font=primaryFont
)
erreurLabel.pack(expand=True)

jeu.after(1000, misAJourScoreErreurs)


def startGame():
    pygameGame.jeuLancer()


#Debut de code tkinter->interface.py

def affichage_interface() :











if __name__ == "__main__":
    pygame_thread = threading.Thread(target=startGame)
    pygame_thread.daemon = True #Fermer Pygame quand Tkinter se fermer

    pygame_thread.start()


    jeu.mainloop()
    