# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

# ********************************************************************************
# CLASSE FILE - CREATION D'UNE STRUCTURE DE TYPE PILE en POO avec une List Python
# ********************************************************************************

class Pile:
    '''Classe définissant une structure de données de type Pile (LIFO: Last In First Out) avec méthodes'''
    
    # Méthode: Constructeur de la pile
    def __init__(self,L=None):
        '''Méthode qui construit la Pile à partir d'une liste existante qui peut être vide ou non'''
        if L is None:
            L=[] 
        self.liste=L
    
    # SURCHARGE de la Méthode de destruction de la Pile
    def __del__(self):
        self.vider()
        print ("Pile vidée et détruite")
        
    # SURCHARGE de la Méthode d'AFFICHAGE
    def __repr__(self):
        '''Méthode qui redéfinie l'affichage de la Pile de façon personnalisée, et renvoie False si la Pile est vide''' 
        if not self.estVide(): 
            chaine="Pile: " 
            nbElem=self.hauteur() 
            for i in range (0,nbElem-1): 
                chaine += eval("f'{self.liste[i]} '") 
            chaine += eval("f'{self.liste[nbElem-1]}'") 
            return chaine 
        else: 
            return "Pile vide !"
        
    def empiler(self,e):
        self.liste.append(e)
    
    def depiler(self):
        if not self.estVide():
            return self.liste.pop()
        else:
            print("Pile vide !")
    
    def vider(self):
        self.liste=[]
        #self.liste.clear()
        
    def estVide(self):
        #return len(self.liste)==0
        if len(self.liste) != 0:
            return False
        else:
            return True
        
    def sommet(self,L):
        if not self.estVide():
            return self.liste[-1]
        else:
            print("Pile vide !")
        
    def hauteur(self):
        return len(self.liste)
        