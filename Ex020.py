 # Crie um programa que leia dois valores e mostre um menu na tela:
escolha = 0
while escolha != 5:
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    print('''Escolha uma dessas opções:
    [1] soma
    [2] multiplicar
    [3] maior
    [4] novos números 
    [5] sair do programa''')
    escolha = int(input('Qual sua escolha?: '))
    if escolha == 1:
        resp = num1 + num2
        print('O valor da soma dos seus dois números é de {}'.format(resp))
    elif escolha == 2:
        resp = num1 * num2
        print('O valor da multiplicação dos seus dois números é de {}'.format(resp))
    elif escolha == 3:
        resp = 0
        if num1 > num2:
            resp = num1
            print('O maior número é o {}'.format(num1))
        else:
            resp = num2
            print('O maior número é o {}'.format(num2))
    elif escolha == 4:
        num1 = int(input('Digite seu novo primeiro valor: '))
        num2 = int(input('Digite seu novo segundo valor: '))
    elif escolha == 5:
        print('Finalizando o programa...')
    else:
        print('Opção inválida...')
print('Fim do programa, volte sempre!')