# Melhorando o código de PA
# Faça um programa onde leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais?: '))
print('Progressão finalizada com {} termos mostrados!'.format(total))
