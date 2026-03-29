# Estruturas de Dados: Listas, Árvores e Hash

Este material resume seis estruturas fundamentais para estudo e prática de Estruturas de Dados:

- **Listas**
- **Árvores (Tree)**
- **Hash** (`HashMap` e `HashSet`)
- **Pilha (Stack)**
- **Fila (Queue)**
- **Grafo (Graph)**

---

## 1) Listas

Lista é uma estrutura linear onde os elementos ficam em sequência.

### Tipos comuns

- **Lista estática (array):** tamanho fixo, acesso por índice muito rápido.
- **Lista dinâmica (ArrayList / List):** cresce e diminui conforme necessidade.
- **Lista encadeada (LinkedList):** elementos conectados por ponteiros/referências.

### Operações principais

- Inserir elemento
- Remover elemento
- Buscar elemento
- Percorrer elementos

### Complexidade (geral)

- Acesso por índice:
  - Array/ArrayList: **O(1)**
  - LinkedList: **O(n)**
- Inserção/remoção no fim:
  - ArrayList: **O(1)** amortizado
  - LinkedList: **O(1)** (com referência)
- Inserção/remoção no meio: **O(n)**
- Busca linear: **O(n)**

### Quando usar

- Quando a ordem dos elementos importa.
- Quando você precisa percorrer dados em sequência.
- Quando não precisa de busca extremamente rápida por chave.

---

## 2) Árvores (Tree)

Árvore é uma estrutura hierárquica composta por nós.

Conceitos básicos:

- **Raiz (root):** nó inicial.
- **Pai/Filho:** relação hierárquica entre nós.
- **Folha:** nó sem filhos.
- **Altura:** maior caminho da raiz até uma folha.

### Árvore Binária de Busca (BST)

Regra da BST:

- Valores menores ficam à esquerda.
- Valores maiores ficam à direita.

### Operações principais

- Inserir
- Buscar
- Remover
- Percursos: pré-ordem, em-ordem, pós-ordem

### Complexidade (BST)

- Média: **O(log n)** para inserir/buscar/remover
- Pior caso (árvore desbalanceada): **O(n)**

> Observação: árvores balanceadas (AVL, Red-Black) mantêm melhor desempenho no pior caso.

### Quando usar

- Quando há relações hierárquicas naturais.
- Quando você precisa de dados ordenados com inserção e busca frequentes.
- Quando deseja percursos ordenados dos elementos.

---

## 3) Hash (`HashMap` e `HashSet`)

Estruturas hash usam função de espalhamento para mapear chaves em posições da tabela.

### `HashMap`

Armazena pares **chave -> valor**.

Exemplos de uso:

- Contagem de frequência
- Índices por identificador
- Cache de dados

Operações típicas:

- Inserir (`put`) 
- Buscar (`get`)
- Remover (`remove`)

Complexidade média: **O(1)**

### `HashSet`

Armazena apenas valores **únicos** (sem repetição).

Exemplos de uso:

- Remover duplicados
- Verificar existência rapidamente
- Operações de conjunto (interseção, união)

Operações típicas:

- Inserir (`add`)
- Verificar existência (`contains`)
- Remover (`remove`)

Complexidade média: **O(1)**

### Colisões
 
Quando duas chaves caem na mesma posição, ocorre colisão.

Estratégias comuns:

- Encadeamento (listas por posição)
- Endereçamento aberto

---

## 4) Pilha (Stack): Last In, First Out (LIFO)

Pilha é uma estrutura onde o último elemento inserido é o primeiro a ser removido.

### Operações principais

- **Push:** Adicionar um elemento no topo da pilha.
- **Pop:** Remover o elemento do topo da pilha.
- **Peek/Top:** Visualizar o elemento no topo sem removê-lo.

### Complexidade

- Todas as operações (push, pop, peek): **O(1)**

### Quando usar

- Para rastrear chamadas de função (pilha de execução).
- Para resolver problemas de backtracking (ex: labirintos, quebra-cabeças).
- Para avaliar expressões (ex: notação pós-fixada).
- Para implementar undo/redo em aplicativos.
- Para verificar correspondência de parênteses em expressões.

---

## 5) Fila (Queue): First In, First Out (FIFO)

Fila é uma estrutura onde o primeiro elemento inserido é o primeiro a ser removido.

### Operações principais

- **Enqueue:** Adicionar um elemento no final da fila.
- **Dequeue:** Remover o elemento do início da fila.
- **Peek/Front:** Visualizar o elemento no início sem removê-lo.

### Complexidade
- Todas as operações (enqueue, dequeue, peek): **O(1)**

### Quando usar
- Para gerenciar tarefas em ordem de chegada (ex: impressão, atendimento).
- Para implementar buffers (ex: streaming de dados).
- Para realizar travessias em largura (BFS) em grafos.
- Para simular filas de espera (ex: filas de banco, filas de supermercado).

---

## 6) Grafo (Graph) 

Grafo é uma estrutura composta por vértices (nós) e arestas (conexões entre nós).

### Tipos de grafos

- **Grafo dirigido:** arestas têm direção (ex: Twitter).
- **Grafo não dirigido:** arestas sem direção (ex: Facebook).
- **Grafo ponderado:** arestas têm peso (ex: mapas de rotas).
- **Grafo não ponderado:** arestas sem peso (ex: redes sociais).

### Representação

- **Matriz de adjacência:** matriz 2D indicando conexões entre vértices.
- **Lista de adjacência:** lista de vértices com suas conexões.

### Operações principais

- Adicionar vértice
- Adicionar aresta
- Buscar vértice
- Percorrer vértices (DFS, BFS)
- Verificar conexões

### Complexidade

- Adicionar vértice: **O(1)**
- Adicionar aresta: **O(1)** (lista de adjacência), **
O(1)** (matriz de adjacência)
- Buscar vértice: **O(V)** (V = número de vértices)
- Percorrer vértices: **O(V + E)** (V = vértices, E = arestas)

### Quando usar

- Para modelar redes (ex: redes sociais, redes de transporte).
- Para resolver problemas de caminho mínimo (ex: Dijkstra, A*).
- Para detectar ciclos e componentes conectados.
- Para realizar travessias e buscas em estruturas complexas.

---

## Comparativo rápido

| Estrutura | Melhor para | Busca média | Mantém ordem? |
|---|---|---|---|
| Lista | Sequência e iteração | O(n) | Sim |
| Árvore (BST) | Dados ordenados e hierarquia | O(log n)* | Sim (em-ordem) |
| HashMap | Chave-valor rápido | O(1) | Não |
| HashSet | Unicidade e presença rápida | O(1) | Não |
| Pilha (Stack) | LIFO | O(1) | Sim (ordem de inserção) |
| Fila (Queue) | FIFO | O(1) | Sim (ordem de inserção) |
| Grafo | Relações complexas | O(V + E) | Não |


\* Em árvore balanceada.

---
