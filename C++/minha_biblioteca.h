#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <fstream>
#include <string>

using namespace std;

/**
 * @brief Função para popular um vetor com números aleatórios   
 * @param vetor 
 * @param quantidade 
 * @return 
 */


// função para popular um vetor com números aleatórios
void popular_aleatorio(vector<int>& vetor, int quantidade) {
    random_device rd; // gerador de números aleatórios
    mt19937 gen(rd()); // motor de geração de números aleatórios
    
    // distribuição uniforme de números entre 1 e 100
    uniform_int_distribution<> dis(1, 100);

    for (int i = 0; i < quantidade; ++i) {
        int numero_aleatorio = dis(gen); // gera um número aleatório
        vetor.push_back(numero_aleatorio); // adiciona ao vetor
    }
}


/**
 * @brief método para popular um vetor a partir de um arquivo
 * 
 * @param lista 
 * @param nome_arquivo 
 */
void popular_de_arquivos(vector<int>& vetor, string nome_arquivo) {
    // implementação para popular o vetor a partir de um arquivo

    ifstream procurador;
    procurador.open(nome_arquivo); // abre o arquivo para leitura
    // verifica se o arquivo foi aberto 

    if (!procurador){
        cout << "Erro ao abrir o arquivo: " << nome_arquivo << endl;
        return; // sai da função se o arquivo não puder ser aberto
    }

    string linha;
    while (!procurador.eof()) { // enquanto não chegar ao final do arquivo
        getline(procurador, linha); // lê uma linha do arquivo
        if (!linha.empty()) { // verifica se a linha não está vazia
            try {
                int numero = stoi(linha); // converte a linha para um número inteiro
                vetor.push_back(numero); // adiciona o número ao vetor
            } catch (const invalid_argument& e) {
                cout << "Linha inválida no arquivo: " << linha << endl; // mensagem de erro para linhas que não podem ser convertidas
            }
        }
    }
}


/**
 * @brief método para exibir os elementos de um vetor
 * 
 * @param lista 
 */
void exibir(const vector<int>& lista){
    // percorre a lista exibindo cada elemento
    for (int i : lista){
        cout << i << endl;
    }

    cout << "-----------------------------" << endl;

    // .size() é equivalente ao len() do Python, retorna a quantidade de elementos no vetor
    cout << "Quantidade de elementos: " << lista.size() << endl;
}

void copiar_lista_sem_republicados(const vector<int>& lista_origem, vector<int>& lista_destino) {
    // copia os elementos da lista de origem para a lista de destino, sem repetições
    for (int i : lista_origem) {
        // verifica se o número já existe na lista de destino
        if (find(lista_destino.begin(), lista_destino.end(), i) == lista_destino.end()) {
            lista_destino.push_back(i); // adiciona o número à lista de destino
        }
    }
}



