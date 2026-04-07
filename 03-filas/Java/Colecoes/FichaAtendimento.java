package Colecoes;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;


public class FichaAtendimento {
    /**
     * método de classe que gera ficha normal
     * @param filaNormal - classe Queue do tipo Integer que representa a fila normal
     * @param contadorNormal - variável do tipo int que representa o contador de fichas normais, inicia em 1 e vai até 500
     * @return
     */
    public static int geraFichaNormal(Queue<Integer> filaNormal, int contadorNormal) {
        /* */
        System.out.print("Imprimindo ficha normal....");
        System.out.println(contadorNormal);
        filaNormal.offer(contadorNormal);
        contadorNormal++;

        return contadorNormal;
    }

    /**
     * método de classe que gera ficha prioritária
     * @param filaPrioritaria - classe Queue do tipo Integer que representa a fila prioritária
     * @param contadorPrioritaria - variável do tipo int que representa o contador de fichas prioritárias, inicia em 501 e vai até 1000
     * @return
     */

    public static int geraFichaPrioritaria(Queue<Integer> filaPrioritaria, int contadorPrioritaria) {
        
        System.out.print("Imprimindo ficha prioritária....");
        System.out.println(contadorPrioritaria);
        filaPrioritaria.offer(contadorPrioritaria);
        contadorPrioritaria++;

        return contadorPrioritaria;
    }

    /**
     * método de classe que gera atendimento, a cada 3 fichas normais, chama uma ficha prioritária, testar se a fila que for chamar não está vazia, se estiver vazia chamar a outra fila
     * @param filaNormal - classe Queue do tipo Integer que representa a fila normal
     * @param filaPrioritaria - classe Queue do tipo Integer que representa a fila prioritária
     * @param contadorAtendimentos - variável do tipo int que representa o contador de atendimentos, inicia em 0 e vai incrementando a cada atendimento gerado
     * @return
     */

    public static int geraAtendimento(Queue<Integer> filaNormal, Queue<Integer> filaPrioritaria, int contadorAtendimentos) {
        if (filaNormal.isEmpty() && filaPrioritaria.isEmpty()) {
            System.out.println("Não há fichas para chamar");

            return contadorAtendimentos;
        }

        System.out.print("Chamando ficha... ");
        int ficha;

        if (contadorAtendimentos % 3 == 0 || filaNormal.isEmpty()) {
            //chamar prioritario
            if (!filaPrioritaria.isEmpty()) {
                ficha = filaPrioritaria.poll();
                System.out.println("PRIORITARIA: "+ ficha);
                contadorAtendimentos++;
                return contadorAtendimentos;
            }
        } 
        if (!filaNormal.isEmpty()) {
            ficha = filaNormal.poll();
            System.out.println("NORMAL: "+ ficha);
            contadorAtendimentos++;
        }

        return contadorAtendimentos;
    }

    /**
     * metodo de classe que mostra as fichas faltantes para chegar em 500 fichas normais e 1000 fichas prioritárias, ou seja, mostra quantas fichas normais e prioritárias faltam para chegar em 500 e 1000 respectivamente
     * @param filaNormal - classe Queue do tipo Integer que representa a fila normal
     * @param filaPrioritaria - classe Queue do tipo Integer que representa a fila prioritária
     */

    public static void mostrarFichasFaltantes(Queue<Integer> filaNormal, Queue<Integer> filaPrioritaria) {
        System.out.println("Mostrando fichas faltantes... ");
        if(!filaNormal.isEmpty()){
            System.out.println("Fichas normais faltantes: " + filaNormal.size() + " - " + filaNormal);
        }
        if(!filaPrioritaria.isEmpty()){
            System.out.println("Fichas prioritárias faltantes: " + filaPrioritaria.size() + " - " + filaPrioritaria);
        }
    }

    /**
     * método de classe que exibe o menu para o usuário escolher as opções, a cada opção escolhida, chama o método correspondente, o menu deve ser exibido até que o usuário escolha a opção de sair, ou seja, a opção 5
     * @param filaNormal - classe Queue do tipo Integer que representa a fila normal
     * @param filaPrioritaria - classe Queue do tipo Integer que representa a fila prioritária
     */

    public static void menu(Queue<Integer> filaNormal, Queue<Integer> filaPrioritaria) {
        Scanner teclado = new Scanner(System.in);

        int contadorNormal = 1;
        int contadorPrioritaria = 501;
        int contadorAtendimentos = 0;
        String opcao = "";

         //Menu:
        // 1 - Ficha normal -> sua ficha é 1 a 500 - imprimir/exibir na tela e inserir da filaNormal
        // 2 - Ficha prioritária -> sua ficha é 501 a 1000 - imprimir/exibir na tela e inserir da filaPrioritaria
        // 3 - Chamar ficha - a cada 3 fichas normais, chama uma prioriedade - testar se a que for chamar não está vazia, se estiver vazia chamar a outra fila
        // 4 - Mostrar fichas faltantes - mostrar quantas fichas faltam para chegar em cada fila, ou seja, quantas fichas normais e prioritárias faltam para chegar em 500 e 1000 respectivamente
        // 5 - Sair

        do {
            System.out.println("\n");
            System.out.println("--- MENU ---");
            System.out.println("1 - Ficha normal");
            System.out.println("2 - Ficha prioritária");
            System.out.println("3 - Chamar ficha");
            System.out.println("4 - Mostrar fichas faltantes");
            System.out.println("5 - Sair");
            System.out.print("Escolha uma opção: \n");
            opcao = teclado.nextLine();

            switch (opcao) {
                case "1":
                    contadorNormal = geraFichaNormal(filaNormal, contadorNormal);
                    break;
                case "2":
                    contadorPrioritaria = geraFichaPrioritaria(filaPrioritaria,  contadorPrioritaria);
                    break;
                case "3":
                    contadorAtendimentos = geraAtendimento(filaNormal, filaPrioritaria, contadorAtendimentos);
                    break;
                case "4":
                    FichaAtendimento.mostrarFichasFaltantes(filaNormal, filaPrioritaria);
                    // System.out.println("Mostrando fichas faltantes...");
                    // if(!filaNormal.isEmpty()){
                    //     System.out.println("Fichas normais faltantes: " + filaNormal.size() + "-'" + filaNormal);
                    // }
                    // if(!filaPrioritaria.isEmpty()){
                    //     System.out.println("Fichas prioritárias faltantes: " + filaPrioritaria.size() + "-'" + filaPrioritaria);
                    // }
                    // break;
                case "5":
                    System.out.println("Saindo...");
                    break;
                
                default:
                    System.out.println("Opção inválida!");
                    break;
            }

        } while (!opcao.equals("5"));

    }
                   
    public static void main(String[] args) {

        Queue<Integer> filaNormal = new LinkedList<>();
        Queue<Integer> filaPrioritaria = new LinkedList<>();
    
        FichaAtendimento.menu(filaNormal, filaPrioritaria);
    }
    
}