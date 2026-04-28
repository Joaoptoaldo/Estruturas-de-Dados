from aluno import aluno
import csv

class sistema_academico:
    def __init__(self):
        self.__alunos = []  # lista privada de objetos aluno

    def carregar_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
                leitor = csv.reader(arquivo)
                for linha in leitor:
                    # pula linhas vazias
                    if not linha or all(not campo.strip() for campo in linha):
                        continue

                    # exige pelo menos 4 campos (nome, curso, sexo, ano)
                    if len(linha) < 4:
                        continue

                    primeiro_quatro = ' '.join(linha[:4]).lower()
                    if any(pal in primeiro_quatro for pal in ('nome', 'curso', 'sexo', 'ano')):
                        continue

                    # valida ano como inteiro
                    # se inválido, pula a linha
                    try:
                        int(linha[3].strip())
                    except ValueError:
                        continue

                    # cria instância do aluno 
                    try:
                        novo_aluno = aluno(linha[0].strip(), linha[1].strip(), linha[2].strip(), linha[3].strip())
                        self.__alunos.append(novo_aluno)
                    except Exception:
                        # pula linhas malformadas sem interromper o processamento
                        continue

            print(f"Dados carregados com sucesso! ({len(self.__alunos)} alunos)")
        except FileNotFoundError:
            print("Arquivo não encontrado")

    def ordenar(self, criterio):
        """_summary_: método para ordenar a lista de alunos com base no critério fornecido (nome ou ano)

        Args:
            criterio (_type_): _description_: "nome" ou "ano"
        """
        if criterio.lower() == "nome":
            self.__alunos.sort(key=lambda x: x.nome)
        elif criterio.lower() == "ano":
            self.__alunos.sort(key=lambda x: x.ano_ingresso)

    def buscar_aluno(self, nome_procurado):
        """_summary_: método para buscar um aluno pelo nome exato

        Args:
            nome_procurado (_type_): _description_: nome do aluno a ser buscado

        Returns:
            _type_: _description_
        """
        for aluno in self.__alunos:
            if aluno.nome.lower() == nome_procurado.lower():
                return aluno.exibir_completo()
        return "Aluno não encontrado."

    def calcular_agregacao(self):
        """_summary_: método para calcular a quantidade de alunos ingressantes por ano, retornando um dicionário com o ano como chave e a quantidade como valor

        Returns:
            _type_: _description_
        """
        contagem = {}
        for aluno in self.__alunos:
            contagem[aluno.ano_ingresso] = contagem.get(aluno.ano_ingresso, 0) + 1
        return contagem

    def listar_todos(self):
        for aluno in self.__alunos:
            print(aluno.exibir_completo())
            
            