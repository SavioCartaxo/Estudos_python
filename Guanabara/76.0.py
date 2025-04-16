lista = ('CadernoPreço:10.00', 'LápisPreço:1.00', 'BorrachaPreço:3.00')

for posicao,elemento in enumerate(lista):
    print(f'''{elemento[0:lista[posicao].find('Preço:')]:.<20}R${elemento[lista[posicao].find(':')+1:]:>6}''')