N = 5
notas = []

# Ler notas
for i in range(N):
    x = int(input("Nota do aluno: "))
    notas.append(x)

# Calcular média
media = sum(notas) / N

# Mostrar notas acima da média
for nota in notas:
    if nota > media:
        print("Aprovado:", nota)