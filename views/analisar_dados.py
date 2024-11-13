
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
from datetime import datetime
from auxiliar import *

st.set_page_config(page_title="Trabalho de estatística", page_icon="🕒", layout="wide")

def load_main_dataframe(worksheet):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet=worksheet)
    return df


df = generate_sample_dataframe(100)

# Streamlit app for displaying base characteristics
st.title("Características da Base de Dados")

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
st.subheader("Análise Agrupada")
grouped_analysis = df.groupby(["Curso Matriculado", "Gênero"])["Idade"].describe()
st.write(grouped_analysis)
