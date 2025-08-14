
loja1 = {"iPhone 15", "Galaxy S23", "Moto G84", "Xiaomi 13"}
loja2 = {"Galaxy S23", "Pixel 8", "iPhone 15", "Xiaomi 14"}


todos_modelos = loja1 | loja2   


modelos_comuns = loja1 & loja2  # 

print("Loja 1 vende:", loja1)
print("Loja 2 vende:", loja2)
print("Modelos no total disponíveis:", todos_modelos)
print("Modelos disponíveis em ambas as lojas:", modelos_comuns)