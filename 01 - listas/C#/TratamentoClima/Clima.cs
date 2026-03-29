using System;

namespace SistemaClima 
{
    public class Clima 
    {
        public string Ano { get; set; }
        public string Mes { get; set; }
        public string Temperatura { get; set; }
        public int Precipitacao { get; set; }

        public Clima(string ano, string mes, string temp, int chuva) 
        {
            Ano = ano;
            Mes = mes;
            Temperatura = temp;
            Precipitacao = chuva;
        }

        public override string ToString() 
        {
            string chuvaTexto = "nada";
            if (Precipitacao == 3) chuvaTexto = "muita";
            else if (Precipitacao == 2) chuvaTexto = "média";
            else if (Precipitacao == 1) chuvaTexto = "pouca";

            return $"[{Ano} | {Mes}] Temp: {Temperatura}, Chuva: {chuvaTexto}";
        }

        public override bool Equals(object? obj) 
        {
            return obj is Clima outro && Ano == outro.Ano && Mes == outro.Mes;
        }

        public override int GetHashCode() => HashCode.Combine(Ano, Mes);
    }
}