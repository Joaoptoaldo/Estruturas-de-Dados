namespace Exemplo
{
    public class Aluno
    {
        public string Nome { get; set; }
        public string Email { get; set; }

        public Aluno(string nome)
        {
            Nome = nome;
            Email = GerarEmail(nome);
        }

        private string GerarEmail(string nome)
        {
            var dadosNome = nome.Split(' ', StringSplitOptions.RemoveEmptyEntries);
            var email = dadosNome[0].ToLower() + "." + dadosNome[^1].ToLower() + "@ufn.edu.br";
            return email;
        }
    }
}