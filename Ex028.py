# Faça um programa que mostre a tabuada de vários números um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado por negativo

num = cont = 0
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    print('-'*30)
    for c in range(0,10):
        value = num * (c+1)
        print(f'{num} X {c+1} = {value}')
    print('-' * 30)
    cont += 1
print(f'O processo da tabuana foi finalizado com {cont} números digitados')