def dobro(numero):
    return numero *2


def multiplicacao(*fatores):
    
    produto = 1
    
    for numero in fatores:
        produto *= numero
    
    return produto


def fatorial(fatoriando):
    resultado = 1

    for numero in range(1,fatoriando+1):
        resultado *= numero

    return resultado


def moeda(valor):
    return f'R$ {valor:.2f}'