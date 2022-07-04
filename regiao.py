class Regiao:
    def __init__ (self, usuario, regiao, expRegiao):
        self.usuario = usuario
        self.regiao = regiao
        self.expRegiao = expRegiao
    
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
        self.expRegiao = self.expRegiao + 5
        self.usuario.expRegiao = self.usuario.expRegiao + 5
        print(self)

    def avancarNivelRegiao(self):  #precisa ver com o get e set expRegiao e nivelRegiao
        pass

    def __str__ (self):
        print("")
        return "REGIÃO ATUAL DO USUÁRIO\t{}\n".format(self.usuario.nome) + "Região:\t{}\nExperiência da Região:\t{}\n".format(self.regiao, self.expRegiao)