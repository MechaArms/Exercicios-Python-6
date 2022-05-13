#Exercicio 7
'''
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

    a.quantos espaços em branco existem na frase.
    b.quantas vezes aparecem as vogais a, e, i, o, u.
'''

frase = str(input('Digite uma frase: ')).lower()
espacos = frase.count(' ')
vogais = []
for i in range(len(frase)):
    if frase[i] in ['a', 'e', 'i', 'o', 'u']:
        vogais.append(frase[i])
    else:
        continue
print('\nExistem ', espacos, 'espaços na frase.')
print('A: ', vogais.count('a'), '\nE: ', vogais.count('e'), '\nI: ', vogais.count('i'), '\nO: ', vogais.count('o'), '\nU: ', vogais.count('u'))