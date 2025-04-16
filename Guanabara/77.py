lista = ('pao', 'queijo', 'presunto','tender','biscoito')

for elemento in lista:
    elemento = elemento.upper()
    print(f'''Na palavra '{elemento:^10}',existem as Vogais: ''',end='')
    
    for letra in range(0,len(elemento)):
        if elemento[letra] in 'AEIOU':
            print(elemento[letra], end=' ')
    
    print('')