class Usuario: 

    def __init__ (self, nome, qntPo, qntCoringa, exp, regiao, expRegiao, minhasCartas):
        self.nome = nome
        self.qntPo= qntPo
        self.qntCoringa = qntCoringa
        self.exp = exp
        self.regiao = regiao
        self.expRegiao = expRegiao
        self.minhasCartas = minhasCartas
            

    def __str__ (self):
        print("")
        return "Usuário:\t{}\nPó de Carta:\t{}\nCoringa:\t{}\nXP da Conta:\t{}\nRegião:\t{}\nXP Região:\t{}\nMinhas Cartas:\t{}\n".format(self.nome, self.qntPo, self.qntCoringa, self.exp, self.regiao, self.expRegiao, self.minhasCartas)
