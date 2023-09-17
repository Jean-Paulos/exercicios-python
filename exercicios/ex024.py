'''
Desafio 024 - Verificando o Nome da Cidade Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
'''

nome = input('Digite o nome da cidade: ').split()
print('SANTO' in nome[0].upper())