lista_glicemica = []
nome_arquivo = './glicemia.txt'

lista_dicionarios_glicemica = []

def calcular_media(lista):
    soma = 0
    for item in lista:
        soma += int(item["valor"])
    
    return int(soma/len(lista))

def esta_contido(dicionario, lista_dicionarios):
    for item in lista_dicionarios:
        if item["data"] == dicionario["data"] and item["hora"] == dicionario["hora"]:
            return True
        
    return False

with open(nome_arquivo, 'r', encoding='utf8') as leitor:
    for linha in leitor:
        valor, data, hora = linha.split(',')
        dados = {
            "valor": valor,
            "data": data,
            "hora": hora
        }
        if not esta_contido(dados, lista_dicionarios_glicemica):
            lista_dicionarios_glicemica.append(dados)
    

print('Quantidade de dados lidos: ', len(lista_dicionarios_glicemica))
print('Media glicemica', calcular_media(lista_dicionarios_glicemica))
