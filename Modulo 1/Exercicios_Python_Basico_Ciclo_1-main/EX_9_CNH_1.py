# Escreva um programa simples que pede a idade do usuário e 
# depois mostre na tela com valor BOOLEANO (True ou False) se o usuário pode tirar a CNH (Carteira Nacional de Habilitação) ou não.
# Para tirar carteira no Brasil, a idade mínima é 18 anos.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite sua idade: 19
# Pode tirar carteira de motorista? True

# Exemplo 2:
# Digite sua idade: 17
# Pode tirar carteira de motorista? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('-- CNH --')
nome = input('Digite seu nome: ')
ida = int(input('Digite sua idade: '))

if ida >= 18:
    print('o usuario pode tirar a CNH !')
elif ida < 18:
    print('o usuario não pode tirar a CNH! ')
else: 
    print('idade não identificada! Tentar novamente.')
