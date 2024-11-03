
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


sample_df = create_sample_df(100)
st.title("Análise dos dados")


# Título principal
st.title("Análise dos Dados da Pesquisa")

# Distribuição de Idade
st.subheader("1. Distribuição de Idade dos Respondentes")
fig_age = px.histogram(sample_df, x="Idade", nbins=10, title="Distribuição de Idade dos Respondentes")
st.plotly_chart(fig_age)

# Distribuição das Avaliações da Qualidade das Aulas
st.subheader("2. Distribuição da Avaliação da Qualidade das Aulas")
fig_qualidade = px.histogram(sample_df, x="Qualidade das aulas", title="Distribuição da Avaliação da Qualidade das Aulas")
st.plotly_chart(fig_qualidade)

# Idade por Gênero
st.subheader("3. Idade por Gênero")
fig_age_gender = px.box(sample_df, x="Gênero", y="Idade", title="Idade por Gênero")
st.plotly_chart(fig_age_gender)

# Avaliação de Qualidade das Aulas por Gênero
st.subheader("4. Avaliação da Qualidade das Aulas por Gênero")
fig_age_eval = px.box(sample_df, x="Gênero", y="Qualidade das aulas", title="Avaliação da Qualidade das Aulas por Gênero")
st.plotly_chart(fig_age_eval)

# Ano de Ingresso e Avaliação das Aulas
st.subheader("5. Avaliação da Qualidade das Aulas por Ano de Ingresso")
fig_year_eval = px.box(sample_df, x="Ano de ingresso", y="Qualidade das aulas", title="Avaliação da Qualidade das Aulas por Ano de Ingresso")
st.plotly_chart(fig_year_eval)

# Ano de Ingresso por Instituto
st.subheader("6. Ano de Ingresso por Instituto")
fig_year_institute = px.histogram(sample_df, x="Ano de ingresso", color="Instituto", title="Ano de Ingresso por Instituto")
st.plotly_chart(fig_year_institute)

# Avaliação da Qualidade das Aulas por Instituto
st.subheader("7. Avaliação da Qualidade das Aulas por Instituto")
fig_institute_eval = px.box(sample_df, x="Instituto", y="Qualidade das aulas", title="Avaliação da Qualidade das Aulas por Instituto")
st.plotly_chart(fig_institute_eval)

# Distribuição do Tipo de Curso por Instituto
st.subheader("8. Distribuição do Tipo de Curso por Instituto")
fig_course_institute = px.histogram(sample_df, x="Instituto", color="Curso", title="Distribuição do Tipo de Curso por Instituto")
st.plotly_chart(fig_course_institute)

# Motivação por Tipo de Curso
st.subheader("9. Motivação por Tipo de Curso")
fig_course_motivation = px.box(sample_df, x="Curso", y="Desmotivação por reprovação", title="Motivação por Tipo de Curso")
st.plotly_chart(fig_course_motivation)

# Preparação para o Mercado por Tipo de Curso
st.subheader("10. Preparação para o Mercado por Tipo de Curso")
fig_market_course = px.box(sample_df, x="Curso", y="Preparação para mercado", title="Preparação para o Mercado por Tipo de Curso")
st.plotly_chart(fig_market_course)

# Avaliação da Qualidade das Aulas por Intenção de Continuidade
st.subheader("11. Avaliação da Qualidade das Aulas por Intenção de Continuidade")
fig_continue_quality = px.box(sample_df, x="Continuidade no curso", y="Qualidade das aulas", title="Avaliação da Qualidade das Aulas por Intenção de Continuidade")
st.plotly_chart(fig_continue_quality)

# Intenção de Continuidade por Gênero
st.subheader("12. Intenção de Continuidade por Gênero")
fig_continue_gender = px.histogram(sample_df, x="Continuidade no curso", color="Gênero", title="Intenção de Continuidade por Gênero")
st.plotly_chart(fig_continue_gender)
