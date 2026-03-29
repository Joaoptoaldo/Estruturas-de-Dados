using System;
using System.Collections.Generic;
using System.IO;

namespace SistemaClima 
{
    class Principal 
    {
        static List<Clima> dados = new List<Clima>();
static string arquivo = Path.GetFullPath(@"..\..\Data\dadosClimaticos.csv");
        
        static List<Clima> lista_verao = new List<Clima>();
        static List<Clima> lista_outono = new List<Clima>();
        static List<Clima> lista_inverno = new List<Clima>();
        
        static string path = arquivo;

        static void Main() 
        {
            CarregarDados();
            ExibirLista();
            GerarRelatorio();
        }

        static void CarregarDados() 
        {
            if (string.IsNullOrEmpty(path) || !File.Exists(path)) 
            {
                Console.WriteLine("Erro: CSV não encontrado.");
                return;
            }

            var linhas = File.ReadAllLines(path);
            for (int i = 1; i < linhas.Length; i++) 
            {
                var l = linhas[i];
                var col = l.Split(',');
                if (col.Length < 4) continue;

                int peso = 0;
                string p = col[3].ToLower().Trim();
                if (p == "muita") peso = 3;
                else if (p == "média") peso = 2;
                else if (p == "pouca") peso = 1;

                Clima clima = new Clima(col[0], col[1], col[2], peso);
                dados.Add(clima);
                
                if (clima.Mes == "Dezembro" || clima.Mes == "Janeiro" || clima.Mes == "Fevereiro" || clima.Mes == "Março")
                    lista_verao.Add(clima);
                else if (clima.Mes == "Abril" || clima.Mes == "Maio" || clima.Mes == "Junho" || clima.Mes == "Julho")
                    lista_outono.Add(clima);
                else
                    lista_inverno.Add(clima);
            }
        }

        static void ExibirLista() {
            Console.WriteLine("\n--- DADOS CLIMÁTICOS ---");
            foreach (var item in dados) 
            {
                Console.WriteLine(item);
            }
            Console.WriteLine($"Total de registros: {dados.Count}\n");
        }

        static void GerarRelatorio() 
        {
            int chuvaV = 0, chuvaO = 0, chuvaI = 0;
            int quenteV = 0, quenteO = 0, quenteI = 0;
            int amenoV = 0, amenoO = 0, amenoI = 0;

            foreach (var item in lista_verao) 
            {
                chuvaV += item.Precipitacao;
                if (item.Temperatura.Equals("Quente", StringComparison.OrdinalIgnoreCase)) quenteV++;
                if (item.Temperatura.Equals("Ameno", StringComparison.OrdinalIgnoreCase)) amenoV++;
            }
            
            foreach (var item in lista_outono) 
            {
                chuvaO += item.Precipitacao;
                if (item.Temperatura.Equals("Quente", StringComparison.OrdinalIgnoreCase)) quenteO++;
                if (item.Temperatura.Equals("Ameno", StringComparison.OrdinalIgnoreCase)) amenoO++;
            }
            
            foreach (var item in lista_inverno) 
            {
                chuvaI += item.Precipitacao;
                if (item.Temperatura.Equals("Quente", StringComparison.OrdinalIgnoreCase)) quenteI++;
                if (item.Temperatura.Equals("Ameno", StringComparison.OrdinalIgnoreCase)) amenoI++;
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
        
            Console.WriteLine("--- RESULTADOS DO CLIMA ---");
            Console.WriteLine($"Estação mais chuvosa:  {maisChuva.ToUpper()}");
            Console.WriteLine($"Estação menos chuvosa: {menosChuva.ToUpper()}");
            Console.WriteLine($"Estação mais quente:   {maisQuente.ToUpper()}"); 
            Console.WriteLine($"Estação mais amena:    {maisAmeno.ToUpper()}");
            Console.WriteLine("---------------------------\n");
        }

    }
}