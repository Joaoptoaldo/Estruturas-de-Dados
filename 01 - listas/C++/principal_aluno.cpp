#include <iostream>
#include <string>
#include <vector>
#include <clocale>
#include "aluno.h" // incluindo o arquivo onde a struct Aluno está definida

using namespace std;


int main() {
    setlocale(LC_ALL, "Portuguese");

    vector<Aluno> lista;
    string nome;

    while (true) {
        cout << "Digite o nome do aluno (ou 'sair' para encerrar): ";
        getline(cin, nome);

        // verifica se o usuário quer sair (convertendo pra conferir)
        string buscaSair = nome;
        for (int i = 0; i < buscaSair.length(); i++) {
            buscaSair[i] = tolower(buscaSair[i]);
        }

        if (buscaSair == "sair") {
            break;
        }

        // verifica se a string está vazia
        if (nome.empty() || nome.find_first_not_of(' ') == string::npos) {
            continue;
        }

        // criando o objeto aluno e adicionando no vector
        Aluno novoAluno(nome);
        lista.push_back(novoAluno);
        
        cout << "Email gerado: " << novoAluno.Email << "\n" << endl;
    }

    cout << "\n--- ALUNOS CADASTRADOS ---" << endl;
    

    for (const auto& aluno : lista) {
        cout << "Nome: " << aluno.Nome << " | Email: " << aluno.Email << endl;
    }

    return 0;
}