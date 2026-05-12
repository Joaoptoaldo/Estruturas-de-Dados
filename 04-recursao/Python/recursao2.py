# prós da recursão: 
  # código mais limpo, fácil de ler e entender, e pode ser mais eficiente em alguns casos
# contras da recursão: 
  # pode consumir mais memória e ser mais lenta do que a iteração, especialmente se a profundidade da recursão for muito grande (pode causar stack overflow)

def contagem_regressiva(n):# n é a variável de controle 
  if n > 0: # condição de parada
    print(n)
    contagem_regressiva(n - 1) # atualiza a variável de controle da recursão a cada chamada
    
contagem_regressiva(5)

def contagem_progressiva(n):
  if n > 0:
    contagem_progressiva(n - 1)
    print(n) # executando o desenpilhamento de processos
    
contagem_progressiva(5)

def soma_elementos(n):
  if n > 0: 
    soma = n + soma_elementos(n - 1) # a função chama a si mesma e acumula o resultado da soma
    return soma
  else:
    return 0 # condição de parada, quando n chega a 0, a função retorna 0 e começa a desenpilhar as chamadas anteriores, acumulando a soma total
  
  
  # def soma_elementos(n):
  #   if n > 0: 
  #     return n + soma_elementos(n - 1) 
  #   else:
  #     return 0 
  
  if __name__ == "__main__":
  
    lista = [10, 15, 20, 25, 30]
   
   
  #print (soma_lista(lista, len(lista))) 
  
def conta_pares(lista, n):
  if n == 0: # condição de parada, quando n chega a 0,
    return 0
  else:
    if lista[n-1] % 2 == 0: # verifica se o último elemento da lista é par
      return 1 + conta_pares(lista, n - 1) # se for par, soma 1 e chama a função novamente com n-1
    print(conta_pares(lista, len(lista)))