# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:43:05 2020

@author: axel.vaganay
"""

from ClassRectangle import Rectangle

longueur = int(input("Longueur ?"))
largeur = int(input("Largeur ?"))

rec1 = Rectangle(longueur, largeur)

print(rec1.gL())
print(rec1.gl())
print(rec1.perimetre())
print(rec1.surface())