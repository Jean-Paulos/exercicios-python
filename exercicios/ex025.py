'''
Desafio 025 - Verificando a Presença de "SILVA" no Nome Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

nome = input('Digite o seu nome completo: ')
print('SILVA' in nome.upper().split())