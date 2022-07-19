from usuario import Usuario

class ForjaCarta: 

    def __init__ (self, usuario):
        self.usuario = usuario
        self.qntPo =  Usuario.getQntPo(usuario)
        self.qntCoringa = Usuario.getQntCoringa(usuario)
        self.minhasCartas = Usuario.getMinhasCartas(usuario)

    def listarNaoTenho(self):
        todasCartas = [1,2,3,4,5,6,7,8,9,10,13,15,20,26,89,58,100]
        tenhoCartas = self.minhasCartas
        naoTenhoCartas = [item for item in todasCartas if item not in tenhoCartas]
        self.naoTenhoCartas= naoTenhoCartas

    def escolherMetodoCriacao(self):
        print("\nCriar carta através de:\n \n1- Pó \n2- Coringa \n")
        selecionandoMetodo = int(input("Escolha o que pretende gastar para fazer carta: "))
        return selecionandoMetodo

    def verificarSaldo(self, moeda, metodo):
        if (metodo == 1 and moeda > 10) or (metodo == 2 and moeda != 0):
            return True
        else:
            return False

    def criarCarta(self):
        metodo = ForjaCarta.escolherMetodoCriacao(self)
        ForjaCarta.listarNaoTenho(self)
        minhasCartasAntesCriacao = self.minhasCartas
        if metodo == 1:
            moeda = self.qntPo
            saldoPositivo = ForjaCarta.verificarSaldo(self, moeda, metodo)
            if saldoPositivo == True: 
                print("\nCartas para fazer usando Pó\n")
                for indexP, valueP in enumerate(self.naoTenhoCartas):
                    print(valueP)
                cartaEscolhida = int(input("\nEscolha a carta que pretende criar: "))
                for indexEs, valueEs in enumerate(self.naoTenhoCartas):
                    if cartaEscolhida == valueEs:
                        print("A seguinte carta foi criada usando Pó: {}".format(cartaEscolhida))
                        self.minhasCartas.append(cartaEscolhida)
                        moeda -= 10
                self.usuario.qntPo = moeda
                self.qntPo = self.usuario.qntPo
            else:
                print("\nVocê não possui saldo para criar carta usando Pó")
        elif metodo == 2:
            moeda = self.qntCoringa
            saldoPositivo = ForjaCarta.verificarSaldo(self, moeda, metodo)
            if saldoPositivo == True: 
                print("\nCartas para fazer usando Coringa\n")
                for indexP, valueP in enumerate(self.naoTenhoCartas):
                    print(valueP)
                cartaEscolhida = int(input("\nEscolha a carta que pretende criar: "))
                for indexEs, valueEs in enumerate(self.naoTenhoCartas):
                    if cartaEscolhida == valueEs:
                        print("A seguinte carta foi criada usando Coringa: {}".format(cartaEscolhida))
                        self.minhasCartas.append(cartaEscolhida)
                        moeda -= 1
                self.usuario.qntCoringa = moeda
                self.qntCoringa = self.usuario.qntCoringa
            else:
                print("\nVocê não possui saldo para criar carta usando Coringa")
        print(self)

    def desfazerCarta(self):
        cartasSobreviventes = []
        print("\nCartas possíveis de serem desfeitas:\n")
        for indexMC, valueMC in enumerate(self.minhasCartas):
            print(valueMC)
        cartaSelecionada = int(input("\nEscolha a carta que pretende desfazer:"))
        for indexDC, valueDC in enumerate(self.minhasCartas):
            if cartaSelecionada != valueDC:
                cartasSobreviventes.append(valueDC)
        if cartasSobreviventes == self.minhasCartas:
            print("Não é possível desfazer a carta selecionada")
        else:
            print("\nCarta {}".format(cartaSelecionada)+" desfeita com sucesso")
            self.qntPo += 5 
            self.usuario.qntPo += 5
            self.minhasCartas = cartasSobreviventes
            self.usuario.minhasCartas = cartasSobreviventes
        print(self)

    def __str__ (self):
        print("")
        return "Pó de Carta:\t{}\nCoringa:\t{}\nMinhas Cartas:\t{}\n".format(self.qntPo, self.qntCoringa, self.minhasCartas)
