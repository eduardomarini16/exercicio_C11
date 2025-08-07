numero = int(input("Digite um número entre 1000 e 9999. "))

while numero < 1000 or numero > 9999:
    print("Entrada invalida")
    numero = int(input("Digite um número entre 1000 e 9999. "))

print(numero)
numero_str = str(numero)

print( f"UNIDADE = {numero_str[-1]}")
print( f"DEZENA = {numero_str[-2]}")
print( f"CENTENA = {numero_str[-3]}")
print( f"MILHAR = {numero_str[0]}")


