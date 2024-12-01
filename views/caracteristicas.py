
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

st.subheader("Distribuição por instituto")
instituto_col_1, instituto_col_2 = st.columns([1, 1])

with instituto_col_1:

    fig_age = px.histogram(df, x="instituto", title="Distribuição por Instituto", labels={"Instituto": "Contagem"})
    st.plotly_chart(fig_age)

with instituto_col_2:

    distribution = df["instituto"].value_counts().reset_index()
    distribution.columns = ["Instituto", "Contagem"]
    st.write("**Tabela de Distribuição por Instituto**")
    st.dataframe(distribution, use_container_width=True,hide_index=True)

# Distribution by Course
st.subheader("Distribuição por curso")
curso_col_1, curso_col_2 = st.columns([1, 1])

with curso_col_1:

    fig_course = px.histogram(
        df,
        x="Curso Matriculado",
        title="Distribuição de Alunos por Curso Matriculado",
        labels={"Curso Matriculado": "Curso"}
    )
    st.plotly_chart(fig_course)

with curso_col_2:

    distribution = df["Curso Matriculado"].value_counts().reset_index()
    distribution.columns = ["Curso Matriculado", "Contagem"]
    st.write("**Tabela de Distribuição por Curso Matriculado**")
    st.dataframe(distribution, use_container_width=True,hide_index=True)

# Distribution by Gender
st.subheader("Distribuição por Gênero")
genero_col_1, genero_col_2 = st.columns([1, 1])

with genero_col_1:
    fig_gender = px.histogram(
        df,
        x="Gênero",
        title="Distribuição de Alunos por Gênero",
        labels={"Gênero": "Gênero"}
    )
    st.plotly_chart(fig_gender)

with genero_col_2:
    distribution = df["Gênero"].value_counts().reset_index()
    distribution.columns = ["Gênero", "Contagem"]
    st.write("**Tabela de Distribuição por Gênero**")
    st.dataframe(distribution, use_container_width=True, hide_index=True)

# Distribution by Age
st.subheader("Distribuição por Idade")
idade_col_1, idade_col_2 = st.columns([1, 1])

with idade_col_1:
    fig_age = px.histogram(
        df,
        x="Idade",
        title="Distribuição de Alunos por Idade",
        labels={"Idade": "Idade"}
    )
    st.plotly_chart(fig_age)

with idade_col_2:
    distribution = df["Idade"].value_counts().reset_index()
    distribution.columns = ["Idade", "Contagem"]
    st.write("**Tabela de Distribuição por Idade**")
    st.dataframe(distribution, use_container_width=True, hide_index=True)

# Distribution by Year of Admission
st.subheader("Distribuição por Ano de Ingresso")
ano_col_1, ano_col_2 = st.columns([1, 1])

with ano_col_1:
    fig_admission_year = px.histogram(
        df,
        x="Ano de Ingresso",
        title="Distribuição de Alunos por Ano de Ingresso",
        labels={"Ano de Ingresso": "Ano"}
    )
    st.plotly_chart(fig_admission_year)

with ano_col_2:
    distribution = df["Ano de Ingresso"].value_counts().reset_index()
    distribution.columns = ["Ano de Ingresso", "Contagem"]
    st.write("**Tabela de Distribuição por Ano de Ingresso**")
    st.dataframe(distribution, use_container_width=True, hide_index=True)

# Distribution by Years in USP
st.subheader("Distribuição por Tempo na USP")
tempo_col_1, tempo_col_2 = st.columns([1, 1])

with tempo_col_1:
    fig_time_in_usp = px.histogram(
        df,
        x="Há quantos anos você está na USP?",
        title="Distribuição de Alunos por Tempo na USP",
        labels={"Há quantos anos você está na USP?": "Anos na USP"}
    )
    st.plotly_chart(fig_time_in_usp)

with tempo_col_2:
    distribution = df["Há quantos anos você está na USP?"].value_counts().reset_index()
    distribution.columns = ["Anos na USP", "Contagem"]
    st.write("**Tabela de Distribuição por Tempo na USP**")
    st.dataframe(distribution, use_container_width=True, hide_index=True)

# Distribution by Type of High School
st.subheader("Distribuição por Tipo de Escola no Ensino Médio")
escola_col_1, escola_col_2 = st.columns([1, 1])

with escola_col_1:
    fig_school_type = px.histogram(
        df,
        x="Em que tipo de escola você estudou a maior parte do Ensino médio?",
        title="Distribuição de Alunos por Tipo de Escola no Ensino Médio",
        labels={"Em que tipo de escola você estudou a maior parte do Ensino médio?": "Tipo de Escola"}
    )
    st.plotly_chart(fig_school_type)

with escola_col_2:
    distribution = df["Em que tipo de escola você estudou a maior parte do Ensino médio?"].value_counts().reset_index()
    distribution.columns = ["Tipo de Escola", "Contagem"]
    st.write("**Tabela de Distribuição por Tipo de Escola no Ensino Médio**")
    st.dataframe(distribution, use_container_width=True, hide_index=True)

