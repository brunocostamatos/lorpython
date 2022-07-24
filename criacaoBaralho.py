from usuario import Usuario
from persistencia import Persistencia

class ForjaDeck: 

    def __init__ (self, usuario):
        self.usuario = usuario
        self.baralho = []
        self.meusDecks = Usuario.getMeusDecks(usuario)
        self.minhasCartas = Usuario.getMinhasCartas(usuario)

    def listaCartasDisponiveis(self):
        print("\nLista de Cartas Disponíveis: \n")
        for index, value in enumerate(self.minhasCartas):
            print((index + 1), "->", value)
        print("")

    def adicionarCarta(self):   #precisa rever para corrigir com o get e set expRegiao e regiao
            cartaEscolhida = int(input("Escolha a carta que será adicionada no Deck: "))
            if cartaEscolhida > len(self.minhasCartas) or cartaEscolhida <= 0:
                print("\nEscolha inválida\n")
            else:
                print("")
                for index, value in enumerate(self.minhasCartas):
                    if cartaEscolhida == (index + 1):
                        print(value, "\n")
                        self.baralho.append(value)
            print(self)

    def criarBaralho(self):
        cont = 10
        for _ in range(cont):
            self.listaCartasDisponiveis()
            self.adicionarCarta()
        print(self)        
        self.meusDecks.append(self.baralho)
        Usuario.setMeusDecks(self.usuario, self.meusDecks)
        persistencia = Persistencia(self.usuario)
        persistencia.salvar()

    def __str__ (self): #precisa inserir os sets
        print("")
        return "Pó de Carta:\t{}\nCoringa:\t{}\nMinhas Cartas:\t{}\n".format(Usuario.getQntPo(self.usuario), Usuario.getQntCoringa(self.usuario), Usuario.getMinhasCartas(self.usuario))
