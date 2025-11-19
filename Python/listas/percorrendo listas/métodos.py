lista = [3, 1, 4, 2]

lista.append(5)        # Adiciona no final: [3, 1, 4, 2, 5]
lista.insert(1, 10)    # Insere na posição 1: [3, 10, 1, 4, 2, 5]
lista.remove(1)        # Remove o elemento 1: [3, 10, 4, 2, 5]
lista.sort()           # Ordena: [2, 3, 4, 5, 10]
valor = lista.pop(2)   # Remove e retorna elemento da posição 2