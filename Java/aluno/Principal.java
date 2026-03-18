package aluno;
import java.util.ArrayList;
import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        ArrayList<Aluno> alunos = new ArrayList<>();
        
        Scanner leitor = new Scanner(System.in);
        for (int i = 0; i < 3; i++) {
            System.out.print("Digite o nome do aluno: ");
            String nome = leitor.nextLine().toUpperCase();
            Aluno aluno = new Aluno(nome);
            if (!alunos.contains(aluno)) {
                alunos.add(aluno);
            }
        }
        
        for (Aluno aluno : alunos) {
            System.out.println(aluno);
        }
    }
}