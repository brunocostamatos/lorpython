from usuario import Usuario
from persistencia import Persistencia

class ForjaCarta: 

    def __init__ (self, usuario):
        self.usuario = usuario
        self.qntPo =  Usuario.getQntPo(usuario)
        self.qntCoringa = Usuario.getQntCoringa(usuario)
        self.minhasCartas = Usuario.getMinhasCartas(usuario)
        self.meusDecks = Usuario.getMeusDecks(usuario)
        self.naoTenhoCartas = []

    def listarNaoTenho(self):
        todasCartas = []
        cartasJson = Persistencia.getCartasJson()
        for i in cartasJson:
            todasCartas.append(i['name'])
        tenhoCartas = self.minhasCartas
        naoTenhoCartas = [item for item in todasCartas if item not in tenhoCartas]
        self.naoTenhoCartas= naoTenhoCartas

    def escolherMetodoCriacao(self):
        print("\nCriar carta através de:\n \n1- Pó \n2- Coringa \n")
        selecionandoMetodo = int(input("Escolha o que pretende gastar para fazer carta: "))
        return selecionandoMetodo

    def verificarSaldo(self, moeda, metodo):
        if (metodo == 1 and moeda >= 10) or (metodo == 2 and moeda != 0):
            return True
        else:
            return False

    def verificarCartaBaralho(self, carta):
        for i in self.meusDecks:
            for j in i:
                if j == carta:
                    return 0


    def criarCarta(self):
        metodo = ForjaCarta.escolherMetodoCriacao(self)
        ForjaCarta.listarNaoTenho(self)
        minhasCartasAntesCriacao = self.minhasCartas
        if metodo == 1:
            moeda = Usuario.getQntPo(self.usuario)
            saldoPositivo = ForjaCarta.verificarSaldo(self, moeda, metodo)
            if saldoPositivo == True: 
                print("\nCartas para fazer usando Pó\n")
                for index, value in enumerate(self.naoTenhoCartas):
                    print((index + 1), "->", value)
                print(0,"-> Sair")
                cartaEscolhida = int(input("\nEscolha a carta que pretende criar: "))
                if cartaEscolhida == 0:
                    print("")
                else:
                    for indexEs, valueEs in enumerate(self.naoTenhoCartas):
                        if cartaEscolhida == (indexEs + 1) :
                            print("\nA seguinte carta foi criada usando Pó: {}".format(valueEs))
                            self.minhasCartas.append(valueEs)
                            moeda -= 10
                    Usuario.setMinhasCartas(self.usuario, self.minhasCartas)
                    Usuario.setQntPo(self.usuario, moeda)
                    persistencia = Persistencia(self.usuario)
                    persistencia.salvar()
            else:
                print("\nVocê não possui saldo para criar carta usando Pó")
        elif metodo == 2:
            moeda =  Usuario.getQntCoringa(self.usuario)
            saldoPositivo = ForjaCarta.verificarSaldo(self, moeda, metodo)
            if saldoPositivo == True: 
                print("\nCartas para fazer usando Coringa\n")
                for index, value in enumerate(self.naoTenhoCartas):
                    print((index + 1), "->", value)
                print(0,"-> Sair")
                cartaEscolhida = int(input("\nEscolha a carta que pretende criar: "))
                if cartaEscolhida == 0:
                    print("")
                else:
                    for indexEs, valueEs in enumerate(self.naoTenhoCartas):
                        if cartaEscolhida == (indexEs + 1):
                            print("\nA seguinte carta foi criada usando Coringa: {}".format(valueEs))
                            self.minhasCartas.append(valueEs)
                            moeda -= 1
                    Usuario.setMinhasCartas(self.usuario, self.minhasCartas)
                    Usuario.setQntCoringa(self.usuario, moeda)
                    persistencia = Persistencia(self.usuario)
                    persistencia.salvar()
            else:
                print("\nVocê não possui saldo para criar carta usando Coringa")
        print(self)

    def desfazerCarta(self):
        cartasSobreviventes = []
        cartaExcluida = ""
        print("\nCartas possíveis de serem desfeitas:\n")
        for index, value in enumerate(self.minhasCartas):
                print((index + 1), "->", value)
        print(0,"-> Sair")
        cartaSelecionada = int(input("\nEscolha a carta que pretende desfazer:"))
        for indexDC, valueDC in enumerate(self.minhasCartas):
            if cartaSelecionada != (indexDC + 1):
                cartasSobreviventes.append(valueDC)
            else:
                if ForjaCarta.verificarCartaBaralho(self, valueDC) != 0:
                    cartaExcluida = valueDC
                else:
                    print("\nVocê não pode excluir essa carta pois ela está sendo usada em um Baralho.")
                    cartaSelecionada = 0
        if cartaSelecionada == 0:
            print("")
        elif cartasSobreviventes == self.minhasCartas:
            print("\nOpção inválida.")
            print(self)
        else:
            print("\nCarta {}".format(cartaExcluida)+" desfeita com sucesso")
            self.qntPo += 5 
            Usuario.setQntPo(self.usuario, self.qntPo)
            Usuario.setMinhasCartas(self.usuario, cartasSobreviventes)
            persistencia = Persistencia(self.usuario)
            persistencia.salvar()
            print(self)

    def __str__ (self):
        print("")
        return "Pó de Carta:\t{}\nCoringa:\t{}\nMinhas Cartas:\t{}\n".format(Usuario.getQntPo(self.usuario), Usuario.getQntCoringa(self.usuario), Usuario.getMinhasCartas(self.usuario))
