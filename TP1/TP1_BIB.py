import json
import os

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        elif isinstance(obj, Livre):
            return vars(obj)
        return super().default(obj)

class Livre:
    def __init__(self, auteur, titre, tag, image=None):
        self.auteur = auteur
        self.titre = titre
        self.tag = tag
        self.image = image

    def mettre_a_jour(self, auteur=None, titre=None, tag=None, image=None):
        if auteur:
            self.auteur = auteur
        if titre:
            self.titre = titre
        if tag:
            self.tag = tag
        if image:
            self.image = image

    def consulter(self):
        return self.auteur, self.titre, self.tag, self.image

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def supprimer_livre(self, livre):
        self.livres = [l for l in self.livres if l != livre]

    def afficher_livres(self):
        for livre in self.livres:
            print(livre.consulter())

    def sauvegarder(self, fichier):
        with open(fichier, 'w') as f:
            json.dump(self.livres, f, cls=ComplexEncoder)

class Librairie:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        
    def supprimer_livre(self, livre):
        if livre in self.livres:
            for i in range(len(self.livres)):
                if livre == self.livres[i]:
                    del self.livres[i]
                    break

    def afficher_livres(self):
        for livre in self.livres:
            print(livre.consulter())

class Utilisateur:
    def __init__(self, bibliotheque, librairie):
        self.bibliotheque = bibliotheque
        self.librairie = librairie

    def ajouter_livre_bibliotheque(self, livre):
        self.bibliotheque.ajouter_livre(livre)

    def ajouter_livre_librairie(self, livre):
        self.librairie.ajouter_livre(livre)
        
    def verifier_livre(self, livre):
        if not livre.auteur or not livre.titre:
            print("L'auteur et le titre sont obligatoires.")
            return False
        return True

if __name__ == '__main__':
    bib = Bibliotheque()
    while True:
        print("1. Ajouter un livre")
        print("2. Afficher les livres")
        print("3. Sauvegarder et quitter")
        choix = input("Choisissez une option : ")
        if choix == '1':
            auteur = input("Entrez l'auteur du livre : ")
            titre = input("Entrez le titre du livre : ")
            tag = input("Entrez le tag du livre : ")
            image = input("Entrez le lien vers l'image de couverture du livre : ")
            bib.ajouter_livre(Livre(auteur, titre, tag, image))
        elif choix == '2':
            bib.afficher_livres()
        elif choix == '3':
            chemin = os.path.join('C:', os.sep, 'Users', 'alice', 'OneDrive', 'HEXAGONE', 'Système Information', 'TP1', 'bib.json')
            bib.sauvegarder(chemin)
            break