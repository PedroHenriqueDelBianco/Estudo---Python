Trabalho 02
Instruções
● O desenvolvimento deverá ser na sintaxe utilizada pelo portugol.dev, exclusivamente;
● Encaminhe as questões em um arquivo .txt
QUESTÕES
1. Uma loja online oferece descontos especiais baseados em dois critérios:
● Idade do cliente (estudante: <25 anos OU sênior: ≥60 anos)
● Valor total da compra
As regras de desconto são:
● Clientes estudantes (<25 anos) OU sênior (≥60 anos) recebem desconto adicional
● Compras acima de R$ 200,00 têm desconto base de 10%
● Compras acima de R$ 500,00 têm desconto base de 15%
Descontos especiais por categoria:
● Estudantes: +5% de desconto adicional
● Sênior: +7% de desconto adicional
Escreva um programa em Python que:
1. Solicite a idade do cliente e o valor total da compra
2. Calcule o valor final com os descontos apropriados
3. Informe:
○ O valor do desconto base
○ O valor do desconto adicional (se aplicável)
○ O valor final a ser pago
1 de 2
Boa sorte =)
2. Uma escola precisa de um sistema para cadastrar notas dos alunos e gerar relatórios
estatísticos. O programa deve:
1. Cadastrar múltiplos alunos (nome e nota)
2. Calcular estatísticas das notas
3. Permitir que o usuário cadastre quantos alunos desejar
4. Validar notas (apenas entre 0 e 10)
5. Gerar relatório final
Escreva um programa em Python que:
● Use um loop para cadastrar alunos até que o usuário decida parar
● Para cada aluno, solicite nome e nota (validando a entrada)
● Ao final, exiba:
○ Quantidade de alunos cadastrados
○ Média geral das notas
○ Maior e menor nota
○ Porcentagem de alunos aprovados (nota ≥ 7)
○ Lista de alunos com suas situações (Aprovado/Reprovado)
3. A MODA de um vetor de números é o número no vetor que é repetido com maior frequência. Se
mais de um número for repetido com frequência máxima igual, não existirá uma moda. Fazer um
programa que leia um vetor de números positivos (validar a entrada de dados) e imprima a moda
do vetor ou uma mensagem que a moda não existe. Fazer uma função para a moda.


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
