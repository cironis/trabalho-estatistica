
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

import os
import streamlit as st

# Define the path to your cloned GitHub repository
repo_path = os.getcwd()  # Current working directory of the Streamlit script

# Walk through the directory and list all files and folders
file_structure = []
for root, dirs, files in os.walk(repo_path):
    for file in files:
        file_structure.append(os.path.join(root, file))

# Display the structure in Streamlit
st.markdown("### Files and Folders in the GitHub Repository")
for file in file_structure:
    st.write(file)

# Data for the group
data = {
    "Foto": ["assets/Bruna.enc",
                "/assets/Ciro.enc",
                "/assets/Enzo.enc",
                "/assets/Gustavo.enc",
                "/assets/Icaro.enc",
                "/assets/Mateus.enc"], 
    "Nome": ["Bruna Hellmeister Bugari",
             "Ciro Nogueirão Shia",
             "Enzo Massato Kuniyoshi",
             "Gustavo Pedro Simplício Correa",
             "Ícaro Maringelli",
             "Mateus Eiji Miyazaki Pelegrina"
             ],
    "Número USP": ["11223041", "5158197", "13689712", "14577107","XXXXXXXXX","14597642"],
}

# Create a DataFrame
df = pd.DataFrame(data)
df["Foto"] = df["Foto"].apply(lambda path: Image.open(path))

# # Display the table with image column configuration
# st.markdown("### Tabela do Grupo")
# st.dataframe(
#     df,
#     column_config={
#         "Foto": st.column_config.ImageColumn("Foto", width="small"),
#     },
#     use_container_width=True,
# )
