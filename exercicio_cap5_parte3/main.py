import pandas as pd

# Questão 1
df = pd.read_csv('paises.csv', delimiter=';')
oceania = df[df['Region'].str.contains('OCEANIA')]

print("\nPaíses da OCEANIA:")
print(oceania['Country'])

print("\nQuantidade de países da OCEANIA:")
print(len(oceania))

# Questão 2
most_populated = df.loc[df['Population'].idxmax()]

print("\nPaís com maior população:")
print(most_populated['Country'])

print("Região:")
print(most_populated['Region'])

# Questão 3
region_grouped = df.groupby('Region')
literacy_mean = region_grouped['Literacy (%)'].mean()

print("\nMédia de alfabetização por região:")
print(literacy_mean)

# Questão 4
no_coast = df[df['Coastline (coast/area ratio)'] == 0]
no_coast.to_csv('noCoast.csv', index=False)

# Questão 5
def humanitarian_help(deathrate):
    if deathrate < 9:
      return 'Balanced'
    
    return 'Urgent'

df['Humanitarian Help'] = df['Deathrate'].apply(humanitarian_help)
print("\nDataset com a nova coluna 'Humanitarian Help':")
print(df[['Country', 'Deathrate', 'Humanitarian Help']])