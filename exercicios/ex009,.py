'''
Desafio 009 - Tabuada
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
'''
numero = int(input('Qual tabuada gostaria de ver: '))
print(f'Tabuada do {numero}')
print('-' * 15)
for i in range(1, 11):
  print(f"{i} X {numero} = {i * numero}")
print('-' * 15)