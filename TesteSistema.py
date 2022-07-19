from usuario import Usuario
from bau import Bau
from menu import menu, menuRegiao, menuPartida, menuForjaCarta, menuInventario, menuPersistencia
from regiao import Regiao
from partida import Partida
from criacaoCarta import ForjaCarta
from carta import Carta
from baralho import Baralho
from persistencia import Persistencia

import os


usuario1= Usuario("DrMonty", 1000, 3, 95, 1, "Demacia", 90, 1, [2,6])
bau1 = Bau(usuario1)
regiao1 = Regiao(usuario1, usuario1.regiao, usuario1.expRegiao, usuario1.nivelRegiao)
forjaCarta = ForjaCarta(usuario1)
inventarioCartas = Carta(usuario1)
inventarioDecks = Baralho(usuario1)
partida = Partida(usuario1)
persistencia = Persistencia(usuario1.nome, usuario1.qntPo, usuario1.qntCoringa, usuario1.exp, usuario1.nivel, usuario1.regiao, usuario1.expRegiao, usuario1.nivelRegiao, usuario1.minhasCartas)


print("Trabalho de Comp 2 dos alunos Bruno Costa e Gustavo Camilo.")
print(usuario1)
menu()
opcao = int(input("\nEntre com sua opção: "))

while opcao != 0:
    if opcao == 1:
        print(usuario1)
    elif opcao == 2:
        
        print(bau1)
        bau1.sortearCartas([])
        bau1.verificarSorteio()
        bau1.tranformarSorteio()
        #bau1.teste(usuario1)
        print(usuario1)
    elif opcao == 3:
        menuPartida()
        opcaoPartida = int(input("\nEntre com sua opção: "))
        while opcaoPartida != 0:
            if opcaoPartida == 1:
                partida.escolherDificuldade()
                partida.jogo()
                partida.verificarVencedor()
                if partida.vencedor == 1:
                    partida.incrementarXPUsuario()
                    regiao1.incrementarXPRegiao()
                    if usuario1.exp >= 100:
                        partida.avancarNivelUsuario()
                    if regiao1.expRegiao >= 100:
                        regiao1.avancarNivelRegiao()
            else:
                print("\nOpção inválida.\n")
            menuPartida()
            opcaoPartida = int(input("\nEntre com sua opção: "))
    elif opcao == 4 :
        print(regiao1)
        menuRegiao()
        opcaoRegiao = int(input("\nEntre com sua opção: "))
        while opcaoRegiao != 0:
            if opcaoRegiao == 1:
                regiao1.listarRegioes()
                regiao1.mudarRegiao()
            elif opcaoRegiao == 2:
                regiao1.incrementarXPRegiao()
            elif opcaoRegiao == 3:
                regiao1.avancarNivelRegiao()
            else:
                print("\nOpção inválida.\n")
            menuRegiao()
            opcaoRegiao = int(input("\nEntre com sua opção: "))
    elif opcao == 5 :
        print(forjaCarta)
        menuForjaCarta()
        opcaoForjaCarta = int(input("\nEntre com sua opção: "))
        while opcaoForjaCarta != 0:
            if opcaoForjaCarta == 1:
                forjaCarta.criarCarta()
            elif opcaoForjaCarta == 2:
                forjaCarta.desfazerCarta()
            else:
                print("\nOpção inválida.\n")
            menuForjaCarta()
            opcaoForjaCarta = int(input("\nEntre com sua opção: "))
    elif opcao == 6 :
        print("\nEM DESENVOLVIMENTO")
    elif opcao == 7 :
        menuInventario()
        opcaoInventario = int(input("\nEntre com sua opção: "))
        while opcaoInventario != 0:
            if opcaoInventario == 1:
                inventarioCartas.verCartas()
            elif opcaoInventario == 2:
                inventarioDecks.verDecks()
            else:
                print("\nOpção inválida.\n")
            menuInventario()
            opcaoInventario = int(input("\nEntre com sua opção: "))
    elif opcao == 8:
        menuPersistencia()
        opcaoPersistencia = int(input("\nEntre com sua opção: "))
        while opcaoPersistencia != 0:
            if opcaoPersistencia == 1:
                persistencia.ler()
            elif opcaoPersistencia == 2:
                persistencia.salvar(usuario1.nome, usuario1.qntPo, usuario1.qntCoringa, usuario1.exp, usuario1.nivel, usuario1.regiao, usuario1.expRegiao, usuario1.nivelRegiao, usuario1.minhasCartas)
            else:
                print("\nOpção inválida.\n")
            menuPersistencia()
            opcaoPersistencia = int(input("\nEntre com sua opção: "))
    else:
        print("\nOpção inválida.\n")
    print("")
    menu()
    option = opcao = int(input("\nEntre com sua opção: "))

os.system('cls||clear')

#NAO ESQUECER DE MELHORAR A FORMA QUE CHAMA CADA FUNÇÃO DENTRO DE CADA CLASSE
#FAZER AS CORREÇÕES DE QUANDO O USUARIO ENTRA COM ALGO ERRADO NOS INPUTS
