def linha():
    return '='*34


def isalphaspace(texto):
    
    for digito in texto:
        contador = 0
        if digito.isalpha() or digito.isspace():
            contador += 0
        else: 
            contador +=1
            break
    
    if contador == 0:
        return True
    else:
        return False