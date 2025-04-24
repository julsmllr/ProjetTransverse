from matplotlib import pyplot as plt
from math import cos,sin, radians, tan

angle = 0
#tentative d'utilisation avec le while
while not (angle > 0 and angle < 180):
    angle = int(input("Angle de tir (angle entre 0 et 180 degré:"))
    angle = radians(angle)
puissance = int(input("Vitesse initiale :"))


global gravite, x_0, y_0
gravite = 9.81
x_0, y_0 = 0, 0

temps = []
base = 0
for i in range(1000):
    temps.append(base)
    base +=0.1

def x_y_vers_t(vitesse_initiale, angle_tir, temps):
    position_x_t, position_y_t = [], []

    for i in range(len(temps)):
        if angle > 90:
            x_t = vitesse_initiale * sin(angle_tir) * temps[i] + x_0
            y_t = -(gravite / 2) * (temps[i] ** 2) - vitesse_initiale * cos(angle_tir) * temps[i] + y_0
        else :
            x_t = vitesse_initiale * cos(angle_tir) * temps[i] + x_0
            y_t = -(gravite / 2) * (temps[i] ** 2) + vitesse_initiale * sin(angle_tir) * temps[i] + y_0

        position_x_t.append(x_t)
        position_y_t.append(y_t)
        

    return position_x_t, position_y_t



def y_vers_x(vitesse_initiale, angle_tir, x_t):

    position_y_x = []
    for i in range(len(x_t)):
        y_fonction_x = -(gravite / 2) * ((x_t[i]/(vitesse_initiale*cos(angle_tir))) ** 2) + vitesse_initiale * sin(angle_tir) * (x_t[i]/(vitesse_initiale*cos(angle_tir))) + y_0

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

indice_valide = 0
while tab_pos_y[indice_valide] >= 0:
    indice_valide += 1

temps = temps[:indice_valide-1]
tab_pos_x = tab_pos_x[:indice_valide-1]
tab_pos_y = tab_pos_y[:indice_valide-1]
tab_pos_y_x = tab_pos_y_x[:indice_valide-1]


print("Tableau du temps :",temps)
print("Tableau du pos x en fct t :",tab_pos_x)
print("Tableau du pos y en fct t :",tab_pos_y)
print("Tableau du pos y en fct x :", tab_pos_y_x)

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