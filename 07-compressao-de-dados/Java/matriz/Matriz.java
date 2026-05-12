import java.util.ArrayList;

public class Matriz {
    /**
     * método de classe que inicializa uma matriz de inteiros
     * @param matriz - matriz de inteiros a ser inicializada
     * @param qtdL - quantidade de linhas
     * @param qtdC - quantidade de colunas
     */
    public static void inicializarMatriz(int matriz[][], int qtdL, int qtdC) {
        for (int i = 0; i < qtdL; i++) {
            for (int j = 0; j < qtdC; j++) {
                matriz[i][j] = 0;
            }
        }
    }
    /**
     * método de classe que exibe uma matriz de inteiros
    * @param matriz - matriz de inteiros a ser exibida
     * @param qtdL - quantidade de linhas
     * @param qtdC - quantidade de colunas
     */
    public static void exibirMatriz(int matriz[][], int qtdL, int qtdC) {
        for (int i = 0; i < qtdL; i++) {
            for (int j = 0; j < qtdC; j++) {
                System.out.print(matriz[i][j] + "\t");
            }
            System.out.println();
        }

    }

    /**
     * método de classe que converte uma matriz de inteiros em uma lista de dados
     * @param matriz - matriz de inteiros a ser convertida
     * @param qtdL - quantidade de linhas
     * @param qtdC - quantidade de colunas
     * @param lista - lista de dados a ser preenchida com os dados da matriz
     */
    public static void converterMatrizLista(int matriz[][], int qtdL, int qtdC, ArrayList<Dado> lista) {
        for (int i = 0; i < qtdL; i++) {
            for (int j = 0; j < qtdC; j++) {
                if (matriz[i][j] != 0) {
                    lista.add(new Dado(matriz[i][j], i, j));
                }
            }
        }
    }

    /**
     * método de classe que exibe uma lista de dados
     * @param lista - lista de dados a ser exibida
     */
    public static void exibirLista(ArrayList<Dado> lista) {
        for (Dado dado : lista) {
            System.out.println(dado);
        }
        System.out.println("------------------------------");
        System.out.println("Total de elementos não nulos: " + lista.size());
    }
}