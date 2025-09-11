import numpy as np
import pandas as pd

# Questão 1
seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

# Questão 2
totalAno1 = seriesAno1.sum()
totalAno2 = seriesAno2.sum()
print('\nTotal ano 1:', totalAno1)
print('Total ano 2:', totalAno2)

# Questão 3
crescimento = seriesAno2 - seriesAno1
print('\nCrescimento/Declínio:\n', crescimento)

# Questão 4
crescimentoPositivo = crescimento[crescimento > 0]
print('\nCrescimento:\n', crescimentoPositivo)

# Questão 5
projecao = seriesAno2 + crescimento
projecao_dois_anos = projecao + crescimento
linguagem_mais_popular = projecao_dois_anos.nlargest(1)
print('\nProjeção para dois anos:\n', projecao_dois_anos)
print('Linguagem mais popular:', linguagem_mais_popular)

# Questão 6
df = pd.DataFrame(
  index=['A', 'B', 'C', 'D', 'E'],
  columns=['W', 'X', 'Y', 'Z'],
  data=np.random.randint(1, 50, [5, 4])
)
media = df['X'][df['X'] < 30].mean()
print('\nMédia:', round(media, 2))

# Questão 7
mediaD = df.loc['D'].mean()
somaE = df.iloc[4].sum()
print('\nMédia dos elementos da linha D:', mediaD)
print('Soma dos elementos da linha E:', somaE)

# Questão 8
slicing = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print('\nSlicing das linhas A, C, E e colunas X e Y:\n', slicing)
print('\nSoma das linhas:\n', slicing.sum(axis=1))
print('\nSoma das colunas:\n', slicing.sum(axis=0))