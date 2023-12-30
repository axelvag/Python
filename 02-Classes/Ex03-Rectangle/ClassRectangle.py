class Rectangle:
    
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur
        
    def perimetre(self):
        return (self.longueur + self.largeur)*2
        
    def surface(self):
        return self.longueur * self.largeur
    
    def gL(self):
        return f'Longueur : {self.longueur}'
    
    def gl(self):
        return f'Largeur : {self.largeur}'