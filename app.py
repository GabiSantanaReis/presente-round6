import streamlit as st
import time
import random

# Inicializa o estado da sessão
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'respostas' not in st.session_state:
    st.session_state.respostas = {}
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

# Função para avançar de etapa
def proxima_pagina():
    st.session_state.step += 1

st.set_page_config(page_title="Round 6 - Gabrielle", page_icon="🎮")

# ========== Etapa 1: Boas-vindas ==========
if st.session_state.step == 1:
    st.title("🟥 Round 6: Desafios Iniciados 🟥")

    st.markdown("""
    ## Bem-vinda, Palhaça.

    Você foi selecionada para participar de uma sequência de desafios nada convencionais.

    Hoje não é um dia comum. É o seu aniversário. Na verdade, já passou, desculpe o atraso, mas montar isso foi complicado kkkk

    Inspirado em Round 6, você enfrentará provas de percepção, lógica e coragem.

    Siga as instruções com atenção. Errar pode ter consequências... ou não. Só há um jeito de descobrir.

    Que os jogos comecem. 
    ● ▲ ■            

    """)

    st.button("Avançar para o primeiro desafio", on_click=proxima_pagina)

# ========== Etapa 2: Desafio 1 ==========
elif st.session_state.step == 2:
    st.header("Desafio 1: Parado ou Dançou 🎶")

    # Inicializa timer na primeira visita
    if st.session_state.start_time is None:
        st.session_state.start_time = time.time()
        st.session_state.finished = False  # Marca se já terminou o desafio
        st.session_state.acertou_tudo = False  # Resultado do desafio

    # Calcula tempo restante
    tempo_passado = time.time() - st.session_state.start_time
    tempo_restante = int(30 - tempo_passado)

    # Mostra o áudio
    audio_file_path = "batatinha_audio.mp3"
    audio_html = f'''
    <audio autoplay>
      <source src="{audio_file_path}" type="audio/mp3">
      Seu navegador não suporta o elemento de áudio.
    </audio>
    '''
    st.markdown(audio_html, unsafe_allow_html=True)

    try:
        audio_file = open("batatinha_audio.mp3", "rb")
        st.audio(audio_file.read(), format='audio/mp3')
    except FileNotFoundError:
        st.warning("⚠️ Áudio não encontrado. Verifique o caminho do arquivo.")

    st.write("Responda com VERDADEIRO ou FALSO. Acerte todas para não ser eliminada!")

    perguntas = {
        "Gabrielle já dormiu no cinema.": False,
        "Gabrielle odeia chocolate meio amargo.": True,
        "Gabrielle tem 5 pets.": True
    }

    # Exibe as perguntas com radio buttons
    for pergunta in perguntas:
        st.radio(pergunta, ["Verdadeiro", "Falso"], key=pergunta)

    if not st.session_state.finished:
        if st.button("Confirmar respostas"):

            # Verifica se acertou todas as respostas
            acertou_tudo = True
            for pergunta, gabarito in perguntas.items():
                resposta_usuario = st.session_state.get(pergunta)
                correta = "Verdadeiro" if gabarito else "Falso"
                if resposta_usuario != correta:
                    acertou_tudo = False
                    break

            st.session_state.finished = True
            st.session_state.acertou_tudo = acertou_tudo

            if acertou_tudo:
                st.session_state.score += len(perguntas)

            st.rerun()

    else:
        # Se já terminou, mostra resultado final
        if st.session_state.acertou_tudo:
            st.success("🎉 Parabéns! Você acertou todas as respostas!")
            st.balloons()
            if st.button("Avançar para o próximo desafio"):
                st.session_state.step += 1
                st.session_state.start_time = None
                st.session_state.finished = False
                st.rerun()
        else:
            st.error("💀 Você perdeu! Respostas incorretas ou tempo esgotado.")
            if st.button("Tentar de novo"):
                # Reseta tudo para recomeçar
                st.session_state.step = 1
                st.session_state.start_time = None
                st.session_state.finished = False
                for pergunta in perguntas:
                    if pergunta in st.session_state:
                        del st.session_state[pergunta]
                st.rerun()

    # Controle do timer: só mostra e atualiza se ainda não terminou e tem tempo
    if not st.session_state.finished:
        if tempo_restante <= 0:
            st.session_state.finished = True
            st.session_state.acertou_tudo = False
            st.rerun()
        else:
            st.markdown(f"### ⏳ Tempo restante: {tempo_restante} segundos")
            time.sleep(1)
            st.rerun()

