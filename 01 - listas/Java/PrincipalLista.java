import java.util.ArrayList;

public class PrincipalLista {
    public static void main(String[] args) {
        ArrayList<Aluno> alunos = new ArrayList<>();

        alunos.add(new Aluno("João Silva"));
        alunos.add(new Aluno("João Pedro"));
        alunos.add(new Aluno("João A"));
        alunos.add(new Aluno("João P"));

        for (Aluno aluno : alunos) {
            System.out.println(aluno);
        }
    }
}

