# Estruturas de Dados: Listas, Árvores e Hash

Este material resume três estruturas fundamentais para estudo e prática de Estruturas de Dados:

- **Listas**
- **Árvores (Tree)**
- **Hash** (`HashMap` e `HashSet`)

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

## Comparativo rápido

| Estrutura | Melhor para | Busca média | Mantém ordem? |
|---|---|---|---|
| Lista | Sequência e iteração | O(n) | Sim |
| Árvore (BST) | Dados ordenados e hierarquia | O(log n)* | Sim (em-ordem) |
| HashMap | Chave-valor rápido | O(1) | Não |
| HashSet | Unicidade e presença rápida | O(1) | Não |

\* Em árvore balanceada.

---

## Conclusão

- Use **listas** para dados sequenciais e manipulação simples.
- Use **árvores** para relações hierárquicas e cenários com ordenação estrutural.
- Use **hash** (`HashMap`/`HashSet`) quando a prioridade for acesso rápido por chave ou verificação de existência.

Escolher a estrutura correta impacta diretamente desempenho, memória e clareza do código.
