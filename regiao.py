from bau import Bau
from usuario import Usuario
from persistencia import Persistencia

class Regiao:
    def __init__ (self, usuario):
        self.usuario = usuario
        self.regiao = Usuario.getRegiao(usuario)
        self.expRegiao = Usuario.getExpRegiao(usuario)
        self.nivelRegiao = Usuario.getNivelRegiao(usuario)
        self.qntCoringa = Usuario.getQntCoringa(usuario)
        self.listaRegioes = []

    def listarRegioes(self):
        listaRegioes=['Aguas de Sentina', 'Bandópolis', 'Demacia', 'Freljord', 'Ilha das Sombras', 'Ionia', 'Noxus', 'Piltover e Zaun', 'Shurima', 'Targon']
        print("\nLista de Regiões: \n")
        for index, value in enumerate(listaRegioes):
            print((index + 1), "->", value)
        print("")
        self.listaRegioes = listaRegioes

    def mudarRegiao(self):
        mudandoRegiao = int(input("Escolha sua nova Região: "))
        if mudandoRegiao > 10 or mudandoRegiao <= 0:
            print("\nEscolha inválida\n")
        else:
            print("")
            for index, value in enumerate(self.listaRegioes):
                if mudandoRegiao == (index + 1):
                    if value != self.regiao:
                        print(value, "\n")
                        print("Mudança realizada com sucesso.")
                        #self.usuario.regiao = value
                        Usuario.setRegiao(self.usuario, value)
                        #self.usuario.expRegiao = 0
                        Usuario.setExpRegiao(self.usuario, 0)
                        #self.usuario.nivelRegiao = 1
                        Usuario.setNivelRegiao(self.usuario, 1)
                        #self.regiao = value
                        #self.expRegiao = 0
                        #self.nivelRegiao = 1
                        persistencia = Persistencia(self.usuario)
                        persistencia.salvar()
                    else:
                        print("A sua atual Região já é", Usuario.getRegiao(self.usuario),", mudança não realizada.")
            
        print(self)

    def incrementarXPRegiao(self):
        self.expRegiao += 10
        Usuario.setExpRegiao(self.usuario, self.expRegiao)
        print("\nExperiência da Região {}".format(Usuario.getRegiao(self.usuario)) + ": {}".format(Usuario.getExpRegiao(self.usuario)) + "\n")
        persistencia = Persistencia(self.usuario)
        persistencia.salvar()

    def avancarNivelRegiao(self):
        recompensa = Bau(self.usuario)
        print(recompensa)
        recompensa.sortearCartas([])
        recompensa.verificarSorteio()
        recompensa.tranformarSorteio()
        #self.expRegiao = 0
        Usuario.setExpRegiao(self.usuario, 0)
        self.nivelRegiao += 1
        Usuario.setNivelRegiao(self.usuario, self.nivelRegiao)
        self.qntCoringa += 1
        Usuario.setQntCoringa(self.usuario, self.qntCoringa)
        print("\n Parabéns! Você ganhou mais 1 coringa por aumentar o nível da Região: " + format(Usuario.getRegiao(self.usuario)))
        #self.usuario.expRegiao = 0
        #self.usuario.nivelRegiao += 1
        print("\nBAÚ PARA O USUÁRIO\t{}\n".format(Usuario.getNome(self.usuario)) + "Pó de Carta:\t{}\nCoringa:\t{}\nXP da Conta:\t{}\nNível da Conta:\t{}\nMinhas Cartas:\t{}\n".format(Usuario.getQntPo(self.usuario),Usuario.getQntCoringa(self.usuario), Usuario.getExp(self.usuario), Usuario.getNivel(self.usuario), Usuario.getMinhasCartas(self.usuario)))
        persistencia = Persistencia(self.usuario)
        persistencia.salvar()

    def __str__ (self):
        print("")
        return "REGIÃO ATUAL DO USUÁRIO\t{}\n".format(Usuario.getNome(self.usuario)) + "Região:\t{}\nNível da Região:\t{}\nExperiência da Região:\t{}\n".format(Usuario.getRegiao(self.usuario), Usuario.getNivelRegiao(self.usuario), Usuario.getExpRegiao(self.usuario))
