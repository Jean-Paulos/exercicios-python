'''
Desafio 023 - Separando Dígitos de um Número 
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''

numero = int(input('Digite um número de 0 a 9999: '))
preencher = f'{numero:0>4}'

print(f'Uni: {preencher[3]}\nDez: {preencher[2]}\nCen: {preencher[1]}\nMil: {preencher[0]} ')