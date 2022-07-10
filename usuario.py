class Usuario: 

    def __init__ (self, nome, qntPo, qntCoringa, exp, nivel, regiao, expRegiao, nivelRegiao, minhasCartas):
        self.nome = nome
        self.qntPo= qntPo
        self.qntCoringa = qntCoringa
        self.exp = exp
        self.nivel = nivel
        self.regiao = regiao
        self.expRegiao = expRegiao
        self.nivelRegiao = nivelRegiao
        self.minhasCartas = minhasCartas
            

    def __str__ (self):
        print("")
        return "Usuário:\t{}\nPó de Carta:\t{}\nCoringa:\t{}\nXP da Conta:\t{}\nNível da Conta:\t{}\nRegião:\t{}\nNível Região:\t{}\nMinhas Cartas:\t{}\n".format(self.nome, self.qntPo, self.qntCoringa, self.exp, self.nivel, self.regiao, self.nivelRegiao, self.minhasCartas)
