import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('PS4_GamesSalesLimpo.csv', encoding='latin1')

st.set_page_config(
    page_title='Dashboard - Mercado de Games',
    layout='wide'
)

st.markdown(
    "<h1 style='text-align: center;'>Dashboard de Vendas Globais de Jogos de PS4</h1>",
    unsafe_allow_html=True
)

if not df.empty:
    tot_games = df['Game'].count()
    tot_publisher = df['Publisher'].nunique()
    tot_genre = df['Genre'].nunique()
    tot_vendas = df['Global'].sum()
    serie_top = df.groupby('Game')['Global'].sum().nlargest(1)
    game_mais_vendido = serie_top.index[0]
else:
    tot_games, tot_publisher, tot_genre, tot_games, game_mais_vendido = 0, 0, 0, 0, ""

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric('Total de Jogos', f'{tot_games}')
col2.metric('Total de Editoras', f'{tot_publisher}')
col3.metric('Total de Gêneros', f'{tot_genre}')
col4.metric('Total de Vendas (mi)', f'{tot_vendas:,.2f}')
col5.metric('Jogo Mais Vendido', f'{game_mais_vendido}')

st.markdown('---')

col_graf1, col_graf2 = st.columns(2)

with col_graf1:

    vendas_globais = (
        df.groupby('Year', as_index=False)
        [['Global', 'North America', 'Europe', 'Japan', 'Rest of World']]
        .sum()
    )

    grafico1 = px.line(
        vendas_globais,
        y=['North America', 'Europe', 'Japan', 'Rest of World'],
        x='Year',
        markers=True,
        text='Global',
        labels={
            'value': 'Vendas (milhões)',
            'Year': 'Ano',
            'variable': 'Região'
        },
        title='Evolução das Vendas de Jogos por Região (mi)'
    )

    grafico1.update_traces(
        texttemplate='%{y:.2f}',
        textposition='top center'
    )

    grafico1.update_layout(
        title=dict(
            x=0.5,
            xanchor='center',
            xref='paper'
        ),
        title_font_size=18
    )

    st.plotly_chart(grafico1, use_container_width=True)

with col_graf2:

    divisao_regiao = (
        df.melt(
            value_vars=['North America', 'Europe', 
                    'Japan', 'Rest of World'],
            var_name='Região',
            value_name='Quantidade'
        )
        .groupby('Região', as_index=False)
        .sum()
    )

    grafico2 = px.pie(
        divisao_regiao,
        names='Região',
        values='Quantidade',
        title='Proporção das Vendas de Jogos por Região'
    )

    grafico2.update_traces(textinfo='percent+label')

    grafico2.update_layout(
        title=dict(
            x=0.5,
            xanchor='center',
            xref='paper'
        ),
        title_font_size=18
    )

    st.plotly_chart(grafico2, use_container_width=True)

col_graf3, col_graf4 = st.columns(2)

with col_graf3:

    top_games = (
        df.groupby('Game', as_index=False)['Global']
        .sum()
        .nlargest(12, columns='Global')
        .reset_index()
    )

    grafico3 = px.bar(
        top_games.sort_values(by='Global'),
        y='Game',
        x='Global',
        text='Global',
        labels={'Global': 'Vendas (milhões)',
                'Game': 'Jogo'},
        title='Jogos Mais Vendidos (mi)'
    )

    grafico3.update_traces(
        textposition='outside',
        marker_color='#005bc5'
    )

    grafico3.update_layout(
        title=dict(
            x=0.5,
            xanchor='center',
            xref='paper'
        ),
        title_font_size=18
    )

    st.plotly_chart(grafico3, use_container_width=True)

with col_graf4:

    top_publisher = (
        df.groupby('Publisher')['Global']
        .sum()
        .nlargest(12)
        .reset_index()
    )

    grafico4 = px.bar(
        top_publisher.sort_values(by='Global'),
        y='Publisher',
        x='Global',
        text='Global',
        labels={'Global': 'Vendas (milhões)',
                'Publisher': 'Editora'},
        title='Editoras com Maior Volume de Vendas (mi)'
    )

    grafico4.update_traces(
        textposition='outside',
        texttemplate='%{x:.2f}',
        marker_color='#005bc5'
    )

    grafico4.update_layout(
        title=dict(
            x=0.5,
            xanchor='center',
            xref='paper'
        ),
        title_font_size=18
    )

    st.plotly_chart(grafico4, use_container_width=True)

col_graf5, col_graf6 = st.columns(2)

with col_graf5:

    top_genre = (
        df.groupby('Genre')['Global']
        .sum()
        .nlargest(12)
        .reset_index()
    )

    grafico5 = px.bar(
        top_genre.sort_values(by='Global'),
        y='Genre',
        x='Global',
        text='Global',
        labels={'Genre': 'Gênero',
                'Global': 'Vendas (milhões)'},
        title='Gêneros com Maior Volume de Vendas (mi)'
    )

    grafico5.update_traces(
        textposition='outside',
        marker_color='#005bc5'
    )

    grafico5.update_layout(
        title=dict(
            x=0.5,
            xanchor='center',
            xref='paper'
        ),
        title_font_size=18
    )

    st.plotly_chart(grafico5, use_container_width=True)

with col_graf6:

    top_publisher2 = (
        df['Publisher']
        .value_counts()
        .nlargest(12)
        .reset_index()
    )

    top_publisher2.columns = ['Publisher', 'Quantidade']

    grafico6 = px.bar(
        top_publisher2.sort_values(by='Quantidade'),
        y='Publisher',
        x='Quantidade',
        text='Quantidade',
        labels={'Publisher': 'Editora'},
        title='Editoras Com Mais Jogos Publicados'
    )

    grafico6.update_traces(
        textposition='outside',
        marker_color='#005bc5'
    )

    grafico6.update_layout(
        title=dict(
            x=0.5,
            xanchor='center',
            xref='paper'
        ),
        title_font_size=18
    )

    st.plotly_chart(grafico6, use_container_width=True)