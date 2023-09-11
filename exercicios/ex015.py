'''
Desafio 015 - Cálculo do Aluguel de Carro
Faça um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por quilômetro rodado.
'''

quantidade_rodada = float(input('Digite quantidade de quilômetros percorridos: '))
quantidade_dia = int(input('Digite quantos dias foram: '))

custo_km = quantidade_rodada * 0.15
custo_dia = quantidade_dia * 60

print(f'O valor que deve ser pago é de R$ {custo_km + custo_dia}.')