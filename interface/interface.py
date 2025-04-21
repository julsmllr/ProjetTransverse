
# ------------ IMPORTATIONS LIBRAIRIES ------------ #
import tkinter as t
from tkinter import font

from numpy import pad

# ------------ VARIABLES GLOBALES ------------ #


# Couleurs de l'interface
bg_color = "#F8F8F8"
primary_color = "#FCA311"
text_color = "#14213D"

dark_bg_color = "#213241"
dark_primary_color = "#FC8E11"
dark_text_color = "#F8F8F8"


# Initialisation de la police par défaut



# ------------ INITIALISATION FENETRE ------------ #

jeu = t.Tk()


jeu.title("Simulation de projectile")
jeu.geometry("1920x1080")
jeu.attributes('-fullscreen', True)
jeu.bind('<Escape>',lambda e: jeu.destroy()) # Pour quitter l'application avec la touche "Echap"


gameInterface = t.Frame(jeu, bg=dark_bg_color)
gameInterface.pack(expand=True, fill="both")

# Organisation de l'interface
gameGestionSettings = t.Frame(gameInterface, bg=bg_color)
gameInterfaceMiddle = t.Frame(gameInterface, bg='blue')
gameInformations = t.Frame(gameInterface, bg=bg_color)
gameGestionSettings.pack(side="left", fill="both", expand=True)   
gameInterfaceMiddle.pack(side="left", fill="both", expand=True)
gameInformations.pack(side="left", fill="both", expand=True)



# ------------ Gestion Settings ------------ #

# Frames
gestionSettingsFrame = t.Frame(gameGestionSettings, bg='purple')
gestionSettingsFrame.pack(expand=True, fill="both", padx=20, pady=20)   

gestionSettingsEntriesFrame = t.Frame(gestionSettingsFrame, bg=bg_color)
gestionSettingsConfirmationFrame = t.Frame(gestionSettingsFrame, bg='yellow')
gestionSettingsEntriesFrame.pack(expand=True, fill="both")
gestionSettingsConfirmationFrame.pack(fill="both", ipady=100, pady=10, padx=10)

# Frame Game Settings
gestionSettingsEntriesTitle = t.Frame(gestionSettingsEntriesFrame, bg='red')
gestionSettingsEntriesDirection = t.Frame(gestionSettingsEntriesFrame, bg='green')
gestionSettingsEntriesPower = t.Frame(gestionSettingsEntriesFrame, bg='blue')


gestionSettingsEntriesTitle.pack(fill="both")
gestionSettingsEntriesDirection.pack(expand=True, fill="both")
gestionSettingsEntriesPower.pack(expand=True, fill="both")

# Frame Game Settings Entries
gestionSettingsEntriesTitleLabel = t.Label(gestionSettingsEntriesTitle, text="Ajustez votre tir :", fg=text_color, font=("Arial", 20))
gestionSettingsEntriesTitleLabel.pack(expand=True)

gestionSettingsEntriesDirectionLabel = t.Label(gestionSettingsEntriesDirection, text="Angle de tir :", fg=text_color, font=("Arial", 20))
gestionSettingsEntriesDirectionLabel.pack(side="top", pady=50)

# Frame Game Settings Entries Direction
gestionSettingsEntriesDirectionButtonFrame = t.Frame(gestionSettingsEntriesDirection, bg='orange')
gestionSettingsEntriesDirectionButtonFrame.pack(expand=True, fill="both", side="bottom")

gestionSettingsEntriesDirectionButtonPlus = t.Button(gestionSettingsEntriesDirectionButtonFrame, text=">", bg=primary_color, fg=text_color, font=("Arial", 20))
gestionSettingsEntriesDirectionButtonMinus = t.Button(gestionSettingsEntriesDirectionButtonFrame, text="<", bg=primary_color, fg=text_color, font=("Arial", 20))
gestionSettingsEntriesDirectionButtonPlus.pack(side="right", expand=True)
gestionSettingsEntriesDirectionButtonMinus.pack(side="left", expand=True)

# Frame Game Settings Entries Power
gestionSettingsEntriesPowerLabel = t.Label(gestionSettingsEntriesPower, text="Puissance de tir :", fg=text_color, font=("Arial", 20))
gestionSettingsEntriesPowerLabel.pack(side="top", pady=50)


mon_slider = t.Scale(gestionSettingsEntriesPower, from_=0, to=100, orient='horizontal')
mon_slider.pack(expand=True, side="bottom")

# Frame Game Settings  Confirmation
gestionSettingsConfirmationButton = t.Button(gestionSettingsConfirmationFrame, text="Lancer", bg=primary_color, fg=text_color, font=("Arial", 20), width=20)
gestionSettingsConfirmationButton.pack(expand=True, ipady=20)


# Frame Game

GameLabel = t.Label(gameInterfaceMiddle, text="Espace pour le jeu pygame", bg='red', fg=text_color, font=("Arial", 20))
GameLabel.pack(expand=True)

# Frame Game Informations

if __name__ == "__main__":
    jeu.mainloop()


