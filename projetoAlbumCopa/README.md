## Sistema desenvolvido para implementar conceitos de **Estruturas de Dados**, focado na gestão e cruzamento de dados (match) para troca de figurinhas da Copa do Mundo de 2026. O projeto aplica conceitos de persistência em arquivos, manipulação de coleções dinâmicas e lógica de conjuntos.

### Tecnologias e Conceitos Utilizados

*   **Linguagem:** Java 17+
*   **Paradigma:** Orientação a Objetos (Encapsulamento, Polimorfismo e Composição).
*   **Estruturas de Dados:** `ArrayList` (Lista Linear Dinâmica).
*   **Persistência:** Manipulação de arquivos CSV via `java.nio.file` (NIO.2) e `BufferedReader/PrintWriter`.
*   **Algoritmos:** Busca linear e interseção de listas para lógica de trocas.



O projeto utiliza uma estrutura simplificada com um único pacote `pkg`:

*   **`pkg`**: Pacote contendo todas as classes principais:
    *   `Figura.java` - POJO (Plain Old Java Object) que representa a entidade figurinha com atributos e comportamentos.
    *   `GerenciadorArquivo.java` - Responsável pela persistência em arquivos CSV (leitura e escrita).
    *   `Principal.java` - Classe com método `main()` que gerencia a interface de console e fluxo do programa.

**Estrutura de diretórios:**
```
projetoAlbumCopa/
├── Java/
│   └── pkg/
│       ├── Figura.java
│       ├── GerenciadorArquivo.java
│       └── Principal.java
├── Data/
│   ├── figuras_repetidas_pessoais.csv
│   └── figuras_desejadas_pessoais.csv
└── README.md
```

### Funcionalidades

1.  **Gestão Pessoal:** Cadastro e listagem de figurinhas repetidas e desejadas.
2.  **Persistência Automática:** Os dados são salvos em arquivos `.csv` na pasta `/Data` a cada alteração.
3.  **Lógica de Match (Interseção):**
    *   **Match de Entrada:** O sistema lê as repetidas de um terceiro e filtra apenas as que você deseja.
    *   **Match de Saída:** O sistema lê as desejadas de um terceiro e mostra quais das suas repetidas podem interessar a ele.


### Formato do CSV

Os arquivos são salvos utilizando o separador `;` (ponto e vírgula) seguindo o padrão:
`selecao;numero;descricao;quantidade;raridade`

---

### Decisões Técnicas (Notas de Estudo)

*   **Por que ArrayList?** Escolhida pela facilidade de iteração e busca sequencial, ideal para conjuntos de dados de tamanho moderado onde o acesso por índice não é a prioridade, mas sim a busca por atributos específicos.
*   **Equals & HashCode:** Sobrescritos na classe `Figura` para garantir que o método `lista.contains()` identifique figurinhas iguais baseando-se apenas na *Seleção* e no *Número*, ignorando a raridade ou descrição na hora do match.
*   **Robustez:** Implementado `try-with-resources` para garantir que os fluxos de arquivos sejam fechados corretamente, evitando vazamento de memória (*memory leaks*).

### Como Compilar e Executar

#### Compilação
```bash
cd projetoAlbumCopa/Java/pkg
javac *.java
```

#### Execução
```bash
cd projetoAlbumCopa/Java
java pkg.Principal
```

**Nota:** A execução deve ser realizada a partir do diretório `projetoAlbumCopa/Java/` para que o caminho relativo dos arquivos CSV (pasta `Data`) seja encontrado corretamente. O Java executará a classe `Principal` dentro do pacote `pkg`.

### Estrutura de Dados Utilizadas

- **ArrayList<Figura>:** Armazena a coleção de figurinhas
- **CSV:** Formato de persistência dos dados (separador `;`)
- **Equals/HashCode:** Implementado customizado para comparação de figurinhas por seleção e número