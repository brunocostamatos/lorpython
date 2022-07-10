
class ForjaCarta: 

    def __init__ (self, usuario):
        self.usuario = usuario
        self.qntPo = usuario.qntPo
        self.qntCoringa = usuario.qntCoringa
        self.minhasCartas = usuario.minhasCartas

    def listarNaoTenho(self):
        todasCartas = [1,2,3,4,5,6,7,8,9,10,13,15,20,26,89,58,100]
        tenhoCartas = self.minhasCartas
        naoTenhoCartas = [item for item in todasCartas if item not in tenhoCartas]
        self.naoTenhoCartas= naoTenhoCartas

    def escolherMetodoCriacao(self):
        print("\nCriar carta através de:\n \n1- Pó \n2- Coringa \n")
        selecionandoMetodo = int(input("Escolha o que pretende gastar para fazer carta: "))
        return selecionandoMetodo

    def criarCarta(self):
        metodo = ForjaCarta.escolherMetodoCriacao(self)
        ForjaCarta.listarNaoTenho(self)
        if metodo == 1:
            moeda = self.qntPo
            print("\nCartas para fazer usando Pó\n")
            for indexP, valueP in enumerate(self.naoTenhoCartas):
                print(valueP)
            cartaEscolhida = int(input("Escolha a carta que pretende criar: "))
            for indexEs, valueEs in enumerate(self.naoTenhoCartas):
                if cartaEscolhida == valueEs:
                    print("A seguinte carta foi criada usando Pó: {}".format(cartaEscolhida))
                    self.minhasCartas.append(cartaEscolhida)
                    moeda -= 10
            self.qntPo = moeda
            self.usuario.qntPo = moeda
        elif metodo == 2:
            moeda = self.qntCoringa
            print("\nCartas para fazer usando Coringa\n")
            for indexP, valueP in enumerate(self.naoTenhoCartas):
                print(valueP)
            cartaEscolhida = int(input("Escolha a carta que pretende criar: "))
            for indexEs, valueEs in enumerate(self.naoTenhoCartas):
                if cartaEscolhida == valueEs:
                    print("A seguinte carta foi criada usando Coringa: {}".format(cartaEscolhida))
                    self.minhasCartas.append(cartaEscolhida)
                    moeda -= 1
            self.qntCoringa = moeda
            self.usuario.qntCoringa = moeda
        print(self)
    def desfazerCarta(self):
        print("\n{}".format(self.qntCoringa))
    
    def __str__ (self):
        print("")
        return "Pó de Carta:\t{}\nCoringa:\t{}\nMinhas Cartas:\t{}\n".format(self.qntPo, self.qntCoringa, self.minhasCartas)
