using System;
using System.Collections.Generic;

namespace Exemplo
{
	public class PrincipalAluno
	{
		public static void Main(string[] args)
		{
			var lista = new List<Aluno>();

			while (true)
			{
				Console.Write("Digite o nome do aluno (ou 'sair' para encerrar): ");
				var nome = Console.ReadLine();

				if (nome != null && nome.ToLower() == "sair")
				{
					break;
				}

				if (string.IsNullOrWhiteSpace(nome))
				{
					continue;
				}

				var aluno = new Aluno(nome);
				lista.Add(aluno);
				Console.WriteLine($"Email gerado: {aluno.Email}\n");
			}

			Console.WriteLine("\n--- ALUNOS CADASTRADOS ---");
			foreach (var aluno in lista)
			{
				Console.WriteLine($"Nome: {aluno.Nome} | Email: {aluno.Email}");
			}
		}
	}
}

