
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

df = generate_sample_dataframe(100)

# Streamlit app for displaying base characteristics
st.title("Descrição da População")

# Distribution of Age
st.subheader("Distribuição de Idade dos Alunos")
fig_age = px.histogram(df, x="Idade", title="Distribuição de Idade dos Alunos", labels={"Idade": "Idade"})
st.plotly_chart(fig_age)

# Distribution by Course
st.subheader("Distribuição de Alunos por Curso Matriculado")
fig_course = px.histogram(
    df,
    x="Curso Matriculado",
    title="Distribuição de Alunos por Curso Matriculado",
    labels={"Curso Matriculado": "Curso"}
)
st.plotly_chart(fig_course)

# Distribution by Gender
st.subheader("Distribuição de Alunos por Gênero")
fig_gender = px.histogram(
    df,
    x="Gênero",
    title="Distribuição de Alunos por Gênero",
    labels={"Gênero": "Gênero"}
)
st.plotly_chart(fig_gender)

# Summary Statistics Table
st.subheader("Resumo Estatístico da Base de Dados")
summary_stats = df.describe(include="all").transpose()
st.dataframe(summary_stats)

# Age vs. Course
st.subheader("Idade x Curso Matriculado")
fig_age_course = px.box(
    df,
    x="Curso Matriculado",
    y="Idade",
    title="Distribuição de Idade por Curso Matriculado",
    labels={"Curso Matriculado": "Curso", "Idade": "Idade"}
)
st.plotly_chart(fig_age_course)

# Age vs. Gender
st.subheader("Idade x Gênero")
fig_age_gender = px.box(
    df,
    x="Gênero",
    y="Idade",
    title="Distribuição de Idade por Gênero",
    labels={"Gênero": "Gênero", "Idade": "Idade"}
)
st.plotly_chart(fig_age_gender)

# Course vs. Gender
st.subheader("Curso Matriculado x Gênero")
fig_course_gender = px.histogram(
    df,
    x="Curso Matriculado",
    color="Gênero",
    barmode="group",
    title="Distribuição de Gênero por Curso Matriculado",
    labels={"Curso Matriculado": "Curso", "Gênero": "Gênero"}
)
st.plotly_chart(fig_course_gender)

# Table: Grouped Analysis
st.subheader("Análise Agrupada - Curso Matriculado -  Gênero Idade")
grouped_analysis = df.groupby(["Curso Matriculado", "Gênero"])["Idade"].describe()
st.write(grouped_analysis)

# Gender vs. Years in USP
st.subheader("Gênero x Anos na USP")
fig_gender_years = px.box(
    df,
    x="Gênero",
    y="Há quantos anos você está na USP?",
    title="Distribuição de Anos na USP por Gênero",
    labels={"Gênero": "Gênero", "Há quantos anos você está na USP?": "Anos na USP"}
)
st.plotly_chart(fig_gender_years)

# Course vs. Years in USP
st.subheader("Curso Matriculado x Anos na USP")
fig_course_years = px.box(
    df,
    x="Curso Matriculado",
    y="Há quantos anos você está na USP?",
    title="Distribuição de Anos na USP por Curso Matriculado",
    labels={"Curso Matriculado": "Curso", "Há quantos anos você está na USP?": "Anos na USP"}
)
st.plotly_chart(fig_course_years)

# Gender vs. Year of Entry
st.subheader("Gênero x Ano de Ingresso")
fig_gender_entry = px.histogram(
    df,
    x="Ano de Ingresso",
    color="Gênero",
    barmode="group",
    title="Distribuição de Ano de Ingresso por Gênero",
    labels={"Ano de Ingresso": "Ano de Ingresso", "Gênero": "Gênero"}
)
st.plotly_chart(fig_gender_entry)

# Course vs. Year of Entry
st.subheader("Curso Matriculado x Ano de Ingresso")
fig_course_entry = px.histogram(
    df,
    x="Ano de Ingresso",
    color="Curso Matriculado",
    barmode="group",
    title="Distribuição de Ano de Ingresso por Curso Matriculado",
    labels={"Ano de Ingresso": "Ano de Ingresso", "Curso Matriculado": "Curso"}
)
st.plotly_chart(fig_course_entry)

st.subheader("Análise Agrupada: Idade x Anos na USP")
grouped_years_age = df.groupby(["Curso Matriculado", "Gênero"])[["Idade", "Há quantos anos você está na USP?"]].mean()
st.dataframe(grouped_years_age)


# 1. Distribuição do Tipo de Escola
st.subheader("Distribuição por Tipo de Escola no Ensino Médio")
fig_school_type = px.histogram(
    df,
    x="Em que tipo de escola você estudou a maior parte do Ensino médio?",
    title="Distribuição por Tipo de Escola no Ensino Médio",
    labels={"Em que tipo de escola você estudou a maior parte do Ensino médio?": "Tipo de Escola"},
)
st.plotly_chart(fig_school_type)

# 2. Tipo de Escola x Curso Matriculado
st.subheader("Tipo de Escola x Curso Matriculado")
fig_school_course = px.histogram(
    df,
    x="Curso Matriculado",
    color="Em que tipo de escola você estudou a maior parte do Ensino médio?",
    barmode="group",
    title="Tipo de Escola x Curso Matriculado",
    labels={
        "Curso Matriculado": "Curso",
        "Em que tipo de escola você estudou a maior parte do Ensino médio?": "Tipo de Escola",
    },
)
st.plotly_chart(fig_school_course)

# 3. Tipo de Escola x Gênero
st.subheader("Tipo de Escola x Gênero")
fig_school_gender = px.histogram(
    df,
    x="Gênero",
    color="Em que tipo de escola você estudou a maior parte do Ensino médio?",
    barmode="group",
    title="Tipo de Escola x Gênero",
    labels={
        "Gênero": "Gênero",
        "Em que tipo de escola você estudou a maior parte do Ensino médio?": "Tipo de Escola",
    },
)
st.plotly_chart(fig_school_gender)
