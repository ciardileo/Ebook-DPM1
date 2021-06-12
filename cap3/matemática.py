'''
Já que aprendemos como fazer contas
no Python, vamos treinar um pouco!
'''

print(12 * 10)

numero1 = 19
numero2 = 234

produto = numero1 * numero2
potencia = numero1 ** numero2
soma = numero1 + numero2
subtracao = numero2 - numero1
divisao = numero2 / numero1

# Caso você não tenha entendido muito bem,
# o "//" mostrará o resto da divisão caso ela
# não for exata, por exemplo, 10 / 2 é uma divisão
# exata com resto 0,  já 5 / 2 não, nesse caso o resultado
# será decimal. Podemos usar isso para descobrir se um número
# é par, pois se o resto da divisão dele por 2 for igual a 0, ele é par

numero_par = 38 // 2

# Agora, importaremos a bliblioteca "Math"
# A seguir temos dois jeitos diferentes de se
# chegar ao mesmo resultado

import math

raiz_quadrada = math.sqrt(64)

raiz_quadrada2 = 64 ** (1 / 2)

# Outra coisa importante a considerar é que,
# na programação, a ordem das operações é a mesma
# ou seja, primeiro, os parênteses, segundo, potências e raízes,
# terceiro, multiplicação e divisão e por último, adição e subtração

nome = input('Qual é seu nome?: ')
print('Bem vindo(a)', nome)

# Não se esqueça, que o tipo primitivo da resposta
# será sempre "string", então caso queira fazer contas,
# você tem que transformar o valor com a função int() ou float():

num1 = input('Digite um número')
num1 = int(num1)
num2 = input('Digite outro número: ')
num2 = int(num2)

print('A soma entre eles é igual a ', num1 + num2)

# Um adendo, se você quiser usar a parte decimal, troque o int()
# por float(). Outra coisa importante para vermos, é que podemos
# reduzir esse código desse jeito:

num1 = int(input('Digite um número'))

# Colocar o int() atrás do input dá no mesmo, pois o resultado do input será
# o número que o usuário digitar, apenas preste atenção para nao colocar parênteses a mais

# DESAFIOS:
# DESAFIO 7: Fazer a conta a seguir: 230 + 140 x 200 : 2, armazenando cada número
# em uma variável diferente e colocando os símbolos de conta certos
# DESAFIO 8: Faça sua própia "calculadora" de soma que aceite números DECIMAIS
# DESAFIO 9: Use a função "trunc()" da biblioteca "Math" para mostrar apenas a parte
# inteira do resultado das contas decimais do desafio anterior. Se necessário, pesquise na documentação para saber usa-lá
# ou veja no arquivo de resoluções desse capítulo
