algoritmo "DescontoLojaOnline"
// Programa que calcula o valor final de uma compra com descontos baseados em idade e valor total.
// Critérios: Estudante (<25 anos) ou Sênior (>=60 anos) recebem desconto adicional.
// Descontos base: 10% para compras > R$200, 15% para > R$500.
// Descontos adicionais: +5% para estudantes, +7% para sênior.

var
   idade: inteiro
   valorCompra, descontoBase, descontoAdicional, valorFinal: real
   ehEstudante, ehSenior: logico

inicio
   // Solicitar idade e valor da compra
   escreva("Digite a idade do cliente: ")
   leia(idade)
   escreva("Digite o valor total da compra (em R$): ")
   leia(valorCompra)

   // Inicializar variáveis
   descontoBase <- 0.0
   descontoAdicional <- 0.0
   ehEstudante <- (idade < 25)
   ehSenior <- (idade >= 60)

   // Calcular desconto base
   se (valorCompra > 500) entao
      descontoBase <- valorCompra * 0.15
   senao se (valorCompra > 200) entao
      descontoBase <- valorCompra * 0.10
   fimse

   // Calcular desconto adicional se aplicável
   se (ehEstudante) entao
      descontoAdicional <- valorCompra * 0.05
   senao se (ehSenior) entao
      descontoAdicional <- valorCompra * 0.07
   fimse

   // Calcular valor final
   valorFinal <- valorCompra - descontoBase - descontoAdicional

   // Exibir resultados
   escreva("Valor do desconto base: R$ ", descontoBase:2:2)
   escreva("Valor do desconto adicional: R$ ", descontoAdicional:2:2)
   escreva("Valor final a ser pago: R$ ", valorFinal:2:2)
fimalgoritmo
