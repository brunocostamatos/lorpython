class Usuario:

    def __init__ (self, nome, qntPo, qntCoringa, exp, nivel, regiao, expRegiao, nivelRegiao, minhasCartas, meusDecks):
        self.nome = nome
        self.qntPo= qntPo
        self.qntCoringa = qntCoringa
        self.exp = exp
        self.nivel = nivel
        self.regiao = regiao
        self.expRegiao = expRegiao
        self.nivelRegiao = nivelRegiao
        self.minhasCartas = minhasCartas
        self.meusDecks = meusDecks


    def __str__ (self):
        print("")
        return "Usuário:\t{}\nPó de Carta:\t{}\nCoringa:\t{}\nXP da Conta:\t{}\nNível da Conta:\t{}\nRegião:\t{}\nNível Região:\t{}\nMinhas Cartas:\t{}\n".format(self.nome, self.qntPo, self.qntCoringa, self.exp, self.nivel, self.regiao, self.nivelRegiao, self.minhasCartas)

    def setNomeUsuario(self, nome):
        self.nome = nome

    def setQntPo(self, qntPo):
        self.qntPo = qntPo

    def setQntCoringa(self, qntCoringa):
        self.qntCoringa = qntCoringa

    def setExp(self, exp):
        self.exp = exp
    
    def setNivel(self, nivel):
        self.nivel = nivel

    def setRegiao(self, regiao):
        self.regiao = regiao
    
    def  setExpRegiao(self, expRegiao):
        self.expRegiao = expRegiao

    def setNivelRegiao(self, nivelRegiao):
        self.nivelRegiao = nivelRegiao
    
    def setMinhasCartas(self, minhasCartas):
        self.minhasCartas = minhasCartas

    def setMeusDecks(self, meusDecks):
        self.meusDecks = meusDecks
    
    def getNome(self):
        return self.nome

    def getQntPo(self): 
        return self.qntPo
    
    def getQntCoringa(self):
        return self.qntCoringa
    
    def getExp(self):
        return self.exp
    
    def getNivel(self):
        return self.nivel
    
    def getRegiao(self):
        return self.regiao
    
    def getExpRegiao(self):
        return self.expRegiao
    
    def getNivelRegiao(self):
        return self.nivelRegiao
    
    def getMinhasCartas(self):
        return self.minhasCartas
    
    def getMeusDecks(self):
        return self.meusDecks
    
