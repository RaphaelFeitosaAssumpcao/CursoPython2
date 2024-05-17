# Crie um programa onde com o ano de nascimento de uma pessoa defina a pessoa pela idade entre:
# MIRIM (MENOS DE 9 ANOS), INFANTIL (ENTRE 9 E 14 ANOS),JUNIOR (ENTRE 14 A 19 ANOS), SENIOR (ENTRE 19 A 25 ANOS), MASTER(MAIOR DE 25 ANOS)
import datetime
atual = datetime.date.today().year
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = atual - nascimento

if idade <=9:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: SENIOR')
else:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: MASTER')