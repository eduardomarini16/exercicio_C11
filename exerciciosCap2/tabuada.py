numero = int(input("Entre com o número para verificar sua tabuada. "))

intervalo = int(input("Digite o intervalo de cálculo para a tabuada. "))

for i in range(1, (intervalo + 1)):
    resultado = numero*i
    print(f"{numero} X {i} = {resultado}")