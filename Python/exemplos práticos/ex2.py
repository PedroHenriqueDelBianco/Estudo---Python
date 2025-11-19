# Com for
N = int(input("Digite um número: "))
fatorial = 1

for i in range(1, N + 1):
    fatorial = fatorial * i

print(f"Fatorial de {N} é {fatorial}")

# Com while
N = int(input("Digite um número: "))
fatorial = 1
i = 1

while i <= N:
    fatorial = fatorial * i
    i = i + 1

print(f"Fatorial de {N} é {fatorial}")