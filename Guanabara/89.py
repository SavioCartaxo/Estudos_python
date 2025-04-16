lista = []
sublista = []

while True:
    
    sublista.append(input('Nome: ').upper())
    sublista.append(float(input('Nota 1: ')))
    sublista.append(float(input('Nota 2: ')))
    lista.append(sublista[:])
    sublista.clear()
    
    resposta = input('Adicionar mais uma pessoa [S/N]? ').upper()

    if resposta == 'N':
        break

print('_'*48)
print(f'|NOME DOS ALUNOS{' '*25}|MÉDIA|')
print('_'*48)

for aluno in lista:
    print(f'|{aluno[0]:.<40}|', end='')
    media = (aluno[1] + aluno[2]) / 2
    print(f'{media:>5.2f}|')
    print('_'*48)