#exercício 1
'''
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

    Compara duas strings
    String 1: Brasil Hexa 2006
    String 2: Brasil! Hexa 2006!
    Tamanho de "Brasil Hexa 2006": 16 caracteres
    Tamanho de "Brasil! Hexa 2006!": 18 caracteres
    As duas strings são de tamanhos diferentes.
    As duas strings possuem conteúdo diferente.
'''

string1 = str(input('Digite a primeira string: '))
string2 = str(input('Digite a segunda string: '))
print('\n')
print(f'String 1: {string1}')
print(f'String 2: {string2}')
print('\n')
print(f'Tamanho de "{string1}":{len(string1)}')
print(f'Tamanho de "{string2}":{len(string2)}')
print('\n')
if string1 == string2:
    print('As duas strings são identicas.')
else:
    print('As duas strings são diferentes.')
if len(string1) == len(string2):
    print('As duas strings tem o mesmo tamanho.')
else:
    print('As duas strings tem tamanhos diferentes.')