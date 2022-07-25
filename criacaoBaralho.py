from usuario import Usuario
from persistencia import Persistencia

class ForjaDeck: 

    def __init__ (self, usuario):
        self.usuario = usuario
        self.baralho = []
        self.naoTenhoCartas = []
        self.meusDecks = Usuario.getMeusDecks(usuario)
        self.minhasCartas = Usuario.getMinhasCartas(usuario)

    def listaCartasDisponiveis(self):
        print("\nLista de Cartas Disponíveis: \n")
        self.naoTenhoCartas = [item for item in self.minhasCartas if item not in self.baralho]
        for index, value in enumerate(self.naoTenhoCartas):
            print((index + 1), "->", value)
        print("")

    def adicionarCarta(self):   #precisa rever para corrigir com o get e set expRegiao e regiao
            cartaEscolhida = int(input("Escolha a carta que será adicionada no Deck: "))
            if cartaEscolhida > len(self.naoTenhoCartas) or cartaEscolhida <= 0:
                print("\nEscolha inválida\n")
            else:
                print("")
                for index, value in enumerate(self.naoTenhoCartas):
                    if cartaEscolhida == (index + 1):
                        print(value, "\n")
                        self.baralho.append(value)
            print(self)

    def criarBaralho(self):
        if len(self.meusDecks) < 3 and len(self.meusDecks) >= 0:
            self.baralho = []
            cont = 10
            for _ in range(cont):
                self.listaCartasDisponiveis()
                self.adicionarCarta()
            self.meusDecks.append(self.baralho)
            Usuario.setMeusDecks(self.usuario, self.meusDecks)
            persistencia = Persistencia(self.usuario)
            persistencia.salvar()
        else:
            print("\nQuantidade máxima de decks alcançada\n")

    def desfazerBaralho(self):
        print("\nBaralhos que podem ser excluidos:\n")
        for index, value in enumerate(self.meusDecks):
            print((index + 1), "->", value)

        DeckEscolhido = int(input("Escolha a carta que será adicionada no Deck:\n"))
        if DeckEscolhido > len(self.meusDecks) or DeckEscolhido <= 0:
            print("\nEscolha inválida\n")
        else:
            print("")
            for index, value in enumerate(self.meusDecks):
                if DeckEscolhido == (index + 1):
                    del self.meusDecks[index]
            print(self)
            Usuario.setMeusDecks(self.usuario, self.meusDecks)
            persistencia = Persistencia(self.usuario)
            persistencia.salvar()  

    def __str__ (self): #precisa inserir os sets
        print("")
        return "Meu Deck:\t{}\n".format(self.baralho)
