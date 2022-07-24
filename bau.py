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
        if self.exp >= 100 or self.expRegiao >= 100:
            print("Você tem experiência suficiente, vou sortear as cartas.")
            l = list(range(1, 8))
            random.shuffle(l)
            for i in range(5):
                sorteadas.append(l.pop()) 
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
                self.usuario.qntPo += 10 #precisa inserir o set usuario qntpo
            else:
                self.minhasCartas.append(valueS)
        persistencia = Persistencia(self.usuario)
        persistencia.salvar()
        #Usuario.setQntPo(self, self.qntPo)        
        #Usuario.setMinhasCartas(self, self.minhasCartas)
        
    #def teste(self, usuario):
        #teste2 = Usuario.getQntPo(usuario)
        #tes = teste2 + 2
        #teste = Usuario.setQntPo(self, tes)
        #teste3 = Usuario.getQntPo(usuario)
        #print(teste3, "cu")

    def __str__ (self):
        print("")
        return "BAÚ PARA O USUÁRIO\t{}\n".format(self.nome) + "Pó de Carta:\t{}\nCoringa:\t{}\nXP da Conta:\t{}\nNível da Conta:\t{}\nMinhas Cartas:\t{}\n".format(self.qntPo, self.qntCoringa, self.exp, self.nivel, self.minhasCartas)