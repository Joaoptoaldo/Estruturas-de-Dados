import random
from util import ler_arquivo_lista, popular_lista_arquivo

letras = 'abcdefghijklmnopqrstuvwxyz '
lista = []

n = int(input("Quantas palavras quer gerar? "))
tamanho_palavra = int(input('Digite o tamanho da palavra que quer gerar? '))

i = 0
while (i < n):
    palavra = ''
    for i in range(n):
        palavra = ''
        for j in range(tamanho_palavra):
            posicao_letra = random.randint(0, len(letras)-1)
            palavra += letras[posicao_letra]
        
        if(palavra not in lista):
            lista.append(palavra)
            i += 1

lista.sort()
print("Palavras sorteadas:", lista)
popular_lista_arquivo(lista, 'nomes.txt')

