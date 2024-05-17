# Crie um projeto onde mostre se o triãngulo é equilátero, isósceles ou escaleno
lado1 = float(input('Qual o valor do primeiro lado do triângulo?: '))
lado2 = float(input('Qual o valor do segundo lado do triângulo?: '))
lado3 = float(input('Qual o valor do terceiro lado do triângulo?: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 and lado2 == lado3:
        print('O triângulo informado possui todos os lados iguais, sendo um triângulo EQUILÁTERO!')
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        print('O triângulo informado possui dois lados iguais, sendo um triângulo ISÓSCELES!')
    else:
        print('O triângulo informado possui todos os lados diferentes, sendo um triângulo ESCALENO!')
else:
    print('Os lados acima não formam um triângulo!')