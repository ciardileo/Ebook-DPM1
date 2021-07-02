"""
Partindo para a análise de strings, que vai ter, sem dúvidas,
as funções que você mais vai usar em seus scripts, com o que você aprendeu agora
não conseguiremos fazer grandes coisas, mas a alguns capítulos a frente, essas funções se
tornaram bastante úteis
"""

nome = input('Qual é seu nome? ')
print(f'Seu nome tem {len(nome)} letras')  # se acostume a usar as F Strings, pois elas agilizarão muito o seu código

# Nesse script básico, perguntamos o nome do usuário e em seguida, usando o len(), mostramos quantas letras esse nome tem
# Porém, esse código pode não funcionar para nomes completos, pois o len() não conta somente letras, e sim todas as "casas de memória"
# da string, ou variável e agora vai um exemplo:

nomes = 'João', 'Alberto', 'Rodrigo'
print(nomes[0])

# Se você achou que o print iria gerar a letra "J", se confundiu, pois quando há mais de 1 elemento na variável, ela criará
# uma "casa de memória" pra cada um desses elementos e ainda criará mais casas de memória dentro dessas casas, por exemplo,
# a casa 0 dessa variável, é a string "João", e a letra "J" é a casa 0 da string "João", e não a casa 0 da variável, isso é basicamente
# uma casa com várias casas dentro, que são as letras da string
# No próximo capítulo abordaremos melhor as variáveis com múltiplos valores

palavra = input('Escreva uma palavra qualquer: ')
numero_de_vogais = palavra.count('a') + palavra.count('e') + palavra.count('i') + palavra.count('o') + palavra.count('u')
print(f'Esta palavra tem {numero_de_vogais} vogais')

# Neste código, somamos os valores do count() de todas as vogais e mostramos na tela
# Mais para frente aprenderemos como encurtar esse código seguindo as normas do Python, deixando o código "bonito"

frase = 'Programação Programa Programador'
print(frase.find('Pro'))

# Usei esse exemplo, para mostrar que o find() só vai nos dizer a casa inicial do primeiro valor que ele encontrar na string
# então se o "Pro" aparecer mais vezes na frase, não saberemos, pois a função só mostra a primeira vez em que ele aparece, que no caso, começa na casa 0

# DESAFIOS
# Neste assunto, não temos muito o que inventar *POR ENQUANTO*, então terá apenas 1 desafio:
# DESAFIO 4: Crie um "Analisador de Texto", que pede uma frase para um usuário e então mostra:
# quantas vogais ela tem, quantas consoantes, e por fim quantas letras no total
