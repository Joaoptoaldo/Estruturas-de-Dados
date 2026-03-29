class Aluno:
    def __init__(self, nome):
        """_summary_
        método construtor da classe Aluno, recebe o nome do aluno e gera um email com base nesse nome

        Args:
            nome (_type_): nome do aluno para gerar o email

        Returns:
            _type_: email gerado para o aluno
        """
        self.nome = nome
        self.email = self.gerar_email(self.nome)

    def gerar_email(self, nome):
        """_summary_
        método que gera um email para o aluno com base no nome fornecido, utilizando um formato específico

        Args:
            nome (_type_): nome do aluno para gerar o email
        Returns:
            _type_: email gerado para o aluno
        """
        dados_nome = nome.split() # split é usado para dividir o nome em partes, criando uma lista de palavras
        email = dados_nome[0].lower() + "." + dados_nome[-1].lower() + "@ufn.edu.br" # o email é formado pelo primeiro nome, um ponto, o último nome e o domínio "@ufn.edu.br"
        return email

                