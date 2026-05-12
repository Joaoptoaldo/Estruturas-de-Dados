class Dado:

    def __init__(self, valor: int, lin: int, col: int):
        """_summary_: construtor da classe Dado

        Args:
            valor (int): _description_: valor inteiro armazenado na célula da matriz
            lin (int): _description_: índice da linha onde o valor se encontra na matriz
            col (int): _description_: índice da coluna onde o valor se encontra na matriz
        """
        self.valor = valor
        self.lin = lin
        self.col = col

    def __eq__(self, other):
        """_summary_: compara dois objetos Dado pela linha e coluna, ignorando o valor

        Args:
            other (_type_): _description_: objeto a ser comparado

        Returns:
            _type_: _description_: True se lin e col forem iguais, False caso contrário
        """
        if self is other:
            return True
        if other is None or not isinstance(other, Dado):
            return False
        return self.lin == other.lin and self.col == other.col

    def __repr__(self):
        """_summary_: retorna uma representação textual do objeto Dado

        Returns:
            _type_: _description_: string no formato Dado{valor=X, lin=Y, col=Z}
        """
        return f"Dado{{valor={self.valor}, lin={self.lin}, col={self.col}}}"