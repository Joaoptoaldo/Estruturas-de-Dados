package stack002;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Stack;

public class Pilha {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Stack<Integer> pilha = new Stack<>();
        int opcao;

        System.out.println("Exemplo simples de Pilha com inteiros (glicemia)");
        System.out.println("1. Empilhar (push)");
        System.out.println("2. Desempilhar (pop)");
        System.out.println("3. Ver topo (peek)");
        System.out.println("4. Ver tamanho");
        System.out.println("5. Ver se está vazia");
        System.out.println("6. Carregar glicemia.txt");
        System.out.println("0. Sair");

        do {
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    System.out.print("Digite o número para empilhar: ");
                    pilha.push(scanner.nextInt());
                    System.out.println("Número empilhado. Pilha: " + pilha);
                    break;
                case 2:
                    if (!pilha.isEmpty()) {
                        int removido = pilha.pop();
                        System.out.println("Número desempilhado: " + removido + ". Pilha: " + pilha);
                    } else {
                        System.out.println("Pilha vazia!");
                    }
                    break;
                case 3:
                    if (!pilha.isEmpty()) {
                        System.out.println("Topo: " + pilha.peek());
                    } else {
                        System.out.println("Pilha vazia!");
                    }
                    break;
                case 4:
                    System.out.println("Tamanho da pilha: " + pilha.size());
                    break;
                case 5:
                    System.out.println("Pilha " + (pilha.isEmpty() ? "vazia" : "não vazia"));
                    break;
                case 6:
                    carregarGlicemia(pilha);
                    break;
                case 0:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção inválida!");
            }
        } while (opcao != 0);

        scanner.close();
    }

    private static void carregarGlicemia(Stack<Integer> pilha) {
        try {
            File arquivo = new File("../../01-listas/Data/glicemia.txt");
            Scanner fileScanner = new Scanner(arquivo);
            int count = 0;

            while (fileScanner.hasNextLine()) {
                String linha = fileScanner.nextLine();
                String[] partes = linha.split(",");
                if (partes.length > 0) {
                    try {
                        int glicose = Integer.parseInt(partes[0].trim());
                        pilha.push(glicose);
                        count++;
                    } catch (NumberFormatException e) {
                        System.out.println("Linha inválida: " + linha);
                    }
                }
            }
            fileScanner.close();
            System.out.println("Carregados " + count + " valores de glicemia na pilha. Topo: " + (pilha.isEmpty() ? "vazia" : pilha.peek()));
        } catch (FileNotFoundException e) {
            System.out.println("Arquivo glicemia.txt não encontrado em ../../01-listas/Data/");
        }
    }
}
