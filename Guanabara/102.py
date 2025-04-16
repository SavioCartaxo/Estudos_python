def fatorial(numero_fatorial, show=True):
    resultado = 1
    
    for numero_da_multiplicacao in range(numero_fatorial,0,-1):

        resultado *= numero_da_multiplicacao
        
        if show == True:
            print(numero_da_multiplicacao, end='')

            if numero_da_multiplicacao > 1:
                print(' x ',end='')
            else:
                print(f' = {resultado}', end='')

        if show == False:
            return resultado


print(fatorial(5,show=False))