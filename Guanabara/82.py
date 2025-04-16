lista = []
par = []
impar = []

while True:
    numero = int(input('Numero: '))
    if numero == 0:
        break
    lista.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(lista,par,impar)