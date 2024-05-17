# Crie um programa onde mostre uma loja e sesus métodos de pagemento e seus descontos em cada método.
print('='*15, 'LOJAS RAPHAEL', '='*15)
c = float(input('Digite o valor de suas compras: '))
print('''FORMAS DE PAGAMENTO
[1] Á vista dinheiro / cheque
[2] Á vista no cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão''')
e = int(input('Qual a opção que deseja realizar o pagamento?: '))

if e == 1:
    value = c * (10/100)
    newValue = c - value
    print ('Você teve um desconto de 10% na sua compra de {} e teve um novo valor com a promoção de {}.'.format(c,newValue))
elif e == 2:
    value = c * (5/100)
    newValue = c - value
    print('Você teve um desconto de 10% na sua compra de {} e teve um novo valor com a promoção de {}.'.format(c,newValue))
elif e == 3:
    print('Você não possuiu desconto e sua compra permaneceu no valor de {}'.format(c))
else:
    value = c * (20/100)
    newValue = c + value
    print('Você recebeu um juros de 20% em sua compra, o valor antigo da sua compra era {} e o novo valor com juros é {}'.format(c,newValue))

