import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
from datetime import datetime
from auxiliar import *

st.set_page_config(page_title="Dados coletados", page_icon="🕒", layout="wide")

def load_main_dataframe(worksheet):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet=worksheet)
    return df

st.title("Dados Coletados")

df = load_main_dataframe("base_respostas")
quantitade_de_respostas = df.shape[0]

st.markdown(f"## Quantidade de respostas coletadas: {quantitade_de_respostas}/100")

col_1,col_2 = st.columns(2)

df['Curso Matriculado'] = df['Curso Matriculado'].astype(str)
df['Curso Matriculado'] = df['Curso Matriculado'].fillna('')
df['instituto'] = df['Curso Matriculado'].str.split(' - ').str[0]

contagem_de_institutos = df.groupby(['instituto'])['instituto'].count().sort_values(ascending=False)

st.subheader("Quantidade de respostas por Instituto")

with col_2:
    
    st.dataframe(contagem_de_institutos)

with col_1:
    fig = px.bar(
    x=contagem_de_institutos.index,
    y=contagem_de_institutos.values,
    labels={'x': 'Instituto', 'y': 'Count'},
    title='Count of Institutes'
    )

    fig.update_layout(xaxis_title="Instituto", yaxis_title="Count")
    st.plotly_chart(fig)

st.markdown("# Tabela com as respostas")
st.dataframe(df)
