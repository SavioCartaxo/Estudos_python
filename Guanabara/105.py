def notas(*num):

    lista = []
    for numero in num:
        lista.append(numero)
    maior = max(lista)
    menor = min(lista)

    soma = 0
    for numero in lista:
        soma += numero
    media = soma / len(lista)
    
    return print(f'''
Maior nota: {maior}
Menor nota: {menor}
Quantidade de notas: {len(lista)}
Media das notas: {media}
Notas: {lista}
''')


print(notas(10,10,10,9))