from matplotlib import pyplot as plt
from math import cos,sin, radians

angle = int(input("Angle de tir :"))
angle = radians(angle)
puissance = int(input("Vitesse initiale :"))


global gravite, x_0, y_0
gravite = 9.81

x_0, y_0 = 0, 0

temps = []
base = 0
for i in range(100):
    temps.append(base+3)
    base +=3


def x_y_vers_t(vitesse_initiale, angle_tir, temps):
    position_x_t, position_y_t = [], []

    for i in range(len(temps)):
        x_t = vitesse_initiale * cos(angle_tir) * temps[i] + x_0
        y_t = -(gravite / 2) * (temps[i] ** 2) + vitesse_initiale * sin(angle_tir) * temps[i] + y_0
        position_x_t.append(x_t)
        position_y_t.append(y_t)

    return position_x_t, position_y_t



def y_vers_x(vitesse_initiale, angle_tir, x_t):

    position_y_x = []
    for i in range(len(x_t)):
        t_fonction_x = (x_t[i]-x_0)/(vitesse_initiale*cos(angle_tir))
        y_fonction_x = -(gravite / 2) * (t_fonction_x ** 2) + vitesse_initiale * sin(angle_tir) * t_fonction_x + y_0
        position_y_x.append(y_fonction_x)

    return position_y_x


def affichage_x_y_t(temps, x_t, y_t):
    plt.plot(temps, x_t, linestyle='-', color='b')
    plt.plot(temps, y_t, linestyle='-', color='r')
    plt.show()

def affichage_y_x(x_t, y_x):
    plt.plot(x_t, y_x, linestyle='-', color='b')
    plt.show()



tab_pos_x, tab_pos_y = x_y_vers_t(puissance, angle, temps)
tab_pos_y_x = y_vers_x(puissance, angle, tab_pos_x)

print(temps)
print(tab_pos_x)
print(tab_pos_y)
print(tab_pos_y_x)

affichage_x_y_t(temps, tab_pos_x, tab_pos_y)
affichage_y_x(tab_pos_x, tab_pos_y_x)

# Affichage de x(t) et y(t)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(temps, tab_pos_x, label="x(t)", color='b')
plt.plot(temps, tab_pos_y, label="y(t)", color='r')
plt.xlabel("Temps (s)")
plt.ylabel("Position")
plt.legend()
plt.title("Évolution de x(t) et y(t)")
plt.grid()

# Affichage de y(x) (la vraie trajectoire parabolique)
plt.subplot(1, 2, 2)
plt.plot(tab_pos_x, tab_pos_y_x, label="y(x)", color='g')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Trajectoire y(x)")
plt.grid()

plt.show()