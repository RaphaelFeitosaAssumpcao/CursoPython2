# Crie um projeto onde mostre seu imc:
#  menor que 18.5 = abaixo do peso / de 18.5 a 25 = ideal / 25 até 30 = sobrepeso / 30 até 40 = obesidade / 40 + = obesidade mórbida
p = float(input('Qual seu peso?: '))
a = float(input('Qual sua altura?: '))
imc = p /( a * 2)

if imc < 18.5:
    print('Você está abaixo do peso ideal com {:.2f} de imc.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Parabéns você tem o imc de {:.2f} e está no peso ideal para sua saúde '.format(imc))
elif imc >= 25 and imc < 30:
    print('Cuidado, você está com imc de {:.2f} e está com sobrepeso.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Cuidade, você está com imc de {:.2f} e está com obesidade.'.format(imc))
else:
    print('ATENÇÃO MÁXIMA, você está com imc de {:.2f} e está com OBESIDADE MÓRBIDA.'.format(imc))