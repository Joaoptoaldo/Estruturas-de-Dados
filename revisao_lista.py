from minha_biblioteca import popular_aleatorio, popular_de_arquivos, exibir, copiar_lista_sem_replicados

lista_numerosA = []
lista_numerosB = []

popular_aleatorio(lista_numerosA, 10)
nome_arquivo = "numeros.txt"

popular_de_arquivos(lista_numerosB, nome_arquivo)

print("Lista A:", lista_numerosA)
print("Lista B:", lista_numerosB)

lista_resultado = []
copiar_lista_sem_replicados(lista_numerosB, lista_resultado)
exibir(lista_resultado)