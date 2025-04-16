import funcoes


while True:
    
    print(f'''
              Menu
{funcoes.linha()}
1. Mostra a Lista de pessoas.
2. Adicionar uma pessoa à lista.
3. Encerrar programa.
{funcoes.linha()}''')

    while True:

        try:
            opcao_escolhida = int(input('Escolha a opção: '))

            if opcao_escolhida in (1,2,3):    
                break
            else:
                print('ERRO. DIGITE UMA ENTRADA VÁLIDA')

        except:
            print('ERRO. DIGITE UMA ENTRADA VÁLIDA')


    if opcao_escolhida == 1:
        try:
            with open('lista.txt', 'r', encoding='UTF-8') as nomes:
                print('\n',nomes.read(), '\n')
        except:
            print('A lista está vazia')

    elif opcao_escolhida == 2:

        while True:    
            nome_a_ser_adicionado = input('Nome da Pessoa: ')

            if funcoes.isalphaspace(nome_a_ser_adicionado[0:-3]):
                nome_formatado = (f'{nome_a_ser_adicionado[:-3]:<28}{nome_a_ser_adicionado[-2:]} Anos')
                break
            else:
                print('ISSO NÃO É UM NOME DE PESSOA.')
        
        with open('lista.txt', 'a', encoding='UTF-8') as lista:
            lista.write(nome_formatado + '\n')
        
        print(f'{nome_a_ser_adicionado[0:-3]} adicionado à lista.')

    elif opcao_escolhida == 3:
        print('FIM DA OPEREÇÃO')
        break