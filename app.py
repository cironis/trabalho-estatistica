import streamlit as st

# --- PAGE SETUP ---
analisar_dados = st.Page(
    "views/analisar_dados.py",
    title="Trabalho de Estatística",
    icon=":material/overview:",
)



# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Visualização": [analisar_dados]
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")

# --- RUN NAVIGATION ---
pg.run()
