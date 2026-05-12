package model;

import java.io.BufferedReader;//para ler o arquivo
import java.io.FileReader;//para abrir o arquivo para leitura
import java.io.FileWriter;//para escrever no arquivo
import java.io.PrintWriter;//para escrever no arquivo
import java.io.IOException;//para lidar com erros de leitura/escrita
import java.nio.file.Files;//para verificar se o arquivo existe
import java.nio.file.Path;//para lidar com caminhos de arquivos
import java.nio.file.Paths;//para montar o caminho completo
import java.util.ArrayList;//para criar uma lista de figuras
import java.util.List;//para usar a interface List

public class GerenciadorArquivo {

    /**
     * método auxiliar privado para padronizar a busca pela pasta "Data"
     * @param nomeArquivo - nome do arquivo a ser buscado
     * @return - caminho completo do arquivo dentro da pasta "Data"
     */
    private static Path obterCaminho(String nomeArquivo) {
        return Paths.get(System.getProperty("user.dir"), "Data", nomeArquivo)
                .toAbsolutePath()
                .normalize();
    }

    /**
     * método para carregar as figuras de um arquivo CSV
     * @param nomeArquivo - nome do arquivo a ser lido
     * @return - lista de figuras carregadas do arquivo
     */
    public static List<Figura> carregar(String nomeArquivo) {
        List<Figura> lista = new ArrayList<>();
        Path caminho = obterCaminho(nomeArquivo);

        // se não existe, avisa e retorna lista vazia
        if (!Files.exists(caminho)) {
            System.out.println("Arquivo " + nomeArquivo + " não encontrado. Iniciando lista vazia.");
            return lista;
        }

        try (BufferedReader leitor = new BufferedReader(new FileReader(caminho.toFile()))) {
            String linha = leitor.readLine(); // pula o cabeçalho

            while ((linha = leitor.readLine()) != null) {
                String[] partes = linha.split(";"); 
                
                if (partes.length != 5) {
                    continue; 
                }

                // usando o .trim() para remover espaços em branco 
                String selecao = partes[0].trim();
                int numero = Integer.parseInt(partes[1].trim());
                String descricao = partes[2].trim();
                int quantidade = Integer.parseInt(partes[3].trim());
                boolean rara = Boolean.parseBoolean(partes[4].trim());

                lista.add(new Figura(selecao, numero, descricao, quantidade, rara));
            }
        } catch (IOException e) {
            System.out.println("Erro ao ler arquivo: " + e.getMessage());
        } catch (NumberFormatException e) {
            System.out.println("Erro na formatação dos números no arquivo: " + nomeArquivo);
        }

        return lista;
    }

    /**
     * método para salvar a lista de figuras em um arquivo CSV
     * @param nomeArquivo - nome do arquivo onde as figuras serão salvas
     * @param lista - lista de figuras a ser salva no arquivo
     */
    public static void salvar(String nomeArquivo, List<Figura> lista) {
        Path caminho = obterCaminho(nomeArquivo);

        try {
            Files.createDirectories(caminho.getParent());
        } catch (IOException e) {
            System.out.println("Não foi possível criar o diretório 'data'.");
        }

        try (PrintWriter writer = new PrintWriter(new FileWriter(caminho.toFile()))) {
            writer.println("selecao;numero;descricao;quantidade;raridade");
            
            for (Figura figura : lista) {
                writer.println(figura.toCSV()); // chama o método da classe Figura
            }
        } catch (IOException e) {
            System.out.println("Erro ao salvar arquivo: " + e.getMessage());
        }
    }

}


