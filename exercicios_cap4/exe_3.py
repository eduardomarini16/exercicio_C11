import numpy as np
import random

# a) Criar matriz 2x2 de zeros
matriz = np.zeros((2, 2), dtype=int)

# b) Adicionar número 1 em posição aleatória
linha = random.randint(0, 1)
coluna = random.randint(0, 1)
matriz[linha, coluna] = 1

# Para testes (pode comentar depois se quiser esconder o "mina")
print("DEBUG (posição da mina):\n", matriz)

# c) Jogo
tentativas = 0
acertou = False

while tentativas < 3 and not acertou:
    print("\nJogada", tentativas + 1)
    l = int(input("Escolha a linha (0 ou 1): "))
    c = int(input("Escolha a coluna (0 ou 1): "))

    if matriz[l, c] == 1:
        print("Game Over! :( Try Again!")
        acertou = True
    else:
        print("✔️ Posição segura!")
    tentativas += 1

# Se não achou a mina em 3 jogadas → venceu
if not acertou:
    print("\nCongratulations! You beat the game! :)")
