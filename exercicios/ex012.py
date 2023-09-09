'''
Desafio 012 - Cálculo de Desconto em um Produto 
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. 
'''

valor_do_produto = float(input('Digite o valor do produto: '))
desconto = valor_do_produto * 5 / 100
print(f'Com desconto de 5%, o seu produto vai sair por R$ {valor_do_produto - desconto:.2f}.')