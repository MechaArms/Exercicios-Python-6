#Exercicio 11
'''
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

    Digite uma letra: A
    -> Você errou pela 1ª vez. Tente de novo!
    
    Digite uma letra: O
    A palavra é: _ _ _ _ O
    
    Digite uma letra: E
    A palavra é: _ E _ _ O
    
    Digite uma letra: S
    -> Você errou pela 2ª vez. Tente de novo!
'''

import random

palavras = ['melancia', 'tangerina', 'carro', 'dia', 'universo', 'galaxia', 'amor',
    'filosofia', 'antagonista']

palavraEscolhida = palavras[
    random.randint(0, len(palavras) - 1)].upper().strip()
tamanhoPalavra = len(palavraEscolhida)
palavraAdivinhada = ['_'] * tamanhoPalavra

numTentativas = 0
numErros = 0

while (''.join(palavraAdivinhada) != palavraEscolhida) and (numErros < 6):

    letra = input('\nDigite uma letra: ').upper()
    numTentativas += 1
    acertou = False

    print('A palavra é: ',end = '')
    for i in range(0, tamanhoPalavra):
        if (palavraEscolhida[i] == letra):
            palavraAdivinhada[i] = letra
            acertou = True
        print (palavraAdivinhada[i], end='')
    print('')
    if (not acertou):
        numErros += 1
        print('Voce errou pela ',numErros, 'vez.')

if (numErros < 6):
    print('\nVoce acertou!')
else:
    print('\nVoce perdeu!')
    print('A palavra era ',palavraEscolhida)