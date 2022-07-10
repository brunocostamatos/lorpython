class Carta: 

    def __init__ (self, usuario):
        self.nome = usuario.nome
        self.minhasCartas = usuario.minhasCartas            

    def verCartas(self):
        print("")
        for indexP, valueP in enumerate(self.minhasCartas):
                    print(valueP)
        print("")

    def __str__ (self):
        print("")
        return "Usuário:\t{}\nMinhas Cartas:\t{}\n".format(self.nome, self.minhasCartas)
