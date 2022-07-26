from menu import menu, menuRegiao, menuPartida, menuForjaCarta, menuForjaDeck, menuInventario, menuPersistencia
from usuario import Usuario
from bau import Bau
from regiao import Regiao
from partida import Partida
from criacaoCarta import ForjaCarta
from criacaoBaralho import ForjaDeck
from carta import Carta
from baralho import Baralho
from persistencia import Persistencia

import os

existenciaArquivo = Persistencia.verificarExistencia()


usuario1= Usuario("Usuario Não Identificado", 100, 0, 0, 1, "Demacia", 0, 1, [],[])

persistencia = Persistencia(usuario1)

print("Trabalho de Comp 2 dos alunos Bruno Costa e Gustavo Camilo.")

if(existenciaArquivo == True):
    persistencia.recuperarInformacoes()
else:
    nomeUsuario = str(input("\nInsira o nome do seu usuário:"))
    Usuario.setNomeUsuario(usuario1, nomeUsuario)
    persistencia = Persistencia(usuario1)
    persistencia.salvar()

bau1 = Bau(usuario1)
regiao1 = Regiao(usuario1)
forjaCarta = ForjaCarta(usuario1)
forjaDeck = ForjaDeck(usuario1)
inventarioCartas = Carta(usuario1)
inventarioDecks = Baralho(usuario1)
partida = Partida(usuario1)
persistencia = Persistencia(usuario1)


controleError = 0

while controleError != 1:
    try:
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
                        if partida.selecionarDeck() != 0:
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
                            print("\nVocê não pode iniciar uma partida sem um deck.\n")
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
                menuForjaDeck()
                opcaoForjaDeck = int(input("\nEntre com sua opção: "))
                while opcaoForjaDeck != 0:
                    if opcaoForjaDeck == 1:
                        forjaDeck.criarBaralho()
                    elif opcaoForjaDeck == 2:
                        forjaDeck.desfazerBaralho()
                    else:
                        print("\nOpção inválida.\n")
                    menuForjaDeck()
                    opcaoForjaDeck = int(input("\nEntre com sua opção: "))
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
                    if opcaoPersistencia == 2:
                        persistencia = Persistencia(usuario1)
                        persistencia.salvar()
                    else:
                        print("\nOpção inválida.\n")
                    menuPersistencia()
                    opcaoPersistencia = int(input("\nEntre com sua opção: "))
            else:
                print("\nOpção inválida.\n")
            print(usuario1)
            menu()
            opcao = int(input("\nEntre com sua opção: "))
        controleError += 1
    except ValueError:
        print("\nInserção inválida.")



os.system('cls||clear')

#NAO ESQUECER DE MELHORAR A FORMA QUE CHAMA CADA FUNÇÃO DENTRO DE CADA CLASSE

