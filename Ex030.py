# Crie um programa que leia a idade e sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer continuar ou não
# No final mostre: - quantas pessoas tem mais de 18 anos - quantos homens foram cadastrados - quantas mulheres tem menos de 20 anos
contIdade = contHomem = contMulher = 0
while True:
    sexo = ' '
    continuar = ' '
    idade = int(input('Digite sua idade: '))
    while sexo not in 'MmFf':
        sexo = str(input('Digite seu gênero [M/F]: ')).upper().strip()[0]
    if idade > 18:
        contIdade += 1
    if sexo in 'Mn':
        contHomem += 1
    if sexo in 'Ff' and idade <20:
        contMulher += 1
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    if continuar in 'Nn':
        break
print('-'*30)
print('O processo foi encerrado!!')
print(f'O processo obteve um resultado de {contIdade} pessoas com mais de 18 anos, {contHomem} homens cadastrados, {contMulher} mulheres com menos de 20 anos cadastradas.')