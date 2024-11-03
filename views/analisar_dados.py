
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


# Streamlit header
st.title("Survey Data Analysis")

# Age Distribution
st.subheader("1. Age Distribution of Respondents")
fig_age = px.histogram(sample_df, x="Idade", nbins=10, title="Age Distribution of Respondents")
st.plotly_chart(fig_age)

# Evaluation Scores Distribution
st.subheader("2. Distribution of Class Quality Evaluation")
fig_qualidade = px.histogram(sample_df, x="Qualidade das aulas", title="Distribution of Class Quality Evaluation")
st.plotly_chart(fig_qualidade)

# Age by Gender
st.subheader("3. Age by Gender")
fig_age_gender = px.box(sample_df, x="Gênero", y="Idade", title="Age by Gender")
st.plotly_chart(fig_age_gender)

# Box plot of age with evaluation scores for class quality
st.subheader("4. Class Quality Evaluation by Gender")
fig_age_eval = px.box(sample_df, x="Gênero", y="Qualidade das aulas", title="Class Quality Evaluation by Gender")
st.plotly_chart(fig_age_eval)

# Admission Year and Evaluation Score
st.subheader("5. Class Quality Evaluation by Admission Year")
fig_year_eval = px.box(sample_df, x="Ano de ingresso", y="Qualidade das aulas", title="Class Quality Evaluation by Admission Year")
st.plotly_chart(fig_year_eval)

# Admission Year by Institute
st.subheader("6. Year of Admission by Institute")
fig_year_institute = px.histogram(sample_df, x="Ano de ingresso", color="Instituto", title="Year of Admission by Institute")
st.plotly_chart(fig_year_institute)

# Evaluation Scores by Institute
st.subheader("7. Evaluation of Class Quality by Institute")
fig_institute_eval = px.box(sample_df, x="Instituto", y="Qualidade das aulas", title="Evaluation of Class Quality by Institute")
st.plotly_chart(fig_institute_eval)

# Course Type by Institute
st.subheader("8. Course Type Distribution by Institute")
fig_course_institute = px.histogram(sample_df, x="Instituto", color="Curso", title="Course Type Distribution by Institute")
st.plotly_chart(fig_course_institute)

# Course Type and Motivation
st.subheader("9. Motivation by Course Type")
fig_course_motivation = px.box(sample_df, x="Curso", y="Desmotivação por reprovação", title="Motivation by Course Type")
st.plotly_chart(fig_course_motivation)

# Market Preparedness by Course Type
st.subheader("10. Market Preparedness by Course Type")
fig_market_course = px.box(sample_df, x="Curso", y="Preparação para mercado", title="Market Preparedness by Course Type")
st.plotly_chart(fig_market_course)

# Continuity Intent and Evaluation Scores
st.subheader("11. Class Quality Evaluation by Continuity Intent")
fig_continue_quality = px.box(sample_df, x="Continuidade no curso", y="Qualidade das aulas", title="Class Quality Evaluation by Continuity Intent")
st.plotly_chart(fig_continue_quality)

# Continuity Intent by Gender
st.subheader("12. Continuity Intent by Gender")
fig_continue_gender = px.histogram(sample_df, x="Continuidade no curso", color="Gênero", title="Continuity Intent by Gender")
st.plotly_chart(fig_continue_gender)
