import streamlit as st

# --- PAGE SETUP ---

home = st.Page(
    "views/home.py",
    title="Introdução",
    icon=":material/overview:",
    default=True,
)


descricao = st.Page(
    "views/descricao.py",
    title="Descrição",
    icon=":material/overview:",
)

analise_independencia = st.Page(
    "views/analise_independencia.py",
    title="Análise de Independência",
    icon=":material/overview:",
)


dados_coletados = st.Page(
    "views/dados_coletados.py",
    title="Dados Coletados",
    icon=":material/overview:"
)

analisar_dados = st.Page(
    "views/analisar_dados.py",
    title="Análise de satisfação",
    icon=":material/overview:",
)

caracteristicas = st.Page(
    "views/caracteristicas.py",
    title="Características da População",
    icon=":material/overview:",
)



# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Visualização": [home,dados_coletados,caracteristicas,analisar_dados,analise_independencia]
    }
)



# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")

# --- RUN NAVIGATION ---
pg.run()
