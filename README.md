# PS4 Global Game Sales

### 📌 Visão Geral do Projeto

Empresas do setor de games utilizam análises de vendas para identificar mercados mais relevantes, franquias de maior sucesso e tendências de consumo. Este projeto simula um cenário de Business Intelligence no qual dados históricos de vendas de jogos de PlayStation 4 foram tratados e transformados em um dashboard interativo para apoiar decisões de negócio.

Neste projeto foi realizada uma análise exploratória dos dados de vendas globais de jogos de PlayStation 4 utilizando Python, seguida da construção de um dashboard interativo em Streamlit para facilitar a exploração dos resultados.

### 🔗 [Acesse o Dashboard pelo Streamlit](https://mercado-de-games.streamlit.app/)
### 🔗 [Base de Dados](https://www.kaggle.com/datasets/sidtwr/videogames-sales-dataset/data)

---

### 📝 Processo de Desenvolvimento

Durante a construção do projeto foram realizadas as seguintes etapas:

### Importação dos dados

- Carregamento do dataset utilizando Pandas.

### Análise inicial

- Verificação das dimensões da base;
- Inspeção das primeiras linhas;
- Identificação dos tipos de dados.

### Tratamento dos dados

- Identificação de valores ausentes;
- Remoção de registros incompletos;
- Remoção dos registros referentes aos anos de 2019 e 2020 por apresentarem inconsistências na base utilizada.

### Análise Exploratória (EDA)

Foram realizadas diversas análises exploratórias, incluindo:

- Evolução das vendas globais ao longo dos anos;
- Distribuição das vendas;
- Identificação de outliers;
- Análise dos jogos com maior volume de vendas;
- Participação percentual das regiões nas vendas globais;
- Comportamento de editoras, gêneros e jogos.

### Preparação dos dados
- Codificação das variáveis categóricas utilizando LabelEncoder;
- Exportação da base tratada para utilização no dashboard.

---

### 💪🏽 Desafios encontrados

Durante o desenvolvimento do projeto alguns desafios precisaram ser resolvidos:

- Identificação e remoção de registros com valores ausentes;
- Tratamento de anos com informações inconsistentes (2019 e 2020);
- Consolidação das vendas por região;
- Transformação de variáveis categóricas para análises numéricas;
- Organização das informações para construção dos indicadores utilizados no dashboard.

---

### 🧠 Principais Insights

Após a análise exploratória foi possível identificar alguns padrões relevantes:

- América do Norte e Europa concentram a maior parte das vendas globais de jogos de PS4.
- O mercado japonês possui participação significativamente menor quando comparado às demais regiões.
- Poucos jogos ultrapassaram a marca de 10 milhões de unidades vendidas, evidenciando uma forte concentração de vendas em grandes franquias.
- Editoras como Activision, Ubisoft, Electronic Arts e Sony figuram entre as principais responsáveis pelos títulos de maior sucesso comercial.
- As vendas apresentam comportamento concentrado, com poucos jogos responsáveis por grande parte do volume comercializado.


---

### 🎯 Perguntas Respondidas pelo Projeto

- Quantos jogos de PS4 existem na base analisada?

- Quantas editoras participaram do mercado de jogos do PS4?

- Quantos gêneros diferentes estão representados?

- Qual foi o volume total de vendas globais (em milhões de unidades)?

- Qual foi o jogo mais vendido do PS4?

- Como as vendas evoluíram ao longo do tempo em cada região?

- Qual é a participação percentual de cada região nas vendas globais?

- Quais são os jogos mais vendidos?

- Quais editoras concentram o maior volume de vendas?

- Quais gêneros apresentam maior volume de vendas?

- Quais editoras publicaram mais jogos?

---

### 📊 Indicadores Principais

- Total de Jogos: quantidade total de jogos de PS4 analisados.

- Total de Editoras: número de editoras únicas presentes na base.

- Total de Gêneros: quantidade de gêneros distintos.

- Total de Vendas (mi): soma das vendas globais em milhões de unidades.

- Jogo Mais Vendido: título com o maior volume de vendas globais.

- Esses indicadores fornecem uma visão rápida e objetiva do tamanho e da relevância do mercado analisado.

---

### 1️⃣ Evolução das Vendas de Jogos por Região (mi)

Este gráfico de linha mostra como as vendas evoluíram ao longo dos anos em diferentes regiões (North America, Europe, Japan e Rest of World). Ele permite identificar tendências de crescimento, estabilidade ou queda, além de comparar o desempenho regional ao longo do tempo.

<img width="904" height="443" alt="image" src="https://github.com/user-attachments/assets/273b4463-3aee-4732-82b1-73b97dc391a5" />

---

### 2️⃣ Proporção das Vendas de Jogos por Região

O gráfico de pizza apresenta a participação percentual de cada região no total de vendas globais. A visualização evidencia quais mercados são mais relevantes para o PS4, destacando a concentração de vendas entre as principais regiões.

<img width="779" height="475" alt="image" src="https://github.com/user-attachments/assets/1bcd0ba0-e68e-4c33-bceb-03d0ff9c5fa1" />

---

### 3️⃣ Jogos Mais Vendidos (mi)

Este ranking mostra os jogos com maior volume de vendas globais. Ele ajuda a identificar os jogos de maior sucesso comercial e compreender quais franquias e estilos tiveram maior impacto no mercado.

<img width="885" height="453" alt="image" src="https://github.com/user-attachments/assets/e1c35f51-9f3d-4cae-8f4a-34b9ea3b2c2c" />

---

### 4️⃣ Editoras com Maior Volume de Vendas (mi)

O gráfico apresenta as editoras responsáveis pelo maior volume de vendas globais. A análise permite observar a concentração de mercado e identificar as empresas que mais se destacaram comercialmente no ecossistema do PS4.

<img width="934" height="469" alt="image" src="https://github.com/user-attachments/assets/716f55bc-1db3-4568-b741-7ade16cf83b5" />

---

### 5️⃣ Gêneros com Maior Volume de Vendas (mi)

Neste gráfico é possível analisar quais gêneros de jogos geraram mais vendas. Ele ajuda a compreender as preferências do público e os tipos de jogos com maior apelo comercial na plataforma.

<img width="895" height="449" alt="image" src="https://github.com/user-attachments/assets/37921963-12f3-4ed7-af94-6f9d81fcc83f" />

---

### 6️⃣ Editoras com Mais Jogos Publicados

Este gráfico apresenta as editoras que mais publicaram jogos, independentemente do volume de vendas. A análise complementa a visão comercial ao mostrar quais empresas apostaram em maior diversidade e quantidade de jogos.

<img width="914" height="443" alt="image" src="https://github.com/user-attachments/assets/2d0fbecc-732a-4ea2-94d8-249d93fbfd9c" />

---

### 🛠️ Tecnologias Utilizadas

- Python

- Pandas

- Plotly

- Plotly Express

- Streamlit

- Google Colab

---

### 🚀 Conclusão

Este projeto demonstra a aplicação de técnicas de análise de dados utilizando Python, Pandas e Plotly para transformar dados brutos em informações estratégicas. O dashboard desenvolvido permite explorar indicadores do mercado de jogos de PS4 de forma interativa, apoiando a identificação de tendências, comparação entre mercados e análise do desempenho comercial de jogos, gêneros e editoras.
