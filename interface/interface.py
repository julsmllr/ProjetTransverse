# =============================================================================
# IMPORTATIONS
# =============================================================================
import tkinter as t
from tkinter import font
import os

# =============================================================================
# CONSTANTES ET VARIABLES GLOBALES
# =============================================================================

# Couleurs
bg_color = "#F8F8F8"
primary_color = "#FCA311"
text_color = "#14213D"
dark_bg_color = "#213241"
dark_primary_color = "#FC8E11"
dark_text_color = "#F8F8F8"

# Polices
primaryFont = ("Alata-Regular", 20)

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
# =============================================================================
# CONFIGURATION INITIALE
# =============================================================================

# Création de la fenêtre principale
jeu = t.Tk()
jeu.title("Simulation de projectile")
jeu.geometry("1920x1080")
jeu.attributes('-fullscreen', True)
jeu.bind('<Escape>', lambda e: jeu.destroy())

# Configuration de la police
font_path = "../assets/fonts/Alata-Regular.ttf"
tk_font = font.Font(family="Alata-Regular", size=12)
jeu.tk.call("font", "create", "Alata-Regular", "-family", "Alata-Regular", "-size", "12")

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
gameGestionSettings = t.Frame(gameInterface, bg=bg_color, width=640)
gameInterfaceMiddle = t.Frame(gameInterface, bg='red', width=640)
gameInformations = t.Frame(gameInterface, bg='purple', width=640)

gameGestionSettings.pack_propagate(False)
gameInterfaceMiddle.pack_propagate(False)
gameInformations.pack_propagate(False)

gameGestionSettings.pack(side="left", fill="both", expand=True)
gameInterfaceMiddle.pack(side="left", fill="both", expand=True)
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
    cursor="hand2"
)

gestionSettingsEntriesDirectionButtonMinus = t.Button(
    gestionSettingsEntriesDirectionButtonFrame,
    image=GameSettingDirectionLeft,
    bd=0,
    highlightthickness=0,
    relief="flat",
    bg=bg_color,
    activebackground=bg_color,
    cursor="hand2"
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

mon_slider = t.Scale(gestionSettingsEntriesPower, from_=0, to=100, orient='horizontal')
mon_slider.pack(expand=True, side="bottom")

# =============================== CONFIRMATION BUTTON =============================== #

gestionSettingsConfirmationButton = t.Button(
    gestionSettingsConfirmationFrame,
    image=BoutonLancer,
    bd=0,
    highlightthickness=0,
    relief="flat",
    bg=bg_color,
    activebackground=bg_color
)
gestionSettingsConfirmationButton.pack(expand=True, ipady=20)


gestionSettingsConfirmationButton.bind("<Button-1>", LaunchButtonClicked)
gestionSettingsConfirmationButton.bind("<ButtonRelease-1>", LaunchButtonNotClicked)



# =============================================================================
# SECTION JEU
# =============================================================================

GameLabel = t.Label(
    gameInterfaceMiddle,
    text="Espace pour le jeu pygame",
    bg=bg_color,
    fg=text_color,
    font=primaryFont
)
GameLabel.pack(expand=True)

# =============================================================================
# SECTION INFORMATIONS
# =============================================================================

score = 0
scoreLabel = t.Label(
    gameInformations,
    text="Score : " + str(score),
    bg=bg_color,
    fg=text_color,
    font=primaryFont
)
scoreLabel.pack(expand=True)

if __name__ == "__main__":
    jeu.mainloop()