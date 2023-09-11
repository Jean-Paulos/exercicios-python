'''
Desafio 014 - Conversor de Temperatura
Escreva um programa que converta uma temperatura digitada em graus Celsius para graus Fahrenheit.
'''

celsius = int(input('Digite a temperatura em celsius: '))

fahrenheit = celsius * (9 / 5) + 32

print(f'{celsius} °C equivalem a {fahrenheit} °F')