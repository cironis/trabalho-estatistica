import pandas as pd
import streamlit as st
import random

@st.cache_data
def generate_sample_dataframe(sample_size=100):
    """
    Generates a sample dataframe with random responses based on the defined survey structure.

    Parameters:
        sample_size (int): Number of random responses to generate.

    Returns:
        pd.DataFrame: A dataframe with the generated sample responses.
    """
    # Define the possible responses for each question
    data = {
        "Curso Matriculado": ["Licenciatura", "Bacharelado"],
        "Gênero": ["Masculino", "Feminino", "Outros"],
        "Idade": range(17, 35),
        "Ano de Ingresso": range(2015, 2024),
        "Há quantos anos você está na USP?": range(1, 10),
        "Avaliação do Curso [Como você avalia a qualidade das aulas no seu Instituto?]": range(0, 6),
        "Avaliação do Curso [Como você avalia a infraestrutura física do seu Instituto?]": range(0, 6),
        "Avaliação do Curso [Como você avalia o suporte acadêmico oferecido pelas disciplinas?]": range(0, 6),
        "Avaliação do Curso [Como você avalia a carga horária e o ritmo do seu curso?]": range(0, 6),
        "Avaliação do Curso [Você se sente preparado para o mercado de trabalho?]": range(0, 6),
        "Avaliação do Curso [O índice de reprovação das disciplinas do seu curso é desmotivador?]": range(0, 6),
        "Avaliação do Curso [O planejamento do seu curso é alinhado com sua futura área de atuação?]": range(0, 6),
        "Você pretende continuar no seu curso?": ["Sim", "Não"],
        "Você sente que se identifica com o curso em que está matriculado?": [
            "Sim, me identifico completamente.",
            "Em parte, mas tenho dúvidas.",
            "Não, entrei no curso sem vontade própria ou por pressão.",
        ],
        "O curso tem atendido às suas expectativas desde que você iniciou?": [
            "Sim, está dentro ou acima do esperado.",
            "Em parte, mas há aspectos que me decepcionaram.",
            "Não, estou completamente decepcionado(a).",
        ],
        "Você consegue equilibrar suas responsabilidades acadêmicas com sua vida pessoal?": [
            "Sim, consigo gerenciar bem.",
            "Em parte, mas enfrento algumas dificuldades.",
            "Não, está sendo muito difícil ou impossível conciliar.",
        ],
        "Como você avalia seu desempenho acadêmico em termos de notas e possibilidade de reprovações ou jubilamento?": [
            "Tenho boas notas e estou longe de risco de jubilamento.",
            "Minhas notas são medianas, mas consigo me manter regular.",
            "Estou com dificuldades e em risco de reprovações ou jubilamento.",
        ],
        "O curso tem impactado sua saúde física ou mental de alguma forma?": [
            "Não, consigo manter meu bem-estar físico e mental.",
            "Em parte, sinto leves impactos ocasionais.",
            "Sim, tem afetado minha saúde física e/ou mental de maneira significativa.",
        ],
    }

    # Generate random responses
    dataframe = pd.DataFrame(
        {
            column: [
                random.choice(list(options)) if isinstance(options, range) else random.choice(options)
                for _ in range(sample_size)
            ]
            for column, options in data.items()
        }
    )
    return dataframe
