from aluno import aluno
import csv

class sistema_academico:
    def __init__(self):
        self.__alunos = []  # lista de objetos aluno

    def carregar_arquivo(self, nome_arquivo):
        """_summary_: lê um csv, cria objetos aluno e adiciona os registros válidos à lista interna

        returns:
            _type_: ignora linhas vazias, cabeçalhos, linhas com menos de 4 campos e valores de ano inválidos, e exibe uma mensagem ao final do carregamento
        """
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
        """_summary_: ordena a lista de alunos por nome ou por ano de ingresso

        returns:
            _type_: se o critério informado não for "nome" nem "ano", a lista permanece inalterada
        """
        if criterio.lower() == "nome":
            self.__alunos.sort(key=lambda x: x.nome)
        elif criterio.lower() == "ano":
            self.__alunos.sort(key=lambda x: x.ano_ingresso)

    def buscar_aluno(self, nome_procurado):
        """_summary_: busca um aluno pelo nome exato

        returns:
            _type_: retorna a string formatada com os dados do aluno ou "Aluno não encontrado."
        """
        for aluno in self.__alunos:
            if aluno.nome == nome_procurado:
                return aluno.exibir_completo()
        return "Aluno não encontrado."

    def calcular_agregacao(self):
        """_summary_: conta quantos alunos existem por ano de ingresso

        returns:
            _type_: retorna um dicionário em que a chave é o ano de ingresso e o valor é a quantidade de alunos daquele ano
        """
        contagem = {}
        for aluno in self.__alunos:
            contagem[aluno.ano_ingresso] = contagem.get(aluno.ano_ingresso, 0) + 1
        return contagem

    def listar_todos(self):
        """_summary_: exibe os dados completos de todos os alunos cadastrados, um por linha
        """
        for aluno in self.__alunos:
            print(aluno.exibir_completo())
            
            