# ========== Etapa 3: Jogo da Memória ==========
elif st.session_state.step == 3:

    # Inicialização das variáveis da fase 3 (jogo da memória)
    if 'cards' not in st.session_state:
        cartas = ['🐍', '🐍', '🐢', '🐢', '🐸', '🐸', '🐰', '🐰']
        random.shuffle(cartas)
        st.session_state.cards = cartas
        st.session_state.revealed = [False] * len(cartas)
        st.session_state.first_choice = None
        st.session_state.second_choice = None
        st.session_state.pairs_found = 0
        st.session_state.message = ""

    def reset_memory_game():
        cartas = ['🐍', '🐍', '🐢', '🐢', '🐸', '🐸', '🐰', '🐰']
        random.shuffle(cartas)
        st.session_state.cards = cartas
        st.session_state.revealed = [False] * len(cartas)
        st.session_state.first_choice = None
        st.session_state.second_choice = None
        st.session_state.pairs_found = 0
        st.session_state.message = ""
        # Força a atualização da página
        st.query_params = {"refresh": str(int(time.time()))}


    st.title("🧠 Desafio 2 – Jogo da Memória - Round 6")
    st.markdown("""
    Clique duas vezes em cada carta para que a imagem apareça, caso o par esteja errado, tente novamente!

    """)

    cols = st.columns(4)

    # Mostrar as cartas
    for i in range(len(st.session_state.cards)):
        with cols[i % 4]:
            if st.session_state.revealed[i] or i == st.session_state.first_choice or i == st.session_state.second_choice:
                st.button(st.session_state.cards[i], key=f"card_{i}", disabled=True)
            else:
                if st.button("❓", key=f"card_{i}"):
                    if st.session_state.first_choice is None:
                        st.session_state.first_choice = i
                    elif st.session_state.second_choice is None and i != st.session_state.first_choice:
                        st.session_state.second_choice = i

    # Verificar escolha de pares
    if st.session_state.first_choice is not None and st.session_state.second_choice is not None:
        first_idx = st.session_state.first_choice
        second_idx = st.session_state.second_choice

        if st.session_state.cards[first_idx] == st.session_state.cards[second_idx]:
            st.session_state.revealed[first_idx] = True
            st.session_state.revealed[second_idx] = True
            st.session_state.pairs_found += 1
            st.session_state.message = "Par encontrado! 🎉"
        else:
            st.session_state.message = "Não é par, tente novamente. ❌"

        # Pequena pausa para o usuário ver o resultado (opcional)
        time.sleep(1)

        # Resetar escolhas para a próxima tentativa
        st.session_state.first_choice = None
        st.session_state.second_choice = None
        st.query_params = {"refresh": str(int(time.time()))}


    st.write(st.session_state.message)

    # Vitória e opção para avançar para próxima fase
    if st.session_state.pairs_found == len(st.session_state.cards) :
        st.balloons()
        st.success("Você encontrou todos os pares! Parabéns! 🎊")
        if st.button("Avançar para a próxima fase"):
            # Limpar as variáveis da fase 3 para evitar conflito
            for key in ['cards', 'revealed', 'first_choice', 'second_choice', 'pairs_found', 'message']:
                if key in st.session_state:
                    del st.session_state[key]
            # Avançar etapa do seu jogo maior
            if 'step' in st.session_state:
                st.session_state.step += 1
            else:
                st.session_state.step = 4
            st.query_params = {"refresh": str(int(time.time()))}


