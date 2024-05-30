# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não
# Qual o total gasto na compra - quantos produtos custam mais de R$1000 - qual é o nome do produto mais barato

total = soma = totalp = menor = cont = 0
while True:
    nproduto = str(input('Digite o nome do produtor: '))
    total = float(input('Digite o valor do produto: R$ '))
    soma += total
    cont +=1
    if cont == 1:
        menor = total
    else:
        if total < menor:
            menor = total
    if total > 1000:
        totalp += 1
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O total de produtos comprados é {totalp}, o valor de tudo deu {soma} ')
print(f'O produto mais barato é R${menor}')

