distancia = float(input("Digite a distância que será percorrida "))

if distancia > 200:
    valor = distancia * 0.45
elif distancia <= 200:
    valor = distancia * 0.50

print(f"Preço da viagem é de R${valor:.2f} ")


