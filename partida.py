import random
from bau import Bau

class Partida:
    def __init__ (self, usuario):
        self.usuario = usuario
    

    def selecionarDeck(self):
        print("EM DESENVOLVIMENTO")

    def escolherDificuldade(self):
        print("\nDificuldades:\n \n1- Fácil \n2- Normal \n3- Difícil\n")
        selecionandoDificuldade = int(input("Escolha a dificuldade da partida: "))
        self.dificuldade = selecionandoDificuldade
        if(self.dificuldade == 1):
            print("\nEscolheu a dificuldade FÁCIL")
        elif(self.dificuldade == 2):
            print("\nEscolheu a dificuldade NORMAL")
        elif(self.dificuldade == 3):
            print("\nEscolheu a dificuldade DIFÍCIL")

    def jogo(self):
        resultado = 0
        for i in range(1):
            resultado = random.randint(1,4)
        self.resultado = resultado

    def verificarVencedor(self):
        if self.dificuldade == 1:
            if self.resultado == 1 or self.resultado == 2 or self.resultado == 3 :
                print("\nVocê ganhou :D")
                self.vencedor = 1
            else:
                print("\nVocê perdeu :(")
                self.vencedor = 0
        elif self.dificuldade == 2:
            if self.resultado == 1 or self.resultado == 2 :
                print("\nVocê ganhou :D")
                self.vencedor = 1
            else:
                print("\nVocê perdeu :(")
                self.vencedor = 0
        elif self.dificuldade == 3:
            if self.resultado == 1:
                print("\nVocê ganhou :D")
                self.vencedor = 1
            else:
                print("\nVocê perdeu :(")
                self.vencedor = 0

    def incrementarXPUsuario(self):
        if self.vencedor == 1:
            if self.dificuldade == 1:
                self.usuario.exp +=  5
                print("\nExperiência da conta:\t{}".format(self.usuario.exp))
            elif self.dificuldade == 2:
                self.usuario.exp += 25
                print("\nExperiência da conta:\t{}".format(self.usuario.exp))
            elif self.dificuldade == 3:
                self.usuario.exp += 75
                print("\nExperiência da conta:\t{}".format(self.usuario.exp))

    def avancarNivelUsuario(self):        
        recompensa = Bau(self.usuario)
        print(recompensa)
        recompensa.sortearCartas([])
        recompensa.verificarSorteio()
        recompensa.tranformarSorteio()
        self.usuario.exp = 0
        self.usuario.nivel += 1
        print("\nBAÚ PARA O USUÁRIO\t{}\n".format(self.usuario.nome) + "Pó de Carta:\t{}\nCoringa:\t{}\nXP da Conta:\t{}\nNível da Conta:\t{}\nMinhas Cartas:\t{}\n".format(self.usuario.qntPo, self.usuario.qntCoringa, self.usuario.exp, self.usuario.nivel, self.usuario.minhasCartas))
    
    def __str__ (self):
        print("")
        return "REGIÃO ATUAL DO USUÁRIO\t{}\n".format(self.usuario.nome) + "Região:\t{}\nExperiência da Região:\t{}\n".format(self.regiao, self.expRegiao)
