def popular_lista_arquivo(lista, nome_arquivo):
    """_summary_
    método que recebe uma lista e um nome de arquivo, e escreve os elementos da lista no arquivo, um por linha

    Args:
        lista (_type_): lista de objetos a serem escritos no arquivo
        nome_arquivo (_type_): nome do arquivo onde os dados serão escritos
    """
    with open(nome_arquivo, 'w', encoding='utf8') as escritor:
        for i in lista:
            escritor.write(str(i) + '\n')

def ler_arquivo_lista(lista, nome_arquivo):
    """_summary_
    método que recebe uma lista e um nome de arquivo, e lê os dados do arquivo, adicionando-os à lista

    Args:
        lista (_type_): lista onde os dados do arquivo serão adicionados
        nome_arquivo (_type_): nome do arquivo de onde os dados serão lidos
    """

    with open(nome_arquivo, 'r', encoding='utf8') as leitor:
        for linha in leitor:
            lista.append(linha.strip())