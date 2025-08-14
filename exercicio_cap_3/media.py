
aluno = {}

aluno["nome"] = input("Digite o nome do aluno: ")
aluno["media"] = float(input("Digite a média do aluno: "))

if aluno["media"] >= 50:
    aluno["situacao"] = "AP"  
else:
    aluno["situacao"] = "RP"  

print("\nDados do aluno:")
print(aluno)
