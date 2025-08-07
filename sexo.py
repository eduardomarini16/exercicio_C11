
sexo = str(input("Digite [M] para msculino ou [F] para feminino. ")).upper()

while sexo != "M" and sexo !="F":
    print("Entrada inválida. Por favor Digite [M] para masculino ou [F] para feminimo ")
    sexo = str(input("Digite M para msculino ou F para feminino. ")).upper()

if sexo == 'M':
    sexo = 'MASCULINO'
elif sexo == 'F':
    sexo = 'FEMININO'

print(sexo)
