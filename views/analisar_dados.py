
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
from datetime import datetime
from auxiliar import *
import statsmodels

st.set_page_config(page_title="Trabalho de estatística", page_icon="🕒", layout="wide")

def load_main_dataframe(worksheet):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet=worksheet)
    return df


df = generate_sample_dataframe(100)

st.title("Impacto das Características nas Respostas")


# Impacto do Gênero nas Avaliações do Curso
st.subheader("Gênero x Avaliações do Curso")
fig_gender_eval = px.box(
    df,
    x="Gênero",
    y="Avaliação do Curso [Como você avalia a infraestrutura física do seu Instituto?]",
    title="Gênero x Infraestrutura Física",
    labels={"Gênero": "Gênero", "Avaliação do Curso [Como você avalia a infraestrutura física do seu Instituto?]": "Infraestrutura Física"},
)
st.plotly_chart(fig_gender_eval)

# Impacto do Curso Matriculado nas Respostas
st.subheader("Curso Matriculado x Identificação com o Curso")
fig_course_identification = px.histogram(
    df,
    x="Você sente que se identifica com o curso em que está matriculado?",
    color="Curso Matriculado",
    barmode="group",
    title="Curso Matriculado x Identificação",
    labels={"Você sente que se identifica com o curso em que está matriculado?": "Identificação com o Curso", "Curso Matriculado": "Curso"},
)
st.plotly_chart(fig_course_identification)

# Anos na USP x Desempenho Acadêmico
st.subheader("Anos na USP x Desempenho Acadêmico")
fig_years_performance = px.box(
    df,
    x="Há quantos anos você está na USP?",
    y="Como você avalia seu desempenho acadêmico em termos de notas e possibilidade de reprovações ou jubilamento?",
    title="Anos na USP x Desempenho Acadêmico",
    labels={"Há quantos anos você está na USP?": "Anos na USP", "Como você avalia seu desempenho acadêmico em termos de notas e possibilidade de reprovações ou jubilamento?": "Desempenho Acadêmico"},
)
st.plotly_chart(fig_years_performance)

# Saúde Física e Mental x Características
st.subheader("Impacto na Saúde Física e Mental x Características")
fig_health_course = px.histogram(
    df,
    x="O curso tem impactado sua saúde física ou mental de alguma forma?",
    color="Curso Matriculado",
    barmode="group",
    title="Impacto na Saúde x Curso Matriculado",
    labels={"O curso tem impactado sua saúde física ou mental de alguma forma?": "Impacto na Saúde", "Curso Matriculado": "Curso"},
)
st.plotly_chart(fig_health_course)
