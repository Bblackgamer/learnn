class Bibliotheque():
    def __init__(self, capacite):
        self.capacite = capacite
        self.livres = []

    def add_livres(self, nom):
        if self.capacite_restante() <= 0 : 
            return False
        self.livres.append(nom)
        return True

    def capacite_restante(self):
        return self.capacite - len(self.livres)
    
nbr = input("Combien de livres voulez vous ranger: ")
bbt = Bibliotheque(int(nbr))

rangement = ["Python", "Java", "C++", "HTML", "CSS", "JavaScript"]
for book in rangement:
    success = bbt.add_livres(book)
    if success:
        print(f"Le livre {book} à été ajouté.")
    else:
        print(f"Désolé la bibliotheque est trop pleine pour accueillir le livre {book}")