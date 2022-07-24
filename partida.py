import random
from bau import Bau
from usuario import Usuario
from persistencia import Persistencia

class Partida:
    def __init__ (self, usuario):
        self.usuario = usuario
        self.nome =  Usuario.getNome(usuario)
        self.qntPo = Usuario.getQntPo(usuario)
        self.qntCoringa = Usuario.getQntCoringa(usuario)
        self.exp = Usuario.getExp(usuario)
        self.nivel = Usuario.getNivel(usuario)
        self.minhasCartas = Usuario.getMinhasCartas(usuario)
    
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

    def incrementarXPUsuario(self): #INSERIR SET EXP USUARIO
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
            persistencia = Persistencia(self.usuario)
            persistencia.salvar()

    def avancarNivelUsuario(self):      #INSERIR SET EXP USUARIO E NIVEL DE USUARIO  
        recompensa = Bau(self.usuario)
        print(recompensa)
        recompensa.sortearCartas([])
        recompensa.verificarSorteio()
        recompensa.tranformarSorteio()
        self.usuario.exp = 0
        self.usuario.nivel += 1
        print("\nBAÚ PARA O USUÁRIO\t{}\n".format(self.nome) + "Pó de Carta:\t{}\nCoringa:\t{}\nXP da Conta:\t{}\nNível da Conta:\t{}\nMinhas Cartas:\t{}\n".format(self.qntPo, self.qntCoringa, self.exp, self.nivel, self.minhasCartas))
        persistencia = Persistencia(self.usuario)
        persistencia.salvar()
        
    def __str__ (self):
        print("")
        return "Partida do jogo Legends of Runeterra"
