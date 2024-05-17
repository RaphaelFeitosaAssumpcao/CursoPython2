#Faça um programa que fala em que ano de nascimento de um jovem e informe de acordo com sua idade
#- Se ele ainda vai se alistar ao serviço militar
#- Se é a hora de se alistar
#- Se ele já passou do tempo do alistamento
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento

print('Quem nasceu em {} tem a idade de {} anos.'.format(nascimento,idade))

if idade < 18:
    print('Ainda não está na hora de se alistar')
    saldo = 18 - idade
    print ('Falta apenas {} anos para realizar seu alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será no ano de {}'.format(ano))
elif idade == 18:
    print('Você deve se alistar esse ano!')
else:
    print('Você já passou do tempo de se alistar')
    saldo = idade - 18
    print('Você passou {} anos de tempo do seu alistamento'.format(saldo))
    ano = atual - saldo
    print('O seu alistamento foi no ano de {}'.format(ano))