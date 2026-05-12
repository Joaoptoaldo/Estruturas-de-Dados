public class Dado {
  public int valor;
  public int lin;
  public int col;

  public Dado(int valor, int lin, int col) {
    this.valor = valor;
    this.lin = lin;
    this.col = col;
  }

    @Override 
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Dado other = (Dado) obj;
        if (this.lin != other.lin) {
            return false;
        }
        return this.col == other.col;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Dado{");
        sb.append("valor=").append(valor);
        sb.append(", lin=").append(lin);
        sb.append(", col=").append(col);
        sb.append('}');
        return sb.toString();
    }
}
