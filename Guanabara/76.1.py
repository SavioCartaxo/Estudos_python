lista = ('Caderno', 10, 'Lápis', 1, 'Borracha', 3.)

for posicao, elemento in enumerate(lista):
    if posicao % 2 == 0:
        print(f'{elemento:.<20}R${lista[posicao+1]:>5.2f}')