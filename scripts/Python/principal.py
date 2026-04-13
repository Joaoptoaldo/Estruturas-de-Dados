import os
from glicemia import Glicemia

lista_glicemica = []
nome_arquivo = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '01-listas', 'Data', 'glicemia.txt')
print(f'Tentando carregar: {nome_arquivo}')

# leitura e limpeza de dados
try:
    with open(nome_arquivo, 'r', encoding='utf8') as leitor:
        for linha in leitor:
            partes = linha.strip().split(',')
            if len(partes) == 3:
                valor, data, hora = partes
                objeto = Glicemia(valor, data, hora)
                if objeto not in lista_glicemica:
                    lista_glicemica.append(objeto)
except FileNotFoundError:
    print("Arquivo não encontrado!")
    exit(1)

# dicionário para agrupar os valores por turno
turnos_dados = {
    "Manhã": [],
    "Tarde": [],
    "Noite": []
}

# distribuindo os objetos nos turnos
for g in lista_glicemica:
    turno = g.definir_turno()
    turnos_dados[turno].append(g)

# cálculo das médias por turno
medias_por_turno = {}
print("Médias por Turno:")
for turno, objetos in turnos_dados.items():
    media = Glicemia.calcular_media(objetos)
    medias_por_turno[turno] = media
    print(f"{turno}: {media}")

# identificando o turno mais alto
turno_mais_alto = max(medias_por_turno, key=medias_por_turno.get)

print("\nResultados:")
print(f"O turno com a glicemia mais alta é: {turno_mais_alto}")
print(f"Valor médio: {medias_por_turno[turno_mais_alto]}")
