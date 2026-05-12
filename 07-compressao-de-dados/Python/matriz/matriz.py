from typing import List
from dado import Dado


class Matriz:

    @staticmethod
    def inicializar_matriz(matriz: List[List[int]], qtd_l: int, qtd_c: int) -> None:
        """_summary_: método de classe que inicializa uma matriz de inteiros com zeros

        Args:
            matriz (List[List[int]]): _description_: matriz de inteiros a ser inicializada
            qtd_l (int): _description_: quantidade de linhas
            qtd_c (int): _description_: quantidade de colunas
        """
        for i in range(qtd_l):
            for j in range(qtd_c):
                matriz[i][j] = 0

    @staticmethod
    def exibir_matriz(matriz: List[List[int]], qtd_l: int, qtd_c: int) -> None:
        """_summary_: método de classe que exibe uma matriz de inteiros

        Args:
            matriz (List[List[int]]): _description_: matriz de inteiros a ser exibida
            qtd_l (int): _description_: quantidade de linhas
            qtd_c (int): _description_: quantidade de colunas
        """
        for i in range(qtd_l):
            for j in range(qtd_c):
                print(f"{matriz[i][j]}\t", end="")
            print()

    @staticmethod
    def converter_matriz_lista(
        matriz: List[List[int]], qtd_l: int, qtd_c: int, lista: List[Dado]
    ) -> None:
        """_summary_: método de classe que converte uma matriz de inteiros em uma lista de dados

        Args:
            matriz (List[List[int]]): _description_: matriz de inteiros a ser convertida
            qtd_l (int): _description_: quantidade de linhas
            qtd_c (int): _description_: quantidade de colunas
            lista (List[Dado]): _description_: lista de dados a ser preenchida com os elementos não nulos da matriz
        """
        for i in range(qtd_l):
            for j in range(qtd_c):
                if matriz[i][j] != 0:
                    lista.append(Dado(matriz[i][j], i, j))

    @staticmethod
    def exibir_lista(lista: List[Dado]) -> None:
        """_summary_: método de classe que exibe uma lista de dados

        Args:
            lista (List[Dado]): _description_: lista de objetos Dado a ser exibida
        """
        for dado in lista:
            print(dado)
        print("------------------------------")
        print("Total de elementos não nulos: " + str(len(lista)))