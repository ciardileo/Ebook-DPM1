'''
Espero que você tenha tentado resolver os desafios
antes de vir aqui ver a resolução, mas de qualquer jeito
nunca deixe de relembrar este capítulo, pois o BÁSICO é o FUNDAMENTO
de toda sua jornada de aprendizado na programação!
'''

# DESAFIO 1: criar um script que escreverá na tela "Python é muito legal"

print('Python é muito legal (e esse desafio foi moleza)')

# DESAFIO 2: criar um script que escreverá "O Python é "top"" (cuidado com a pegadinha das aspas)
# se você prestou atenção na explicação, deve lembrar de um erro bem comum que citei, agora era sua hora de provar que não cairá nele!

print('O Python é "top"')  # use as aspas simples para mostrar a string e aspas duplas para a palavra "top"

# DESAFIO 3: criar um script escrevendo o que você quiser, porém colocando comentários explicativos em cada comando do seu código

# o print() escreve/imprime algo na tela
print('EU VOU DOMINAR O PYTHON!!')

# DESAFIO 4: Escreva uma frase qualquer com o print(), porém cada palavra da frase deve ser armazenada em uma variável diferente

palavra1 = "Estou"
palavra2 = "Aprendendo"
palavra3 = "Programação"

print(palavra1, palavra2, palavra3)

# DESAFIO 5: Usando a função type(), descubra os tipos de dados das variáveis das palavras do desafio anterior

# a variável palavra2 é do tipo string/str (texto)
print(type(palavra2))

# DESAFIO 6: Escreva na tela a soma de duas variáveis do tipo int

print("10 mais 10 é ", 10 + 10)

# DESAFIO 7: Fazer a conta a seguir: 230 + 140 x 200 : 2, armazenando cada número em uma variável diferente e colocando os símbolos de conta certos

num1 = 230
num2 = 140
num3 = 200
num4 = 2

print(num1 + num2 * num3 / num4)

# DESAFIO 8: Faça sua própia "calculadora" de soma que aceite números DECIMAIS

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

print(num1, "mais", num2, "é igual a", num1 + num2)

# DESAFIO 9: Use a função "trunc()" da biblioteca "Math" para mostrar apenas a parte inteira do resultado das contas decimais do desafio anterior

import math

print(math.trunc(num1), "mais", math.trunc(num2), "é igual a", math.trunc(num1 + num2))

# FIM DO CAPÍTULO 3! Espero que tenha conseguido resolver todos os desafios, se você não conseguiu, não se preocupe, vamos ter que errar bastante para aprender!
# Agora, corre lá que no capítulo 4 você aprenderá sobre listas, tuplas e dicionários!!!
# Você já sabe o procedimento, leia as explicações, e ao final da explicação de algum assunto, abra o arquivo sobre ele,
# tente entender, execute o código para ver o resultado e então resolva os desafios

