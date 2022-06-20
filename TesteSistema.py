from usuario import Usuario
from bau import Bau


usuario1= Usuario("DrMonty", 1000, 3, 10, 50, [2,6])

print(usuario1)


bau1 = Bau(usuario1)

print(bau1)

bau1.sortearCartas([])

bau1.verificarSorteio()

bau1.tranformarSorteio()

print(bau1)







