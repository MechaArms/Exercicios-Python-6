#Exercicio 12
'''
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

    Valida e corrige número de telefone
    Telefone: 461-0133
    Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
    Telefone corrigido sem formatação: 34610133
    Telefone corrigido com formatação: 3461-0133
'''

#555-9999
n_telefone = str(input('Digite o n° do telefone: '))

while len(n_telefone) > 9 or len(n_telefone) < 8:
    print('O número precisa ter 8 ou 7 digitos')
    n_telefone = str(input('Digite o n° do telefone: '))
print(len(n_telefone))

if len(n_telefone) == 8:
    print ('Telefone possui 7 digitos. Vou acrescentar o digito tres na frente.')
    n_telefone = '3' + n_telefone

telefoneLimpo = n_telefone.replace('-', '')

print('Telefone corrigido sem formatacao: ', telefoneLimpo)
print('Telefone corrigido com formatacao: ',n_telefone) 