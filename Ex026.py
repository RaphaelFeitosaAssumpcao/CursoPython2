# Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os valores e qual foi maior e o menor dos valores
escolha = 'S'
soma = media = quant = maior = menor =  0
while escolha in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    escolha = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
media = soma / quant
print('A média dos valores é de {}, seu maior número é {} e seu menor número é {}'.format(media, maior, menor))

