 # Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
genero  = str(input('Digite seu gênero [M/F]: ')).strip().upper()[0]

while genero not in 'MmFf':
    genero = str(input('Dados inválidos, por favor coloque seu gênero novamente: ')).upper()[0].strip()
print('Gênero registrado com sucesso, seu gênero é {}'.format(genero))