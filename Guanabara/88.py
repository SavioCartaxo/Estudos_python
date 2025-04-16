from random import randint

quantos_jogos = int(input('Quatos jogos você fará? '))
lista_de_numeros = []

for jogo in range(0,quantos_jogos):
    
    for numero in range(0,1):
        print(f'jogo número {jogo+1}: ',end ='')
    
    while len(lista_de_numeros) < 6:
        numero = randint(1,60)
        if numero not in lista_de_numeros:
            lista_de_numeros.append(numero)
            
    lista2 = lista_de_numeros[:]
    lista2.sort()
    lista_de_numeros.clear()
    print(lista2, end='')
    print('')