lista = []
while True:
    numero = int(input('Número: '))
    resposta = input('Continuar?')
    if resposta in 'nN':
        break
    else:
        lista.append(numero)

if 5 in lista:
    aparicoes_do_5 = lista.count(5)
else:
    aparicoes_do_5 = 0

print(len(lista))
lista.sort(reverse=True)
print(lista)
print(f'O 5 apareceu {aparicoes_do_5} vezes')