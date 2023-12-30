

class Combattant:

    def __init__(self, vie, attaque,nom):
        self.vie = vie
        self.attaque = attaque
        self.vivant = True
        self.nom = nom
        
    def __str__(self):
        if self.vivant: vivantOuMort="VIVANT"
        else: vivantOuMort="MORT"
        texte = f'pv: {self.vie}     attaque: {self.attaque}  \n'
        texte+= f'{vivantOuMort}'
        return texte
    		
    def	_perdreVie(self, points):
        self.vie = self.vie - points
        if  self.vie  <=  0:
            self.vivant = False
            self.vie = 0
            
    def _gagneVie(self, points):
        self.vie = self.vie + points
           
    def	attaquer(self, adversaire):
        adversaire._perdreVie(self.attaque)
    
    def estVivant(self):
        return self.vivant
    
    def seBlesse(self,ptBlessure):
        self._perdreVie(ptBlessure)
        
    def seSoigne(self,ptGagne):
        self._gagneVie(ptGagne)
    
    def combat(self,adversaire):
        while self.estVivant() and adversaire.estVivant():
            attaquant=randint(1,2)
            if attaquant==1: self.attaquer(adversaire)
            else: adversaire.attaquer(self)
        if not self.estVivant():
            print(f'{adversaire.nom} remporte avec bravoure lze combat !')
            print(adversaire)
        else:
            print(f'{self.nom}remporte avec bravoure le comabt !')
            print(self)