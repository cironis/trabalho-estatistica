
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

# Streamlit App
st.title("Análise de Resultados do Formulário")
st.write("Este painel apresenta visualizações e análises baseadas nos dados coletados.")

# Visualização 1: Distribuição por Curso Matriculado
st.subheader("Distribuição por Curso Matriculado")
fig1 = px.histogram(df, x="Curso Matriculado", title="Distribuição por Curso Matriculado")
st.plotly_chart(fig1)

# Visualização 2: Distribuição por Gênero
st.subheader("Distribuição por Gênero")
fig2 = px.histogram(df, x="Gênero", title="Distribuição por Gênero")
st.plotly_chart(fig2)

# Visualização 3: Idade dos Alunos
st.subheader("Distribuição de Idade")
fig3 = px.histogram(df, x="Idade", title="Distribuição de Idade")
st.plotly_chart(fig3)

# Visualização 4: Identificação com o Curso
st.subheader("Identificação com o Curso")
fig4 = px.histogram(
    df,
    x="Você sente que se identifica com o curso em que está matriculado?",
    title="Identificação com o Curso",
)
st.plotly_chart(fig4)

# Visualização 5: Impacto na Saúde Física e Mental
st.subheader("Impacto do Curso na Saúde Física e Mental")
fig5 = px.histogram(
    df,
    x="O curso tem impactado sua saúde física ou mental de alguma forma?",
    title="Impacto na Saúde Física e Mental",
)
st.plotly_chart(fig5)

# Visualização 6: Avaliação das Aulas
st.subheader("Avaliação da Qualidade das Aulas")
fig6 = px.box(
    df,
    y="Avaliação do Curso [Como você avalia a qualidade das aulas no seu Instituto?]",
    title="Qualidade das Aulas - Avaliação",
)
st.plotly_chart(fig6)

# Visualização 7: Expectativas com o Curso
st.subheader("Expectativas Atendidas")
fig7 = px.histogram(
    df,
    x="O curso tem atendido às suas expectativas desde que você iniciou?",
    title="Expectativas Atendidas",
)
st.plotly_chart(fig7)

# Visualização 8: Planejamento do Curso e Futuro
st.subheader("Planejamento do Curso em Relação à Área de Atuação")
fig8 = px.box(
    df,
    y="Avaliação do Curso [O planejamento do seu curso é alinhado com sua futura área de atuação?]",
    title="Planejamento do Curso - Avaliação",
)
st.plotly_chart(fig8)

st.write("Explore mais interativamente ou adicione filtros para detalhar as análises!")


