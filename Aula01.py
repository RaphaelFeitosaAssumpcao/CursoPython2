nome = str(input('Qual é seu nome? '))
if nome == 'Raphael':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Matheus':
    print('Seu nome é bastante usado, tenha um bom dia {}!'.format(nome))
else:
    print('Seu nome é comum, tenha um bom dia {}'.format(nome))