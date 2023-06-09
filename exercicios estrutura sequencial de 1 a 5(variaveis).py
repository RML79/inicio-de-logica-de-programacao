# 1 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = input('digite um numero: ')
print('o numero informado foi:', numero)

# quando quiser colocar uma string seguida de uma variavel no print,deve-se usar " , " para variaveis q sao numeros e
# " + " para variaveis que estao ligadas a palavras

# 2 Faça um Programa que peça dois números e imprima a soma.
valor_1 = int(input('digite o primeiro valor: '))
valor_2 = int(input('digite o segundo valor: '))
total = valor_1 + valor_2
print(total)

# 3 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota_1 = int(input('digite a primeira nota: '))
nota_2 = int(input('digite a segunda nota: '))
nota_3 = int(input('digite a terceira nota: '))
nota_4 = int(input('digite a quarta nota: '))
resultado = ((nota_1) + (nota_2) + (nota_3) + (nota_4)) / 4
print('a media é:', resultado)
# nesse caso deve-se colocar o () entre as somas para que elas sejam realizadas primeiro e o resultado seja dividido


# 4 Faça um Programa que converta metros para centímetros.
metro = int(input('digite a metragem: '))
cm = 100
metros = (metro) * (cm)
print('essa metragem equivale a:', metros, 'centimetros')

# 5 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = int(input('digite o valor do raio: '))
area = (raio) ** 2 * 3.14
print('o valor da area é:', area)
# A área de um círculo é pi vezes o raio elevado ao quadrado
