#Exercicio 13
'''
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
'''

import random

biblioteca = ['atleta', 'carro', 'verdura', 'cachorro']
vidas_usuario = 7
palavra_aleatoria = random.choice(biblioteca)
palavra_embaralhada = ''.join(random.sample(palavra_aleatoria, len(palavra_aleatoria)))

while vidas_usuario != 0:
    print('quantidade de vidas: ', vidas_usuario)
    print(palavra_embaralhada)
    resposta_usuario = input('Que palavra é essa? : ')
    if resposta_usuario == palavra_aleatoria:
        print('Você acertou, a palavra era: ', palavra_embaralhada)
        break
    else:
        vidas_usuario -= 1