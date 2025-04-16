expressao = input('Expressao: ')
contador1 = contador2 = 0
resposta = 'Expressão funcional.'

for elemento in expressao:
    
    if elemento == '(':
        contador1 += 1
    elif elemento == ')':
        contador2 += 1

    if contador2 > contador1:
        resposta = 'expressão não está correta.'

if contador1 != contador2:
    resposta = 'expressão não está correta.'

print(resposta)