
pessoas = []


n = int(input("Quantas pessoas deseja cadastrar? "))


for i in range(n):
    print(f"\nCadastro da {i+1}ª pessoa:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()
    
    pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})


soma_idades = sum(p["idade"] for p in pessoas)
media_idade = soma_idades / n


mulheres_menos_20 = sum(1 for p in pessoas if p["sexo"] == "F" and p["idade"] < 20)


print("\nResultados:")
print(f"Média de idade do grupo: {media_idade:.2f} anos")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")
