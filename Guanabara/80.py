lista = []
for numero in range(1,6):
    numero = int(input('Número: '))
    if len(lista) == 0 or numero >= lista[-1]:
        lista.append(numero)
    elif numero <= lista[0]:
        lista.insert(0,numero)
    else:
        for posicao in range(0, len(lista)-1):
            if numero >= lista[posicao] and numero <= lista[posicao+1]:
                lista.insert(posicao+1,numero)
                break

print(lista)