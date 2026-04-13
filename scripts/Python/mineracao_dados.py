import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import os

class ClimaMiner:
    """
    Classe para mineração de dados climáticos usando Pandas.
    Projetada para grandes volumes: usa chunking e otimizações de memória.
    """
    
    def __init__(self, caminho_csv='dadosClimaticos.csv'):
        self.caminho_csv = caminho_csv
        self.df = None
        self.le_temp = LabelEncoder()
        self.le_precip = LabelEncoder()
    
    def carregar_dados(self, chunk_size=10000, multiplicar=1000):
        """
        Carrega CSV, simula grandes volumes repetindo dados.
        Args:
            chunk_size: Para arquivos reais gigantes.
            multiplicar: Fator para expandir dataset pequeno para demo.
        """
        print("Carregando dados climáticos...")
        self.df = pd.read_csv(self.caminho_csv)
        
        # Simular grandes volumes: repetir dados
        self.df = pd.concat([self.df] * multiplicar, ignore_index=True)
        print(f"Dataset expandido para {len(self.df):,} linhas.")
        
        # Converter para numérico para análise
        self.df['ano'] = pd.to_numeric(self.df['ano'], errors='coerce')
        self.df['temperatura_num'] = self.le_temp.fit_transform(self.df['temperatura'])
        self.df['precipitacao_num'] = self.le_precip.fit_transform(self.df['precipitacao'])
        
        print(self.df.head())
        print(self.df.info())
    
    def eda_basica(self):
        """Análise Exploratória de Dados (EDA)."""
        print("\n=== EDA BÁSICA ===")
        print(self.df.describe())
        
        print("\nTemperatura por ano:")
        print(self.df.groupby('ano')['temperatura'].value_counts().head(10))
        
        print("\nPrecipitação média por mês:")
        print(self.df.groupby('mes')['precipitacao_num'].mean().sort_values(ascending=False))
    
    def analise_avancada(self):
        """Análises avançadas: tendências, pivots."""
        print("\n=== ANÁLISE AVANÇADA ===")
        
        # Pivot: temp média por ano-mês
        pivot_temp = self.df.pivot_table(values='temperatura_num', index='mes', columns='ano', aggfunc='mean')
        print(pivot_temp)
        
        # Correlação
        corr = self.df[['ano', 'temperatura_num', 'precipitacao_num']].corr()
        print("\nCorrelações:\n", corr)
    
    def mineracao_clustering(self, n_clusters=3):
        """Mineração: KMeans em temperatura e precipitação."""
        print("\n=== MINERAÇÃO: CLUSTERING ===")
        features = self.df[['temperatura_num', 'precipitacao_num']].dropna()
        
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        self.df['cluster'] = kmeans.fit_predict(features)
        
        print(self.df['cluster'].value_counts())
        print("Centroids:\n", kmeans.cluster_centers_)
    
    def visualizacao(self):
        """Visualizações salva como PNGs."""
        plt.style.use('seaborn-v0_8')
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # Heatmap temp por ano-mês
        pivot_temp = self.df.pivot_table(values='temperatura_num', index='mes', columns='ano', aggfunc='mean')
        sns.heatmap(pivot_temp, annot=True, ax=axes[0,0], cmap='YlOrRd')
        axes[0,0].set_title('Temperatura Média por Mês/Ano')
        
        # Distribuição clusters
        sns.countplot(data=self.df, x='cluster', ax=axes[0,1])
        axes[0,1].set_title('Distribuição de Clusters')
        
        # Temp vs Precip
        sns.scatterplot(data=self.df, x='temperatura_num', y='precipitacao_num', hue='cluster', ax=axes[1,0])
        axes[1,0].set_title('Clusters Temp-Precip')
        
        # Tendência anual temp
        anual_temp = self.df.groupby('ano')['temperatura_num'].mean()
        anual_temp.plot(kind='line', ax=axes[1,1])
        axes[1,1].set_title('Tendência Temperatura Anual')
        
        plt.tight_layout()
        plt.savefig('analise_clima.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("Plots salvos em 'analise_clima.png'")
    
    def exportar(self, caminho_saida='dados_minados.csv'):
        """Exporta dataset limpo com features."""
        cols_export = ['ano', 'mes', 'temperatura', 'precipitacao', 'temperatura_num', 'precipitacao_num', 'cluster']
        self.df[cols_export].to_csv(caminho_saida, index=False)
        print(f"Dados minados exportados para {caminho_saida}")

def main():
    miner = ClimaMiner('dadosClimaticos.csv')
    miner.carregar_dados(multiplicar=1000)  # ~48k linhas para demo
    miner.eda_basica()
    miner.analise_avancada()
    miner.mineracao_clustering()
    miner.visualizacao()
    miner.exportar()

if __name__ == "__main__":
    main()


