"""
Neste capítulo estudamos mais a fundo o tipo de dado String, equivalente ao texto em Python
As funções de manipulação das strings serão muito importante para você mais a frente, exemplo:
criando um programa que precisamos do cadastro do usuário e para evitar erros e bugs no registro, pois devemos
justar os dados antes de armazená-los e nem sempre o usuário enviará os dados do jeito certo
Não se esqueça que os índices, a numeração das "casas de memória" começa com 0, e sempre que indicarmos a casa final no fatiamento
devemos colocar uma casa a mais, pois o Python vai até a casa que você indicou, porém corta ela
"""

nome = input('Qual é o seu nome? ')
print(f'Seu nome começa com a letra "{nome[0]}" e termina com a letra "{nome[-1]}"')

# Nesse script, perguntamos o nome do usuário e logo mostramos a primeira e última letra do nome dele
# usando o fatiamento de strings, PORÉM, você deve ter notado algo estranho: o que é o "f" antes das aspas e essas chaves?
# Isso é chamado de "F String", um tipo de formatação em que podemos mostrar variáveis durante a string, sem precisar fazer o preocesso chato
# de: fechar as aspas, colocar a vírgula, citar a variável, colocar outra vírgula e abrir as aspas de novo
# Basicamente, o "f" deve ser colocado antes das aspas para indicar que aquela é uma f string, então, nos lugares em que
# queremos mostrar algo que não seja texto, abrimos as chaves e colocamos dentro dela o que queremos, exemplos:

print(f'5 x 5 é igual a {5 * 5}')

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
print(f'{numero1} + {numero2} é igual a {numero1 + numero2}')

# Preferi deixar essa dica no script para só quem estiver fazendo tudo certo poder aprender e se você aprendeu as F Strings agora,
# parabéns, continue seguindo o livro e os arquivos para realmente "Dominar o Python"

codigo = 'Pcystlhmosn  #é  8mQu:i6t,o  !l.e-gRa$l'
print(f'O código decifrado é: {codigo[::2]}')

# Usando o fatiamento conseguimos esconder uma mensagem dentro de vários caracteres que parecem ser sem sentido
# Lembre-se: ["casa inicial": "casa final": "passada"], e quando nao colocamos nada na casa inicial, o Python vai interpretar
# como "desde o início" e se não colocarmos nada na casa final ele entenderá como "até o final", com isso podemos omitir
# informações que não vamos mudar, no caso, queriamos só alterar a passada, colocando "::2"

# DESAFIOS
# DESAFIO 1: Considerando uma variável com valor de string "Programação", mostre com o print: a primeira casa, a casa 1 e somente a última letra
# DESAFIO 2: Escreva uma mensagem "criptografada" em uma string, e mostre a mensagem secreta no print (CRIE SUA PRÓPIA MENSAGEM)
# DESAFIO 3: Crie um script que pergunte ao usuário o nome dele e o mostre na tela com as letras alternadas (mudando a passada no fatiamento da string), PORÉM, somente até a penultima letra
