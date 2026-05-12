from typing import List
from dado import Dado
from matriz import Matriz

def main():
    dimensao = 10
    matriz: List[List[int]] = [[0] * dimensao for _ in range(dimensao)]
    Matriz.inicializar_matriz(matriz, dimensao, dimensao)

    matriz[0][3] = 1
    matriz[2][5] = 1
    matriz[5][7] = 1
    matriz[6][6] = 1
    matriz[9][0] = 1

    Matriz.exibir_matriz(matriz, dimensao, dimensao)

    lista: List[Dado] = []
    Matriz.converter_matriz_lista(matriz, dimensao, dimensao, lista)
    Matriz.exibir_lista(lista)


if __name__ == "__main__":
    main()