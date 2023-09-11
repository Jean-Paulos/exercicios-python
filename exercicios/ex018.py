'''
Desafio 018 - Seno, Cosseno e Tangente
Faça um programa que leia um ângulo qualquer e mostre na tela o seno, cosseno e tangente desse ângulo.
'''
import math

angulo = float(input('Digite o ângulo que deseja calcular: '))

radiano = math.radians(angulo)

print(f'O ângulo de {angulo} graus tem:\nSeno: {math.sin(radiano):.2f}\nCosseno: {math.cos(radiano):.2f}\nTangente: {math.tan(radiano):.2f}')