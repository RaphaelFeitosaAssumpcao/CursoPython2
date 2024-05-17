# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
soma = 0
count = 0
for c in range(1,7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        count += 1
        soma += num
print('Possuem {} números  pares digitados e a soma deles é {}'.format(count, soma))