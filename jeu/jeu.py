import pygame as pg
import tkinter as tk
from tkinter import messagebox #j'ai full trust Chat GPT askip ce module il est souvent utilisé pour les graphismes

# Fonction appelée quand on clique sur "Commencer le jeu"
def lancer_jeu():
    messagebox.showinfo("Démarrage", "Prépare toi la partie va bientot commencer (Big J il me faut ton aide pour co au jeu)")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("EFREI BALLERS :) - Écran d'accueil")
fenetre.geometry("500x400")
fenetre.config(bg="#282c34")

# Titre du jeu
titre = tk.Label(fenetre, text="EFREI BALLERS(donnez titre svp)", font=("Arial", 24, "bold"), fg="pink", bg="#282c34")
titre.pack(pady=20)

# Règles du jeu
regles = """
• Utilise ta souris pour viser et tirer la balle sur l'arceau.
• Vise le panier pour accéder au niveau suivant.
• Attention : Plus tu marques, plus le niveau devient difficile !
• Conseil: utilise les rebonds sur les murs pour t'aider :) !
"""
label_regles = tk.Label(fenetre, text=regles, font=("Arial", 12), fg="white", bg="#282c34", justify="left")
label_regles.pack(padx=20, pady=10)

# Bouton pour commencer
bouton_commencer = tk.Button(fenetre, text="Démarrer l'expérience", font=("Arial", 20), bg="#61afef", fg="white", command=lancer_jeu)
bouton_commencer.pack(pady=20)

fenetre.mainloop()

