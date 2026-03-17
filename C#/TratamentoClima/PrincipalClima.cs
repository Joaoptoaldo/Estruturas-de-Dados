using System;
using System.Collections.Generic;
using System.IO;

namespace SistemaClima {
    class Principal {
        static List<Clima> dados = new List<Clima>();
        static string path = ResolverCaminhoCsv();

        static void Main() {
            CarregarDados();
            GerarRelatorio();
        }

        static void CarregarDados() {
            if (string.IsNullOrEmpty(path) || !File.Exists(path)) {
                Console.WriteLine("Erro: CSV não encontrado.");
                return;
            }

            var linhas = File.ReadAllLines(path);
            for (int i = 1; i < linhas.Length; i++) {
                var l = linhas[i];
                var col = l.Split(',');
                if (col.Length < 4) continue;

                int peso = 0;
                string p = col[3].ToLower().Trim();
                if (p == "muita") peso = 3;
                else if (p == "média") peso = 2;
                else if (p == "pouca") peso = 1;

                dados.Add(new Clima(col[0], col[1], col[2], peso));
            }
        }

        static void GerarRelatorio() {
            int chuvaV = 0, chuvaO = 0, chuvaI = 0;
            int quenteV = 0, quenteO = 0, quenteI = 0;
            int amenoV = 0, amenoO = 0, amenoI = 0;

            foreach (var item in dados) {
                bool eVerao = item.Mes == "Dezembro" || item.Mes == "Janeiro" || item.Mes == "Fevereiro" || item.Mes == "Março";
                bool eOutono = item.Mes == "Abril" || item.Mes == "Maio" || item.Mes == "Junho" || item.Mes == "Julho";

                if (eVerao) {
                    chuvaV += item.Precipitacao;
                    if (item.Temperatura.Equals("Quente", StringComparison.OrdinalIgnoreCase)) quenteV++;
                    if (item.Temperatura.Equals("Ameno", StringComparison.OrdinalIgnoreCase)) amenoV++;
                }
                else if (eOutono) {
                    chuvaO += item.Precipitacao;
                    if (item.Temperatura.Equals("Quente", StringComparison.OrdinalIgnoreCase)) quenteO++;
                    if (item.Temperatura.Equals("Ameno", StringComparison.OrdinalIgnoreCase)) amenoO++;
                }
                else {
                    chuvaI += item.Precipitacao;
                    if (item.Temperatura.Equals("Quente", StringComparison.OrdinalIgnoreCase)) quenteI++;
                    if (item.Temperatura.Equals("Ameno", StringComparison.OrdinalIgnoreCase)) amenoI++;
                }
            }

            string maisChuva = "Inverno";
            if (chuvaV >= chuvaO && chuvaV >= chuvaI) maisChuva = "Verão";
            else if (chuvaO >= chuvaV && chuvaO >= chuvaI) maisChuva = "Outono";

            string menosChuva = "Inverno";
            if (chuvaV <= chuvaO && chuvaV <= chuvaI) menosChuva = "Verão";
            else if (chuvaO <= chuvaV && chuvaO <= chuvaI) menosChuva = "Outono";

            string maisQuente = "Inverno";
            if (quenteV >= quenteO && quenteV >= quenteI) maisQuente = "Verão";
            else if (quenteO >= quenteV && quenteO >= quenteI) maisQuente = "Outono";

            string maisAmeno = "Inverno";
            if (amenoV >= amenoO && amenoV >= amenoI) maisAmeno = "Verão";
            else if (amenoO >= amenoV && amenoO >= amenoI) maisAmeno = "Outono";
        
            Console.WriteLine("\n--- RESULTADOS DO CLIMA ---");
            Console.WriteLine($"Estação mais chuvosa:  {maisChuva.ToUpper()}");
            Console.WriteLine($"Estação menos chuvosa: {menosChuva.ToUpper()}");
            Console.WriteLine($"Estação mais quente:   {maisQuente.ToUpper()}"); 
            Console.WriteLine($"Estação mais amena:    {maisAmeno.ToUpper()}");
            Console.WriteLine("---------------------------\n");
        }

        static string ResolverCaminhoCsv() {
            string[] caminhos = {
                "dadosClimaticos.csv",
                "..\\dadosClimaticos.csv",
                "..\\..\\dadosClimaticos.csv",
                "..\\..\\..\\dadosClimaticos.csv"
            };

            foreach (var caminho in caminhos) {
                string absoluto = Path.GetFullPath(caminho);
                if (File.Exists(absoluto)) {
                    return absoluto;
                }
            }

            return string.Empty;
        }
    }
}