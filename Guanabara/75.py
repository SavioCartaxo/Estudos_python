lista_de_numeros = ((int(input('Número: '))),
                    (int(input('Número: '))),
                    (int(input('Número: '))),
                    (int(input('Número: '))))

print(f'O valor 9 apareceu {lista_de_numeros.count(9)} vezes.')
print(f'O valor 3 apareceu primeiro na posiçã {lista_de_numeros.index(3)+1}.')

numeros_pares = 0

for numero in lista_de_numeros:
    if numero % 2 == 0:
        numeros_pares += 1

print(f'Há {numeros_pares} números pares.')