'''
Desafio 013 - Aumento de Salário
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

salario = float(input('Digite o seu salario: '))
aumento = salario * 15 / 100
print(f'Com o aumento de 15%, o seu novo salario é R$ {salario + aumento:.2f}.')