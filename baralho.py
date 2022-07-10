class Baralho: 

    def __init__ (self, usuario):
        self.nome = usuario.nome
        self.meusDecks = "EM DESENVOLVIMENTO"            

    def verDecks(self):
        print("EM DESENVOLVIMENTO")

    def __str__ (self):
        print("")
        return "Usuário:\t{}\nMeus Decks:\t{}\n".format(self.nome, self.minhasCartas)
