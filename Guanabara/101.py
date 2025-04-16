def voto(ano_de_nascimento):
    from datetime import datetime
    idade = datetime.now().year - ano_de_nascimento
    
    resposta = f'Para a idade de {idade}: '

    if idade <= 15:
        resposta += ('Não pode votar')
    elif 16 == idade or idade == 17:
        resposta += ('Voto opicional')
    else:
        resposta += ('Voto obigatório')
    
    return resposta

ano = int(input('Em que ano você nsceu? '))

print(voto(ano))