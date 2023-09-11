'''
Desafio 019 - Sorteio do Aluno para Apagar o Quadro
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome do escolhido.
'''

import random

primeiro_aluno = input('Nome do primeiro aluno: ')
segundo_aluno = input('Nome do segundo aluno: ')
terceiro_aluno = input('Nome do terceiro aluno: ')
quarto_aluno = input('Nome do quarto aluno: ')

alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
sorteado = random.choice(alunos)

print(f'O aluno sorteado foi: {sorteado}')