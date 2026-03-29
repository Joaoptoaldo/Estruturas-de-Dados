package clima;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class PrincipalClima {

    public static void main(String[] args) {
        String caminhoArquivo = Paths.get(System.getProperty("user.dir"), "data", "dadosClimaticos.csv")
                .toAbsolutePath()
                .normalize()
                .toString();

        if (!Files.exists(Paths.get(caminhoArquivo))) {
            System.out.println("Arquivo CSV não encontrado.");
            return;
        }

        List<Clima> registros = lerDadosClimaticos(caminhoArquivo);

        if (registros.isEmpty()) {
            System.out.println("Nenhum dado foi carregado.");
            return;
        }

        int chuvaVerao = 0;
        int chuvaOutono = 0;
        int chuvaInverno = 0;

        int quenteVerao = 0;
        int quenteOutono = 0;
        int quenteInverno = 0;

        int amenoVerao = 0;
        int amenoOutono = 0;
        int amenoInverno = 0;

        for (Clima registro : registros) {
            int estacao = obterEstacao(registro.mes);

            if (estacao == 1) {
                chuvaVerao += registro.precipitacao;
                if ("Quente".equalsIgnoreCase(registro.temperatura)) quenteVerao++;
                if ("Ameno".equalsIgnoreCase(registro.temperatura)) amenoVerao++;
            } else if (estacao == 2) {
                chuvaOutono += registro.precipitacao;
                if ("Quente".equalsIgnoreCase(registro.temperatura)) quenteOutono++;
                if ("Ameno".equalsIgnoreCase(registro.temperatura)) amenoOutono++;
            } else if (estacao == 3) {
                chuvaInverno += registro.precipitacao;
                if ("Quente".equalsIgnoreCase(registro.temperatura)) quenteInverno++;
                if ("Ameno".equalsIgnoreCase(registro.temperatura)) amenoInverno++;
            }
        }

        String estacaoMenosChuvosa = "Inverno";
        if (chuvaVerao <= chuvaOutono && chuvaVerao <= chuvaInverno) estacaoMenosChuvosa = "Verão";
        else if (chuvaOutono <= chuvaVerao && chuvaOutono <= chuvaInverno) estacaoMenosChuvosa = "Outono";

        String estacaoMaisChuvosa = "Inverno";
        if (chuvaVerao >= chuvaOutono && chuvaVerao >= chuvaInverno) estacaoMaisChuvosa = "Verão";
        else if (chuvaOutono >= chuvaVerao && chuvaOutono >= chuvaInverno) estacaoMaisChuvosa = "Outono";

        String estacaoMaisQuente = "Inverno";
        if (quenteVerao >= quenteOutono && quenteVerao >= quenteInverno) estacaoMaisQuente = "Verão";
        else if (quenteOutono >= quenteVerao && quenteOutono >= quenteInverno) estacaoMaisQuente = "Outono";

        String estacaoMaisAmena = "Inverno";
        if (amenoVerao >= amenoOutono && amenoVerao >= amenoInverno) estacaoMaisAmena = "Verão";
        else if (amenoOutono >= amenoVerao && amenoOutono >= amenoInverno) estacaoMaisAmena = "Outono";

        System.out.println("\n--- RESULTADOS DO CLIMA ---");
        System.out.println("Estação que menos chove: " + estacaoMenosChuvosa);
        System.out.println("Estação que mais chove: " + estacaoMaisChuvosa);
        System.out.println("Estação mais quente: " + estacaoMaisQuente);
        System.out.println("Estação mais amena: " + estacaoMaisAmena);
        System.out.println("---------------------------\n");
    }

    private static List<Clima> lerDadosClimaticos(String caminhoArquivo) {
        List<Clima> lista = new ArrayList<>();

        try (BufferedReader leitor = new BufferedReader(new FileReader(caminhoArquivo))) {
            String linha = leitor.readLine();

            while ((linha = leitor.readLine()) != null) {
                String[] partes = linha.split(",");
                if (partes.length != 4) {
                    continue;
                }

                String ano = partes[0].trim();
                String mes = partes[1].trim();
                String temperatura = partes[2].trim();
                int precipitacao = converterPrecipitacao(partes[3].trim());

                lista.add(new Clima(ano, mes, temperatura, precipitacao));
            }
        } catch (IOException e) {
            System.out.println("Erro ao ler arquivo: " + e.getMessage());
        }

        return lista;
    }

    private static int converterPrecipitacao(String precipitacaoTexto) {
        if ("nada".equalsIgnoreCase(precipitacaoTexto)) {
            return 0;
        }
        if ("pouca".equalsIgnoreCase(precipitacaoTexto)) {
            return 20;
        }
        if ("média".equalsIgnoreCase(precipitacaoTexto) || "media".equalsIgnoreCase(precipitacaoTexto)) {
            return 40;
        }
        if ("muita".equalsIgnoreCase(precipitacaoTexto)) {
            return 60;
        }
        return 0;
    }

    private static int obterEstacao(String mes) {
        if ("Dezembro".equalsIgnoreCase(mes)
                || "Janeiro".equalsIgnoreCase(mes)
                || "Fevereiro".equalsIgnoreCase(mes)
                || "Março".equalsIgnoreCase(mes)
                || "Marco".equalsIgnoreCase(mes)) {
            return 1;
        }

        if ("Abril".equalsIgnoreCase(mes)
                || "Maio".equalsIgnoreCase(mes)
                || "Junho".equalsIgnoreCase(mes)
                || "Julho".equalsIgnoreCase(mes)) {
            return 2;
        }

        if ("Agosto".equalsIgnoreCase(mes)
                || "Setembro".equalsIgnoreCase(mes)
                || "Outubro".equalsIgnoreCase(mes)
                || "Novembro".equalsIgnoreCase(mes)) {
            return 3;
        }

        return 0;
    }
}
