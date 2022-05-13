#Exercicio 4
'''
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

    F
    FU
    FUL
    FULA
    FULAN
    FULANO
'''

nome = str(input('Informe o nome: '))
vazia = ''
for letra in nome:
    vazia += letra
    print(vazia)