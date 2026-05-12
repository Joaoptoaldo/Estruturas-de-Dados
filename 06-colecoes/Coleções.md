# Coleções Lineares

Coleções lineares são estruturas de dados que armazenam elementos em uma sequência ordenada. Elas incluem:

- Listas (List)
- Filas (Queue)
- Pilhas (Stack)

Cada uma dessas estruturas tem suas próprias características e usos específicos:

- **Listas** permitem acesso direto a qualquer elemento, mas podem ser mais lentas para inserção e remoção.
- **Filas** seguem a ordem de chegada (FIFO - First In, First Out),
sendo ideais para situações onde a ordem de processamento é importante.
- **Pilha** segue a ordem inversa de chegada (LIFO - Last In, First Out),
sendo útil para situações onde o último elemento inserido deve ser o primeiro a ser processado.

Alocação de memória:

- Listas geralmente usam alocação dinâmica, permitindo crescimento conforme necessário.
- Filas e pilhas podem ser implementadas usando arrays ou listas encadeadas, dependendo dos requisitos de desempenho e memória.

Alocação dinâmica é uma técnica onde a memória é alocada durante a execução do programa, permitindo que as estruturas de dados cresçam ou encolham conforme necessário, sem a necessidade de definir um tamanho fixo antecipadamente. Isso é especialmente útil para coleções lineares, onde o número de elementos pode variar significativamente.
