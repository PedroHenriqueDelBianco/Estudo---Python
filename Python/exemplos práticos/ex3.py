# Quadrados dos números de 0 a 9
quadrados = [x**2 for x in range(10)]
# Resultado: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtrar números menores que 4
numeros = [1, 2, 3, 4, 5]
menores = [n for n in numeros if n < 4]
# Resultado: [1, 2, 3]

# Quadrados dos números menores que 4
quadrados_menores = [n**2 for n in numeros if n < 4]
# Resultado: [1, 4, 9]