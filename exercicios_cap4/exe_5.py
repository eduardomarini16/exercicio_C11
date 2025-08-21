import numpy as np

# Fixar  para números aleatórios
np.random.seed(10)

# Criar matriz 4x4 com inteiros entre 1 e 50
matriz = np.random.randint(1, 51, size=(4, 4))
print("Matriz 4x4:\n", matriz)

# a) Média de cada linha e cada coluna
media_linhas = np.mean(matriz, axis=1)
media_colunas = np.mean(matriz, axis=0)

print("\nMédia de cada linha:", media_linhas)
print("Média de cada coluna:", media_colunas)

# b) Maior valor das médias
maior_media_linha = np.max(media_linhas)
maior_media_coluna = np.max(media_colunas)

print("\nMaior média das linhas:", maior_media_linha)
print("Maior média das colunas:", maior_media_coluna)

# c) Contagem das aparições de cada número
valores, contagens = np.unique(matriz, return_counts=True)

print("\nQuantidade de aparições de cada número:")
for v, c in zip(valores, contagens):
    print(f"Número {v}: {c} vez(es)")

# Mostrar apenas números que aparecem 2 vezes
numeros_duplos = valores[contagens == 2]
print("\nNúmeros que aparecem exatamente 2 vezes:", numeros_duplos)
