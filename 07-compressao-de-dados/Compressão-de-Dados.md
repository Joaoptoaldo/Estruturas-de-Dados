# Compressão de Dados

## Introdução

A compressão de dados é uma técnica utilizada para reduzir o tamanho de arquivos ou conjuntos de dados, facilitando o armazenamento e a transmissão. Existem diversos algoritmos de compressão, cada um com suas próprias características e aplicações. Neste guia, exploraremos alguns dos algoritmos mais comuns e como implementá-los em Java.

## Algoritmos de Compressão

### 1. RLE (Run-Length Encoding)

O RLE é um algoritmo simples que substitui sequências de caracteres repetidos por um único caractere seguido do número de repetições. Por exemplo, a string "AAAABBBCCDAA" seria comprimida para "4A3B2C1D2A".

```java
public class RLE {
    public static String compress(String input) {
        StringBuilder compressed = new StringBuilder();
        int count = 1;

        for (int i = 1; i < input.length(); i++) {
            if (input.charAt(i) == input.charAt(i - 1)) {
                count++;
            } else {
                compressed.append(count).append(input.charAt(i - 1));
                count = 1;
            }
        }
        compressed.append(count).append(input.charAt(input.length() - 1));
        return compressed.toString();
    }

    public static void main(String[] args) {
        String input = "AAAABBBCCDAA";
        String output = compress(input);
        System.out.println("Compressed: " + output);
    }
}
```

### 2. Huffman Coding

O Huffman Coding é um algoritmo de compressão que utiliza uma árvore binária para representar os caracteres de forma eficiente. Caracteres mais frequentes são representados por códigos mais curtos, enquanto caracteres menos frequentes são representados por códigos mais longos.

```java
import java.util.PriorityQueue;
import java.util.HashMap;

class Node implements Comparable<Node> {
    char character;
    int frequency;
    Node left, right;

    public Node(char character, int frequency) {
        this.character = character;
        this.frequency = frequency;
        this.left = null;
        this.right = null;
    }

    @Override
    public int compareTo(Node other) {
        return this.frequency - other.frequency;
    }
}

public class HuffmanCoding {
    public static void main(String[] args) {
        String input = "hello huffman";
        String compressed = compress(input);
        System.out.println("Compressed: " + compressed);
    }

    public static String compress(String input) {
        HashMap<Character, Integer> frequencyMap = new HashMap<>();
        for (char c : input.toCharArray()) {
            frequencyMap.put(c, frequencyMap.getOrDefault(c, 0) + 1);
        }

        PriorityQueue<Node> pq = new PriorityQueue<>();
        for (char c : frequencyMap.keySet()) {
            pq.add(new Node(c, frequencyMap.get(c)));
        }

        while (pq.size() > 1) {
            Node left = pq.poll();
            Node right = pq.poll();
            Node parent = new Node('\0', left.frequency + right.frequency);
            parent.left = left;
            parent.right = right;
            pq.add(parent);
        }

        Node root = pq.poll();
        HashMap<Character, String> huffmanCodes = new HashMap<>();
        generateCodes(root, "", huffmanCodes);

        StringBuilder compressed = new StringBuilder();
        for (char c : input.toCharArray()) {
            compressed.append(huffmanCodes.get(c));
        }
        return compressed.toString();
    }

    private static void generateCodes(Node node, String code, HashMap<Character, String> huffmanCodes) {
        if (node == null) return;
        if (node.character != '\0') {
            huffmanCodes.put(node.character, code);
        }
        generateCodes(node.left, code + "0", huffmanCodes);
        generateCodes(node.right, code + "1", huffmanCodes);
    }
}
```