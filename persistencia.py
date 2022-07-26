import os.path
import ast
import json
from usuario import Usuario

class Persistencia:
    def __init__ (self, usuario):
        self.usuario = usuario
        self.nome = Usuario.getNome(usuario)
        self.qntPo= str(Usuario.getQntPo(usuario))
        self.qntCoringa = str(Usuario.getQntCoringa(usuario))
        self.exp = str(Usuario.getExp(usuario))
        self.nivel = str(Usuario.getNivel(usuario))
        self.regiao = Usuario.getRegiao(usuario)
        self.expRegiao = str(Usuario.getExpRegiao(usuario))
        self.nivelRegiao = str(Usuario.getNivelRegiao(usuario))
        self.minhasCartas = str(Usuario.getMinhasCartas(usuario))
        self.meusDecks = str(Usuario.getMeusDecks(usuario))



    def salvar(self):
        f = open('banco.txt', 'w')
        f.write(self.nome+"\n")
        f.write(self.qntPo+"\n")
        f.write(self.qntCoringa+"\n")
        f.write(self.exp+"\n")
        f.write(self.nivel+"\n")
        f.write(self.regiao+"\n")
        f.write(self.expRegiao+"\n")
        f.write(self.nivelRegiao+"\n")
        f.write(self.minhasCartas+"\n")
        f.write(self.meusDecks)
        f.close()
        print(self)

    def verificarExistencia(): #metodo para verificar se o arquivo txt existe ou não, se nao existir irei fazer um usuario "novo"
        existenciaArquivo = os.path.isfile('banco.txt')
        return existenciaArquivo
    
    def recuperarInformacoes(self):
        f = open('banco.txt', 'r')
        teste = []
        for line in f:
            teste.append(line.rstrip('\n'))
        f.close()
        #self.usuario.nome = teste[0]
        Usuario.setNomeUsuario(self.usuario, teste[0])
        #self.usuario.qntPo = int(teste[1])
        Usuario.setQntPo(self.usuario, int(teste[1]))
        #self.usuario.qntCoringa = int(teste[2])
        Usuario.setQntCoringa(self.usuario, int(teste[2]))
        #self.usuario.exp = int(teste[3])
        Usuario.setExp(self.usuario, int(teste[3]))
        #self.usuario.nivel = int(teste[4])
        Usuario.setNivel(self.usuario, int(teste[4]))
        #self.usuario.regiao = teste[5]
        Usuario.setRegiao(self.usuario, teste[5])
        #self.usuario.expRegiao = int(teste[6])
        Usuario.setExpRegiao(self.usuario, int(teste[6]))
        #self.usuario.nivelRegiao = int(teste[7])
        Usuario.setNivelRegiao(self.usuario, int(teste[7]))
        #self.usuario.minhasCartas = convertendoLista
        Usuario.setMinhasCartas(self.usuario, ast.literal_eval(teste[8]))
        #self.usuario.meusDecks = convertendoLista
        Usuario.setMeusDecks(self.usuario, ast.literal_eval(teste[9]))
    
    def getCartasJson(): #metodo para pegar todas as cartas do cartas.json
        cartasJson = open("cartas.json")
        cartas = json.load(cartasJson)
        cartasJson.close()
        return cartas


    def __str__ (self):
        print("")
        return "Salvando\n"
