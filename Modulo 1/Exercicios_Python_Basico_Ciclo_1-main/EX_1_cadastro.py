# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('Bem vindo!!')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
email = input('Digite seu email: ')
senha = input('Digite sua senha: ')

print(f'''

| ------------------------------ |
 | ---------- CADASTRO ---------- |
 | ------------------------------ |
 | Nome: {nome}
 | Idade: {idade}
 | Email: {email}
 | Senha: {senha}

 | ------------------------------ |
 | ----- USUÁRIO CADASTRADO ----- |
 | Seja bem vindo(a) {nome}!
 | Email: {email}
 | ------------------------------ |
      
      
      
      ''')