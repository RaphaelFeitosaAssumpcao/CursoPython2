# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o valor 999 for digitado.
# No final mostre quantos números foram digitados e qual foi a soma entre eles

cont = soma = num = 0
while True:
    num =int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'O usuário digitou {cont} números e a soma desses números deu {soma}')