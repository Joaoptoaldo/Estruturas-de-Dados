import random

from util import popular_lista_arquivo

letras = 'abcdefghijklmnopqrstuvwxyz '
lista = []

n = int(input("Quantas palavras quer gerar? "))
tamanho_palavra = 10 

contador = 0
while contador < n:
    palavra = ''

    for j in range(tamanho_palavra):
        posicao_letra = random.randint(0, len(letras) - 1)
        palavra += letras[posicao_letra]

    print("Palavra sorteada:", palavra)

    if palavra not in lista:
        lista.append(palavra)
        contador += 1  

lista.sort()
print("Palavras únicas geradas (ordenadas):")
print(lista)

