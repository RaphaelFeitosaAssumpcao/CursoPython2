# Crie um projeto que mostre a soma de números divisíveis por 3
soma = 0
count = 0
for c in range(1,501,2):
    if c % 3 == 0:
        count += 1
        soma += c
print('O soma de todos os valores solicitados é {} e possui {} numeros'.format(soma,count))