elif st.session_state.step == 4:
    st.title("🎲 Desafio 3: Adivinhe o Número")

    if 'target_number' not in st.session_state:
        st.session_state.target_number = random.randint(1, 20)
        st.session_state.guesses_left = 5
        st.session_state.message = ""
        st.session_state.acertou_numero = False
        st.session_state.perdeu_numero = False

    # Jogo em andamento
    if not st.session_state.acertou_numero and not st.session_state.perdeu_numero:
        st.write("Estou pensando em um número entre 1 e 20. Tente adivinhar!")
        guess = st.number_input("Digite seu palpite:", min_value=1, max_value=20, step=1, key='palpite_numero')

        if st.button("Enviar palpite"):
            if guess == st.session_state.target_number:
                st.success(f"🎉 Parabéns! Você acertou o número {st.session_state.target_number}!")
                st.session_state.acertou_numero = True
            else:
                st.session_state.guesses_left -= 1
                if guess < st.session_state.target_number:
                    st.session_state.message = "Muito baixo! Tente um número maior."
                else:
                    st.session_state.message = "Muito alto! Tente um número menor."

                if st.session_state.guesses_left == 0:
                    st.session_state.perdeu_numero = True
                    st.error(f"💀 Você perdeu! O número era {st.session_state.target_number}.")

        st.write(f"Tentativas restantes: {st.session_state.guesses_left}")
        st.write(st.session_state.message)

    # Acertou
    if st.session_state.acertou_numero:
        st.balloons()
        if st.button("Avançar para a próxima etapa"):
            # Reseta as variáveis do jogo imediatamente e muda a etapa
            for key in ['target_number', 'guesses_left', 'message', 'acertou_numero', 'perdeu_numero', 'palpite_numero']:
                st.session_state.pop(key, None)
            st.session_state.step += 1
            st.rerun()

    # Perdeu
    elif st.session_state.perdeu_numero:
        if st.button("Voltar para o início"):
            for key in ['target_number', 'guesses_left', 'message', 'acertou_numero', 'perdeu_numero', 'palpite_numero']:
                st.session_state.pop(key, None)
            st.session_state.step = 1
            st.rerun()



if st.session_state.step == 5:

    st.title("🎁 Desafio 4: Caixa Misteriosa 🎲")

    if 'boxes' not in st.session_state:
        caixas = [True, False, False]
        random.shuffle(caixas)
        st.session_state.boxes = caixas
        st.session_state.opened = [False, False, False]
        st.session_state.score = 0
        st.session_state.game_over = False
        st.session_state.message = "Escolha uma caixa para abrir."

    def reset_game():
        caixas = [True, False, False]
        random.shuffle(caixas)
        st.session_state.boxes = caixas
        st.session_state.opened = [False, False, False]
        st.session_state.score = 0
        st.session_state.game_over = False
        st.session_state.message = "Escolha uma caixa para abrir."

    st.write(st.session_state.message)

    cols = st.columns(3)

    for i in range(3):
        with cols[i]:
            if st.session_state.opened[i]:
                if st.session_state.boxes[i]:
                    st.success("🎉 Prêmio! 🎉")
                else:
                    st.error("💥 Armadilha! Você perdeu tudo! 💥")
            else:
                if not st.session_state.game_over:
                    if st.button(f"Abrir Caixa {i+1}", key=f"box_{i}"):
                        st.session_state.opened[i] = True
                        if st.session_state.boxes[i]:
                            st.session_state.score += 10
                            st.session_state.message = f"🎉 Você encontrou o prêmio na caixa {i+1}! Pontos: {st.session_state.score}. Pode abrir outra caixa ou avançar."
                        else:
                            st.session_state.game_over = True
                            st.session_state.message = f"💥 Armadilha na caixa {i+1}! Você perdeu tudo! Voltando ao início..."
                        st.rerun()
                else:
                    st.button(f"Caixa {i+1}", disabled=True)

    st.write(f"Pontuação atual: {st.session_state.score}")

    if st.session_state.game_over:
        # Voltar para o início
        if st.button("Voltar ao início"):
            st.session_state.step = 1
            for key in ['boxes', 'opened', 'score', 'game_over', 'message']:
                st.session_state.pop(key, None)
            st.rerun()
    else:
        # Pode abrir todas caixas ou avançar
        if all(st.session_state.opened):
            st.success(f"🎉 Parabéns! Você abriu todas as caixas e terminou com {st.session_state.score} pontos!")
            if st.button("Avançar para a próxima fase"):
                # Limpar e avançar
                for key in ['boxes', 'opened', 'score', 'game_over', 'message']:
                    st.session_state.pop(key, None)
                st.session_state.step += 1
                st.rerun()
        else:
            if st.button("Parar e garantir pontos (avançar)"):
                for key in ['boxes', 'opened', 'score', 'game_over', 'message']:
                    st.session_state.pop(key, None)
                st.session_state.step += 1
                st.rerun()

