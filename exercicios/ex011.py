'''
Desafio 011 - Calculadora de Tinta
Faça um programa que leia a altura e largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
'''
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
print(f'A área da parede é {area}m²\nA quantidade necessária de tinta vai ser {area / 2}')