# Faça um programa que jogue par ou impar com o computador
# O jogo só terminará na hora que o jogador perder, mostrando o número de vitórias consecutivas dele.
from random import randint
v = 0
while True:
    num = int(input('Digite seu número: '))
    computador = randint(0,11)
    total = num + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou impar?[P/I]:')).upper().strip()[0]
    print(f'Você jogou {num} e o computador jogou {computador} o total é {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!!')
            break
    print('Vamos jogar novamente....')
print(f'Game over você perdeu, porém ganhou {v} vezes')