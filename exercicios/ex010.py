'''
Desafio 010 - Conversão de Moeda 
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere que US$1,00 é igual a R$3,27. 
'''

reais = float(input('Quanto dinheiro você tem na carteira? '))
dolar = 3.27
print(f'Com valor de R$ {reais}, você consegue comprar U$ {reais / dolar:.2f}')

# Desafio Extra: Adicionado mais moedas e use a taxa de câmbio atual.

reais = float(input('Quanto dinheiro você tem na carteira? '))
dolar = 4.99
euro = 5.34
pesos_argentino = 0.014
print(f'Com valor de R$ {reais}, você consegue comprar aproximadamente:\nU$ {reais / dolar:.2f}\nEUR € {reais / euro:.2f}\nARS $ {reais / pesos_argentino:.2f}')