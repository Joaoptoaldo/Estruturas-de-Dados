/**
 * EX ÁRVORE BINÁRIA DE BUSCA (BST - Binary Search Tree)
 * 
 * Conceitos:
 * - Estrutura hierárquica com nós
 * - Inserção mantendo ordem (esquerda < pai < direita)
 * - Busca eficiente
 * - Travessia em-ordem (in-order)
 */

public class ArvoreBinariaBusca {
    
    // Classe interna para representar cada nó da árvore
    static class No {
        int valor;
        No esquerda;
        No direita;
        
        No(int valor) {
            this.valor = valor;
            this.esquerda = null;
            this.direita = null;
        }
    }
    
    // Raiz da árvore
    private No raiz;
    
    /**
     * Construtor da árvore binária de busca
     */
    public ArvoreBinariaBusca() {
        this.raiz = null;
    }
    
    /**
     * insere um valor na árvore mantendo a ordem da BST
     * @param valor - valor a ser inserido
     */
    public void inserir(int valor) {
        raiz = inserirRecursivo(raiz, valor);
    }
    
    /**
     * método recursivo para inserir um valor na árvore
     * @param no - nó atual na recursão
     * @param valor - valor a ser inserido
     * @return - nó atualizado após inserção
     */
    private No inserirRecursivo(No no, int valor) {
        // caso base: se o nó é nulo, cria um novo nó
        if (no == null) {
            return new No(valor);
        }
        
        // se o valor é menor, vai para a esquerda
        if (valor < no.valor) {
            no.esquerda = inserirRecursivo(no.esquerda, valor);
        }
        // se o valor é maior, vai para a direita
        else if (valor > no.valor) {
            no.direita = inserirRecursivo(no.direita, valor);
        }
        // se for igual, não insere (sem duplicatas)
        
        return no;
    }
    
    /**
     * busca um valor na árvore
     * @param valor - valor a ser procurado
     * @return true se encontrado, false caso contrário
     */
    public boolean buscar(int valor) {
        return buscarRecursivo(raiz, valor);
    }
    
    private boolean buscarRecursivo(No no, int valor) {
        if (no == null) {
            return false;
        }
        
        if (valor == no.valor) {
            return true;
        } else if (valor < no.valor) {
            return buscarRecursivo(no.esquerda, valor);
        } else {
            return buscarRecursivo(no.direita, valor);
        }
    }
    
    /**
     * Travessia em-ordem (in-order): esquerda -> raiz -> direita
     * Resultado: números em ordem crescente
     */
    public void traversiaInOrdem() {
        System.out.print("Travessia In-Order: ");
        traversiaInOrdemRecursivo(raiz);
        System.out.println();
    }
    
    private void traversiaInOrdemRecursivo(No no) {
        if (no != null) {
            traversiaInOrdemRecursivo(no.esquerda);
            System.out.print(no.valor + " ");
            traversiaInOrdemRecursivo(no.direita);
        }
    }

    /**
     * travessia pré-ordem (pre-order): raiz -> esquerda -> direita
     */
    public void traversiaPreOrdem() {
        System.out.print("Travessia Pré-Ordem: ");
        traversiaPreOrdemRecursivo(raiz);
        System.out.println();
    }
    
    private void traversiaPreOrdemRecursivo(No no) {
        if (no != null) {
            System.out.print(no.valor + " ");
            traversiaPreOrdemRecursivo(no.esquerda);
            traversiaPreOrdemRecursivo(no.direita);
        }
    }
    
    /**
     * método para encontrar o valor mínimo da árvore (nó mais à esquerda)
     * @return - valor mínimo encontrado na árvore
     */
    public int encontrarMinimo() {
        No no = raiz;
        while (no.esquerda != null) {
            no = no.esquerda;
        }
        return no.valor;
    }
    
    /**
     * método para encontrar o valor máximo da árvore (nó mais à direita)
     * @return - valor máximo encontrado na árvore
     */
    public int encontrarMaximo() {
        No no = raiz;
        while (no.direita != null) {
            no = no.direita;
        }
        return no.valor;
    }
    
    public int calcularAltura() {
        return calcularAlturaRecursivo(raiz);
    }
    
    private int calcularAlturaRecursivo(No no) {
        if (no == null) {
            return -1;
        }
        return 1 + Math.max(calcularAlturaRecursivo(no.esquerda), 
                            calcularAlturaRecursivo(no.direita));
    }
    

    public static void main(String[] args) {
        System.out.println("=== EXEMPLO 1: ÁRVORE BINÁRIA DE BUSCA (BST) ===\n");
        
        ArvoreBinariaBusca arvore = new ArvoreBinariaBusca();
        
        // inserindo valores
        System.out.println("1. Inserindo valores: 50, 30, 70, 20, 40, 60, 80");
        int[] valores = {50, 30, 70, 20, 40, 60, 80};
        for (int valor : valores) {
            arvore.inserir(valor);
        }
        
        // Travessias
        System.out.println("\n2. TRAVESSIAS:");
        arvore.traversiaInOrdem();
        arvore.traversiaPreOrdem();
        
        // Buscas
        System.out.println("\n3. BUSCAS:");
        System.out.println("Buscar 40: " + arvore.buscar(40) + " (esperado: true)");
        System.out.println("Buscar 25: " + arvore.buscar(25) + " (esperado: false)");
        System.out.println("Buscar 80: " + arvore.buscar(80) + " (esperado: true)");
        
        // Min e Max
        System.out.println("\n4. VALORES EXTREMOS:");
        System.out.println("Valor mínimo: " + arvore.encontrarMinimo());
        System.out.println("Valor máximo: " + arvore.encontrarMaximo());
        
        // Altura
        System.out.println("\n5. PROPRIEDADES:");
        System.out.println("Altura da árvore: " + arvore.calcularAltura());
        System.out.println("\nEstrutura da árvore:");
        System.out.println("        50");
        System.out.println("       /  \\");
        System.out.println("      30   70");
        System.out.println("     / \\  / \\");
        System.out.println("    20 40 60 80");
    }
}
