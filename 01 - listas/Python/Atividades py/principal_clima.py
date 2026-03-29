import os # importa o módulo os para manipulação de arquivos e diretórios
from clima import Clima 

class Principal:
    def __init__(self):
        self.dados = [] 
        pasta_script = os.path.dirname(os.path.abspath(__file__)) 
        pasta_projeto = os.path.abspath(os.path.join(pasta_script, "..", ".."))
        self.arquivo = os.path.join(pasta_projeto, "data", "dadosClimaticos.csv")
        
        # listas para armazenar os objetos da classe Clima separados por estação do ano
        self.lista_verao = []
        self.lista_outono = []
        self.lista_inverno = []
        
    def carregar_dados(self):
        """_summary_
        metodo que carrega os dados do arquivo CSV, criando objetos da classe Clima e distribuindo-os em listas por estação do ano
        """
        path = self.arquivo
        
        if not path or not os.path.exists(path):
            print("Erro: CSV não encontrado.")
            return
        
        with open(path, "r", encoding="utf-8") as arq:
            linhas = arq.read().splitlines()
        
        for linha in linhas[1:]:
            li = linha.split(",")
            if len(li) < 4:
                continue
            
            ano = li[0].strip() 
            mes = li[1].strip()
            temp = li[2].strip()
            chuva_txt = li[3].strip().lower() 
            
            peso = 0
            if chuva_txt == "muita":
                peso = 3
            elif chuva_txt == "média":
                peso = 2
            elif chuva_txt == "pouca":
                peso = 1
            
            clima = Clima(ano, mes, temp, peso)
            self.dados.append(clima)
            
            if mes in ["Dezembro", "Janeiro", "Fevereiro", "Março"]:
                self.lista_verao.append(clima)
            elif mes in ["Abril", "Maio", "Junho", "Julho"]:
                self.lista_outono.append(clima)
            else:
                self.lista_inverno.append(clima)
    
    def exibir_lista(self):
        print("\n--- DADOS CLIMÁTICOS ---")
        for item in self.dados:# itera sobre a lista de dados climáticos e exibe cada registro formatado usando o método __str__ da classe Clima
            print(item)
        print(f"Total de registros: {len(self.dados)}\n")

    
    def analisar(self):
        """_summary_
        método que analisa os dados climáticos, calculando a estação mais chuvosa, a estação menos chuvosa, a estação mais quente e a estação mais amena, e exibe os resultados formatados
        """
        chuva_verao = sum(item.precipitacao for item in self.lista_verao) 
        chuva_outono = sum(item.precipitacao for item in self.lista_outono)
        chuva_inverno = sum(item.precipitacao for item in self.lista_inverno)
        
        quente_verao = sum(1 for item in self.lista_verao if item.temperatura.lower() == "quente")
        quente_outono = sum(1 for item in self.lista_outono if item.temperatura.lower() == "quente")
        quente_inverno = sum(1 for item in self.lista_inverno if item.temperatura.lower() == "quente")
        
        ameno_verao = sum(1 for item in self.lista_verao if item.temperatura.lower() == "ameno")
        ameno_outono = sum(1 for item in self.lista_outono if item.temperatura.lower() == "ameno")
        ameno_inverno = sum(1 for item in self.lista_inverno if item.temperatura.lower() == "ameno")
        
        chuva = {"Verão": chuva_verao, "Outono": chuva_outono, "Inverno": chuva_inverno}
        quente = {"Verão": quente_verao, "Outono": quente_outono, "Inverno": quente_inverno}
        ameno = {"Verão": ameno_verao, "Outono": ameno_outono, "Inverno": ameno_inverno}
        
        mais_chuva = max(chuva, key=chuva.get)
        menos_chuva = min(chuva, key=chuva.get)
        mais_quente = max(quente, key=quente.get)
        mais_ameno = max(ameno, key=ameno.get)
        
        print("\n--- RESULTADOS DO CLIMA ---")
        print(f"Estação mais chuvosa:  {mais_chuva.upper()}")
        print(f"Estação menos chuvosa: {menos_chuva.upper()}")
        print(f"Estação mais quente:   {mais_quente.upper()}")
        print(f"Estação mais amena:    {mais_ameno.upper()}")
        print("---------------------------\n")
    
    def executar(self):
        self.carregar_dados()
        if self.dados:
            self.exibir_lista()
            self.analisar()


if __name__ == "__main__":
    sistema = Principal()
    sistema.executar()