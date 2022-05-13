#Exercicio 9
'''
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.
'''

cpf = str(input('DIgite o CPF no seguinte formato: [xxx.xxx.xxx-xx]: '))

while cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
    print('CPF digitado incorretamente.')
    cpf = str(input('DIgite o CPF no seguinte formato: [xxx.xxx.xxx-xx]'))
print('CPF digitado corretamente.')