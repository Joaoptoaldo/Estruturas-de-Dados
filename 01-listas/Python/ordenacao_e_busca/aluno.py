class aluno:
    def __init__(self, nome, curso, sexo, ano_ingresso):# construtor da classe 
        self.nome = nome
        self.curso = curso
        self.sexo = sexo
        self.ano_ingresso = int(ano_ingresso)


    def exibir_completo(self):
        """_summary_: retorna uma string com o nome, curso, sexo e ano de ingresso do aluno

        Returns:
            _type_: _description_
        """
        return f"{self.nome} - {self.curso} - {self.sexo} - {self.ano_ingresso}"