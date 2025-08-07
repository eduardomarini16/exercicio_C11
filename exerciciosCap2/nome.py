nome = input("Qual é o seu nome? ")
print(f"Seu nome com letras maísculas {nome.upper()}")
print(f"Seu nome com letras minúsculas {nome.lower()}")

tamanho_nome = (len(nome.replace(" ", "")))

print(f"Seu nome tem {tamanho_nome} letras")

novo_sobrenome = 'do Inatel'
nome_modificado = nome.split()

nome_modificado[-1] = novo_sobrenome
nome_modificado = " ".join(nome_modificado)
print(f"Seu novo nome é {nome_modificado.upper()}")

