from usuario import Usuario
from persistencia import Persistencia

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
                Usuario.setMinhasCartas(self.usuario, self.minhasCartas)
                Usuario.setQntPo(self.usuario, moeda)
                persistencia = Persistencia(self.usuario)
                persistencia.salvar()
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
                Usuario.setMinhasCartas(self.usuario, self.minhasCartas)
                Usuario.setQntCoringa(self.usuario, moeda)
                persistencia = Persistencia(self.usuario)
                persistencia.salvar()
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
            print("Inserção inválida.")
        else:
            print("\nCarta {}".format(cartaSelecionada)+" desfeita com sucesso")
            self.qntPo += 5 
            Usuario.setQntPo(self.usuario, self.qntPo)
            Usuario.setMinhasCartas(self.usuario, cartasSobreviventes)
            persistencia = Persistencia(self.usuario)
            persistencia.salvar()
        print(self)

    def __str__ (self): #precisa inserir os sets
        print("")
        return "Pó de Carta:\t{}\nCoringa:\t{}\nMinhas Cartas:\t{}\n".format(Usuario.getQntPo(self.usuario), Usuario.getQntCoringa(self.usuario), Usuario.getMinhasCartas(self.usuario))
