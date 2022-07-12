
class Persistencia:
    def __init__ (self, nome, qntPo, qntCoringa, exp, nivel, regiao, expRegiao, nivelRegiao, minhasCartas):
        self.nome = nome
        self.qntPo= str(qntPo)
        self.qntCoringa = str(qntCoringa)
        self.exp = str(exp)
        self.nivel = str(nivel)
        self.regiao = regiao
        self.expRegiao = str(expRegiao)
        self.nivelRegiao = str(nivelRegiao)
        self.minhasCartas = str(minhasCartas)

    def ler(self):
        f = open('infos.txt', 'r')
        infos = f.read()
        print(infos)
        f.close()

    def salvar(self,  nome, qntPo, qntCoringa, exp, nivel, regiao, expRegiao, nivelRegiao, minhasCartas):
        f = open('infos.txt', 'w')
        f.write(nome+"\n")
        f.write(str(qntPo)+"\n")
        f.write(str(qntCoringa)+"\n")
        f.write(str(exp)+"\n")
        f.write(str(nivel)+"\n")
        f.write(regiao+"\n")
        f.write(str(expRegiao)+"\n")
        f.write(str(nivelRegiao)+"\n")
        f.write(str(minhasCartas)+"\n")
        print(self)
        f.close()
    def __str__ (self):
        print("")
        return "Salvando\n"
