lista = []
while True:
    numero = int(input('Número: '))
    if numero == 0:
        break
    elif numero not in lista:
        lista.append(numero)

lista.sort()
print(lista)