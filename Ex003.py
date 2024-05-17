# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# - o primeiro valor é maior
# - o segundo valor é maior
# - não existe valor maior, os dois são iguais

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O número {} é maior que o número {}'.format(num1,num2))
elif num1 < num2:
    print('O número {} é menor que {}'.format(num1,num2))
else:
    print('O número 1 é igual ao número 2!')