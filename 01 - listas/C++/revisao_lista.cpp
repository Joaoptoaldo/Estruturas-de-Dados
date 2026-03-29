#include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include <cstdlib>
#include <algorithm>

#include "minha_biblioteca.h"

int main(){
    vector<int> lista_numerosA;
    vector<int> lista_numerosB;
    vector<int> lista_resultado;
    string nome_arquivo;
    srand(time(0)); // inicializa a semente para números aleatórios

    popular_aleatorio(lista_numerosA, 10); // popular a lista A com 10 números aleatórios
    exibir(lista_numerosA);// exibe a lista 

    nome_arquivo = "numeros.txt"; // nome do arquivo a ser lido
    popular_de_arquivos(lista_numerosB, nome_arquivo); // popular a lista B a partir do arquivo

    exibir(lista_numerosB); 

    copiar_lista_sem_republicados(lista_numerosB, lista_resultado); // copia os elementos da lista A para a lista resultado, sem repetições
    exibir(lista_resultado); // exibe a lista resultado

    return 1;
}