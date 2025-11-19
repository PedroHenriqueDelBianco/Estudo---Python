dic = {"um": "one", "dois": "two", "tres": "three"}

print(dic.keys())    # Chaves: ['um', 'dois', 'tres']
print(dic.values())  # Valores: ['one', 'two', 'three']
print(dic.items())   # Pares: [('um','one'), ('dois','two'), ...]

valor = dic.get("cinco", 0)  # Retorna 0 se chave não existir
dic.pop("um")                # Remove o par "um":"one"