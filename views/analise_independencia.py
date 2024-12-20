
import streamlit as st
from streamlit_gsheets import GSheetsConnection
from scipy.stats import chi2_contingency
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Análise de Independência", page_icon="📊", layout="wide")

st.title("Análise de Independêcia")

selected_option = st.selectbox(
    "Selecione uma hipótese:",
    ["Desempenho Acadêmico X Qualidade das Aulas",
     "Planejamento Alinhado X Preparação para o Mercados",
     "Identificação com o Curso X Expectativas Atendidas",
     "Impacto na Saúde X Equilíbrio entre vida pessoal e acadêmica",
     "Infraestrutura Física X Suporte Acadêmico",
     "Desempenho Acadêmico X Tipo de Escola"
     ]
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

elif selected_option == "Planejamento Alinhado X Preparação para o Mercados":

    # Step 2: Define the columns to analyze
    column1 = 'Avaliação do Curso [O planejamento do seu curso é alinhado com sua futura área de atuação?]'
    column2 = 'Avaliação do Curso [Você se sente preparado para o mercado de trabalho?]'

    # Passo 2: Definir as colunas para análise
    column1 = 'Avaliação do Curso [O planejamento do seu curso é alinhado com sua futura área de atuação?]'
    column2 = 'Avaliação do Curso [Você se sente preparado para o mercado de trabalho?]'

    new_column_1 = 'Planejamento Alinhado'
    new_column_2 = 'Preparação para o Mercado'

    # Passo 3: Agrupar valores para "Planejamento Alinhado"
    planning_mapping = {
        0: "Desalinhado",
        1: "Desalinhado",
        2: "Desalinhado",
        3: "Alinhado",
        4: "Alinhado",
        5: "Alinhado"
    }
    filtered_df[new_column_1] = filtered_df[column1].map(planning_mapping)

    # Passo 4: Agrupar valores para "Preparação para o Mercado"
    market_mapping = {
        0: "Não Preparado",
        1: "Não Preparado",
        2: "Não Preparado",
        3: "Preparado",
        4: "Preparado",
        5: "Preparado"
    }
    filtered_df[new_column_2] = filtered_df[column2].map(market_mapping)

    explanation = """
                ### Redução de Categorias
                - **Planejamento Alinhado**:
                - As avaliações de 0 a 5 foram agrupadas em duas categorias:
                    - **"Desalinhado"**: Inclui as avaliações 0, 1 e 2, indicando percepção negativa de alinhamento.
                    - **"Alinhado"**: Inclui as avaliações 3, 4 e 5, indicando percepção positiva de alinhamento.

                - **Preparação para o Mercado**:
                - As avaliações de 0 a 5 foram agrupadas em duas categorias:
                    - **"Não Preparado"**: Inclui as avaliações 0, 1 e 2, indicando percepção negativa de preparo.
                    - **"Preparado"**: Inclui as avaliações 3, 4 e 5, indicando percepção positiva de preparo.
                """

elif selected_option == "Identificação com o Curso X Expectativas Atendidas":

    # Passo 2: Definir as colunas para análise
    column1 = 'Você sente que se identifica com o curso em que está matriculado?'
    column2 = 'O curso tem atendido às suas expectativas desde que você iniciou?'

    new_column_1 = 'Identificação com o Curso'
    new_column_2 = 'Expectativas Atendidas'

    # Passo 3: Agrupar valores para "Identificação com o Curso"
    identification_mapping = {
        "Em parte, mas tenho dúvidas.": "Parcial",
        "Sim, me identifico completamente.": "Total"
    }
    filtered_df[new_column_1] = filtered_df[column1].map(identification_mapping)

    # Passo 4: Agrupar valores para "Expectativas Atendidas"
    expectation_mapping = {
        "Não, estou completamente decepcionada.": "Nada ou Parcialmente Atendidas",
        "Em parte, mas há aspectos que me decepcionaram.": "Nada ou Parcialmente Atendidas",
        "Sim, está dentro ou acima do esperado.": "Atendidas"
    }
    filtered_df[new_column_2] = filtered_df[column2].map(expectation_mapping)

    explanation = """
    ### Redução de Categorias
    - **Identificação com o Curso**:
    - As respostas originais foram agrupadas em duas categorias:
        - **"Parcial"**: Inclui respostas como "Em parte, mas tenho dúvidas.".
        - **"Total"**: Representa alunos que disseram "Sim, me identifico completamente.".

    - **Expectativas Atendidas**:
    - As respostas originais foram agrupadas em duas categorias:
        - **"Nada ou Parcialmente Atendidas"**: Inclui "Não, estou completamente decepcionada." e "Em parte, mas há aspectos que me decepcionaram.".
        - **"Atendidas"**: Representa "Sim, está dentro ou acima do esperado.".
    """

    # Step 5: Create the grouped contingency table
    grouped_contingency_table = pd.crosstab(filtered_df[new_column_1], filtered_df[new_column_2])

elif selected_option == "Impacto na Saúde X Equilíbrio entre vida pessoal e acadêmica":
    # Passo 2: Definir as colunas para análise
    column1 = 'O curso tem impactado sua saúde física ou mental de alguma forma?'
    column2 = 'Você consegue equilibrar suas responsabilidades acadêmicas com sua vida pessoal?'

    new_column_1 = 'Impacto na saúde Saúde Mental'
    new_column_2 = 'Equilíbrio entre vida pessoal e acadêmica'

    saude_mapping = {
            "Sim, tem afetado minha saúde física e/ou mental de maneira significativa.": "Impacto Alto ou Mediano",
            "Em parte, sinto leves impactos ocasionais.": "Impacto Alto ou Mediano",
            "Não, consigo manter meu bem-estar físico e mental.": "Impacto Baixo"
        }
    filtered_df[new_column_1] = filtered_df[column1].map(saude_mapping)

    vida_pessoal_mapping = {
        "Não, está sendo muito difícil ou impossível conciliar.": "Dificuldade alta ou média",
        "Em parte, mas enfrento algumas dificuldades.": "Dificuldade alta ou média",
        "Sim, consigo gerenciar bem.": "Pouca dificuldade"
    }
    filtered_df[new_column_2] = filtered_df[column2].map(vida_pessoal_mapping)

    explanation = """
    ### Redução de Categorias
    - **Impacto na Saúde**:
    - As respostas originais foram agrupadas em duas categorias:
        - **"Impacto Alto ou Mediano"**: Inclui "Sim, tem afetado minha saúde física e/ou mental de maneira significativa." e "Em parte, sinto leves impactos ocasionais.".
        - **"Impacto Baixo"**: Representa "Não, consigo manter meu bem-estar físico e mental.".

    - **Dificuldade de Conciliar com a Vida Pessoal**:
    - As respostas originais foram agrupadas em duas categorias:
        - **"Dificuldade alta ou média"**: Inclui "Não, está sendo muito difícil ou impossível conciliar." e "Em parte, mas enfrento algumas dificuldades.".
        - **"Pouca dificuldade"**: Representa "Sim, consigo gerenciar bem.".
    """


elif selected_option == "Infraestrutura Física X Suporte Acadêmico":
    # Passo 2: Definir as colunas para análise
    column1 = 'Avaliação do Curso [Como você avalia a infraestrutura física do seu Instituto?]'
    column2 = 'Avaliação do Curso [Como você avalia o suporte acadêmico oferecido pelas disciplinas?]'

    new_column_1 = 'Infraestrutura Física'
    new_column_2 = 'Suporte Acadêmico'

    # Passo 3: Agrupar valores para "Infraestrutura Física"
    infrastructure_mapping = {
        0: "Insuficiente",
        1: "Insuficiente",
        2: "Insuficiente",
        3: "Adequada",
        4: "Adequada",
        5: "Adequada"
    }
    filtered_df[new_column_1] = filtered_df[column1].map(infrastructure_mapping)

    # Passo 4: Agrupar valores para "Suporte Acadêmico"
    academic_support_mapping = {
        0: "Insuficiente",
        1: "Insuficiente",
        2: "Insuficiente",
        3: "Adequado",
        4: "Adequado",
        5: "Adequado"
    }
    filtered_df[new_column_2] = filtered_df[column2].map(academic_support_mapping)

    explanation = """
    ### Redução de Categorias
    - **Infraestrutura Física**:
    - As avaliações de 0 a 5 foram agrupadas em duas categorias:
        - **"Insuficiente"**: Inclui as avaliações 0, 1 e 2, indicando infraestrutura inadequada.
        - **"Adequada"**: Inclui as avaliações 3, 4 e 5, indicando infraestrutura satisfatória.

    - **Suporte Acadêmico**:
    - As avaliações de 0 a 5 foram agrupadas em duas categorias:
        - **"Insuficiente"**: Inclui as avaliações 0, 1 e 2, indicando suporte inadequado.
        - **"Adequado"**: Inclui as avaliações 3, 4 e 5, indicando suporte satisfatório.
    """

elif selected_option == "Desempenho Acadêmico X Tipo de Escola":
    # Passo 2: Definir as colunas para análise
    column1 = 'Como você avalia seu desempenho acadêmico em termos de notas e possibilidade de reprovações ou jubilamento?'
    column2 = 'Em que tipo de escola você estudou a maior parte do Ensino médio?'

    new_column_1 = 'Desempenho Acadêmico'
    new_column_2 = 'Tipo de Escola'

    # Passo 3: Agrupar valores para "Desempenho Acadêmico"
    performance_mapping = {
            "Estou com dificuldades e em risco de reprovações ou jubilamento.": "Baixo ou Mediano",
            "Minhas notas são medianas, mas consigo me manter regular.": "Baixo ou Mediano",
            "Tenho boas notas e estou longe de risco de jubilamento.": "Boas Notas"
        }
    filtered_df[new_column_1] = filtered_df[column1].map(performance_mapping)

    # Passo 4: Agrupar valores para "Tipo de Escola"
    school_type_mapping = {
        "Mista (alternou entre pública e privada)": "Pública/Mista",
        "Privada": "Privada",
        "Pública": "Pública/Mista"
    }
    filtered_df[new_column_2] = filtered_df[column2].map(school_type_mapping)

    explanation = """
    ### Redução de Categorias
    - **Desempenho Acadêmico**:
    - As respostas originais foram agrupadas em duas categorias:
        - **"Baixo ou Mediano"**: Inclui "Estou com dificuldades e em risco de reprovações ou jubilamento." e "Minhas notas são medianas, mas consigo me manter regular.".
        - **"Boas Notas"**: Representa "Tenho boas notas e estou longe de risco de jubilamento.".

    - **Tipo de Escola**:
    - As respostas originais foram agrupadas em duas categorias:
        - **"Pública/Mista"**: Inclui "Pública" e "Mista (alternou entre pública e privada).".
        - **"Privada"**: Representa "Privada".
    """


# Passo 5: Criar a tabela de contingência agrupada
grouped_contingency_table = pd.crosstab(filtered_df[new_column_1], filtered_df[new_column_2])

# Passo 6: Realizar o teste qui-quadrado
chi2, p_value, dof, expected = chi2_contingency(grouped_contingency_table, correction=False)

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
st.dataframe(chi2_results, use_container_width=True,hide_index=True)
