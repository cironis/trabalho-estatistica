
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

# Analyzing course evaluation questions and correlating them with other characteristics

# 2. Gender vs. Course Evaluation (Infrastructure)
st.subheader("Gênero x Infraestrutura Física")
fig_gender_infrastructure = px.box(
    df,
    x="Gênero",
    y="Avaliação do Curso [Como você avalia a infraestrutura física do seu Instituto?]",
    title="Gênero x Infraestrutura Física",
    labels={
        "Gênero": "Gênero",
        "Avaliação do Curso [Como você avalia a infraestrutura física do seu Instituto?]": "Infraestrutura Física",
    },
)
st.plotly_chart(fig_gender_infrastructure)

# 3. Course vs. Academic Support Evaluation
st.subheader("Curso Matriculado x Suporte Acadêmico")
fig_course_support = px.box(
    df,
    x="Curso Matriculado",
    y="Avaliação do Curso [Como você avalia o suporte acadêmico oferecido pelas disciplinas?]",
    title="Curso Matriculado x Suporte Acadêmico",
    labels={
        "Curso Matriculado": "Curso",
        "Avaliação do Curso [Como você avalia o suporte acadêmico oferecido pelas disciplinas?]": "Suporte Acadêmico",
    },
)
st.plotly_chart(fig_course_support)

# 5. Course Planning Evaluation by Course Type
st.subheader("Planejamento do Curso x Tipo de Curso")
fig_course_planning = px.box(
    df,
    x="Curso Matriculado",
    y="Avaliação do Curso [O planejamento do seu curso é alinhado com sua futura área de atuação?]",
    title="Planejamento do Curso x Tipo de Curso",
    labels={
        "Curso Matriculado": "Curso",
        "Avaliação do Curso [O planejamento do seu curso é alinhado com sua futura área de atuação?]": "Planejamento do Curso",
    },
)
st.plotly_chart(fig_course_planning)

# 6. Overview of Course Evaluations by Gender
st.subheader("Visão Geral das Avaliações do Curso por Gênero")
eval_columns = [
    "Avaliação do Curso [Como você avalia a qualidade das aulas no seu Instituto?]",
    "Avaliação do Curso [Como você avalia a infraestrutura física do seu Instituto?]",
    "Avaliação do Curso [Como você avalia o suporte acadêmico oferecido pelas disciplinas?]",
    "Avaliação do Curso [Como você avalia a carga horária e o ritmo do seu curso?]",
    "Avaliação do Curso [O planejamento do seu curso é alinhado com sua futura área de atuação?]",
]
avg_evals_gender = df.groupby("Gênero")[eval_columns].mean()
st.dataframe(avg_evals_gender)

# Display grouped data in a visual format
fig_avg_eval_gender = px.bar(
    avg_evals_gender.transpose(),
    barmode="group",
    title="Média das Avaliações do Curso por Gênero",
    labels={"value": "Média da Avaliação", "index": "Perguntas de Avaliação"},
)
st.plotly_chart(fig_avg_eval_gender)


# 4. Tipo de Escola x Avaliação de Qualidade das Aulas
st.subheader("Tipo de Escola x Avaliação de Qualidade das Aulas")
fig_school_quality = px.box(
    df,
    x="Em que tipo de escola você estudou a maior parte do Ensino médio?",
    y="Avaliação do Curso [Como você avalia a qualidade das aulas no seu Instituto?]",
    title="Tipo de Escola x Qualidade das Aulas",
    labels={
        "Em que tipo de escola você estudou a maior parte do Ensino médio?": "Tipo de Escola",
        "Avaliação do Curso [Como você avalia a qualidade das aulas no seu Instituto?]": "Qualidade das Aulas",
    },
)
st.plotly_chart(fig_school_quality)

# 5. Média das Avaliações do Curso por Tipo de Escola
st.subheader("Média das Avaliações do Curso por Tipo de Escola")
avg_evals_school = df.groupby("Em que tipo de escola você estudou a maior parte do Ensino médio?")[[
    "Avaliação do Curso [Como você avalia a qualidade das aulas no seu Instituto?]",
    "Avaliação do Curso [Como você avalia a infraestrutura física do seu Instituto?]",
    "Avaliação do Curso [Como você avalia o suporte acadêmico oferecido pelas disciplinas?]",
    "Avaliação do Curso [Como você avalia a carga horária e o ritmo do seu curso?]",
    "Avaliação do Curso [O planejamento do seu curso é alinhado com sua futura área de atuação?]",
]].mean()
st.dataframe(avg_evals_school)

# Visualização dos dados agrupados
fig_avg_eval_school = px.bar(
    avg_evals_school.transpose(),
    barmode="group",
    title="Média das Avaliações do Curso por Tipo de Escola",
    labels={"value": "Média da Avaliação", "index": "Perguntas de Avaliação"},
)
st.plotly_chart(fig_avg_eval_school)
