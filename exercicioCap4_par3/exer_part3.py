import pandas as pd
import numpy as np

# Carrega o conjunto de dados, definindo explicitamente a coluna ` Cost` como string
df = pd.read_csv('space.csv', delimiter=';', dtype={' Cost': str})

# Renomeia a coluna para remover o espaço inicial
df.rename(columns={' Cost': 'Cost'}, inplace=True)

# --- 1. Porcentagem de missões que deram certo ---
total_missions = len(df)
successful_missions = df[df['Status Mission'] == 'Success'].shape[0]
success_percentage = (successful_missions / total_missions) * 100
print(f"Porcentagem de missões de sucesso: {success_percentage:.2f}%")

# --- 2. Média de gastos de uma missão especial (> 0) ---
# Limpando a coluna 'Cost'
df['Cost'] = df['Cost'].str.replace(',', '').str.strip()
# Converte para float, tratando erros
df['Cost'] = pd.to_numeric(df['Cost'], errors='coerce')
# Filtra por custos > 0
missions_with_cost = df[df['Cost'] > 0]
average_cost = missions_with_cost['Cost'].mean()
print(f"Média de gastos de missões com valores disponíveis: ${average_cost:,.2f}")

# --- 3. Missões espaciais realizadas pelos EUA ---
usa_missions = df[df['Location'].str.contains('USA', na=False)].shape[0]
print(f"Número de missões realizadas pelos Estados Unidos: {usa_missions}")

# --- 4. Missão mais cara da SpaceX ---
spacex_missions = df[df['Company Name'] == 'SpaceX'].copy()
# Assegura que a coluna 'Cost' é numérica
spacex_missions['Cost'] = pd.to_numeric(spacex_missions['Cost'], errors='coerce')
# Encontra o valor máximo
max_cost = spacex_missions['Cost'].max()
if not pd.isna(max_cost):
    most_expensive_mission = spacex_missions.loc[spacex_missions['Cost'] == max_cost]
    print(f"Missão mais cara da SpaceX: {most_expensive_mission['Detail'].iloc[0]}")
    print(f"Custo: ${most_expensive_mission['Cost'].iloc[0]:,.2f}")
else:
    print("Nenhum custo disponível para missões da SpaceX.")

# --- 5. Contagem de missões por empresa e loop ---
company_mission_counts = df['Company Name'].value_counts()
for company, count in company_mission_counts.items():
    print(f"Empresa: {company:<20} - Quantidade de Missões: {count}")