"""
Desafio 004 - Tipo Primitivo e Informações
Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele.
"""
valor = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(valor))
print('Só tem espaços? ', valor.isspace())
print('É númerico? ', valor.isnumeric())
print('É alfabético? ', valor.isalpha())
print('É alfanumérico? ', valor.isalnum())
print('Está em maiúsculas?', valor.isupper())
print('Está em minúsculas ', valor.islower())
print('Está capitalizada? ', valor.istitle())