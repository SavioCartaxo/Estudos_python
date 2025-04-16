lista = []
for c in range(1,6):
    numero = int(input('Número: '))
    lista.append(numero)

print(f'O maior valor foi {max(lista)}')
print(f'O menor valor foi {min(lista)}')