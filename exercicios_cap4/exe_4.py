import numpy as np

# Criar uma matriz qualquer (exemplo: 3x4)
matriz = np.arange(12).reshape(3, 4)

print("Matriz:\n", matriz)

# Extrair número de linhas e colunas
linhas, colunas = matriz.shape

print(f"\nLinhas: {linhas}, Colunas: {colunas}")

# Multiplicar linhas * colunas → número total de elementos
total_elementos = linhas * colunas

print("Total de elementos:", total_elementos)

# Verificar se é par ou ímpar
if total_elementos % 2 == 0:
    print("Esta matriz pode virar um vetor unidimensional com quantidade PAR de elementos.")
else:
    print("Esta matriz pode virar um vetor unidimensional com quantidade ÍMPAR de elementos.")
