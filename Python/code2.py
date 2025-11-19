listaProdutos = ["iphone", "ipad", "macbook", "airpods"]
listaPrecos = [16999.80, 3567.90, 34999.99, 1399.99]



if "ipad" in listaProdutos:
    indice = listaProdutos.index("ipad")
    preco_ipad = listaPrecos[indice]
    print("O preço do ipad com desconto é R$", preco_ipad * 0.9)

if "macbook" in listaProdutos:
    indice = listaProdutos.index("macbook")
    preco_macbook = listaPrecos[indice]
    print("O preço do macbook com desconto é R$", preco_macbook * 0.9)

if "airpods" in listaProdutos:
    indice = listaProdutos.index("airpods")
    preco_airpods = listaPrecos[indice]
    print("O preço do airpods com desconto é R$", preco_airpods * 0.9)

if "iphone" in listaProdutos:
    indice = listaProdutos.index("iphone")
    preco_iphone = listaPrecos[indice]
    print("O preço do iphone com desconto é R$", preco_iphone * 0.9)

if "apple watch" not in listaProdutos:
    print("Apple Watch não está na lista de produtos.")

else :
    print("Apple Watch está na lista de produtos.")
