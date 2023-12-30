# Programme qui trace un flocon de vonKoch par récursivité

import turtle
from random import randint


def couleur_aleatoire():
    """
    Fonction qui défini trois couleurs rouge vert bleu aléatoires
    Args: None
    Returns:
        tuple: tuple de trois nombres entiers de 0 à 255 représentant le R, V, B
    """
    turtle.colormode(255)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

def courbeVonKoch(n, cote):
    """
    Fonction récursive qui trace une courbe de von Koch
    Args:
        n (int): profondeur de récursivité.
        cote (int): longueur en pixels.

    Returns:
        trace de la courbe de von Koch
    """
    couleur=couleur_aleatoire()
    turtle.pencolor(couleur)
    if n == 0:                    # Condition d'arrêt -> fin de la récursivité
        turtle.forward(cote)
    else :
        courbeVonKoch(n-1, cote/3)
        turtle.left(60)
        courbeVonKoch(n-1, cote/3)
        turtle.right(120)
        courbeVonKoch(n-1, cote/3)
        turtle.left(60)
        courbeVonKoch(n-1, cote/3)

def floconVonKoch(n, cote):
    """
    Fonction qui fait appel 3 fois à la fonction récursive "courbe de von Koch"
    Args:
        n (int): profondeur de récursivité.
        cote (int): longueur en pixels.

    Returns:
        trace le flocon de von Koch
    """
    for _ in range(3):
        courbeVonKoch(n, cote)
        turtle.right(120)


turtle.setup(800, 600)
turtle.setheading(0)    # orientation intiale de la tête : vers la droite de l'écran
turtle.hideturtle()     # on cache la tortue
turtle.speed(0)	        # on accélère la tortue (vitesse max)

profRecur=int(input("Profondeur de récursivité ?  "))
coteTriangle=int(input("Longueur en pixels des cotés du triangle équilatéral de départ ?  "))

# Positionnement du crayon
turtle.penup()                              # Lève le crayon
turtle.goto(-coteTriangle/2, coteTriangle/2)   # Déplacement du crayon aux coordonnées citées (x,y)
turtle.pendown()                            # Lève le crayon

floconVonKoch(profRecur, coteTriangle)
turtle.exitonclick()                        # Quitte la fenêtre si l'on clique sur la souris


  