# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('--- BEM VINDO A CALCULADORA DE DESCONTOS!!! ---')

nome = input('Digie o nome do produto: ')
produto = input('Digite o preço do produto: ')
porcen = float(input('Qual a porcentagem do desconto: '))

desc = produto * (porcen / 100)

print(f'''
____________________________________
      
 - Produto: {nome}
      
 - Valor do produto: {produto}
      
 - Porcentagem de desconto: {porcen}
      
 - Desconto total: {desc}
____________________________________
      
      ''')
