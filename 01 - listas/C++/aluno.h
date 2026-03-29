#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

struct Aluno {
    string Nome;
    string Email;

    // construtor que recebe o nome completo do aluno e gera o email automaticamente
    Aluno(string nomeCompleto) {
        Nome = nomeCompleto;
        Email = gerarEmail(nomeCompleto);
    }

    // função auxiliar dentro da struct
    string gerarEmail(string n) {
        stringstream ss(n);
        string palavra;
        vector<string> partes;

        while (ss >> palavra) {
            partes.push_back(palavra);
        }

        if (partes.empty()) return "";

        string primeiro = partes.front();
        string ultimo = partes.back();

        // convertendo para minúsculo com for e tolower
        for (int i = 0; i < primeiro.length(); i++) {
            primeiro[i] = tolower(primeiro[i]);
        }
        for (int i = 0; i < ultimo.length(); i++) {
            ultimo[i] = tolower(ultimo[i]);
        }

        return primeiro + "." + ultimo + "@ufn.edu.br";
    }
};