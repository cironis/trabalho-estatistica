
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
        "Foto": st.column_config.ImageColumn("Foto", width="large"),
    },
    use_container_width=True,hide_index=True
)


st.markdown("""
# Resumo:

## Introdução
- **Motivação**: Baseado em artigo da USP sobre evasão na graduação (taxas de 0% a 54%), destacando desafios em cursos de exatas.
- **Objetivo**: Investigar níveis de satisfação dos alunos e propor políticas para reduzir a evasão.

---

## População Estudada
- **Institutos**: IME, IF, IAG.
- **Amostra Válida**: 55 respostas:
  - IME: 32 alunos.
  - IF: 16 alunos.
  - IAG: 8 alunos.

---

## Coleta de Dados
### Metodologias
1. Pesquisas presenciais em corredores (após as aulas).
2. Formulário no Google Forms distribuído em grupos de WhatsApp.

### Observações
- **Metodologia 1**:
  - Mais precisa.
  - Limitada em alcance e mais lenta.
- **Metodologia 2**:
  - Rápida.
  - Maior quantidade de dados, mas menor aleatoriedade.

---

## Estrutura do Questionário
1. **Perfil do Aluno**: Curso, idade, gênero, tipo de escola, etc.
2. **Avaliação do Curso**:
   - Notas de 0 (insatisfação) a 5 (satisfação).
   - Aspectos avaliados: infraestrutura, qualidade das aulas, entre outros.
3. **Permanência**:
   - Intenção de continuar no curso.
   - Impactos na saúde física/mental.
   - Equilíbrio entre vida acadêmica e pessoal.

---

## Análises Inferenciais
### Método
- Teste Qui-Quadrado para verificar relações de independência.

### Hipóteses Testadas
1. **Desempenho ↔ Qualidade das Aulas**:
   - Resultados: Independentes.
2. **Coerência Curricular ↔ Preparação Profissional**:
   - Resultados: Dependentes.
3. **Identificação com o Curso ↔ Expectativas**:
   - Resultados: Dependentes.
4. **Impacto na Saúde ↔ Equilíbrio Vida-Acadêmico**:
   - Resultados: Dados insuficientes.
5. **Desempenho ↔ Tipo de Escola (Pública/Privada)**:
   - Resultados: Dependentes.

---

## Resultados Principais
- **Qualidade das Aulas**: Não afeta diretamente o desempenho acadêmico.
- **Coerência Curricular**: Ligada à percepção de preparação profissional.
- **Impactos na Saúde**: Dados insuficientes para análises conclusivas, mas desafios foram identificados.
- **Tipo de Escola**: Alunos de escolas privadas tiveram melhor desempenho acadêmico.

---

## Conclusão
- Recomendações:
  - Melhorar a coerência curricular.
  - Oferecer suporte à saúde mental.
  - Implementar políticas que aumentem a satisfação e retenção dos alunos.

""")
