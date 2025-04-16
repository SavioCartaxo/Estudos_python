numeros = [[],[]]

for c in range(1,8):
    
    elemento = int(input('Numero: '))
    
    if elemento % 2 == 0:
        numeros[0].append(elemento)

    else:
        numeros[1].append(elemento)
    print(numeros)

numeros[0].sort()
numeros[1].sort()

print(f'A lista de números pares é: {numeros[0]}')
print(f'A lista de números ímpares é: {numeros[1]}')