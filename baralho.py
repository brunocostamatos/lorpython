from usuario import Usuario

class Baralho: 

    def __init__ (self, usuario):
        self.nome = Usuario.getNome(usuario)
        self.meusDecks = Usuario.getMeusDecks(usuario)             

    def verDecks(self):
        print("")
        for indexP, valueP in enumerate(self.meusDecks):
                    print(valueP)
        print("")

    def __str__ (self):
        print("")
        return "Usuário:\t{}\nMeus Decks:\t{}\n".format(self.nome, self.meusDecks)
