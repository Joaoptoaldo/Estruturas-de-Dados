package model;

import java.util.List;
import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        
        // 1 - inicia as listas carregando dos arquivos CSV
        List<Figura> listaRepetidas = GerenciadorArquivo.carregar("figuras_repetidas_pessoais.csv");
        List<Figura> listaDesejadas = GerenciadorArquivo.carregar("figuras_desejadas_pessoais.csv");

        String opcao = "";

    //     MENU:

    // 1 - Cadastrar figuras repetidas pessoais (persistidas em arquivo csv figuras_repetidas_pessoais.csv e adicionadas na ListaRepetidasPessoais)
    // 2 - Listar figuras repetidas pessoais (mostrar a lista respectiva)
    // 3 - Cadastrar figuras desejadas pessoais (persistidas em arquivo csv figuras_desejadas_pessoais.csv e adicionadas na ListaDesejadasPessoais)
    // 4 - Listar figuras desejadas pessoais (mostrar a lista respectiva)
    // 5 - Carregar figuras repetidas OUTRO (carregar o arquivo, listar as figuras e mostrar as figuras que dão match com ListaDesejadasPessoais)
    // 6 - Carregar figuras desejadas OUTRO (carregar o arquivo, listar as figuras e mostrar as figuras que dão match com ListaRepetidasPessoais)
    // 7 - Sair

        do {
            System.out.println("\n--- ÁLBUM COPA 2026 ---");
            System.out.println("1 - Cadastrar repetida");
            System.out.println("2 - Listar minhas repetidas");
            System.out.println("3 - Cadastrar desejada");
            System.out.println("4 - Listar minhas desejadas");
            System.out.println("5 - Match: O que o OUTRO tem que eu quero?");
            System.out.println("6 - Match: O que eu tenho que o OUTRO quer?");
            System.out.println("7 - Sair");
            System.out.print("Escolha: ");
            opcao = teclado.nextLine();

            switch (opcao) {
                case "1":
                    // chamar um método parecido com o seu 'geraFichaNormal'
                    cadastrarFigurinha(teclado, listaRepetidas, "figuras_repetidas_pessoais.csv");
                    break;
                case "2":
                    listarFiguras(listaRepetidas, "MINHAS REPETIDAS");
                    break;
                case "5":
                    verificarMatchEntrada(teclado, listaDesejadas);
                    break;
                case "7":
                    System.out.println("Fim do programa!");
                    break;
                default:
                    System.out.println("Opção inválida!");
            }
        } while (!opcao.equals("7"));
    }

    // MÉTODOS AUXILIARES 

    /**
     * método para cadastrar uma nova figurinha, adicionando na lista e salvando no arquivo CSV
     * @param teclado - Scanner para ler a entrada do usuário
     * @param lista - lista onde a nova figura será adicionada
     * @param arquivo - nome do arquivo CSV onde a figura será salva
     */
    public static void cadastrarFigurinha(Scanner teclado, List<Figura> lista, String arquivo) {
        System.out.print("Seleção: ");
        String selecao = teclado.nextLine();
        System.out.print("Número: ");
        int numero = Integer.parseInt(teclado.nextLine());
        System.out.print("Descrição: ");
        String desc = teclado.nextLine();
        System.out.print("Quantidade: ");
        int qtd = Integer.parseInt(teclado.nextLine());
        System.out.print("É rara? (true/false): ");
        boolean rara = Boolean.parseBoolean(teclado.nextLine());

        Figura nova = new Figura(selecao, numero, desc, qtd, rara);
        lista.add(nova);
        
        // salvando logo após cadastrar
        GerenciadorArquivo.salvar(arquivo, lista);
        System.out.println("Figurinha salva com sucesso!");
    }

    /**
     * método para listar as figuras de uma lista, mostrando um título antes da listagem
     * @param lista - lista de figuras a ser listada
     * @param titulo - título a ser mostrado antes da listagem
     */
    public static void listarFiguras(List<Figura> lista, String titulo) {
        System.out.println("\n--- " + titulo + " ---");
        if (lista.isEmpty()) {
            System.out.println("Lista vazia.");
        } else {
            // aqui entra o método toString() da classe Figura para mostrar as informações de cada figura
            for (Figura f : lista) {
                System.out.println(f);
            }
        }
    }
}