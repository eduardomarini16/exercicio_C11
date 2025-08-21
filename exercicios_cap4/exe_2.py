import numpy as np

# 1. Array de números pares de 0 até 51 (inclusive)
array1 = np.arange(0, 52, 2)  

# 2. Array de números pares de 100 até 50 (decrescente)
array2 = np.arange(100, 49, -2)  

# 3. Concatenar os dois arrays
array_concat = np.concatenate((array1, array2))

# 4. Ordenar o resultado
array_sorted = np.sort(array_concat)

# Exibir resultados
print("Array 1 (0 até 51 pares):", array1)
print("Array 2 (100 até 50 pares decrescente):", array2)
print("Concatenado:", array_concat)
print("Ordenado:", array_sorted)