if st.session_state.step == 6:
    st.title("🎯 Desafio 5: Selecione as Caixas Premiadas")

    if 'boxes6' not in st.session_state:
        total_caixas = 15
        
        #aqui o indice ta um pra frente, depois da pra trocar o tema tbm, de caixa pra alguma coisa q ela tenha que selecionar certo
        premiadas_indices = [1, 4, 8, 11, 13]  # exemplo: caixas 2,5,9,12,14

        caixas = [False] * total_caixas
        for i in premiadas_indices:
            caixas[i] = True

        

        st.session_state.boxes6 = caixas
        st.session_state.selected_boxes = [False] * total_caixas
        st.session_state.finished6 = False
        st.session_state.result6 = None
        st.session_state.message6 = "Selecione apenas as caixas premiadas e confirme."

    st.write(st.session_state.message6)

    total_caixas = len(st.session_state.boxes6)
    cols = st.columns(5)  # 5 colunas

    # Para organizar 15 caixas em 3 linhas x 5 colunas
    for row in range(3):
        for col_idx in range(5):
            idx = row * 5 + col_idx
            with cols[col_idx]:
                label = f"Caixa {idx+1}"
                # Usar key única para cada checkbox
                st.session_state.selected_boxes[idx] = st.checkbox(label, key=f"box6_{idx}", value=st.session_state.selected_boxes[idx])

    if not st.session_state.finished6:
        if st.button("Confirmar escolhas"):
            selecionou = st.session_state.selected_boxes
            caixas = st.session_state.boxes6

            acertou = all((selecionou[i] == caixas[i]) for i in range(total_caixas))

            st.session_state.finished6 = True
            st.session_state.result6 = acertou
            if acertou:
                st.session_state.message6 = "🎉 Parabéns! Você acertou todas as caixas premiadas!"
            else:
                st.session_state.message6 = "❌ Errou! Seleção incorreta."

            st.rerun()

    else:
        if st.session_state.result6:
            st.success(st.session_state.message6)
            if st.button("Avançar para a próxima fase"):
                for key in ['boxes6', 'selected_boxes', 'finished6', 'result6', 'message6']:
                    st.session_state.pop(key, None)
                st.session_state.step += 1
                st.rerun()
        else:
            st.error(st.session_state.message6)
            if st.button("Voltar ao início"):
                for key in ['boxes6', 'selected_boxes', 'finished6', 'result6', 'message6']:
                    st.session_state.pop(key, None)
                st.session_state.step = 1
                st.rerun()

if st.session_state.step == 7:
    st.title("🎨 Desafio 6: Jogo da Lógica das Cores")

    if 'color_sequence' not in st.session_state:
        cores_possiveis = ['🔴', '🔵', '🟢', '🟡']
        st.session_state.color_sequence = [random.choice(cores_possiveis) for _ in range(5)]
        st.session_state.start_time = time.time()
        st.session_state.show_sequence = True
        st.session_state.user_sequence = []
        st.session_state.finished = False
        st.session_state.result = None

    tempo_passado = time.time() - st.session_state.start_time
    tempo_limite = 5  # segundos para mostrar sequência

    if st.session_state.show_sequence:
        st.write("Memorize a sequência de cores:")
        st.markdown(" ".join(st.session_state.color_sequence), unsafe_allow_html=True)
        tempo_restante = int(tempo_limite - tempo_passado)

        if tempo_restante > 0:
            st.markdown(f"⏳ Sequência desaparecerá em {tempo_restante} segundos")
            time.sleep(1)
            st.rerun()
        else:
            st.session_state.show_sequence = False
            st.rerun()
    else:
        st.write("Reproduza a sequência clicando nas cores na ordem correta:")

        cores_possiveis = ['🔴', '🔵', '🟢', '🟡']
        cols = st.columns(len(cores_possiveis))

        for i, cor in enumerate(cores_possiveis):
            with cols[i]:
                if st.button(cor):
                    if not st.session_state.finished:
                        st.session_state.user_sequence.append(cor)
                        st.rerun()

        st.write(f"Sequência selecionada: {' '.join(st.session_state.user_sequence)}")

        if len(st.session_state.user_sequence) == len(st.session_state.color_sequence) and not st.session_state.finished:
            if st.session_state.user_sequence == st.session_state.color_sequence:
                st.success("🎉 Você acertou a sequência!")
                st.balloons()
                
                st.session_state.result = True
            else:
                st.error("❌ Sequência incorreta. Você perdeu!")
                st.session_state.result = False
            st.session_state.finished = True

        if st.session_state.finished:
            if st.session_state.result:
                if st.button("Avançar para a próxima fase"):
                    for key in ['color_sequence', 'start_time', 'show_sequence', 'user_sequence', 'finished', 'result']:
                        st.session_state.pop(key, None)
                    st.session_state.step += 1
                    st.rerun()
            else:
                if st.button("Voltar ao início"):
                    for key in ['color_sequence', 'start_time', 'show_sequence', 'user_sequence', 'finished', 'result']:
                        st.session_state.pop(key, None)
                    st.session_state.step = 1
                    st.rerun()