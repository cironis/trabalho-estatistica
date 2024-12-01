
import streamlit as st
from streamlit_gsheets import GSheetsConnection
from scipy.stats import chi2_contingency
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title="Introdução", page_icon="📊", layout="wide")

st.title("Título Do Trabalho!!!!!!!!")

# Data for the group
data = {
    "Foto": [   
            "https://raw.githubusercontent.com/cironis/trabalho-estatistica/main/images/Bruna.enc",
            "https://raw.githubusercontent.com/cironis/trabalho-estatistica/main/images/Ciro.enc",
            "https://raw.githubusercontent.com/cironis/trabalho-estatistica/main/images/Enzo.webp",
            "https://raw.githubusercontent.com/cironis/trabalho-estatistica/main/images/Gustavo.enc",
            "https://raw.githubusercontent.com/cironis/trabalho-estatistica/main/images/Icaro.enc",
            "https://raw.githubusercontent.com/cironis/trabalho-estatistica/main/images/Mateus.enc"
            ], 
    "Nome": [
            "Bruna Hellmeister Bugari",
             "Ciro Nogueirão Shia",
             "Enzo Massato Kuniyoshi",
             "Gustavo Pedro Simplício Correa",
             "Ícaro Maringelli",
             "Mateus Eiji Miyazaki Pelegrina"
             ],
    "Número USP": [
            "11223041",
            "5158197",
            "13689712",
            "14577107",
            "XXXXXXXXX",
            "14597642"],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the table with image column configuration
st.markdown("### Tabela do Grupo")
st.dataframe(
    df,
    column_config={
        "Foto": st.column_config.ImageColumn("Foto", width="small"),
    },
    use_container_width=True,
)
