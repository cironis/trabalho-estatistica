
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

# Apply mappings to create grouped columns
mappings = {
    "Desempenho Acadêmico": {
        "column": "Como você avalia seu desempenho acadêmico em termos de notas e possibilidade de reprovações ou jubilamento?",
        "mapping": {
        "Estou com dificuldades e em risco de reprovações ou jubilamento.": "Baixo ou Mediano",
        "Minhas notas são medianas, mas consigo me manter regular.": "Baixo ou Mediano",
        "Tenho boas notas e estou longe de risco de jubilamento.": "Boas Notas"
        },
    },
    "Qualidade das Aulas": {
        "column": "Avaliação do Curso [Como você avalia a qualidade das aulas no seu Instituto?]",
        "mapping": {0: "Baixa", 1: "Baixa", 2: "Baixa",3: "Alta", 4: "Alta", 5: "Alta"},
    },
    "Planejamento Alinhado": {
        "column": "Avaliação do Curso [O planejamento do seu curso é alinhado com sua futura área de atuação?]",
        "mapping": {0: "Desalinhado",1: "Desalinhado",2: "Desalinhado",3: "Alinhado",4: "Alinhado",5: "Alinhado"
    },
    },
    "Preparação para o Mercado": {
        "column": "Avaliação do Curso [Você se sente preparado para o mercado de trabalho?]",
        "mapping": {0: "Não Preparado", 1: "Não Preparado", 2: "Não Preparado", 3: "Preparado", 4: "Preparado", 5: "Preparado"},
    },
    "Identificação com o Curso": {
        "column": "Você sente que se identifica com o curso em que está matriculado?",
        "mapping": {
            "Em parte, mas tenho dúvidas.": "Parcial",
            "Sim, me identifico completamente.": "Total",
        },
    },
    "Expectativas Atendidas": {
        "column": "O curso tem atendido às suas expectativas desde que você iniciou?",
        "mapping": {
            "Não, estou completamente decepcionada.": "Nada ou Parcialmente Atendidas",
            "Sim, está dentro ou acima do esperado.": "Atendidas",
        },
    },
    "Impacto na Saúde": {
        "column": "O curso tem impactado sua saúde física ou mental de alguma forma?",
        "mapping": {
            "Sim, tem afetado minha saúde física e/ou mental de maneira significativa.": "Impacto Alto ou Mediano",
            "Não, consigo manter meu bem-estar físico e mental.": "Impacto Baixo",
        },
    },
    "Equilíbrio Vida Pessoal": {
        "column": "Você consegue equilibrar suas responsabilidades acadêmicas com sua vida pessoal?",
        "mapping": {
            "Não, está sendo muito difícil ou impossível conciliar.": "Dificuldade alta ou média",
            "Sim, consigo gerenciar bem.": "Pouca dificuldade",
        },
    },
    "Infraestrutura Física": {
        "column": "Avaliação do Curso [Como você avalia a infraestrutura física do seu Instituto?]",
        "mapping": {0: "Insuficiente", 1: "Insuficiente", 2: "Insuficiente", 3: "Adequada", 4: "Adequada", 5: "Adequada"},
    },
    "Suporte Acadêmico": {
        "column": "Avaliação do Curso [Como você avalia o suporte acadêmico oferecido pelas disciplinas?]",
        "mapping": {0: "Insuficiente", 1: "Insuficiente", 2: "Insuficiente", 3: "Adequado", 4: "Adequado", 5: "Adequado"},
    },
    "Tipo de Escola": {
        "column": "Em que tipo de escola você estudou a maior parte do Ensino médio?",
        "mapping": {
            "Mista (alternou entre pública e privada)": "Pública/Mista",
            "Privada": "Privada",
            "Pública": "Pública/Mista",
        },
    },
}

for key, value in mappings.items():
    filtered_df[key] = filtered_df[value["column"]].map(value["mapping"])

# Define hypotheses
hypotheses = [
    ("Desempenho Acadêmico", "Qualidade das Aulas"),
    ("Planejamento Alinhado", "Preparação para o Mercado"),
    ("Identificação com o Curso", "Expectativas Atendidas"),
    ("Impacto na Saúde", "Equilíbrio Vida Pessoal"),
    ("Infraestrutura Física", "Suporte Acadêmico"),
    ("Desempenho Acadêmico", "Tipo de Escola"),
]

# Create the summary table
summary_data = []
for hypo in hypotheses:
    contingency_table = pd.crosstab(filtered_df[hypo[0]], filtered_df[hypo[1]])
    st.write(hypo)
    st.dataframe(contingency_table)
    chi2, p_value, dof, _ = chi2_contingency(contingency_table, correction=False)
    summary_data.append({"Hipótese": f"{hypo[0]} X {hypo[1]}", "Qui Quadrado": chi2, "p-value": p_value, "Graus de Liberdade": dof})

summary_df = pd.DataFrame(summary_data)

# Display the summary table
st.subheader("Resumo das Hipóteses")
st.dataframe(summary_df, use_container_width=True, hide_index=True)

# Graphs for p-value and chi-square comparison
st.subheader("Comparação de Resultados")

fig_pvalue = px.bar(summary_df, x="Hipótese", y="p-value", title="Comparação de p-values", labels={"p-value": "p-value"})
st.plotly_chart(fig_pvalue, use_container_width=True)

fig_chi2 = px.bar(summary_df, x="Hipótese", y="Qui Quadrado", title="Comparação de Qui Quadrado", labels={"Qui Quadrado": "Qui Quadrado"})
st.plotly_chart(fig_chi2, use_container_width=True)
