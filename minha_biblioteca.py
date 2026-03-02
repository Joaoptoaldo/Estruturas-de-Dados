from random import random
import random


def popular_aleatorio(lista: list, quantidade: int):
    """_summary_
    método que recebe uma lista e popula com números aleatórios

    Args:
        lista (list): lista genérica de dados primitivos
        quantidade (int): quantidade de números gerados aleatoriamente lista
    """
    for i in range(quantidade):
        numero_aleatorio = random.randint(1, 100)
        lista.append(numero_aleatorio)


def popular_de_arquivos(lista, nome_arquivo):
    """_summary_
    método que recebe uma lista e popula com números lidos de um arquivo

    Args:
        lista (_type_): lista genérica 
        nome_arquivo (string): nome do arquivo de onde os números serão lidos
    """
    with open(nome_arquivo, 'r', encoding='utf-8') as leitor:
        for linha in leitor:
            lista.append(linha.strip())


def exibir(lista):
    """_summary_
    método que recebe uma lista genérica e exibe todos os seus elementos contidos nela (um abaixo do outro)
    e no final exibe a quantidade de elementos contidos na lista

    Args:
        lista (_type_): lista genérica
    """
    for i in lista:
        print(i)

    print("-----------------------")
    print("Quantidade de elementos:", len(lista))

def copiar_lista_sem_replicados(lista_origem, lista_destino):
    """
    método que recebe uma lista origem e copia seus elementos para uma lista destino, retirando os replicados

    Args:
        lista_origem (_type_): lista genérica de onde os elementos serão copiados
        lista_destino (_type_): lista genérica para onde os elementos serão copiados
    """
    for i in lista_origem: # para cada elemento i contido na lista origem
        if i not in lista_destino: 
            lista_destino.append(i) 



