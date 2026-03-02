import random
from util import popular_lista_arquivo 
from util import ler_arquivo_lista

lista = []

n = int(input("Quantos numeros inteiros quer gerar? "))

i = 0 
while (i < n):
    numero_sorteado = random.randint(0, 100000)
    if (numero_sorteado not in lista):
        lista.append(numero_sorteado)
        i += 1

lista.sort()
print("Numeros sorteados:", lista)
popular_lista_arquivo(lista, 'numeros.txt')