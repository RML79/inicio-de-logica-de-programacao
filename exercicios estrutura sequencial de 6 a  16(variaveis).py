# 6 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
import math
area = int(input('digite a medida de um dos lados do quadrado: '))
resultado = (area) ** 2
print('a area desse quadrado é:', resultado)
dobro = (resultado) + (resultado)
print('o dobro dessa area é:', dobro)

# 7 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês
# Calcule e mostre o total do seu salário no referido mês.
salario = int(input('quanto ganha no mes:'))
mes = int(input('quantas horas trabalha por mes:'))
total = salario / mes
print('voce ganha por hora:', total)

# 8 Faça um Programa que peça a temperatura em graus Farenheit
# transforme e mostre a temperatura em graus Celsius.
farenheit = int(input('digite em graus farenheit:'))
celcius = (farenheit - 32) / 1.8
print('equivale a', celcius, 'graus celsius')

# 9 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
celsi = int(input('digite em graus celsius:'))
faren = celsi * 1.8 + 32
print('equivale a', faren, 'graus farenheit')

# 10 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo. a soma do triplo do primeiro com o terceiro
# o terceiro elevado ao cubo.
inteiro = int(input('digite o primeiro numero inteiro:'))
inteiro_2 = int(input('digite o seugundo numero inteiro:'))
real = float(input('digite um numero real:'))
result_1 = (inteiro * 2) * inteiro_2 / 2
print('o produto do dobro do primeiro com metade do segundo é:', result_1)
result_2 = inteiro * 3 + real
print('a soma do triplo do primeiro com o terceiro é:', result_2)
result_3 = real ** 3
print(result_3, 'elevado ao cubo')

# 11 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7
altura = float(input('digite sua altura:'))
peso_m = (72.7 * altura) - 58
print('seu peso ideal é (m):', peso_m)
peso_f = (62.1 * altura) - 44.7
print('seu peso ideal é (f):', peso_f)

# 12 João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João
# deverá pagar. Imprima os dados do programa com as mensagens adequadas.
peso_peixes = float(input('digite o peso dos peixes:'))
maximo = 50
excesso = peso_peixes - maximo
print('voce excedeu:', excesso, 'kilos')
multa = (peso_peixes - maximo) * 4
print('sua multa é de', multa, 'reais')

'''13 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS.
quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''
salario_hora = float(input('quanto ganha por hora:'))
hora = int(input('quantas horas trabalha no mes:'))

salario_bruto = salario_hora * hora
print('seu salario bruto é de:', salario_bruto)
ir = salario_bruto * 11/100
print('desconto do IR é de:', ir, 'reais')
inss = salario_bruto * 8/100
print('desconto do inss é de:', inss, 'reais')
sindicato = salario_bruto * 5/100
print('desconto do sindicato é de:', sindicato, 'reais')
salario_liquido = salario_bruto - ir - inss - sindicato
print('seu salario liquido é de:', salario_liquido, 'reais')

# 14 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que
# a tinta é vendida em latas de 18 litros,que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
area = int(input('digite em metros a area quadrada a ser pintada:'))
cobertura = area / 3
latas = math.ceil(cobertura / 18)
valor = latas * 80
print('quantidade de latas nescessarias',
      latas, ',valor da compra', valor, ',00')
# math.ceil = arredonda pra cima,math.floor = arredonda pra baixo

'''15 Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima,
    isto é, considere latas cheias.
'''
metros = int(input('digite o tamanho da area quadrada a ser pintada:'))
cobertura = (metros / 6) * 1.1
latas = math.ceil(cobertura / 18)
valor = latas * 80

galoes = math.ceil(cobertura / 3.6)
v_galoes = galoes * 25

mixlatas = round(cobertura / 18)
mixgaloes = round((cobertura - mixlatas * 18) / 3.6)

if ((cobertura - (mixlatas * 18) % 3.6 != 0)):
    mixgaloes += 1
    total_mix = (mixlatas * 80) + (mixgaloes * 25)

print(f'comprando so latas de 18 litros ira precisar de: {latas} latas(s) ira custar {valor:.2f} R$')
print(f'se for comprar so galoes de 3,6 litros ira precisar de {galoes} galao(oes) e ira custar {v_galoes:.2f} R$')
print(f'se deseja mesclar latas e galoes sera nescessario {mixlatas} latas e {mixgaloes} galoes e ira custar {total_mix:.2f}R$')

'''
16 Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
mb = int(input('digite o temanho do arquivo em MB:'))
link = int(input('digite a velocidade da sua internet em mbps:'))
tempo = (mb / (link / 8)) / 60
print('demorara', round(tempo), 'minutos para baixar este aquirvo')

'''
obs: no momento so consegui fazer ate o 13 sozinho,o exercicio 14,15 e 16 tive q procurar como fazer,parando pra ler o 14
ate consigo entender,mas o 15 e 16 ja reli algumas vezes e mesmo assim n entendo,se puder me ajudar a entender fico muito
agradecido.
'''
#b
