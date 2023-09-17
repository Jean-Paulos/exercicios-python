'''
Desafio 022 - Manipulação de Nomes 
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com todas as letras minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''

nome = input('Digite o seu nome completo: ')
nome_sem_espaco = nome.replace(" ", "")
primeiro_nome = nome.split()

print(f'O nome com todas as letras maiúsculas: {nome.upper()}.')
print(f'O nome com todas as letras minúsculas: {nome.lower()}.')
print(f'Quantas letras ao todo: {len(nome_sem_espaco)}')
print(f'Quantas letras tem o primeiro nome: {len(primeiro_nome[0])}')