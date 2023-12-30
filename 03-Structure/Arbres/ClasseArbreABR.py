# -*- coding: utf-8 -*-
"""
@author: david
"""

from ClassFile import File
from turtle import *


class ArbreABR:
    
    def __init__(self,info=None,fg=None,fd=None):
        """ Méthode spéciale constructeur de la classe """
        self.info = info    # Valeur de l'étiquette du noeud
        self.fg = fg        # Fils Gauche: objet arbre, ou None si pas de fils gauche
        self.fd = fd        # Fils Droit: objet arbre, ou None si pas de fils droit


    def vider(self):
        """ Méthode qui vide l'arbre """
        self.info==None
        self.fg==None
        self.fd==None
    
    def taille(self):
        if self.estVide():
            return 0
        elif self.fg==None and self.fd==None:
            return 1
        elif self.fg!=None and self.fd==None:
            tg = self.fg.taille()
            return 1 + tg
        elif self.fg==None and self.fd!=None:
            td = self.fd.taille()
            return 1 + td
        else:
            tg = self.fg.taille()
            td = self.fd.taille()
            return 1 + tg + td
        
    
    def estVide(self):
        """ Méthode qui informe si l'arbre est vide en renvoyant True, False sinon """
        return self.info==None
    
    
    def insererElement(self,elm):
        """ L'élément est inséré au bon endroit dans l'arbre """
        if self.estVide():          # Le sous arbre existe mais est vide
            self.info=elm           # On met à jour l'info de ce noeud
        else:
            if elm<self.info:       # Si l'élément à insérer est plus petit on doit l'insérer à gauche
                if self.fg:         # Le sous arbre gauche existe est on rentre dedans par récursivité pour essayer d'y insérer l'élément
                    self.fg.insererElement(elm)
                else:               # Le sous arbre gauche n'existe pas alors on le créé
                    self.fg=ArbreABR(elm)
            if elm>self.info:       # Si l'élément à insérer est plus grand on doit l'insérer à droite
                if self.fd:         # Le sous arbre droite existe est on rentre dedans par récursivité pour essayer d'y insérer l'élément
                    self.fd.insererElement(elm)
                else:               # Le sous arbre droit n'existe pas alors on le créé
                    self.fd=ArbreABR(elm)                    
            # si elm = self.info, il n y a rien à faire puisque l'on ne peut pas insérer un élément identique à un existant
     
    
    def rechercherElement(self,elm):
        """ Méthode de recherche d'un élément dans dans l'ABR, renvoie True et le sous arbre si trouvé. False et None sinon """
        pass
        
        
    def hauteur(self):
        ''' - un arbre vide est de hauteur -1
            - un arbre feuille (uniquement la racine) est de hauteur 0
            - un arbre non vide a pour hauteur 1 + la hauteur maximale entre ses fils.'''
        if self.estVide():
            return -1
        if self.fg==None and self.fd==None:
            return 0
        elif self.fg==None and self.fd!=None:
            return 1+self.fd.hauteur()
        elif self.fg!=None and self.fd==None:
            return 1+self.fg.hauteur()    
        else:
            return 1+max(self.fg.hauteur(),self.fd.hauteur())



    """def ParcoursLargeur(self, listeParcours):  # Parcours BFS (Breadth First Search)
        Méthode de parcours en largeur de l'arbre à l'aide d'une File
        F=[]
        f.enfiler(self.info)
        listeParcours.append(self.info)
        while not f.estVide():
            noeud="""


    # 3 parcours en profondeur: Prefixe, Postfixe, Infixe
    def ParcoursPrefixe(self, listeParcours=[]):   # Prefixe = Racine -> fg -> fd
        """ Méthode de parcours en profondeur Prefixe de l'arbre """
        if not self.estVide():
            listeParcours.append(self.info)
            if self.fg is not None:
                self.fg.ParcoursPrefixe(listeParcours)
            if self.fd is not None:
                self.fd.ParcoursPrefixe(listeParcours)
        return listeParcours
                
            
    def ParcoursPostfixe(self, listeParcours=[]):   # Postfixe = fg -> fd -> Racine
        if not self.estVide():
            if self.fg is not None:
                self.fg.ParcoursPrefixe(listeParcours)
            if self.fd is not None:
                self.fd.ParcoursPrefixe(listeParcours)
            listeParcours.append(self.info)
        return listeParcours
    
    
    def ParcoursInfixe(self, listeParcours=[]):   # Infixe = fg -> Racine -> fd
        """ Méthode de parcours en profondeur Infixe de l'arbre """
        if not self.estVide():
            if self.fg is not None:
                self.fg.ParcoursPrefixe(listeParcours)
            listeParcours.append(self.info)
            if self.fd is not None:
                self.fd.ParcoursPrefixe(listeParcours)
        return listeParcours


    def supprimerElement(self, e):
        """ Méthode qui supprime un élement de l'arbre en conservant les propriétés d'un ABR """
        if self.estVide(): return  # rien a faire si arbre vide
        n = self
        pere = None
        trouve = False
        explorer_gauche = True
        # on commence par cherche l'element (et son pere et quel fils il est)
        while n and not trouve:
            if n.info == e:
                trouve = True
            else:
                pere = n
                if e < n.info:
                    explorer_gauche = True
                    n = n.fg
                else:
                    explorer_gauche = False
                    n = n.fd
        if not trouve: return  # cas 0, pas d'effet si pas present
        # l'element est present
        if not n.fg and not n.fd:
            # cas a : c'est une feuille
            if not pere:
                # on supprime la racine
                n.info = None
            else:
                # sinon on vient de la gauche ou de la droite
                if explorer_gauche:
                    pere.fg = None
                else:
                    pere.fd = None
        else:
            # cas b1 : n a seulement un fils gauche
            if n.fg and not n.fd:
                if not pere:
                    # on supprime la racine
                    n.info = n.fg.info
                    n.fg = n.fg.fg
                    n.fd = n.fg.fd
                else:
                    # on court-circuite le noeud
                    if explorer_gauche:
                        pere.fg = n.fg
                    else:
                        pere.fd = n.fg
            else:
                # cas b2 : n a seulement un fils droit
                if not n.fg and n.fd:
                    if not pere:
                        # on supprime la racine
                        n.info = n.fd.info
                        n.fg = n.fd.fg
                        n.fd = n.fd.fd
                    else:
                        # on court-circuite le noeud
                        if explorer_gauche:
                            pere.fg = n.fd
                        else:
                            pere.fd = n.fd
                else:
                    # cas c : n a deux fils
                    # on cherche le plus proche successeur
                    # cad le noeud le plus a gauche du sous arbre droit
                    successeur = n.fd
                    pere_successeur = n
                    while successeur.fg:
                        pere_successeur = successeur
                        successeur = successeur.fg
                    n.info = successeur.info  # pas besoin de changer fg et fd, juste les infos
                    if pere_successeur == n:
                        # le sous-arbre droit etant réduit à une seule feuille, on n'est pas rentré
                        # dans le while, il faut changer le fd de n
                        pere_successeur.fd = successeur.fd
                    else:
                        # on est passé au moins une fois dans le while, c'est le fg d'un des noeuds
                        # du sous-arbre droit qu'il faut changer
                        pere_successeur.fg = successeur.fd  # on court-circuite le successeur
    
    
    def afficheBasic(self):
        if not self.info: return
        h = self.hauteur()
        f = File([])
        ind_racine = ((2 ** h) * 2 - 2) // 2
        decalage = (2 ** h)
        f.enfiler((self, ind_racine, decalage))
        liste = []
        liste.append((self, ind_racine, decalage))
        while not f.estVide():
            (n, i, d) = f.defiler()
            if n.fg:
                f.enfiler((n.fg, i - d // 2, d // 2))
                liste.append((n.fg, i - d // 2, d // 2))
            if n.fd:
                f.enfiler((n.fd, i + d // 2, d // 2))
                liste.append((n.fd, i + d // 2, d // 2))
        (n, i, d) = liste[0]
        for _ in range(d - 2):
            print(' ', end='')
        print(str(n.info), end='')
        (nprec, iprec, dprec) = (n, i, d)
        for (n, i, d) in liste[1:]:
            if d != dprec:
                print()
                iprec = -1
            for _ in range(i - iprec - 1):
                print(' ', end='')
            print(str(n.info), end='')
            (nprec, iprec, dprec) = (n, i, d)
            
    
    def afficheTurtle(self):
        """
        Méthode qui affiche l'arbre à l'aide de la librairie turtle
        """
        def aller(x, y):
            up()
            goto(x, y)
            down()

        def cercle(x, y, r):
            aller(x, y - r)
            color("black", "white")
            begin_fill()
            circle(r)
            end_fill()

        def trace(n, arbre = self, x = 0, y = 200):
            if arbre is None:
                pencolor("lightgrey")
            else:
                pencolor("black")
            goto(x, y)
            if n >= 0 and arbre is not None:
                gauche = (x - 2**(n - 1 + 7 - profondeur) * 3, y - 400 / (profondeur))
                droit = (x + 2**(n - 1 + 7 - profondeur) * 3, y - 400 / (profondeur))
                trace(n - 1, arbre.fg, *gauche)
                aller(x, y)
                trace(n - 1, arbre.fd, *droit)
                aller(x, y)
                cercle(x, y, 10 * (7 - profondeur))
                aller(x + 1, y - taille_police + 2)
                write(f"{arbre.info}", align = "center", font = ("Arial", taille_police, "normal"))
                aller(x - 1, y + taille_police - 2)

        if not self.estVide():
            speed(0)
            hideturtle()
            width(2)
            profondeur = self.hauteur()
            taille_police = 27 - 3 * profondeur
            aller(0, 200)
            trace(profondeur)
            exitonclick()



        
          
if __name__ == '__main__':
   
    a1=ArbreABR(15)
    a1.afficheBasic()
    print()
    print()
    a1.insererElement(56)
    a1.insererElement(10)
    a1.insererElement(2)
    a1.insererElement(5)
    a1.insererElement(12)
    print (f"Hauteur de l'arbre: {a1.hauteur()}")
    print (f"Taille de l'arbre: {a1.taille()}")
    print (a1.ParcoursPrefixe())
    print (a1.ParcoursPostfixe())
    print (a1.ParcoursInfixe())
    a1.afficheBasic()
    a1.afficheTurtle()
    print()
    print()

















        
            