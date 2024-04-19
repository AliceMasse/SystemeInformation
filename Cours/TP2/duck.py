from abc import ABC, abstractmethod

class Canard(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def methode(self, type):
        pass

class ColVert(Canard):
    def __init__(self, type):
        super().__init__(type)

    def methode(self, type):
        print(f"Type de canard: {self.type}, Type de méthode: {type}")

class CouRouge(Canard):
    def __init__(self, type):
        super().__init__(type)

    def methode(self, type):
        print(f"Type de canard: {self.type}, Type de méthode: {type}")

# Création d'une instance de ColVert et CouRouge
mon_canard_colvert = ColVert("ColVert")
mon_canard_courouge = CouRouge("CouRouge")

# Appel de la méthode methode
mon_canard_colvert.methode("voler")
mon_canard_courouge.methode("nager")