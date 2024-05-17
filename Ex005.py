# Crie um programa onde mostre a média de um aluno e fale se ele foi aprovado ou reprovado.
nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a primeira nota do {}: '.format(nome)))
nota2 = float(input('Digite a segunda nota do {}: '.format(nome)))
media = (nota1 + nota2) / 2

if media == 7:
    print('O aluno {} passou na média, parabéns pela sua aprovação!'.format(nome))
elif media > 7:
    print('O aluno {}, passou com média de {}, parabéns pela sua aprovação!'.format(nome, media))
else:
    falta = 7 - media
    print('O aluno {}, infelizmente reprovou com média de {}, precisando de {} para passar'.format(nome, media, falta))