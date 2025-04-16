def leiaint(texto):
    contador_de_numeros = 0
    for caractere in texto:
        if caractere.isnumeric():
            contador_de_numeros += 1
    return contador_de_numeros

txt = input('Texto:\n')

print(leiaint(txt))