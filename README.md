# EFREI BALLERS - Jeu de Basket 2D 🏀

Un jeu de basket 2D développé en Python utilisant Pygame où le joueur doit marquer des paniers en ajustant l'angle et la puissance de tir.

## 📋 Description

EFREI BALLERS est un jeu où vous devez marquer des paniers de basket en tenant compte de:
- L'angle de tir
- La puissance du lancer
- La physique (gravité, rebonds)
- Des bonus spéciaux apparaissant aléatoirement

## 🎮 Contrôles

- **Flèches Haut/Bas**: Ajuster la puissance du tir (0-400)
- **Flèches Gauche/Droite**: Ajuster l'angle de tir (0-180°) 
- **Espace**: Lancer la balle
- **Échap**: Quitter le jeu

## ⚙️ Installation

1. Assurez-vous d'avoir Python 3.12+ installé
2. Installez les dépendances:
```sh
pip install pygame customtkinter pillow
```

## 🚀 Lancement

```sh
python main.py
```

## 🎯 Règles du jeu

- Vous avez 15 erreurs maximum
- Un panier = 1 point
- Un panier avec rebond = 2 points
- Des bonus apparaissent aléatoirement:
  - Coeur: -1 erreur
  - Bonus 1: +1 point
  - Bonus 2: +2 points

## 🗂️ Structure du projet

```
├── assets/               # Images, sons et polices
├── interface/           # Interface d'accueil
├── jeu/                # Logique principale du jeu
├── scriptPhysique/     # Calculs de trajectoire
└── main.py            # Point d'entrée du jeu
```

## 🔧 Configuration requise

- Python 3.12+
- Pygame
- CustomTkinter
- Pillow (PIL)
- Résolution d'écran: 1920x1080
