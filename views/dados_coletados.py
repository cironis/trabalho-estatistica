
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

st.title("Dados Coletados")

df = load_main_dataframe("base_respostas")

st.markdown(f"## Quantidade de respostas coletadas: {df.shape[0]}")

df['instituto'] = df['Curso Matriculado'].str.split(' - ').str[0]

contagem_de_institutos = df.groupby('instituto').count().sort_values(ascending=False)

st.subheader("Quantidade de respostas por Instituto")
st.dataframe(contagem_de_institutos)

st.markdown("# Tabela com as respostas")
st.dataframe(df)
