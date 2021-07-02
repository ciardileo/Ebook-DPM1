"""
Chegamos ao fim do capítulo 4 e para testar seu conhecimento, você deve ter feito os desafios de cada arquivo,
se teve dúvida em algum, veja a resolução abaixo, entenda como funciona e faça sua PRÓPIA resolução
"""

# DESAFIO 1: Considerando uma variável com valor de string "Programação", mostre com o print: a primeira casa, e somente a última letra

# Primeira casa é a casa[0] pois a numeração dos índices começa em 0 e não em 1 --> Letra "P"
# Casa 1 = casa[1] -- > "r"
# Assim como há a numeração positiva, há a numeração negativa, útil quando não sabemos o tamanho da string, por exemplo, quando ela vem de uma resposta do usuários

palavra = "Programação"
print(f'Primeira casa: {palavra[0]}, casa 1: {palavra[1]}, última letra: {palavra[10:]} ou {palavra[-1:]}')
# [-1:] = vai do -1 (casa final) até o 0 (casa inicial) porém, como o Python "corta" a última letra, o zero não é mostrado

# DESAFIO 2: Escreva uma mensagem "criptografada" em uma string, e mostre a mensagem secreta no print (CRIE SUA PRÓPIA MENSAGEM)
# DESAFIO 3: Crie um script que pergunte ao usuário o nome dele e o mostre na tela com as letras alternadas (mudando a passada no fatiamento da string), PORÉM, somente até a penultima letra
