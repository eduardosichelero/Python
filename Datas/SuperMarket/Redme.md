# Desenvolvimento
Aqui está uma explicação detalhada do código

## Importação de bibliotecas:

```python
import streamlit as st
import pandas as pd
import plotly.express as px
```

Importa as bibliotecas necessárias: [Streamlit](https://streamlit.io/) para a construção do aplicativo web, [Pandas](https://pandas.pydata.org/) para manipulação de dados e [Plotly](https://plotly.com/) Express para criação de gráficos interativos.


## Configuração da página

```python
st.set_page_config(layout="wide")
```

Configura a página para ter um layout amplo.

## Leitura e pré-processamento dos dados 

```py
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
```
Carrega o conjunto de dados, converte a coluna "Date" para o formato datetime e cria uma nova coluna "Month" para representar o ano e o mês.

###  Linha a Linha
- Carrega os dados do arquivo CSV (supermarket_sales.csv), define o formato do separador como ponto e vírgula (sep=";")
- Define o  formato do decimal como vírgula **(decimal=",")**.
-  Converte a coluna "Date" para o formato de data e ordena o DataFrame por data.
- Cria uma nova coluna "Month" para armazenar o ano e mês.

## Filtragem dos dados com base no mês selecionado:

```py
month = st.sidebar.selectbox("Mês", df["Month"].unique())
df_filtered = df[df["Month"] == month]
```

Utiliza um seletor na barra lateral para permitir a escolha do mês. Filtra os dados com base no mês selecionado.
###  Linha a Linha
- Cria um seletor na barra lateral para escolher o mês (st.sidebar.selectbox). 
- Filtra os dados com base no mês escolhido.

## Criação do layout da página com colunas:

```py
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)
```

Divide a página em colunas para organizar os gráficos.
###  Linha a Linha
- Divide a página em 2 colunas para os dois primeiros gráficos 
- e em 3 colunas para os três gráficos seguintes.

## Criação e exibição do primeiro gráfico (Faturamento por dia):

```py
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)
```
Cria um gráfico de barras usando o Plotly Express e o exibe na primeira coluna.
###  Linha a Linha
- Cria um gráfico de barras usando Plotly Express, representando o faturamento diário por cidade
- O gráfico é exibido na primeira coluna (col1).

## Criação e exibição do segundo gráfico (Faturamento por tipo de produto):

```py
fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City", title="Faturamento por tipo de produto", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)
```
Cria um gráfico de barras horizontais representando o faturamento por tipo de produto e o exibe na segunda coluna.


## Criação e exibição do terceiro gráfico (Faturamento por filial):

```py
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)
```
Agrupa os dados por filial, calcula o faturamento total e cria um gráfico de barras exibindo o faturamento por filial na terceira coluna.


## Criação e exibição do quarto gráfico (Faturamento por tipo de pagamento):

```py
fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)
```
Cria um gráfico de pizza mostrando a distribuição do faturamento por tipo de pagamento e o exibe na quarta coluna.


## Criação e exibição do quinto gráfico (Avaliação por filial):

```py
city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtered, y="Rating", x="City", title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)
```
Agrupa os dados por filial, calcula a média das avaliações e cria um gráfico de barras representando a avaliação por filial na quinta coluna.
###  Linha a Linha
- Calcula a média das avaliações por filial e cria um gráfico de barras exibindo esses valores na quinta coluna (col5).
