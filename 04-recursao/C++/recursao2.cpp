#include <iostream>

using namespace std;


void mostrarSequenciaD(int numero) {
    for (; numero > 0; numero--) {
        cout << numero << endl;
    }
}
 
void mostrarSequenciaC(int numero) {
    for (int i = 1; i <= numero; i++) {
        cout << i << endl;
    }
}
 
/*
recursão como repetição, obedece a 3 situações classicas:
  a) inicialização da variavel de controle (contador);
  b) teste de parada/continuação com a variavel de controle (condição de parada);
  c) transformação da variavel de controle (atualização do contador).

  void mostrarSequencia(a){
  for(;b;c){
    mostrarSequencia(a);}
  }
}
*/

 void mostrarSequenciaRecursiva(int numero) {
    if (numero > 0) {
        //executar codigo no empilhamento
       
        mostrarSequenciaRecursiva(numero - 1); //PONTO DE RECURSAO COM A TRANSFORMAÇÃO DA VARIAVEL DE CONTROLE
       
        //executar codigo no desempilhamento
        cout << numero << endl;
    }
}

int main() {

  int numero = 5;

  mostrarSequenciaD(numero);
  mostrarSequenciaC(numero);
  mostrarSequenciaRecursiva(numero);

  return 0;
}

