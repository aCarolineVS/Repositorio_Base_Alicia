# Escreva um programa que pede ao usuário o preço de um produto e o valor de desconto em % e depois informe qual será o valor do desconto.
# Dica: 
# use a fórmula 
# desconto = preco * (porcentagem / 100) 
# para calcular o valor do desconto 

# OUTPUT ESPERADO:

# Qual o preço do produto? 300
# Qual a porcentagem de desconto? 10
# O produto que custa R$300.0 terá R$30.0 de desconto.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('--- BEM VINDO A CALCULADORA DE DESCONTOS!!! ---')

produto = float(input('Digite o preço do produto: '))
porcen = float(input('Qual a porcentagem do desconto: '))

desc = produto * (porcen / 100)

print(f'''
____________________________________
      
 - Valor do produto: {produto}
      
 - Porcentagem de desconto: {porcen}
      
 - Desconto total: {desc}
____________________________________
      
      ''')