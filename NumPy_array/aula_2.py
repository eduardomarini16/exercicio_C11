import numpy as np

# CRIANDO UM NUMPY ARRAY 2D
mtz = np.arange(1, 10, 1).reshape(3, 3)
print(mtz)

# EXTRAINDO APENAS UMA LINHA
print(mtz[2])

 # EXTRAINDO A COLUNA (segunda e terceira coluna)
print(mtz[:,1:])

# CONDICIONAIS NO NUMPY
print(mtz>5)
print(mtz[mtz>5])
print(mtz[mtz%2==0])

# TRATAMENTO TEXTUAL
arr = np.array(['Goku', 'Goten', 'Gohan', 'Trunks', 'Bulma'])
print(arr)
print(np.char.find(arr, 'Go')>=0)
print(arr[np.char.find(arr, 'Go')>=0])

# IMPORTANDO DATASETS NO NUMPY
ds = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')
# print(ds)

#COLUNA DO DATASET
print(ds[0, :])

#CALCULANDO A MEDIA DE UMA MISSÃO ESPACILA
#SLICING PARA EXTRAIR A COLUNA CUSTO (COST)
ds_cost = ds[1:, 6]
print(ds_cost)
#Transformando os valores em float
ds_cost = ds_cost.astype(float)
print(ds_cost.mean()) # calculando média

