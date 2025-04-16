matriz = [[0,0,0],[0,0,0],[0,0,0]]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Elemento na Matriz [{linha+1},{coluna+1}] '))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[ {matriz[linha][coluna]} ]', end='')
    print('')

soma = 0

#soma os números pares
for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            soma += numero

print(f'A soma dos números pares é {soma}')

#soma os elementos da terceira linha
soma = 0
for elemento in matriz:
    soma += elemento[2]

print(f'A soma dos elementos da terceira coluna é {soma}')

#maior valor da segunda linha
print(f'O maior valor da segunda linha é: {max(matriz[1])}')