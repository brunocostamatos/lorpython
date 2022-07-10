from bau import Bau

class Regiao:
    def __init__ (self, usuario, regiao, expRegiao, nivelRegiao):
        self.usuario = usuario
        self.regiao = regiao
        self.expRegiao = expRegiao
        self.nivelRegiao = nivelRegiao
    
    def listarRegioes(self): #precisa rever para quando a experiencia da atrelada a regiao e nao vai ser zerada sempre q mudar
        listaRegioes=['Aguas de Sentina', 'Bandópolis', 'Demacia', 'Freljord', 'Ilha das Sombras', 'Ionia', 'Noxus', 'Piltover e Zaun', 'Shurima', 'Targon']
        print("\nLista de Regiões: \n")
        for index, value in enumerate(listaRegioes):
            print((index + 1), "->", value)
        print("")
        self.listaRegioes = listaRegioes

    def mudarRegiao(self):   #precisa rever para corrigir com o get e set expRegiao e regiao
        mudandoRegiao = int(input("Escolha sua nova Região: "))
        if mudandoRegiao > 10:
            print("\nEscolha inválida\n")
        else:
            print("")
            for index, value in enumerate(self.listaRegioes):
                if mudandoRegiao == (index + 1):
                    if value != self.usuario.regiao:
                        print(value, "\n")
                        print("Mudança realizada com sucesso.")
                        self.usuario.regiao = value
                        self.usuario.expRegiao = 0
                        self.regiao = value
                        self.expRegiao = 0
                    else:
                        print("A sua atual Região já é", self.usuario.regiao,", mudança não realizada.")
        print(self)

    def incrementarXPRegiao(self): #precisa rever para corrigir com o get e set expRegiao
        self.expRegiao += 10
        self.usuario.expRegiao += 10
        print("\nExperiência da Região {}".format(self.regiao) + ": {}".format(self.expRegiao) + "\n")

    def avancarNivelRegiao(self):  #precisa ver com o get e set expRegiao e nivelRegiao
        recompensa = Bau(self.usuario)
        print(recompensa)
        recompensa.sortearCartas([])
        recompensa.verificarSorteio()
        recompensa.tranformarSorteio()
        self.expRegiao = 0
        self.nivelRegiao += 1
        self.usuario.expRegiao = 0
        self.usuario.nivelRegiao += 1
        print("\nBAÚ PARA O USUÁRIO\t{}\n".format(self.usuario.nome) + "Pó de Carta:\t{}\nCoringa:\t{}\nXP da Conta:\t{}\nNível da Conta:\t{}\nMinhas Cartas:\t{}\n".format(self.usuario.qntPo, self.usuario.qntCoringa, self.usuario.exp, self.usuario.nivel, self.usuario.minhasCartas))
    

    def __str__ (self):
        print("")
        return "REGIÃO ATUAL DO USUÁRIO\t{}\n".format(self.usuario.nome) + "Região:\t{}\nNível da Região:\t{}\nExperiência da Região:\t{}\n".format(self.regiao, self.nivelRegiao, self.expRegiao)