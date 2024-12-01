
import streamlit as st
from streamlit_gsheets import GSheetsConnection
from scipy.stats import chi2_contingency
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Análise de Independência", page_icon="📊", layout="wide")

st.title("Análise de Independência")

# Load the data
def load_main_dataframe(worksheet):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet=worksheet)
    return df

df = load_main_dataframe("base_respostas")
filtered_df = df[df['Curso Matriculado'] != "Outro"].copy()

# Perform all mappings outside the selector
mappings = {
    "Desempenho Acadêmico": {
        "column": 'Como você avalia seu desempenho acadêmico em termos de notas e possibilidade de reprovações ou jubilamento?',
        "mapping": {
            "Estou com dificuldades e em risco de reprovações ou jubilamento.": "Baixo ou Mediano",
            "Minhas notas são medianas, mas consigo me manter regular.": "Baixo ou Mediano",
            "Tenho boas notas e estou longe de risco de jubilamento.": "Boas Notas"
        }
    },
    "Qualidade das Aulas": {
        "column": 'Avaliação do Curso [Como você avalia a qualidade das aulas no seu Instituto?]',
        "mapping": {0: "Baixa", 1: "Baixa", 2: "Baixa", 3: "Alta", 4: "Alta", 5: "Alta"}
    },
    "Planejamento Alinhado": {
        "column": 'Avaliação do Curso [O planejamento do seu curso é alinhado com sua futura área de atuação?]',
        "mapping": {0: "Desalinhado", 1: "Desalinhado", 2: "Desalinhado", 3: "Alinhado", 4: "Alinhado", 5: "Alinhado"}
    },
    "Preparação para o Mercado": {
        "column": 'Avaliação do Curso [Você se sente preparado para o mercado de trabalho?]',
        "mapping": {0: "Não Preparado", 1: "Não Preparado", 2: "Não Preparado", 3: "Preparado", 4: "Preparado", 5: "Preparado"}
    },
    "Identificação com o Curso": {
        "column": 'Você sente que se identifica com o curso em que está matriculado?',
        "mapping": {
            "Em parte, mas tenho dúvidas.": "Parcial",
            "Sim, me identifico completamente.": "Total"
        }
    },
    "Expectativas Atendidas": {
        "column": 'O curso tem atendido às suas expectativas desde que você iniciou?',
        "mapping": {
            "Não, estou completamente decepcionada.": "Nada ou Parcialmente Atendidas",
            "Em parte, mas há aspectos que me decepcionaram.": "Nada ou Parcialmente Atendidas",
            "Sim, está dentro ou acima do esperado.": "Atendidas"
        }
    },
    "Tipo de Escola": {
        "column": 'Em que tipo de escola você estudou a maior parte do Ensino médio?',
        "mapping": {
            "Mista (alternou entre pública e privada)": "Pública/Mista",
            "Privada": "Privada",
            "Pública": "Pública/Mista"
        }
    }
}

# Apply mappings to create new columns
for key, value in mappings.items():
    filtered_df[key] = filtered_df[value["column"]].map(value["mapping"])

# Define hypotheses
hypotheses = [
    ("Desempenho Acadêmico", "Qualidade das Aulas"),
    ("Planejamento Alinhado", "Preparação para o Mercado"),
    ("Identificação com o Curso", "Expectativas Atendidas"),
    ("Desempenho Acadêmico", "Tipo de Escola"),
]

# Create the summary table
summary_data = []
for hypo in hypotheses:
    contingency_table = pd.crosstab(filtered_df[hypo[0]], filtered_df[hypo[1]])
    chi2, p_value, dof, _ = chi2_contingency(contingency_table, correction=False)
    summary_data.append({"Hipótese": f"{hypo[0]} X {hypo[1]}", "Qui Quadrado": chi2, "p-value": p_value, "Graus de Liberdade": dof})

summary_df = pd.DataFrame(summary_data)

# Display the summary table
st.subheader("Resumo das Hipóteses")
st.dataframe(summary_df, use_container_width=True)

# Graphs for p-value and chi-square comparison
st.subheader("Comparação de Resultados")

fig_pvalue = px.bar(summary_df, x="Hipótese", y="p-value", title="Comparação de p-values", labels={"p-value": "p-value"})
st.plotly_chart(fig_pvalue, use_container_width=True)

fig_chi2 = px.bar(summary_df, x="Hipótese", y="Qui Quadrado", title="Comparação de Qui Quadrado", labels={"Qui Quadrado": "Qui Quadrado"})
st.plotly_chart(fig_chi2, use_container_width=True)

# Selector for detailed analysis
selected_option = st.selectbox(
    "Selecione uma hipótese:",
    summary_df["Hipótese"].tolist()
)

# Detailed Analysis
hypothesis = selected_option.split(" X ")
new_column_1 = hypothesis[0]
new_column_2 = hypothesis[1]

# Contingency table and chi-square test
grouped_contingency_table = pd.crosstab(filtered_df[new_column_1], filtered_df[new_column_2])
chi2, p_value, dof, expected = chi2_contingency(grouped_contingency_table, correction=False)

# Create DataFrames for observed and expected frequencies
expected_df = pd.DataFrame(expected, index=grouped_contingency_table.index, columns=grouped_contingency_table.columns)

# Display detailed analysis
st.title(f"Análise de Independência - {selected_option}")

st.header("Tabela de Frequência Observada")
st.dataframe(grouped_contingency_table, use_container_width=True)

st.header("Frequências Esperadas")
st.dataframe(expected_df, use_container_width=True)

st.header("Resultados do Teste Qui-quadrado")
chi2_results = pd.DataFrame({
    "Métrica": ["Estatística Qui-quadrado", "P-valor", "Graus de Liberdade"],
    "Valor": [chi2, p_value, dof]
})
st.dataframe(chi2_results, use_container_width=True, hide_index=True)
