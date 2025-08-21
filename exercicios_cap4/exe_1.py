import numpy as np

# 1. Criar array de 1's com tamanho 8
array1 = np.ones(8, dtype=int)

# 2. Criar array de números aleatórios entre 0 e 9 (inteiros)
array2 = np.random.randint(0, 10, size=8)

# 3. Somar os dois arrays
array3 = array1 + array2

# 4. Verificar a soma total
soma_total = np.sum(array3)

print("Array 1:", array1)
print("Array 2:", array2)
print("Array Resultante (Array3):", array3)
print("Soma dos elementos:", soma_total)

# 5. Remodelar de acordo com a condição
if soma_total >= 40:
    # Mais linhas do que colunas
    array3_reshaped = array3.reshape(4, 2)  # 4 linhas, 2 colunas
else:
    # Mais colunas do que linhas
    array3_reshaped = array3.reshape(2, 4)  # 2 linhas, 4 colunas

print("Array Remodelado:\n", array3_reshaped)
