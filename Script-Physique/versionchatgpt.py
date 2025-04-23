import pygame
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import random

# Initialisation de Pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 800, 600
gravity = 9.81  # Gravité terrestre
MAX_ATTEMPTS = 5
MAX_SCORE = 3

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
BROWN = (139, 69, 19)

# Création de la fenêtre Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Basket 2D")

# Chargement des images
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
ball_img = pygame.image.load("basketball.png")
ball_img = pygame.transform.scale(ball_img, (30, 30))
hoop_img = pygame.image.load("hoop.png")
hoop_img = pygame.transform.scale(hoop_img, (60, 40))

# Position du joueur et panier
player_pos = (100, HEIGHT - 100)
basket_pos = [700, random.randint(200, HEIGHT - 250)]
ball_radius = 15
hoop_radius = 20

# Variables de puissance et angle
power = 50
theta = 45
ball_pos = list(player_pos)
ball_launched = False
vx, vy = 0, 0
attempts = 0
score = 0

def draw_trajectory(v, angle):
    """Affiche la trajectoire du tir avec matplotlib."""
    angle_rad = np.radians(angle)
    t_flight = (2 * v * np.sin(angle_rad)) / gravity
    t = np.linspace(0, t_flight, num=50)
    x = player_pos[0] + v * np.cos(angle_rad) * t
    y = player_pos[1] - (v * np.sin(angle_rad) * t - 0.5 * gravity * t**2)
    plt.plot(x, y, 'b--')
    plt.xlim(0, WIDTH)
    plt.ylim(0, HEIGHT)
    plt.gca().invert_yaxis()
    plt.show()

def reset_ball():
    global ball_pos, ball_launched
    ball_pos = list(player_pos)
    ball_launched = False

def shoot_ball():
    global ball_launched, vx, vy, ball_pos, attempts
    if attempts >= MAX_ATTEMPTS:
        return
    angle_rad = np.radians(theta)
    vx = power * np.cos(angle_rad)
    vy = -power * np.sin(angle_rad)
    ball_launched = True
    ball_pos = list(player_pos)
    attempts += 1
    draw_trajectory(power, theta)

def update_ball():
    global ball_launched, ball_pos, vy, attempts, score, basket_pos
    if ball_launched:
        ball_pos[0] += vx * 0.1
        ball_pos[1] += vy * 0.1
        vy += gravity * 0.1

        # Vérifier la collision avec le panier
        if (basket_pos[0] - hoop_radius < ball_pos[0] < basket_pos[0] + hoop_radius and
                basket_pos[1] - hoop_radius < ball_pos[1] < basket_pos[1] + hoop_radius):
            score += 1
            print(f"Panier marqué ! Score: {score}")
            if score >= MAX_SCORE:
                print("Gagné !")
                pygame.quit()
                exit()
            attempts = 0
            basket_pos = [random.randint(400, WIDTH - 100), random.randint(200, HEIGHT - 250)]
            reset_ball()

        if ball_pos[1] >= HEIGHT - 20:
            ball_launched = False
            if attempts >= MAX_ATTEMPTS:
                print("Perdu !")
                pygame.quit()
                exit()

def draw_game():
    screen.blit(background, (0, 0))
    pygame.draw.circle(screen, ORANGE, player_pos, 20)
    screen.blit(hoop_img, (basket_pos[0] - 20, basket_pos[1] - 20))
    if ball_launched:
        screen.blit(ball_img, (int(ball_pos[0]) - 15, int(ball_pos[1]) - 15))
    pygame.display.flip()

def main():
    global power, theta
    running = True
    clock = pygame.time.Clock()

    # Interface Tkinter
    root = tk.Tk()
    root.title("Contrôles du Jeu")
    frame = ttk.Frame(root, padding=10)
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(frame, text="Puissance:").grid(row=0, column=0)
    power_slider = ttk.Scale(frame, from_=10, to=100, orient="horizontal", command=lambda v: update_power(v))
    power_slider.set(power)
    power_slider.grid(row=0, column=1)

    ttk.Label(frame, text="Angle:").grid(row=1, column=0)
    angle_slider = ttk.Scale(frame, from_=0, to=90, orient="horizontal", command=lambda v: update_angle(v))
    angle_slider.set(theta)
    angle_slider.grid(row=1, column=1)

    shoot_button = ttk.Button(frame, text="Tirer", command=shoot_ball)
    shoot_button.grid(row=2, column=0, columnspan=2)

    def update_power(v):
        global power
        power = int(float(v))

    def update_angle(v):
        global theta
        theta = int(float(v))

    def close_game():
        global running
        running = False
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", close_game)

    while running:
        update_ball()
        draw_game()
        root.update_idletasks()
        root.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                shoot_ball()
        clock.tick(30)

    pygame.quit()
    root.destroy()

if __name__ == "__main__":
    main()
