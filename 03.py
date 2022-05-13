#Exercicio 3
'''
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

    F
    U
    L
    A
    N
    O
'''

nome = str(input('Digite o seu nome: '))
for i in range(len(nome)):
    print(nome[i].upper(), '\n')