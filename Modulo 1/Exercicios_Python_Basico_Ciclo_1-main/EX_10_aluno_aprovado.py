# Escreva um código que pede a nota de duas provas do aluno e verifique se o aluno foi aprovado com as condições abaixo:
# O aluno precisa ter média maior que 7 e não pode ter tirado zero em nenhuma nota.
# Não é necessário usar estruturas condicionais, apenas expressões lógicas conforme estudado no material de expressões lógicas.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite a primeira nota: 10
# Digite a segunda nota: 8
# Aluno aprovado? True

# Exemplo 2:

# Digite a primeira nota: 10
# Digite a segunda nota: 0
# Aluno aprovado? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print(' - MÉDIA ESCOLAR ! -')

nome = input('Digite o nome do aluno: ')
p1 = float(input('Nota da primeira prova: '))
p2 = float(input('Nota da segunda prova: '))


soma = p1 + p2 
media = soma / 2

if media >= 6:
    print(f''' 
| ______________________________ |
| SISTEMA DE PROVAS
| ______________________________ |
| Nome do aluno: {nome}
| Nota da primeira prova: {p1}
| Nota da segunda prova: {p2}

| ______________________________ |
| Aluno: {nome}
| Média: {media:.2f}
| Aluno APROVADO!!!!
| ______________________________ |
''')
    
elif media < 6:
       print(f''' 
| ______________________________ |
| SISTEMA DE PROVAS
| ______________________________ |
| Nome do aluno: {nome}
| Nota da primeira prova: {p1}
| Nota da segunda prova: {p2}

| ______________________________ |
| Aluno: {nome}
| Média: {media:.2f}
| Aluno REPROVADO!!!!
| ______________________________ |
''')
