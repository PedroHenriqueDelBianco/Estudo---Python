listaProdutos = ["iphone", "ipad", "macbook", "airpods"]
listaPrecos = [16999.80, 3567.90, 34999.99, 1399.99]


print("Digite o nome do produto: ")
produto = input().lower()

print("Digite o seu cupom de desconto: ")
cupom1 = input().upper()
cupom2 = input().upper()
cupom3 = input().upper()
cupom4 = input().upper()
cupom5 = input().upper()

if cupom1 == "DESCONTO10":
    produto * 0.1
    print("Valor do produto é: ")

if cupom2 == "DESCONTO20":
    produto * 0.2
    print("Valor do produto é: ")

if cupom3 == "DESCONTO30":
    produto * 0.3
    print("Valor do produto é: ")

if cupom4 == "DESCONTO40":
    produto * 0.4
    print("Valor do produto é: ")

if cupom5 == "DESCONTO50":
    produto * 0.5
    print("Valor do produto é: ")
    
iphone = input().lower()    