class Clima:
    def __init__(self, ano, mes, temperatura, precipitacao):
        """_sumary_
        metodo construtor da classe clima, recebe os dados do clima e os atribui aos atributos da classe

        Args:
            ano (_type_): ano do registro climático
            mes (_type_): mes do registro climático
            temperatura (_type_): temperatura do registro climático (quente, ameno, frio)
            precipitacao (_type_): precipitação do registro climático (muita, média, pouca)
        """
        self.ano = ano
        self.mes = mes 
        self.temperatura = temperatura
        self.precipitacao = precipitacao

    def __str__(self):
        """_summary_
            método que retorna uma string formatada com os dados do clima
        Returns:
            _type_: string formatada com os dados do clima
        """
        chuva = "nada"
        if self.precipitacao == 3:#self serve para acessar os atributos do objeto atual
            chuva = "muita"
        elif self.precipitacao == 2:
            chuva = "média"
        elif self.precipitacao == 1:
            chuva = "pouca"
        return f"[{self.ano} | {self.mes}] Temp: {self.temperatura}, Chuva: {chuva}"

    def __eq__(self, outro):
        """_summary_
        método que compara dois objetos da classe clima, considerando-os iguais se tiverem o mesmo ano e mês

        Args:
            outro (_type_): objeto da classe clima a ser comparado com o objeto atual
        Returns:
            _type_: True se os objetos forem considerados iguais, False caso contrário
        """
        if not isinstance(outro, Clima):# verifica se o outro objeto é uma instância da classe clima, caso contrário, retorna False
            return False
        return self.ano == outro.ano and self.mes == outro.mes