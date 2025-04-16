from random import randint

lista_de_numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10) )

for numero in lista_de_numeros:
    print(numero, end=' ')

print(f'\n{max(lista_de_numeros)}')
print(f'{min(lista_de_numeros)}')