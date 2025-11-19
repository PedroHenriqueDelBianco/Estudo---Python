# Calcular média de N números
N = int(input("Digite o valor de N: "))
soma = 0
contador = 0

while contador < N:
    x = int(input("Digite um número: "))
    soma = soma + x
    contador = contador + 1

media = soma / N
print("Média =", media)