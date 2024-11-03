import pandas as pd
import streamlit as st
import random

@st.cache_data
def create_sample_df(sample_size):
    # Sample data for each column based on the description
    data = {
        "Gênero": [random.choice(["Masculino", "Feminino", "Outros", "-"]) for _ in range(sample_size)],
        "Idade": [random.randint(18, 30) for _ in range(sample_size)],
        "Ano de ingresso": [random.choice(["Antes de 2020", "2020", "2021", "2022", "2023", "2024"]) for _ in range(sample_size)],
        "Instituto": [random.choice(["IME", "IF", "-"]) for _ in range(sample_size)],
        "Curso": [random.choice(["Licenciatura", "Bacharelado", "-"]) for _ in range(sample_size)],
        "Quanto tempo você esta na USP": [random.randint(1, 5) for _ in range(sample_size)],
        "Qualidade das aulas": [random.randint(0, 5) for _ in range(sample_size)],
        "Infraestrutura física": [random.randint(0, 5) for _ in range(sample_size)],
        "Suporte acadêmico": [random.randint(0, 5) for _ in range(sample_size)],
        "Carga horária e ritmo": [random.randint(0, 5) for _ in range(sample_size)],
        "Preparação para mercado": [random.randint(0, 5) for _ in range(sample_size)],
        "Desmotivação por reprovação": [random.randint(0, 5) for _ in range(sample_size)],
        "Planejamento do curso": [random.randint(0, 5) for _ in range(sample_size)],
        "Continuidade no curso": [random.choice(["Sim", "Não", "-"]) for _ in range(sample_size)]
    }

    # Create DataFrame
    sample_df = pd.DataFrame(data)

    return sample_df
