'''
Desafio 017 - Comprimento da Hipotenusa
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

print(f'O comprimento da hipotenusa é {hipotenusa:.2f}.')