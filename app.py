import streamlit as st

# Inicializa o estado da sessão
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'respostas' not in st.session_state:
    st.session_state.respostas = {}

# Função para avançar de etapa
def proxima_pagina():
    st.session_state.step += 1

st.set_page_config(page_title="Round 6 - Gabrielle", page_icon="🎮")
st.title("🟥 Round 6: Desafios Iniciados 🟥")

# ========== Etapa 1: Boas-vindas ==========
if st.session_state.step == 1:
    st.markdown("""
    ## Bem-vinda, Gabrielle.

    Você foi selecionada para participar de uma sequência de desafios nada convencionais.

    Hoje não é um dia comum. É o seu aniversário... mas aqui, isso não significa bolo e balões.

    Inspirado em Round 6, você enfrentará provas de percepção, lógica e coragem. Cada fase representa uma parte da sua jornada até aqui — suas vitórias, aprendizados e brincadeiras favoritas.

    Siga as instruções com atenção. Errar pode ter consequências... ou não. Só há um jeito de descobrir.

    Que os jogos comecem. 🎂🟥
    """)

    st.button("Avançar para o primeiro desafio", on_click=proxima_pagina)

# ========== Etapa 2: Desafio "Parado ou Dançou" ==========
elif st.session_state.step == 2:
    st.header("Desafio 1: Parado ou Dançou 🎶")

    # Toca o áudio do vídeo tema (salvo localmente)
    try:
        audio_file = open("batatinha_audio.mp3", "rb")
        st.audio(audio_file.read(), format='audio/mp3')
    except FileNotFoundError:
        st.warning("⚠️ Áudio não encontrado. Verifique o caminho do arquivo.")

    st.write("Responda com VERDADEIRO ou FALSO. Acerte para não ser eliminada!")

    perguntas = {
        "Gabrielle já dormiu no cinema.": True,
        "Gabrielle odeia chocolate.": False,
        "Gabrielle já cantou em público.": True
    }

    todas_respondidas = True
    acertos = 0

    for pergunta, gabarito in perguntas.items():
        resposta = st.radio(pergunta, ["Verdadeiro", "Falso"], key=pergunta)
        st.session_state.respostas[pergunta] = resposta

    if st.button("Confirmar respostas"):
        for pergunta, gabarito in perguntas.items():
            resposta_usuario = st.session_state.respostas.get(pergunta)
            if resposta_usuario:
                if resposta_usuario == ("Verdadeiro" if gabarito else "Falso"):
                    acertos += 1
        st.session_state.score += acertos
        proxima_pagina()

# Próximas etapas ainda serão implementadas.
