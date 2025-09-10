# Índice Hash Estático - Sistema de Banco de Dados

Um projeto acadêmico que implementa um sistema de indexação hash estático para demonstrar conceitos fundamentais de banco de dados, incluindo funções hash, estruturas de bucket e técnicas de busca eficiente.

## 📋 Descrição

Este sistema permite:
- **Indexação de palavras** usando diferentes funções hash
- **Busca eficiente** através de índices hash 
- **Comparação de performance** entre busca indexada e varredura de tabela
- **Análise de colisões** e overflow de buckets
- **Interface web interativa** para visualização e teste

## 🚀 Funcionalidades

### Funções Hash Implementadas
- **FNV-1a**: Hash com boa resistência a colisões
- **Polynomial Rolling Hash**: Hash polinomial com multiplicador primo
- **DJB2**: Algoritmo de hash com boa distribuição

### Características do Sistema
- Estrutura de páginas configurável
- Tamanho de bucket ajustável
- Tratamento de colisões com overflow buckets
- Métricas detalhadas de performance
- Comparação entre busca indexada vs. varredura de tabela

## 🛠️ Instalação

### Pré-requisitos
- Python 3.7+
- pip

### Dependências

```bash
pip install -r requirements.txt
```

As dependências incluem:
- `streamlit`: Interface web
- `pandas`: Manipulação de dados
- `loguru`: Sistema de logging

## 📁 Estrutura do Projeto

```
python-database-hash/
├── database/
│   ├── hash_function.py    # Implementações das funções hash
│   ├── buckets.py          # Classe Bucket e gerenciamento de overflow
│   ├── pages.py            # Sistema de paginação
│   ├── metrics.py          # Cálculo de métricas e estatísticas
│   └── read_file.py        # Utilitário para leitura de arquivos
├── main.py                 # Interface principal Streamlit
├── words.txt               # Dataset de palavras (exemplo)
├── full_words.txt          # Dataset completo de palavras
└── requirements.txt        # Dependências do projeto
```

## 🖥️ Como Usar

### 1. Executar a Aplicação

```bash
streamlit run main.py
```

### 2. Configurar Parâmetros

Na barra lateral, configure:
- **Base de Dados**: Arquivo de palavras (words.txt)
- **Função Hash**: Escolha entre FNV-1a, Polynomial Rolling Hash ou DJB2  
- **Linhas por Página**: Número de palavras por página
- **Tamanho do Bucket**: Capacidade máxima de cada bucket

### 3. Construir o Índice

Clique em "Construir Índice" para:
- Carregar as palavras do arquivo
- Criar páginas com base no tamanho configurado
- Gerar buckets usando a função hash selecionada
- Calcular métricas de performance

### 4. Realizar Buscas

Após construir o índice:
- **Busca com Índice**: Busca eficiente usando o índice hash
- **Varredura de Tabela**: Busca sequencial para comparação

## 📊 Métricas Exibidas

O sistema apresenta métricas detalhadas:

- **Total de Páginas**: Número de páginas criadas
- **Total de Palavras**: Quantidade de palavras indexadas
- **Total de Buckets**: Número de buckets criados
- **Total de Colisões**: Número de colisões ocorridas
- **Percentual de Colisões**: Taxa de colisões em relação ao total
- **Percentual de Overflows**: Taxa de buckets que sofreram overflow

## 🔍 Algoritmos Implementados

### Funções Hash

#### FNV-1a
```python
def hash_fnv1a(word, max_number):
    FNV_OFFSET_BASIS = 2166136261
    FNV_PRIME = 16777619
    hash_value = FNV_OFFSET_BASIS
    
    for char in word:
        hash_value ^= ord(char)
        hash_value *= FNV_PRIME
        hash_value &= 0xFFFFFFFF
    
    return hash_value % max_number
```

#### Polynomial Rolling Hash
```python
def hash_word(word, max_number):
    hash_value = 0
    prime = 31
    
    for i, char in enumerate(word):
        hash_value += ord(char) * (prime**i)
    
    return hash_value % max_number
```

### Gerenciamento de Buckets

- Cada bucket tem capacidade configurável
- Overflow é tratado com buckets adicionais encadeados
- Colisões são contabilizadas e reportadas

## 📈 Análise de Performance

O sistema permite comparar:

1. **Busca com Índice**: 
   - Custo: 1 acesso ao disco
   - Tempo: Otimizado pela função hash

2. **Varredura de Tabela**:
   - Custo: N páginas lidas (worst case)
   - Tempo: Linear com o tamanho dos dados

## 🎓 Propósito Educacional

Este projeto demonstra conceitos importantes de banco de dados:

- **Indexação**: Como índices aceleram consultas
- **Funções Hash**: Diferentes estratégias e suas características
- **Colisões**: Como tratar colisões em estruturas hash
- **Paginação**: Organização de dados em páginas
- **Trade-offs**: Espaço vs. tempo nas estruturas de dados

## 📝 Exemplo de Uso

```python
# Exemplo de uso das funções principais
from database.hash_function import hash_fnv1a
from database.buckets import Bucket
from database.pages import mount_pages

# Criar páginas
words = ["casa", "carro", "livro", "mesa"]
pages = mount_pages(2, words)  # 2 palavras por página

# Criar buckets
buckets = Bucket.create_buckets(len(words), 2)  # 2 palavras por bucket

# Inserir palavras nos buckets
for page_index, word_indices in enumerate(pages):
    for word in word_indices:
        bucket_index = hash_fnv1a(word, len(buckets))
        buckets[bucket_index].add_word(word, page_index)
```

## 🤝 Contribuição

Este é um projeto acadêmico. Sugestões e melhorias são bem-vindas através de issues e pull requests.

## 📄 Licença

Projeto desenvolvido para fins educacionais.