
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


