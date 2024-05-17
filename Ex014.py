# Crie um projeto onde mostre a tabuada de um número usando 'for'
num = int(input('Digite o número que queira saber a tabuada: '))
for c in range(1,11):
    print(' {} x {:2} = {}'.format(num, c, num*c))