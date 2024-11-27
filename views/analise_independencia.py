
import streamlit as st
from streamlit_gsheets import GSheetsConnection
from scipy.stats import chi2_contingency
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Análise de Independência", page_icon="📊", layout="wide")

selected_option = st.selectbox(
    "Selecione uma hipótese:",
    ["Desempenho Acadêmico X Qualidade das Aulas"]
)


def load_main_dataframe(worksheet):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet=worksheet)
    return df

df = load_main_dataframe("base_respostas")
filtered_df = df[df['Curso Matriculado'] != "Outro"].copy()

if selected_option == "Desempenho Acadêmico X Qualidade das Aulas":

    # Passo 2: Definir as colunas para análise
    column1 = 'Como você avalia seu desempenho acadêmico em termos de notas e possibilidade de reprovações ou jubilamento?'
    column2 = 'Avaliação do Curso [Como você avalia a qualidade das aulas no seu Instituto?]'

    new_column_1 = 'Desempenho Acadêmico'
    new_column_2 = 'Qualidade das Aulas'

    # Passo 3: Agrupar valores para "Desempenho Acadêmico"
    performance_mapping = {
        "Estou com dificuldades e em risco de reprovações ou jubilamento.": "Baixo ou Mediano",
        "Minhas notas são medianas, mas consigo me manter regular.": "Baixo ou Mediano",
        "Tenho boas notas e estou longe de risco de jubilamento.": "Boas Notas"
    }
    filtered_df["Desempenho Acadêmico"] = filtered_df[column1].map(performance_mapping)
    
    explanation = """
                ### Redução de Categorias
                - **Desempenho Acadêmico**:
                - As categorias originais, que descrevem o desempenho individual dos alunos, foram agrupadas para simplificar a análise:
                    - **"Baixo ou Mediano"**: Inclui respostas relacionadas a dificuldades ou desempenho mediano.
                    - **"Boas Notas"**: Refere-se a alunos com bom desempenho e sem risco de jubilamento.

                - **Qualidade das Aulas**:
                - As avaliações numéricas de 0 a 5 foram mapeadas em grupos mais amplos:
                    - **"Baixa"**: Avaliações de 0 a 2, indicando uma percepção negativa.
                    - **"Alta"**: Avaliações de 3 a 5, indicando uma percepção positiva.
                """

    # Passo 4: Agrupar valores para "Qualidade das Aulas"
    quality_mapping = {0: "Baixa", 1: "Baixa", 2: "Baixa",
                    3: "Alta", 4: "Alta", 5: "Alta"}
    filtered_df["Qualidade das Aulas"] = filtered_df[column2].map(quality_mapping)

# Passo 5: Criar a tabela de contingência agrupada
grouped_contingency_table = pd.crosstab(filtered_df[new_column_1], filtered_df[new_column_2])

# Passo 6: Realizar o teste qui-quadrado
chi2, p_value, dof, expected = chi2_contingency(grouped_contingency_table)

# Passo 7: Criar DataFrames com os resultados
chi2_results = pd.DataFrame({
    "Métrica": ["Estatística Qui-quadrado", "P-valor", "Graus de Liberdade"],
    "Valor": [chi2, p_value, dof]
})
expected_df = pd.DataFrame(expected, 
                           index=grouped_contingency_table.index, 
                           columns=grouped_contingency_table.columns)


# Interface no Streamlit
st.title(f"Análise de Independência - {selected_option}")

st.write(explanation)

# Exibir DataFrames
st.header("Tabela de Frequência Observada")
st.dataframe(grouped_contingency_table, use_container_width=True)

st.header("Frequências Esperadas")
st.dataframe(expected_df, use_container_width=True)

st.header("Resultados do Teste Qui-quadrado")
st.dataframe(chi2_results, use_container_width=True)
