# computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
computador = random.randint(1,10)
print('Sou seu computador, estou pensando em um número aletório.....')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Digite um número de 1 a 10: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    elif jogador > computador:
        print('Menos.. Tente novamente: ')
    else:
        print('Mais... Tente novamente: ')
print('Parabéns você GANHOU o jogo!')
print(' Você tentou {} vezes até acertar.'.format(palpites))