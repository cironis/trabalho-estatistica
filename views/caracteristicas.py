
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
from datetime import datetime
from auxiliar import *

st.set_page_config(page_title="Características da População", page_icon="🕒", layout="wide")

def load_main_dataframe(worksheet):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet=worksheet)
    return df

df = load_main_dataframe("base_respostas")
df['Curso Matriculado'] = df['Curso Matriculado'].astype(str)
df['Curso Matriculado'] = df['Curso Matriculado'].fillna('')
df['instituto'] = df['Curso Matriculado'].str.split(' - ').str[0]
df = df.loc[df['instituto'] != 'Outro']

# df = generate_sample_dataframe(100)

# Streamlit app for displaying base characteristics
st.title("Descrição da População")

# Function to add percentage column
def add_percentage_column(distribution_df):
    total = distribution_df["Contagem"].sum()
    distribution_df["Porcentagem (%)"] = (distribution_df["Contagem"] / total * 100).round(2)
    return distribution_df

# Function to calculate statistical summary
def calculate_summary(column):
    return pd.DataFrame({
        "Métrica": ["Média", "Mediana", "Desvio Padrão", "Máximo", "Mínimo"],
        "Valor": [
            column.mean(),
            column.median(),
            column.std(),
            column.max(),
            column.min()
        ]
    })

# Distribution by Instituto
st.subheader("Distribuição por Instituto")
instituto_col_1, instituto_col_2 = st.columns([1, 1])

with instituto_col_1:
    fig_instituto = px.histogram(df, x="instituto", title="Distribuição por Instituto", labels={"instituto": "Instituto"})
    st.plotly_chart(fig_instituto)

with instituto_col_2:
    distribution = df["instituto"].value_counts().reset_index()
    distribution.columns = ["Instituto", "Contagem"]
    distribution = add_percentage_column(distribution)
    st.write("**Tabela de Distribuição por Instituto**")
    st.dataframe(distribution, use_container_width=True, hide_index=True)

# Distribution by Curso
st.subheader("Distribuição por Curso")
curso_col_1, curso_col_2 = st.columns([1, 1])

with curso_col_1:
    fig_curso = px.histogram(df, x="Curso Matriculado", title="Distribuição por Curso Matriculado", labels={"Curso Matriculado": "Curso"})
    st.plotly_chart(fig_curso)

with curso_col_2:
    distribution = df["Curso Matriculado"].value_counts().reset_index()
    distribution.columns = ["Curso Matriculado", "Contagem"]
    distribution = add_percentage_column(distribution)
    st.write("**Tabela de Distribuição por Curso Matriculado**")
    st.dataframe(distribution, use_container_width=True, hide_index=True)

# Distribution by Gênero
st.subheader("Distribuição por Gênero")
genero_col_1, genero_col_2 = st.columns([1, 1])

with genero_col_1:
    fig_genero = px.histogram(df, x="Gênero", title="Distribuição por Gênero", labels={"Gênero": "Gênero"})
    st.plotly_chart(fig_genero)

with genero_col_2:
    distribution = df["Gênero"].value_counts().reset_index()
    distribution.columns = ["Gênero", "Contagem"]
    distribution = add_percentage_column(distribution)
    st.write("**Tabela de Distribuição por Gênero**")
    st.dataframe(distribution, use_container_width=True, hide_index=True)

# Distribution by Ano de Ingresso
st.subheader("Distribuição por Ano de Ingresso")
ano_col_1, ano_col_2 = st.columns([1, 1])

with ano_col_1:
    fig_ano = px.histogram(df, x="Ano de Ingresso", title="Distribuição por Ano de Ingresso", labels={"Ano de Ingresso": "Ano"})
    st.plotly_chart(fig_ano)

with ano_col_2:
    distribution = df["Ano de Ingresso"].value_counts().reset_index()
    distribution.columns = ["Ano de Ingresso", "Contagem"]
    distribution = add_percentage_column(distribution)
    st.write("**Tabela de Distribuição por Ano de Ingresso**")
    st.dataframe(distribution, use_container_width=True, hide_index=True)

# Distribution by Tipo de Escola
st.subheader("Distribuição por Tipo de Escola no Ensino Médio")
escola_col_1, escola_col_2 = st.columns([1, 1])

with escola_col_1:
    fig_escola = px.histogram(df, x="Em que tipo de escola você estudou a maior parte do Ensino médio?", title="Distribuição por Tipo de Escola no Ensino Médio", labels={"Em que tipo de escola você estudou a maior parte do Ensino médio?": "Tipo de Escola"})
    st.plotly_chart(fig_escola)

with escola_col_2:
    distribution = df["Em que tipo de escola você estudou a maior parte do Ensino médio?"].value_counts().reset_index()
    distribution.columns = ["Tipo de Escola", "Contagem"]
    distribution = add_percentage_column(distribution)
    st.write("**Tabela de Distribuição por Tipo de Escola no Ensino Médio**")
    st.dataframe(distribution, use_container_width=True, hide_index=True)

# Statistical Summary for Idade
st.subheader("Resumo Estatístico por Idade")
idade_col_1, idade_col_2 = st.columns([1, 1])

with idade_col_1:
    fig_idade = px.histogram(df, x="Idade", title="Distribuição de Alunos por Idade", labels={"Idade": "Idade"})
    st.plotly_chart(fig_idade)

with idade_col_2:
    summary = calculate_summary(df["Idade"])
    st.write("**Resumo Estatístico por Idade**")
    st.dataframe(summary, use_container_width=True, hide_index=True)

# Statistical Summary for Tempo na USP
st.subheader("Resumo Estatístico por Tempo na USP")
tempo_col_1, tempo_col_2 = st.columns([1, 1])

with tempo_col_1:
    fig_tempo = px.histogram(df, x="Há quantos anos você está na USP?", title="Distribuição por Tempo na USP", labels={"Há quantos anos você está na USP?": "Tempo na USP"})
    st.plotly_chart(fig_tempo)

with tempo_col_2:
    summary = calculate_summary(df["Há quantos anos você está na USP?"])
    st.write("**Resumo Estatístico por Tempo na USP**")
    st.dataframe(summary, use_container_width=True, hide_index=True)

