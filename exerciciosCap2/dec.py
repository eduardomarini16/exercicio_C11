import math

while True:
    entrada = input("Digite um número decimal: ")

    try:
        numero = float(entrada)
        if not numero.is_integer():
            print(f"Você digitou um número válido: {numero}")
            break
        else:
            print("Número inválido. Digitou um número inteiro.")
    except:
        print("Entrada inválida. Digite apenas números com casas decimais.")

raiz = math.sqrt(numero)
print(f"Raiz quadrada = {raiz:.2f}")
print(f"Sua função teto = {math.ceil(numero)}")
print(f"Sua função chão = {math.floor(numero)}")
print(f"Sua parte inteira = {int(numero)}")
