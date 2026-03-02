
def popular_lista_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf8') as escritor:
        for i in lista:
            escritor.write(str(i) + '\n')

def ler_arquivo_lista(lista, nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as leitor:
        for linha in leitor:
            lista.append(linha.strip())