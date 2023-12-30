# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 14:02:38 2020

@author: davidpaul.granjon
"""

import turtle
import random

# Trace un trait horizontal - ATTENTION le centre du repère est le centre de la fenêtre
# 1er trait
turtle.pensize(3)       # Largeur du trait
turtle.penup()          # Lève le crayon
turtle.goto(0,0)        # Inutile car au départ le curseur est en 0,0
turtle.pendown()        # Pose le crayon
turtle.goto(350,0)      # Déplacement du crayon aux coordonnées citées (x,y)

# Trace un trait horizontal - ATTENTION le centre du repère est le centre de la fenêtre
# 1er trait
turtle.pensize(3)       # Largeur du trait
turtle.penup()          # Lève le crayon
turtle.goto(0,0)        # Inutile car au départ le curseur est en 0,0
turtle.pendown()        # Pose le crayon
turtle.goto(-350,0)      # Déplacement du crayon aux coordonnées citées (x,y)

def couleur_aleatoire():
    turtle.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def trait(x1,y1,x2,y2):
    '''
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    '''
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)

def rectangle(x,y,w,h):
    '''
    Paramètres
        x, y : coordonnées du centre de la base de rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
    '''
    turtle.penup()
    turtle.goto(x-w/2,y)
    turtle.pendown()
    turtle.goto(x+w/2,y)
    turtle.goto(x+w/2,y+h)
    turtle.goto(x-w/2,y+h)
    turtle.goto(x-w/2,y)

# ----- Fenetre -----

def fenetre1(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    '''
    turtle.pensize(1)
    turtle.fillcolor('#eef')
    turtle.begin_fill()
    rectangle(x,y+20,30,30)
    turtle.end_fill()

# ----- Eléments du RDC : Portes -----

def porte1(x,y,couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    '''
    turtle.pensize(1)
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    rectangle(x,y,30,50)
    turtle.end_fill()

def porte2(x,y,couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    '''
    turtle.penup()
    turtle.setheading(90)
    turtle.goto(x-15,y)
    turtle.pensize(1)
    turtle.pendown()
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.goto(x+15,y)
    turtle.goto(x+15,y+40)
    turtle.circle(15,180)
    turtle.goto(x-15,y+40)
    turtle.goto(x-15,y)
    turtle.end_fill()

# ----- Elements des étages : Balcon -----

def fenetre2(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    '''
    turtle.penup()
    turtle.goto(x-15,y)
    turtle.pensize(1)
    # porte-fenetre
    turtle.fillcolor('#eef')
    turtle.begin_fill()
    rectangle(x,y,30,50)
    turtle.end_fill()
    # balcon
    turtle.pensize(3)
    for i in range(0,9):
        trait(x-20+i*5,y,x-20+i*5,y+25)
    trait(x-20,y,x+20,y)
    trait(x-20,y+25,x+20,y+25)

# ----- Facade avec : couleur + 3 élts d'étages -----

def facade(x, y_sol, couleur, niveau):
    '''
    Paramètres :
        x : abcisse du centre de la façade
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    '''
    turtle.pensize(0)
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.pendown()
    rectangle(x, y_sol + niveau * 60, 140, 60)
    turtle.end_fill()

# ----- Toits -----

def toit1(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    '''
    y = y_sol + niveau * 60
    turtle.penup()
    turtle.goto(x-80, y)
    turtle.pensize(0)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.pendown()
    turtle.goto(x+80, y)
    turtle.goto(x, y+40)
    turtle.goto(x-80, y)
    turtle.end_fill()

def toit2(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    '''
    y = y_sol + niveau * 60
    # trait horizontal
    turtle.pensize(10)
    trait(x-70, y+5, x+70, y+5)

'''def etage (x,y_sol):
    numFenetre=random.randint(1,2)
    listePositions = [(x, y_sol),(x-45, y_sol),(x+45, y_sol)]
    random.shuffle(listePositions)
    if numFenetre==1:
        fentre1(listePositions[0][0],listePositions[0][1],couleurPorte)
    else:
        fenetre2(listePositions[0][0],listePositions[0][1],couleurPorte)

    fenetre1(listePositions[1][0],listePositions[1][1])

    fenetre1(listePositions[2][0],listePositions[2][1])'''


 
def rdc (x,y_sol):                   #création de la fonction "rdc"
    numPorte=random.randint(1,2)               #choisi aléatoirement le numéro de la porte entre les nombres entier 1 et 2
    listePositions = [(x, y_sol),(x-45, y_sol),(x+45, y_sol)]            #tuple qui contient les 3 coordonnées des 3 positions éléments possibles par étages
    random.shuffle(listePositions)                                       #shuffle qui mélange le rang des terme du tuple "listePositions"
    couleurPorte=couleur_aleatoire()                                     #met une couleur aléatoire des portes
    if numPorte==1:                                                      #si le numéro de la porte est 2
        porte1(listePositions[0][0],listePositions[0][1],couleurPorte)   #alors on pose "porte1" à la position dans le  premier rang du tuple qui a été mélangé par shuffle
    else:                                                                #sinon c'est "porte2" qui est pausée
        porte2(listePositions[0][0],listePositions[0][1],couleurPorte)

    fenetre1(listePositions[1][0],listePositions[1][1])                  #rempli les autres coordonnées par des "fenetre1"

    fenetre1(listePositions[2][0],listePositions[2][1])


def immeuble (x,y_sol,nbEtages):   #création de la fonction "immeuble"
    couleurF=couleur_aleatoire()        #couleur de façade aléatoire
    for niveau in range (0,nbEtages+1):      #boucle qui prend le numéro de chaque étage généré de bas en haut(avec une incrémentation de 1)
        facade(x, y_sol, couleurF, niveau)   #création d'un étage selon le nombre qu'il dois créer(défini par nbEtage)
        if niveau==0:                        #si le niveau créé est le rez de chaussée alors on appel la fonction rdc
            rdc(x,y_sol)
        '''else:
            etage(x,y_sol)'''
        '''else:
            etage(x,y_sol,niveau)
            fenetre(155,70)
            fenetre(200,70)
            fenetre(245,70)'''



turtle.setup(800, 600)
turtle.speed(0)
turtle.hideturtle()

'''nbetage = randint[1,2]'''
y_sol = 0             #le sol devient le hauteur y: 0

immeuble(250,y_sol,0) #géneration du 4ème immeuble avec une couleur de porte et de façade aléatoire
toit1(250,y_sol,1)


immeuble(85,y_sol,1) #géneration du 3ème immeuble avec une couleur de porte et de façade aléatoire
toit1(85,y_sol,2)
fenetre1(40,63)
fenetre2(85,63)
fenetre2(130,63)


immeuble(-85,y_sol,2) #géneration du 2ème immeuble avec une couleur de porte et de façade aléatoire
toit2(-85,y_sol,3)
fenetre2(-40,63)
fenetre1(-85,63)
fenetre1(-130,63)
fenetre1(-40,125)
fenetre2(-85,125)
fenetre1(-130,125)


immeuble(-250,y_sol,1) #géneration du 1er immeuble avec une couleur de porte et de façade aléatoire
toit1(-250,y_sol,2)
fenetre2(-205,63)
fenetre2(-250,63)
fenetre2(-295,63)







'''niveau=0
couleur=couleur_aleatoire()
facade(200, y_sol, couleur, niveau)
niveau=1
fenetre_balcon(200,y_sol)
couleur=couleur_aleatoire()
porte1(155,y_sol,couleur)
fenetre(245,y_sol)
 #etage
couleur=couleur_aleatoire()
facade(200, y_sol, couleur, niveau)
niveau=2
fenetre_balcon(200,65)
toit2(200, y_sol, niveau)
fenetre(245,65)
fenetre(155,65)'''




turtle.exitonclick()    # Quitte la fenêtre si l'on clique sur la souris





