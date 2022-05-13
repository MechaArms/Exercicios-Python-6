#Exercicio 5
'''
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

    FULANO
    FULAN
    FULA
    FUL
    FU
    F
'''

nome = input('Informe o nome: ')
vazio1 = ''
vazio2 = ''
for letra in nome:
    vazio1 += letra
for i in range(len(nome)):
    vazio2 = vazio1[0:len(nome) -i:]
    print(vazio2)