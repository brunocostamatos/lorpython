import random

class Bau:
    def __init__ (self, usuario):
        self.usuario = usuario
        self.cartasSorteadas = []
    
    def sortearCartas(self, cartasSorteadas): #Precisa ser feito um sorteio que não repita a carta mais de 3 vezes
        sorteadas=[]
        if self.usuario.exp >= 100 or self.usuario.expRegiao >= 100:
            print("Você tem experiência suficiente, vou sortear as cartas.")
            for i in range(5):
                sorteadas.append(random.randint(1,8)) 
            print(sorteadas)
            self.cartasSorteadas = sorteadas
        else:
            print("Você não têm experiência suficiente.")

    def verificarSorteio(self): #Falta fazer a verificacao de se tenho a quantidade de cartas máximas, que é 3 por carta.
        for indexS, valueS in enumerate(self.cartasSorteadas):
            for indexM,valueM in enumerate(self.usuario.minhasCartas):
                if valueS == valueM:
                    print("Já possuo essa carta {}".format(valueS))
                    self.cartasSorteadas[indexS] = "P" 

    def tranformarSorteio(self): # quebro a função para transformarCoringa, transformarPo e transformar em minha carta?
        for indexS, valueS in enumerate(self.cartasSorteadas):
            if valueS == "P":
                self.usuario.qntPo += 10
            else:
                self.usuario.minhasCartas.append(valueS)

    def __str__ (self):
        print("")
        return "BAÚ PARA O USUÁRIO\t{}\n".format(self.usuario.nome) + "Pó de Carta:\t{}\nCoringa:\t{}\nXP da Conta:\t{}\nNível da Conta:\t{}\nMinhas Cartas:\t{}\n".format(self.usuario.qntPo, self.usuario.qntCoringa, self.usuario.exp, self.usuario.nivel, self.usuario.minhasCartas)