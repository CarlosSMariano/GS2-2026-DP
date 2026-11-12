# 🏘️ ConectaBairro — Priorizador de Necessidades Comunitárias

## 📌 Sobre o projeto

O **ConectaBairro** é uma aplicação desenvolvida em Python com Streamlit, cujo objetivo é auxiliar na priorização de necessidades comunitárias.

A aplicação permite cadastrar diferentes necessidades de um bairro, informando o custo estimado e o benefício que cada uma pode proporcionar à comunidade.

Com base nessas informações e em um orçamento disponível, o sistema utiliza Programação Dinâmica para identificar a combinação de necessidades que proporciona o maior benefício possível sem ultrapassar os recursos disponíveis.

## 🎯 Objetivo

Demonstrar a aplicação de conceitos de **Dynamic Programming (Programação Dinâmica)** na resolução de um problema real de otimização de recursos comunitários.

O projeto utiliza o Problema da Mochila (0/1 Knapsack Problem) para selecionar as necessidades que oferecem o maior benefício total dentro de um orçamento limitado.

## ⚙️ Funcionalidades

- **Cadastro de necessidades:** permite informar o nome, custo estimado e benefício de cada necessidade.
- **Listagem:** apresenta as necessidades cadastradas em uma lista com rolagem.
- **Exclusão:** permite remover necessidades cadastradas.
- **Definição de orçamento:** permite informar os recursos financeiros disponíveis.
- **Priorização automática:** executa o algoritmo da mochila para encontrar a melhor combinação.
- **Exibição dos resultados:** apresenta as necessidades selecionadas, o custo total, o benefício máximo e os recursos restantes.

## 🧠 Algoritmo utilizado

O projeto utiliza o **Problema da Mochila 0/1 (0/1 Knapsack Problem)**, implementado por meio da técnica de **Tabulação (Bottom-Up)**.

O algoritmo utiliza uma matriz de programação dinâmica, na qual:

- As linhas representam a quantidade de necessidades consideradas.
- As colunas representam os valores possíveis de orçamento.
- Cada posição armazena o maior benefício que pode ser alcançado considerando determinada quantidade de necessidades e determinado orçamento.

Para cada necessidade, o algoritmo avalia duas possibilidades:

1. Não selecionar a necessidade, mantendo o benefício máximo anterior.
2. Selecionar a necessidade, somando seu benefício ao melhor resultado obtido com o orçamento restante.

A maior dessas possibilidades é armazenada na matriz.

Após preencher a matriz, o algoritmo realiza o processo de reconstrução para identificar quais necessidades foram selecionadas.

### Complexidade

Considerando `n` necessidades e um orçamento inteiro `W`:

- **Tempo:** O(n × W), pois o algoritmo percorre a matriz de programação dinâmica.
- **Espaço:** O(n × W), devido ao armazenamento da matriz.

## 🛠️ Tecnologias utilizadas

- Python 3
- Streamlit
- Programação Dinâmica
- Problema da Mochila 0/1

## 📂 Estrutura do projeto

```text
ConectaBairro/
│
├── app.py
│
├── core/
│   ├── __init__.py
│   └── knapsack.py
│
└── README.md
```

### Descrição dos arquivos

| Arquivo | Responsabilidade |
|---|---|
| `app.py` | Interface gráfica, cadastro e apresentação dos resultados. |
| `core/knapsack.py` | Implementação do algoritmo da mochila utilizando Programação Dinâmica. |
| `README.md` | Documentação do projeto. |

## 🚀 Como executar o projeto

### 1. Pré-requisitos

Certifique-se de possuir o Python 3 instalado.

Verifique a instalação:

```bash
python3 --version
```

### 2. Clonar ou baixar o projeto

Acesse o diretório do projeto pelo terminal.

### 3. Criar um ambiente virtual (recomendado)

```bash
python3 -m venv .venv
```

Ative o ambiente virtual:

**Linux/macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Instalar as dependências

```bash
python -m pip install streamlit
```

### 5. Executar a aplicação

Na pasta principal do projeto, execute:

```bash
python -m streamlit run app.py
```

A aplicação será aberta automaticamente no navegador.

## 📖 Como utilizar

1. Informe o orçamento disponível.
2. Clique em **Adicionar necessidade**.
3. Preencha o nome, o custo estimado e o benefício para o bairro.
4. Cadastre quantas necessidades desejar.
5. Clique em **Priorizar necessidades**.
6. Consulte a combinação selecionada pelo algoritmo e os indicadores apresentados.

## 📊 Exemplo de utilização

Considere as seguintes necessidades fictícias:

| Necessidade | Custo | Benefício |
|---|---:|---:|
| Reforço escolar | R$ 500 | 9 |
| Cestas básicas | R$ 800 | 10 |
| Material escolar | R$ 300 | 7 |
| Horta comunitária | R$ 350 | 6 |

Com um orçamento de R$ 1.000, o algoritmo procura a combinação de necessidades que maximize a soma dos benefícios sem ultrapassar o orçamento.

## ⚠️ Limitações

- Os custos são considerados números inteiros em reais.
- O benefício é representado por uma pontuação de 1 a 10.
- Cada necessidade pode ser selecionada apenas uma vez.
- Os dados são armazenados em sessão utilizando `st.session_state`, não sendo persistidos em banco de dados.
- O benefício é uma estimativa informada pelo usuário e não representa uma medição objetiva do impacto social.

## 👥 Integrantes

| Nome | RM |
|---|---|
| Carlos Eduardo Sanches Mariano | rm561756 |
| Gabriel Hombris | rm566553 |
| Icaro Machado | rm572802 |
| Nicolas Guinante Cavalcanti | rm570222 |

---

**Projeto acadêmico — FIAP | Global Solution 2026**

**Tema:** CitizenTech — Tecnologia a serviço da cidadania.
