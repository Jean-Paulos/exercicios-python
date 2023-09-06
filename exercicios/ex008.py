'''
Desafio 008 - Conversão de Medidas 
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. 
'''

valor = float(input('Digite um valor em metros: '))
print(f'A medida de {valor} M corresponde a {valor * 100} Cm e {valor * 1000} Mm.')

# Extra: use quilômetros, hectômetros,  decâmetros,  decímetros, centímetros e milímetros.

print(f'Também correspondem a {valor / 1000} Km, {valor / 100} Hm e {valor * 10} Dm')