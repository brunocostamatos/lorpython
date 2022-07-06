import random

class Partida:
    def __init__ (self, usuario):
        self.usuario = usuario

    def selecionarDeck(self):
        print("EM DESENVOLVIMENTO")

    def escolherDificuldade(self):
        print("\nDificuldades:\n \n1- Fácil \n2- Normal \n3- Difícil\n")
        selecionandoDificuldade = int(input("Escolha a dificuldade da partida: "))
        self.dificuldade = selecionandoDificuldade

    def jogo(self):
        if(self.dificuldade == 1):
            print("Escolheu fácil")
        elif(self.dificuldade == 2):
            print("Escolheu normal")
        elif(self.dificuldade == 3):
            print("Escolheu difícil")

    def verificarVencedor(self):
        print("EM DESENVOLVIMENTO")

    def incrementarXPUsuario(self):
        print("EM DESENVOLVIMENTO")

    def avancarNivelUsuario(self):
        print("EM DESENVOLVIMENTO")

    def __str__ (self):
        print("")
        return "REGIÃO ATUAL DO USUÁRIO\t{}\n".format(self.usuario.nome) + "Região:\t{}\nExperiência da Região:\t{}\n".format(self.regiao, self.expRegiao)
