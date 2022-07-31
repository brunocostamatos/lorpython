import random
from usuario import Usuario
from persistencia import Persistencia

class Bau:
    def __init__ (self, usuario):
        self.usuario = usuario
        self.nome = Usuario.getNome(usuario)
        self.qntPo = Usuario.getQntPo(usuario)
        self.qntCoringa = Usuario.getQntCoringa(usuario)
        self.exp = Usuario.getExp(usuario)
        self.nivel = Usuario.getNivel(usuario)
        self.expRegiao = Usuario.getExpRegiao(usuario)
        self.minhasCartas = Usuario.getMinhasCartas(usuario)
        self.cartasSorteadas = []
    
    def sortearCartas(self, cartasSorteadas): #https://itecnote.com/tecnote/python-how-to-generate-unique-random-numbers-that-dont-repeat/ aqui tem o link de pq meti o shuffle
        sorteadas=[]
        leituraArquivoCartas = []
        if self.exp >= 100 or self.expRegiao >= 100:
            print("Você tem experiência suficiente, vou sortear as cartas.")
            cartasJson = Persistencia.getCartasJson()
            for i in cartasJson:
                leituraArquivoCartas.append(i['name'])
            random.shuffle(leituraArquivoCartas)
            for i in range(5):
                sorteadas.append(leituraArquivoCartas.pop())
            print(sorteadas)
            self.cartasSorteadas = sorteadas
            
        else:
            print("Você não têm experiência suficiente.")

    def verificarSorteio(self):
        for indexS, valueS in enumerate(self.cartasSorteadas):
            for indexM,valueM in enumerate(self.minhasCartas):
                if valueS == valueM:
                    print("Já possuo essa carta {}".format(valueS))
                    self.cartasSorteadas[indexS] = "P" 

    def tranformarSorteio(self):
        for indexS, valueS in enumerate(self.cartasSorteadas):
            if valueS == "P":
                self.qntPo += 10
                #self.usuario.qntPo += 10
                Usuario.setQntPo(self.usuario, self.qntPo)
            else:
                self.minhasCartas.append(valueS)
        Usuario.setMinhasCartas(self.usuario, self.minhasCartas)
        persistencia = Persistencia(self.usuario)
        persistencia.salvar()
        
    def __str__ (self):
        print("")
        return "BAÚ PARA O USUÁRIO\t{}\n".format(self.nome) + "Pó de Carta:\t{}\nCoringa:\t{}\nXP da Conta:\t{}\nNível da Conta:\t{}\nMinhas Cartas:\t{}\n".format(Usuario.getQntPo(self.usuario), Usuario.getQntCoringa(self.usuario), Usuario.getExp(self.usuario), Usuario.getNivel(self.usuario), Usuario.getMinhasCartas(self.usuario))