def leiaint(msg=''):
    while True:
        try:
            int(msg)
        
        except:
            print('ERRO. DIGITE UM INTEIRO.')
            msg = input('Digite um inteiro: ')
            continue
        
        else:
            return print(f'Você digitou {msg}')
        

leiaint()