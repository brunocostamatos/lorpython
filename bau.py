import random
from usuario import Usuario

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
    
    def sortearCartas(self, cartasSorteadas): #Precisa ser feito um sorteio que não repita a carta mais de 3 vezes
        sorteadas=[]
        if self.exp >= 100 or self.expRegiao >= 100:
            print("Você tem experiência suficiente, vou sortear as cartas.")
            for i in range(5):
                sorteadas.append(random.randint(1,8)) 
            print(sorteadas)
            self.cartasSorteadas = sorteadas
        else:
            print("Você não têm experiência suficiente.")

    def verificarSorteio(self): #Falta fazer a verificacao de se tenho a quantidade de cartas máximas, que é 3 por carta.
        for indexS, valueS in enumerate(self.cartasSorteadas):
            for indexM,valueM in enumerate(self.minhasCartas):
                if valueS == valueM:
                    print("Já possuo essa carta {}".format(valueS))
                    self.cartasSorteadas[indexS] = "P" 

    def tranformarSorteio(self): # quebro a função para transformarCoringa, transformarPo e transformar em minha carta?
        for indexS, valueS in enumerate(self.cartasSorteadas):
            if valueS == "P":
                self.qntPo += 10
            else:
                self.minhasCartas.append(valueS)
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