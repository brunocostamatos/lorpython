from usuario import Usuario
from bau import Bau
from menu import menu, menuRegiao, menuPartida
from regiao import Regiao
import os


""" FORMA ANTIGA 

usuario1= Usuario("DrMonty", 1000, 3, 10, 50, [2,6])

print(usuario1)


bau1 = Bau(usuario1)

print(bau1)

bau1.sortearCartas([])

bau1.verificarSorteio()

bau1.tranformarSorteio()

print(bau1) """

usuario1= Usuario("DrMonty", 1000, 3, 10, "Demacia", 50, [2,6])
print("Trabalho de Comp 2 dos alunos Bruno Costa e Gustavo Camilo.")
print(usuario1)
menu()
opcao = int(input("\nEntre com sua opção: "))

while opcao != 0:
    if opcao == 1:
        print(usuario1)
    elif opcao == 2:
        bau1 = Bau(usuario1)
        print(bau1)
        bau1.sortearCartas([])
        bau1.verificarSorteio()
        bau1.tranformarSorteio()
        print(usuario1)
    elif opcao == 3:

        menuPartida()
        opcaoPartida = int(input("\nEntre com sua opção: "))
        while opcaoPartida != 0:
            if opcaoPartida == 1:
                print("GO")
            menuPartida()
            opcaoPartida = int(input("\nEntre com sua opção: "))
    elif opcao == 4 :
        regiao1 = Regiao(usuario1, usuario1.regiao, usuario1.expRegiao)
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
                print("\nEM DESENVOLVIMENTO")   
            menuRegiao()
            opcaoRegiao = int(input("\nEntre com sua opção: "))
    elif opcao == 5 :
        print("\nEM DESENVOLVIMENTO")
    elif opcao == 6 :
        print("\nEM DESENVOLVIMENTO")
    elif opcao == 7 :
        print("\nEM DESENVOLVIMENTO")
    else:
        print("\nOpção inválida.\n")
    print("")
    menu()
    option = opcao = int(input("\nEntre com sua opção: "))

os.system('cls||clear')




