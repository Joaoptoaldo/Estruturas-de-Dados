import os
from sistema_academico import sistema_academico
from aluno import aluno

if __name__ == "__main__":
    sistema = sistema_academico()
    
    # mostra o caminho absoluto do arquivo CSV 
    caminho_csv = os.path.abspath('alunos.csv')
    print(f"Caminho do arquivo alunos.csv: {caminho_csv}")

    # le o arquivo e instancia os objetos aluno
    sistema.carregar_arquivo('alunos.csv')

    # ordena por ano e exibe
    print("\n--- Alunos Ordenados por Ano de Ingresso ---")
    sistema.ordenar("ano")
    sistema.listar_todos()

    # busca aluno pelo nome exato e exibe resultado
    nome_busca = input("\nDigite o nome do aluno para busca: ")
    resultado_busca = sistema.buscar_aluno(nome_busca)
    print(resultado_busca)

    # agregação (relatório estatístico)
    print("\n--- Estatísticas: Ingressantes por Ano ---")
    estatisticas = sistema.calcular_agregacao()
    
    for ano, qtd in sorted(estatisticas.items()):
        print(f"Ano {ano}: {qtd} alunos")