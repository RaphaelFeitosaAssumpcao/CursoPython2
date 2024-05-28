# Crie um programa que leia vários números inteiros pelo teclado e no final mostre a soma entre eles. Sua ordem de parada é o número 999
num = soma = cont = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma desses números é de {}!!'.format(cont, soma))