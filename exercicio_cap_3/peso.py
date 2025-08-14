
mais_pesado_nome = ""
mais_pesado_peso = 0

mais_leve_nome = ""
mais_leve_peso = 0


for i in range(3):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    peso = float(input(f"Digite o peso de {nome} (em kg): "))
    
    if i == 0:
        mais_pesado_nome = nome
        mais_pesado_peso = peso
        mais_leve_nome = nome
        mais_leve_peso = peso
    else:
        if peso > mais_pesado_peso:
            mais_pesado_nome = nome
            mais_pesado_peso = peso
        if peso < mais_leve_peso:
            mais_leve_nome = nome
            mais_leve_peso = peso

print("\nResultados:")
print(f"Mais pesada: {mais_pesado_nome} ({mais_pesado_peso} kg)")
print(f"Mais leve: {mais_leve_nome} ({mais_leve_peso} kg)")
