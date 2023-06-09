# 1 Faça um Programa que peça dois números e imprima o maior deles.
valor_1 = int(input('digite o primeiro numero: '))
valor_2 = int(input('digite o segundo valor: '))
if valor_1 > valor_2:
    print(valor_1, 'é maior')
else:
    print(valor_2, 'é maior')

# 2 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
num = int(input('digite um numero:'))
if num < 0:
    print(num, '= esse numero e negativo')
else:
    print(num, '= esse numero e positivo')


# 3 Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.
f_m = input('digite F ou M: ')
if f_m == 'f' or f_m == 'F' or f_m == 'm' or f_m == 'M':
    # esse if serve para verificar todas as posibilidades em uma linha ao inves de ir para um if depois um elif e assim por diante
    f_m = input('digite a letra F ou M: ')
    if f_m == 'f' or f_m == 'F':
        print(f_m, '- feminino')
    elif f_m == 'm' or f_m == 'M':
        print(f_m, '- masculino')
else:
    print('sexo invalido')


# 4 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('digite uma letra: ')

Letra_Mm = letra.lower()
# .lower() verifica as variveis,com isso vc n precisa digitar tanto em maiusculo como em minusculo

alfabeto = list(map(chr, range(ord('a'), ord('z') + 1)))
# a lista de range esta passando como parametro para a funçao map,e pra cada item em range,map vai execultar a funçao chr
# para devolver o caracter equivalente aquele numero,entao tudo isso e transformado em uma list atribuida a variavel

if Letra_Mm in alfabeto:
    if Letra_Mm in ['a', 'e', 'i', 'o', 'u']:
        print('essa letra e uma vogal')
    else:
        print('essa letra e uma consoante')
else:
    print('digite apenas letras')


# 5Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar: A mensagem "Aprovado",
# se a média alcançada for maior ou igual a sete; A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota = float(input('digite a primeira nota do aluno: '))
nota_2 = float(input('digite a segunda nota do aluno: '))
media = (nota + nota_2) / 2
print('a media do aluno é', media)
if media == 10:
    print('aprovado com distinçao')
elif media >= 7 and media < 10:
    print('aprovado')
else:
    print('reprovado')


# 6 Faça um Programa que leia três números e mostre o maior deles.
primeiro = int(input('digite o primeiro valor:'))
segundo = int(input('digite o segundo valor:'))
terceiro = int(input('digite o terceiro valor:'))

if primeiro > segundo and primeiro > terceiro:
    print('o primeiro numero é maior')
elif segundo > primeiro and segundo > terceiro:
    print('o segundo numero é maior')
else:
    print('o terceiro numero é maior')

# 7 Faça um Programa que leia três números e mostre o maior e o menor deles.
primeiro = int(input('digite o primeiro valor:'))
segundo = int(input('digite o segundo valor:'))
terceiro = int(input('digite o terceiro valor:'))

if primeiro > segundo and primeiro > terceiro:
    print('o primeiro numero é maior')
    if segundo < terceiro:
        print('o segundo e menor')
    else:
        print('o terceiro e menor')

elif segundo > primeiro and segundo > terceiro:
    print('o segundo e maior')
    if primeiro < terceiro:
        print('o primeiro e menor')
    else:
        print('o terceiro e menor')

elif terceiro > primeiro and terceiro > segundo:
    print('o terceiro e maior')
    if primeiro < segundo:
        print('o primeiro e menor')
    else:
        print('o segundo e menor')


# 8 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

produto_1 = float(input('digite o valor do primeiro prduto: '))
produto_2 = float(input('digite o valor do segundo prduto: '))
produto_3 = float(input('digite o valor do terceiro prduto: '))

if produto_1 < produto_2 and produto_1 < produto_3:
    print('o primeiro produto esta mais em conta')
elif produto_2 < produto_1 and produto_2 < produto_3:
    print('o segundo produto esta mais em conta')
else:
    print('o terceiro produto esta mais em conta')


# 9 Faça um Programa que leia três números e mostre-os em ordem decrescente.
num_1 = float(input('digite o primeiro numero: '))
num_2 = float(input('digite o segundo numero: '))
num_3 = float(input('digite o terceiro numero: '))

if num_1 > num_2 > num_3:
    print('a ordem decrescente é:', num_1, num_2, num_3)
if num_1 > num_3 > num_2:
    print('a ordem decrescente é:', num_1, num_3, num_2)

if num_2 > num_1 > num_3:
    print('a ordem decrescente é:', num_2, num_1, num_3)
if num_2 > num_3 > num_1:
    print('a ordem decrescente é:', num_2, num_3, num_1)

if num_3 > num_1 > num_2:
    print('a ordem decrescente é:', num_3, num_1, num_2)
if num_3 > num_2 > num_1:
    print('a ordem decrescente é:', num_3, num_2, num_1)


# 10 Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.

turno = input('em que turno voce estuda (digite para M-matutino ou V-Vespertino ou N- Noturno): ')

Tmvn = turno.lower()
# .lower() verifica as variveis,com isso vc n precisa digitar tanto em maiusculo como em minusculo

if Tmvn == 'm':
    print('voce estuda na parte da manhã')

elif Tmvn == 'v':
    print('voce estuda na parte da tarde')

elif Tmvn == 'n':
    print('voce estuda na parte da noite')

else:
    print('digite uma letra conforme o pedido')
