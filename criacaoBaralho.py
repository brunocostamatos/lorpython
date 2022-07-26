from usuario import Usuario
from persistencia import Persistencia

class ForjaDeck: 

    def __init__ (self, usuario):
        self.usuario = usuario
        self.baralho = []
        self.naoTenhoCartas = []
        self.meusDecks = Usuario.getMeusDecks(usuario)
        self.minhasCartas = Usuario.getMinhasCartas(usuario)
        self.cartaEscolhida = 999999

    def listaCartasDisponiveis(self):
        print("\nLista de Cartas Disponíveis: \n")
        self.naoTenhoCartas = [item for item in self.minhasCartas if item not in self.baralho]
        for index, value in enumerate(self.naoTenhoCartas):
            print((index + 1), "->", value)
        print(0,"-> Sair")
        print("")

    def adicionarCarta(self):
            cartaEscolhida = int(input("Escolha a carta que será adicionada no Deck:"))
            self.cartaEscolhida = cartaEscolhida
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
                if self.cartaEscolhida != 0:
                    self.listaCartasDisponiveis()
                    self.adicionarCarta()
                else:
                    break
            if len(self.baralho) == 10:
                self.meusDecks.append(self.baralho)
                Usuario.setMeusDecks(self.usuario, self.meusDecks)
                persistencia = Persistencia(self.usuario)
                print("Deck criado com sucesso")
                persistencia.salvar()
        else:
            print("\nQuantidade máxima de decks alcançada\n")

    def desfazerBaralho(self):
        print("\nBaralhos que podem ser excluidos:\n")
        for index, value in enumerate(self.meusDecks):
            print((index + 1), "->", value)
        print(0,"-> Sair")
        DeckEscolhido = int(input("Escolha o Deck para ser excluído:"))
        if DeckEscolhido > len(self.meusDecks) or DeckEscolhido < 0:
            print("\nEscolha inválida\n")
        elif DeckEscolhido == 0:
            print("")
        else:
            print("")
            for index, value in enumerate(self.meusDecks):
                if DeckEscolhido == (index + 1):
                    del self.meusDecks[index]
            print(self)
            Usuario.setMeusDecks(self.usuario, self.meusDecks)
            persistencia = Persistencia(self.usuario)
            persistencia.salvar()  

    def __str__ (self):
        print("")
        return "Meu Deck:\t{}\n".format(self.baralho)
