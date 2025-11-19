lista = [3, 5, 10, 2, 4]
maior = lista[0]

for numero in lista:
    if numero > maior:
        maior = numero

print("Maior elemento:", maior)