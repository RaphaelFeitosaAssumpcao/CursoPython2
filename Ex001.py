# Crie um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O progama vai perguntar o valor da casa . O salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder a 30% do salário ou então o empréstimo será negado.

valor = float(input('Digite o valor da casa:R$ '))
salário = float(input('Digite o salário do comprador:R$ '))
anos = int(input('Digite quantas anos você deseja pagar: '))
parcela = (anos*12)
mensal = valor / parcela

if mensal > salário * (30/100):
    print('A sua parcela seria de {:.2f} e ultrapassa o valor permitido'.format(mensal))
    print('Aumente o número de parcelas ou procure uma casa mais barata.')
elif mensal == salário * (30/100):

    print('A compra foi aprovada com o mensal de {:.2f}, porém tome cuidado porque consumiu 30% do seu salário de {}'.format(mensal,salário))
    print('Parabéns pela sua compra')
else:
    print('A compra foi aprovada com o mensal de {:.2f} e com isso você se mantém uma segurança financeira.'.format(mensal))
    print('Parabéns pela sua compra!')