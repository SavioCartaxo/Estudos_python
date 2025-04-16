lista = []
dados = []

for c in range(0,5):
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()

print(lista)

for posicao, elemento in enumerate(lista):
    
    
    if posicao == 0:
        maior = menor = elemento[1]
        pessoamenos = [elemento[0]]
        pessoamais = [elemento[0]]

    else:
        if elemento[1] > maior:
            maior = elemento[1]
            pessoamais.clear()
            pessoamais.append(elemento[0])
        
        elif elemento[1] < menor:
            menor = elemento[1]
            pessoamenos.clear()
            pessoamenos.append(elemento[0])
        
        elif elemento[1] == maior:
            pessoamais.append(elemento[0])

        elif elemento[1] == menor:
            pessoamenos.append(elemento[0])


print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'A(s) pessoas mais pesada(s) foi(am) {pessoamais}')
print(f'A(s) pessoas mais leve(s) foi(am) {pessoamenos}')