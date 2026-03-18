class Glicemia:
    def __init__(self, valor, data, hora):
        """_summary_
        metodo construtor da classe glicemia, recebe os dados da glicemia e os atribui aos atributos da classe

        Args:
            valor (_type_): valor da glicemia registrada
            data (_type_): data do registro da glicemia 
            hora (_type_): hora do registro da glicemia
        """
        self.valor = int(valor) # convertendo para int para facilitar cálculos
        self.data = data
        self.hora = hora.strip() 

    def definir_turno(self):
        """_summary_
        método que define o turno com base na hora do registro

        Returns:
            _type_: string indicando o turno (manhã, tarde ou noite)
        """
        # extrai apenas a hora (ex: "12:30" vira 12)
        hora_int = int(self.hora.split(':')[0])
        
        if 5 <= hora_int < 12:
            return "Manhã"
        elif 12 <= hora_int < 18:
            return "Tarde"
        else: # das 18h às 4:59h
            return "Noite"

    def __eq__(self, outro):
        """_summary_
        método que compara dois objetos da classe glicemia, considerando-os iguais se tiverem a mesma data e hora

        Args:
            outro (_type_): objeto da classe glicemia a ser comparado com o objeto atual

        Returns:
            _type_: True se os objetos forem considerados iguais, False caso contrário
        """
        if not isinstance(outro, Glicemia):
            return False
        return self.data == outro.data and self.hora == outro.hora
    
    def __str__(self):
        """_summary_
        método que retorna uma string formatada com os dados da glicemia

        Returns:
            _type_: _description_
        """
        return f'Valor: {self.valor} | Data: {self.data} | Hora: {self.hora} | Turno: {self.definir_turno()}'

    @staticmethod
    def calcular_media(lista):
        if not lista: return 0
        soma = sum(item.valor for item in lista)
        return int(soma / len(lista))

    @staticmethod
    def calcular_mediana(lista):
        if not lista: return 0 # evita divisão por zero
        valores = sorted([int(item.valor) for item in lista])
        tamanho = len(valores)
        meio = tamanho // 2
        
        if tamanho % 2 != 0: # se for ímpar, retorna o valor do meio
            return valores[meio]
        else:
            return int((valores[meio] + valores[meio-1]) / 2) # se for par, retorna a média dos dois valores centrais