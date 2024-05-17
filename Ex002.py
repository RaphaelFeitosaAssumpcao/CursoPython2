#Crie um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print ('''Escolha uma dessas bases para conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
esc = int(input('Digite uma opção de 1 a 3: '))
if esc == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif esc == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)))
elif esc == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num,hex(num)))
else:
    print('Opção inválida!')
