import os
import time
import msvcrt

# Posição inicial da nave
x = 40
y = 23  # Nave fica na ultima linha(linha 23)
largura = 80

nave = [
    "  ^",
    " /_\\",
    "|=|=|"
]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def desenhar(x, y):
    for linha in range(y):  # Imprime as linhas vazias acima
        print()
    for parte in nave:  # Desenha a nave
        print(" " * x + parte)

while True:
    limpar_tela()
    desenhar(x, y) # Desenha a nave

    time.sleep(0.05)

    if msvcrt.kbhit():
        tecla = msvcrt.getch()

        if tecla == b'\xe0':  # Tecla especial (setas, etc.)
            direcao = msvcrt.getch()

            # Movimento para esquerda (K) e direita (M)
            if direcao == b'K' and x > 0:        # Esquerda
                x -= 2  # A nave vai se mover um pouco mais de uma posição para um movimento mais visível
            elif direcao == b'M' and x < largura - len(nave[0]):  # Direita
                x += 2

        elif tecla == b'q':  # Sair com 'q'
            break

