from usuario import Usuario

class Carta: 

    def __init__ (self, usuario):
        self.usuario = usuario
        self.nome = Usuario.getNome(self.usuario)
        self.minhasCartas = Usuario.getMinhasCartas(self.usuario)            

    def verCartas(self):
        print("")
        for indexP, valueP in enumerate(Usuario.getMinhasCartas(self.usuario)):
                    print(valueP)
        print("")

    def __str__ (self):
        print("")
        return "Usuário:\t{}\nMinhas Cartas:\t{}\n".format(self.nome, self.minhasCartas)
