# Crie um programa do jogo de Pedra, papel e tesoura
import random
itens = ('Pedra','Papel', 'Tesoura')
computador = random.randint (0,2)
print('''Escolha sua jogada:
[0] Pedra
[1] Papel
[2] Tesoura 
''' )
jogador  = int(input('Qual será sua jogada?: '))

if jogador == 0:
    if computador == 1:
        print('A máquina escolheu Papel e você PERDEU escolhendo Pedra.')
    elif computador == 2:
        print('A máquina escolheu Tesoura e você GANHOU escolhendo Pedra.')
    else:
        print('A partida EMPATOU, jogue novamente e tente a sorte!')
elif jogador == 1:
    if computador == 0:
        print('A máquina escolheu Pedra e você GANHOU escolhendo Papel.')
    elif computador == 2:
        print('A máquina escolheu Tesoura e você PERDEU escolhendo Papel.')
    else:
        print('A partida EMPATOU, jogue novamente e tente a sorte!')
elif jogador == 2:
    if computador == 0:
        print('A máquina escolheu Pedra e você PERDEU escolhendo Tesoura.')
    elif computador == 1:
        print('A máquina escolheu Papel e você GANHOU escolhendo Tesoura')
    else:
        print('A partida EMPATOU, jogue novamente e tente a sorte!')
else:
    print('Você digitou um número inválido!!')

