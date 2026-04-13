import os
lista_glicemica = []
nome_arquivo = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '01-listas', 'Data', 'glicemia.txt')
print(f'Tentando carregar: {nome_arquivo}')

lista_dicionarios_glicemica = []

def calcular_media(lista):
    soma = 0
    for item in lista:
        soma += int(item["valor"])
    return int(soma/len(lista))

def calcular_mediana(lista):
    if not lista: return 0
    
    valores = sorted([int(item["valor"]) for item in lista])
    
    n = len(valores)
    meio = n // 2
    
    if n % 2 != 0:
        return valores[meio]
    else:
        return (valores[meio - 1] + valores[meio]) / 2
    

def esta_contido(dicionario, lista_dicionarios):
    for item in lista_dicionarios:
        if item["data"] == dicionario["data"] and item["hora"] == dicionario["hora"]:
            return True
    
    return False

try:
    with open(nome_arquivo, 'r', encoding='utf8') as leitor:
        for linha in leitor:
            valor, data, hora = linha.split(',')
            dados = {
                "valor": valor.strip(),
                "data": data.strip(),
                "hora": hora.strip()
            }
            if not esta_contido(dados, lista_dicionarios_glicemica):
                lista_dicionarios_glicemica.append(dados)
except FileNotFoundError:
    print(f"Arquivo não encontrado: {nome_arquivo}")
    exit(1)
except Exception as e:
    print(f"Erro ao ler arquivo: {e}")
    exit(1)

print('Quantidade de dados lidos: ', len(lista_dicionarios_glicemica))
print('Media glicemica', calcular_media(lista_dicionarios_glicemica))
print('Mediana glicemica:', calcular_mediana(lista_dicionarios_glicemica))
