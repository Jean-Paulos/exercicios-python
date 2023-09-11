'''
Desafio 020 - Sorteio da Ordem de Apresentação
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random
primeiro_aluno = input('Digite o nome do primeiro aluno: ')
segundo_aluno = input('Digite o nome do segundo aluno: ')
terceiro_aluno = input('Digite o nome do terceiro aluno: ')
quarto_aluno = input('Digite o nome do quarto aluno: ')

alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
random.shuffle(alunos)

print(f'A ordem de apresentação será:\n1° {alunos[0]}\n2° {alunos[1]}\n3° {alunos[2]}\n4° {alunos[3]}')

