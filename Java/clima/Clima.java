package clima;
//Usando sua linguagem de preferência, é preciso tratar os dados climáticos presentes em dadosClimaticos.csv.
//Para isso, crie e utilize a classe Clima...
//Sabendo que Verão são os meses Dezembro, Janeiro, Fevereiro, Março. Que Outono são os meses Abril, Maio, Junho, Julho. Que Inverno são os meses Agosto, Setembro, Outubro, Novembro.
//Preciso descobrir dentro da base dadosClimaticos.csv qual a estação que menos chove; qual a estação que mais chove; qual a estação mais quente; qual a estação mais amena
//Lembrar de documentar corretamente.


public class Clima {
    String ano; //2020, 2021, 2022, 2023, 2024
    String mes; //Janeiro, Fevereiro, Março, Abril, Maio, Junho, Julho, Agosto, Setembro, Outubro, Novembro, Dezembro
    String temperatura; //Frio (até 15°C), Quente (acima de 25°C), Ameno (16°C a 25°C)
    int precipitacao; //nada, pouca (até 20mm), média (21mm a 40mm), muita (mais de 40mm)
    
    public Clima(String ano, String mes, String temperatura, int precipitacao) {
        this.ano = ano;
        this.mes = mes;
        this.temperatura = temperatura;
        this.precipitacao = precipitacao;
    }

    @Override
    public String toString() {
        return "Clima [ano=" + ano + ", mes=" + mes + ", temperatura=" + temperatura + ", precipitacao=" + precipitacao + "]";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Clima other = (Clima) obj;
        if (ano == null) {
            if (other.ano != null)
                return false;
        } else if (!ano.equals(other.ano))
            return false;
        if (mes == null) {
            if (other.mes != null)
                return false;
        } else if (!mes.equals(other.mes))
            return false;
        return true;
    }    
}
