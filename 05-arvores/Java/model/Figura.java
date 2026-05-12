package model;

public class Figura {
    private String nomeSelecao;
    private int numeroFigura;
    private String descricao;
    private int quantidade;
    private boolean raridade;


    /**
     * constructor
     * @param nomeSelecao - nome da seleção
     * @param numeroFigura - número da figura
     * @param descricao - descrição da figura
     * @param quantidade -  quantidade de figuras
     * @param raridade - indica se a figura é rara
     */
    public Figura(String nomeSelecao, int numeroFigura, String descricao, int quantidade, boolean raridade) {
        this.nomeSelecao = nomeSelecao;
        this.numeroFigura = numeroFigura;
        this.descricao = descricao;
        this.quantidade = quantidade;
        this.raridade = raridade;
    }


    public String getNomeSelecao() {
        return nomeSelecao;
    }



    public void setNomeSelecao(String nomeSelecao) {
        this.nomeSelecao = nomeSelecao;
    }



    public int getNumeroFigura() {
        return numeroFigura;
    }



    public void setNumeroFigura(int numeroFigura) {
        this.numeroFigura = numeroFigura;
    }



    public String getDescricao() {
        return descricao;
    }



    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }


    public int getQuantidade() {
        return quantidade;
    }


    public void setQuantidade(int quantidade) {
        if(quantidade < 0) {
            throw new IllegalArgumentException("A quantidade não pode ser negativa");
        }

        this.quantidade = quantidade;
    }


    public boolean isRaridade() {
        return raridade;
    }


    public void setRaridade(boolean raridade) {
        this.raridade = raridade;
    }

    /**
     * retorna uma representação em string da figura
     * @return - string representando a figura
     */
    @Override
    public String toString() {
        return "Figura{" + "nomeSelecao='" + nomeSelecao + '\'' + ", numeroFigura=" + numeroFigura +", descricao='" + descricao + '\'' +", quantidade=" + quantidade +", raridade=" + raridade +'}';
    }


    /**
     * verifica se duas figuras são iguais
     * @param obj - objeto a ser comparado
     * @return - true se as figuras forem iguais, false caso contrário
     */
    @Override
    public boolean equals(Object obj){
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;

        Figura figura = (Figura) obj;

        if (numeroFigura != figura.numeroFigura) return false;
        return nomeSelecao.equals(figura.nomeSelecao);
    }

    /**
     * retorna o código hash da figura
     * @return - código hash da figura
     */
    @Override
    public int hashCode() {
        return java.util.Objects.hash(nomeSelecao, numeroFigura);
    }

    /**
     * método que retorna uma representação em CSV da figura
     * @return - string representando a figura em formato CSV
     */
    public String toCSV() {
        return nomeSelecao + ";" + numeroFigura + ";" + descricao + ";" + quantidade + ";" + raridade;
    }

}
