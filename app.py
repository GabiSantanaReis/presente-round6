import streamlit as st
import time
import random
import os

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

# Estilo visual Round 6
def aplicar_estilo_geral(background_url):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)),
                        url('{background_url}');
            background-size: cover;
            background-position: center;
            color: white;
        }}
        div.stButton > button:first-child {{
            background-color: #c71585;
            color: white;
            font-size: 20px;
            font-weight: bold;
            border: none;
            border-radius: 10px;
            padding: 12px 28px;
            box-shadow: 0px 0px 12px #c71585;
            transition: 0.3s ease;
        }}
        div.stButton > button:first-child:hover {{
            background-color: #d94bbb;
            box-shadow: 0px 0px 18px #d94bbb;
            transform: scale(1.05);
        }}
        </style>
    """, unsafe_allow_html=True)

def tocar_audio(url):
    st.markdown(f"""
        <audio autoplay loop>
            <source src="{url}" type="audio/mpeg">
        </audio>
    """, unsafe_allow_html=True)

def mostrar_intro_fase(step, titulo, descricao):
    flag = f"fase{step}_iniciada"
    if flag not in st.session_state:
        st.session_state[flag] = False

    if not st.session_state[flag]:
        st.markdown(f"## {titulo}")
        st.markdown(f"<p style='white-space:pre-line;'>{descricao}</p>", unsafe_allow_html=True)
        if st.button("🔓 Iniciar desafio"):
            st.session_state[flag] = True
            st.rerun()
        return False
    return True

st.set_page_config(page_title="Round 6 - Gabrielle", page_icon="🎮")


# ========== Etapa 1: Boas-vindas ==========
if st.session_state.step == 1:
    st.title("Round 6: Desafios Iniciados")
    st.markdown("""
    ### Seja bem-vinda, Jogadora Gabrielle (097).

    ###### Você acaba de ser convocada para participar de uma sequência de desafios insanos, imprevisíveis, emocionantes.

    🎂 *Hoje seria um dia comum... se você não estivesse prestes a mergulhar num universo de enigmas e tensão.* Feliz aniversário atrasado — porque nada aqui acontece no tempo convencional.

    ⏳ A partir deste momento, você enfrentará testes de memória, lógica, coragem... e talvez até um pouco de sorte.
                
    🔊 Aumente o volume do celular. Os sons fazem parte da experiência!
                
    📜 Siga cada instrução. Com atenção cirúrgica... Errar pode ter consequências. Ou não. Só há uma forma de descobrir.

    E então...

    🎮 **Você aceita participar do jogo?**  
    """)
    
    aplicar_estilo_geral("https://images3.alphacoders.com/118/thumb-1920-1181423.jpg")
    st.button("Avançar para o primeiro desafio ▲ ● ■", on_click=proxima_pagina)

elif st.session_state.step == 2:

    aplicar_estilo_geral("https://images5.alphacoders.com/117/thumb-1920-1177232.jpg")

    if mostrar_intro_fase(2, "🚦 Desafio 1: Corrida pela Sobrevivência", """ Você tem segundos.
        A boneca já está de costas. O campo está silencioso.
        📢 Assim que a voz ecoar _“Batatinha frita 1, 2, 3...”_, você precisará decidir rapidamente: **O que é verdade. O que é mentira.** 
        Errar uma resposta equivale a tropeçar no campo — e você sabe o que acontece com quem cai.
        💬 São afirmações que testam sua memória, lógica e sangue frio.  
        Você não pode parar. Não pode hesitar.
        Se responder certo: avança.  
        Se responder errado... o jogo reinicia. E você perde tempo precioso.
        Está preparada para correr — com a mente? 🧠💨  
        Seu presente está cada vez mais perto. Mas também... mais protegido.
        ▲ ● ■"""):

        
        tocar_audio("https://www.myinstants.com/media/sounds/squid-game-doll-music.mp3")

        # Botão para iniciar o desafio
        if 'desafio1_iniciado' not in st.session_state:
            
            st.session_state.desafio1_iniciado = True
            st.session_state.start_time = time.time()
            st.session_state.finished = False
            st.session_state.acertou_tudo = False
            st.rerun()

        # Conteúdo principal após clique
        if st.session_state.get("desafio1_iniciado"):
            tempo_passado = time.time() - st.session_state.start_time
            tempo_restante = int(60 - tempo_passado)


            if not st.session_state.finished:
                st.markdown(f"""
                    <div style="text-align:center; font-size:26px; font-weight:bold; color:#FFB6C1;">
                        ⏳ Tempo restante: {tempo_restante} segundos
                    </div>
                """, unsafe_allow_html=True)

            perguntas = {
                "O número do jogador vencedor é 456.": True,
                "O segundo jogo apresentado na série (na primeira temporada) é a corrida de sacos.": False,
                "O símbolo quadrado na máscara representa o nível mais alto entre os soldados.": True,
                "Gi-hun aposta em corridas de cavalo logo antes de entrar no jogo.": True,
                "Sae-byeok é uma ex-policial infiltrada no jogo.": False,
                "No desafio da ponte de vidro, os jogadores tinham que escolher entre vidro temperado e vidro comum para passar de um lado ao outro.": True,
                "O organizador do jogo revela sua identidade apenas no último episódio.": True,
                "A moeda usada para recrutar jogadores é o dólar americano.": False,
                "O jogo da corda exige apenas força física.": False,
                "A série é ambientada em uma ilha escondida e monitorada por câmeras.": True
            }

            for pergunta in perguntas:
                st.radio(pergunta, ["Verdadeiro", "Falso"], key=pergunta)

            if not st.session_state.finished:
                if st.button("Confirmar respostas"):
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
                if st.session_state.acertou_tudo:
                    st.success("🎉 Parabéns! Você acertou todas as respostas!")
                    st.balloons()
                    if st.button("Avançar para o próximo desafio"):
                        st.session_state.step += 1
                        for key in ['desafio1_iniciado', 'start_time', 'finished', 'acertou_tudo', 'fase2_iniciada'] + list(perguntas.keys()):
                            st.session_state.pop(key, None)
                        st.rerun()
                else:
                    st.error("💀 Você perdeu! Respostas incorretas ou tempo esgotado.")
                    st.session_state.step = 9
                    for key in ['desafio1_iniciado', 'start_time', 'finished', 'acertou_tudo', 'fase2_iniciada'] + list(perguntas.keys()):
                        st.session_state.pop(key, None)
                            
                        st.rerun()

            if not st.session_state.finished:
                if tempo_restante <= 0:
                    st.session_state.finished = True
                    st.session_state.acertou_tudo = False
                    st.rerun()
                else:
                    time.sleep(1)
                    st.rerun()


# ========== Etapa 3: Jogo da Memória ==========
elif st.session_state.step == 3:


    aplicar_estilo_geral("https://images.alphacoders.com/118/thumb-1920-1184523.jpg")

    if mostrar_intro_fase(3, "🧠 Desafio 2: Jogo da Memória", """Você está frente a frente com outro jogador. As regras? Simples.
    Descubra pares idênticos. Se acertar, sobrevive.  
    Se errar... o tempo corre, e você se aproxima do fim.
    👁️ Use sua percepção. Sua intuição. E sua memória.
    Assim como na sala das bolinhas de gude, cada movimento importa.  
    Cada escolha pode ser sua última.
    ▲ ● ■"""):
        
        tocar_audio("https://www.myinstants.com/media/sounds/girotondo-squidgame.mp3")

        # 🧠 Inicialização da fase
        if "cards" not in st.session_state:
            emojis = ['⚫', '⚫', '⬛', '⬛', '🎮', '🎮', '💀', '💀']
            random.shuffle(emojis)
            st.session_state.cards = emojis
            st.session_state.revealed = [False] * len(emojis)
            st.session_state.first_choice = None
            st.session_state.second_choice = None
            st.session_state.pairs_found = 0
            st.session_state.message = ""
            st.session_state.memory_started = time.time()
            st.session_state.memory_finished = False
            st.session_state.aguardando_reset = False
            st.session_state.aguardando_exibicao_par = False
            st.session_state3 = False

        # ⏳ Timer
        if not st.session_state.memory_finished:
            tempo_passado = time.time() - st.session_state.memory_started
            tempo_restante = int(60 - tempo_passado)
            if tempo_restante <= 0:
                st.session_state.memory_finished = True
                st.session_state.message = "⏰ Tempo esgotado! Você perdeu esse desafio."
            else:
                st.markdown(f"""
                    <div style="text-align:center; font-size:26px; font-weight:bold; color:#FFB6C1;">
                        ⏳ Tempo restante: {tempo_restante} segundos
                    </div>
                """, unsafe_allow_html=True)

        # 🃏 Cartas
        cols = st.columns(4)
        for i in range(len(st.session_state.cards)):
            with cols[i % 4]:
                mostrar = st.session_state.revealed[i] or i == st.session_state.first_choice or i == st.session_state.second_choice
                emoji = st.session_state.cards[i] if mostrar else "❓"
                if st.button(emoji, key=f"card_{i}", disabled=st.session_state.revealed[i]):
                    if st.session_state.first_choice is None:
                        st.session_state.first_choice = i
                    elif st.session_state.second_choice is None and i != st.session_state.first_choice:
                        st.session_state.second_choice = i

        # 🎥 Renderização sequencial
        if st.session_state.get("aguardando_exibicao_par"):
            st.session_state.aguardando_exibicao_par = False
            st.session_state.aguardando_reset = True
            st.rerun()

        elif st.session_state.get("aguardando_reset"):
            time.sleep(1)
            st.session_state.first_choice = None
            st.session_state.second_choice = None
            st.session_state.aguardando_reset = False
            st.rerun()

        elif st.session_state.first_choice is not None and st.session_state.second_choice is not None:
            idx1 = st.session_state.first_choice
            idx2 = st.session_state.second_choice
            carta1 = st.session_state.cards[idx1]
            carta2 = st.session_state.cards[idx2]

            if carta1 == carta2:
                st.session_state.revealed[idx1] = True
                st.session_state.revealed[idx2] = True
                st.session_state.pairs_found += 1
                st.session_state.message = "Par encontrado! 🎉"
            else:
                st.session_state.message = "Não é par, tente novamente. ❌"
            st.session_state.aguardando_exibicao_par = True
            st.rerun()

        # 💬 Mensagem atual
        st.write(st.session_state.message)

        # 🏆 Vitória
        if st.session_state.pairs_found == len(st.session_state.cards) // 2 and not st.session_state.memory_finished:
            st.balloons()
            st.success("Você encontrou todos os pares! Parabéns! 🎊")
            if st.button("Avançar para a próxima fase"):
                for key in ['cards', 'revealed', 'first_choice', 'second_choice',
                            'pairs_found', 'message', 'memory_started',
                            'memory_finished', 'aguardando_reset', 'aguardando_exibicao_par', 'fase3_iniciada']:
                    st.session_state.pop(key, None)
                st.session_state.step += 1
                st.rerun()

        # 💀 Derrota por tempo
        if st.session_state.memory_finished and st.session_state.pairs_found < len(st.session_state.cards) // 2:
            st.error("Você perdeu! Tempo esgotado ou pares insuficientes.")
            for key in ['cards', 'revealed', 'first_choice', 'second_choice',
                        'pairs_found', 'message', 'memory_started',
                        'memory_finished', 'aguardando_reset', 'aguardando_exibicao_par', 'fase3_iniciada']:
                st.session_state.pop(key, None)
            st.session_state3 = False
            st.session_state.step = 9  # Ou volte para 1 se quiser reiniciar o jogo inteiro
            st.rerun()



elif st.session_state.step == 4:

    aplicar_estilo_geral("https://images2.alphacoders.com/118/thumb-1920-1181149.png")

    if mostrar_intro_fase(4, "🎲 Desafio 3: Código do Número", """
Uma cortina se abre. Você está diante de uma máquina silenciosa.  
Ela esconde um único número — entre 1 e 20.

Você terá **4 tentativas** para descobrir o número exato.  
Se errar, a máquina responde: _Muito alto._ ou _Muito baixo._  
Mas ela nunca revela se está perto… ou longe.

✖️ Se todas as tentativas falharem, o sistema bloqueia.  
O jogo continua… **sem você**.
"""):

        tocar_audio("https://www.myinstants.com/media/sounds/squid-game-announcement-sound.mp3")

        # Inicializa estado do jogo
        if 'target_number' not in st.session_state:
            st.session_state.target_number = random.randint(1, 20)
            st.session_state.guesses_left = 4
            st.session_state.message = ""
            st.session_state.acertou_numero = False
            st.session_state.perdeu_numero = False

        # 👀 Jogo em andamento
        if not st.session_state.acertou_numero and not st.session_state.perdeu_numero:
            st.write("Estou pensando em um número entre 1 e 20. Tente adivinhar!")
            guess = st.number_input("Digite seu palpite:", min_value=1, max_value=20, step=1, key='palpite_numero')

            if st.button("Enviar palpite"):
                if guess == st.session_state.target_number:
                    st.success(f"🎉 Parabéns! Você acertou o número {st.session_state.target_number}!")
                    st.session_state.acertou_numero = True
                else:
                    st.session_state.guesses_left -= 1
                    if st.session_state.guesses_left == 0:
                        st.session_state.perdeu_numero = True
                        st.error(f"💀 Você perdeu! O número era {st.session_state.target_number}.")
                    else:
                        dica = "Muito baixo!" if guess < st.session_state.target_number else "Muito alto!"
                        st.session_state.message = f"{dica} Tente novamente."

            st.write(f"Tentativas restantes: {st.session_state.guesses_left}")
            st.write(st.session_state.message)

        # ✅ Acertou
        if st.session_state.acertou_numero:
            st.balloons()
            if st.button("➡️ Ir para a próxima fase"):
                for key in ['target_number', 'guesses_left', 'message', 'acertou_numero', 'perdeu_numero', 'palpite_numero','fase4_iniciada']:
                    st.session_state.pop(key, None)
                    
                st.session_state.step += 1
                st.rerun()

        # ❌ Perdeu
        elif st.session_state.perdeu_numero:
            for key in ['target_number', 'guesses_left', 'message', 'acertou_numero', 'perdeu_numero', 'palpite_numero', 'fase4_iniciada']:
                st.session_state.pop(key, None)
            st.session_state3 = False
            
            st.session_state.step = 9
            st.rerun()

elif st.session_state.step == 5:

    aplicar_estilo_geral("https://images6.alphacoders.com/117/thumb-1920-1177227.jpg")

    if 'message' in st.session_state:
        st.session_state.pop('message', None)

    for key in ['boxes6', 'selected_boxes', 'finished6', 'result6', 'message6']:
        st.session_state.pop(key, None)

    if mostrar_intro_fase(5, "🎨 Desafio 4: A Sequência das Pedras", """Você se aproxima de uma bancada.  
        Quatro pedrinhas coloridas repousam à sua frente: **vermelho, roxo, verde e amarelo.**
        No visor acima, uma sequência é revelada... por segundos.  
        Você deve memorizar cada cor, cada posição.  
        Porque depois que ela desaparecer, só restará sua memória.
        🧠 Esse é um teste de atenção e lógica —  
        Como os desafios infantis distorcidos pela elite mascarada.
        Clique nas cores na **mesma ordem exata**.  
        Repita sem hesitar.  
        Erros não serão perdoados.
        ⏳ Você tem apenas um momento.  
        Escolha com precisão.  
        ▲ ● ■"""):

        tocar_audio("https://www.myinstants.com/media/sounds/squid-game-jump-rope-song.mp3")


        # Define caminhos locais das imagens
        cores_possiveis = {
            'vermelho': "imagens/vermelho.png",
            'roxo': "imagens/roxo.png",
            'verde': "imagens/verde.png",
            'amarelo': "imagens/amarelo.png"
        }


        # Inicializa sequência
        if 'color_sequence' not in st.session_state:
            st.session_state.color_sequence = [random.choice(list(cores_possiveis.keys())) for _ in range(5)]
            st.session_state.start_time = time.time()
            st.session_state.show_sequence = True
            st.session_state.user_sequence = []
            st.session_state.finished = False
            st.session_state.result = None

        tempo_passado = time.time() - st.session_state.start_time
        tempo_limite = 10

        if st.session_state.show_sequence:
            st.write("Memorize a sequência de cores:")
            cols = st.columns(len(st.session_state.color_sequence))
            for i, cor in enumerate(st.session_state.color_sequence):
                with cols[i]:
                    caminho = cores_possiveis.get(cor)
                    if caminho and os.path.exists(caminho):
                        st.image(caminho, width=60)
                    else:
                        st.warning(f"Imagem não encontrada: {caminho}")

            tempo_restante = int(tempo_limite - tempo_passado)
            if tempo_restante > 0:
                st.markdown(f"⏳ Sequência desaparecerá em {tempo_restante} segundos")
                time.sleep(1)
                st.rerun()
            else:
                st.session_state.show_sequence = False
                st.rerun()

        else:
            st.write("Clique nas pedrinhas na mesma ordem da sequência 👇")
            cols = st.columns(len(cores_possiveis))

            for i, (nome_cor, caminho_img) in enumerate(cores_possiveis.items()):
                with cols[i]:
                    if os.path.exists(caminho_img):
                        st.image(caminho_img, width=60)
                    else:
                        st.warning(f"Imagem não encontrada: {caminho_img}")

                    if st.button(f"Selecionar {nome_cor}", key=f"botao_{nome_cor}"):
                        if not st.session_state.finished:
                            st.session_state.user_sequence.append(nome_cor)
                            st.rerun()

            st.write("Sequência selecionada:")
            if st.session_state.user_sequence:
                cols_sel = st.columns(len(st.session_state.user_sequence))
                for i, cor in enumerate(st.session_state.user_sequence):
                    with cols_sel[i]:
                        caminho = cores_possiveis.get(cor)
                        if caminho and os.path.exists(caminho):
                            st.image(caminho, width=60)
                        else:
                            st.warning(f"Imagem não encontrada: {caminho}")
            else:
                st.info("🔎 Você ainda não selecionou nenhuma cor.")

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
                        for key in ['color_sequence', 'start_time', 'show_sequence', 'user_sequence', 'finished', 'result', 'fase5_iniciada']:
                            st.session_state.pop(key, None)
                        st.session_state.step += 1
                        st.rerun()
                else:
                    for key in ['color_sequence', 'start_time', 'show_sequence', 'user_sequence', 'finished', 'result','fase5_iniciada']:
                        st.session_state.pop(key, None)
                    st.session_state.step = 9
                    st.rerun()

elif st.session_state.step == 6:

    aplicar_estilo_geral("https://images.alphacoders.com/117/thumb-1920-1177234.jpg")

    for key in ['color_sequence', 'start_time', 'show_sequence', 'user_sequence', 'finished', 'result']:
        st.session_state.pop(key, None)

    if mostrar_intro_fase(5, "🎯 Desafio 5: Decifre a Verdade", """O jogo foi cruel.  
        Mentes foram manipuladas.  
        Alguns venceram pela lógica, outros... pela sorte.
        Na sua frente, quinze afirmações. Algumas verdadeiras. Outras, falsificadas por quem controla tudo.
        🧠 Sua missão: **Selecionar apenas os eventos que realmente aconteceram na série.**
        Cada marcação errada pode custar tudo.  
        Cada verdade ignorada... uma chance perdida.
        Escolha com sabedoria.  
        Confirme com coragem.  
        E avance apenas se souber **o que foi real.**
        ▲ ● ■"""):

        tocar_audio("https://www.myinstants.com/media/sounds/squid-game-tone.mp3")


        # Lista de afirmações (aquelas que são verdadeiras devem estar nas premiadas_indices)
        afirmacoes = [
            "Gi-hun é o jogador número 456.",
            "Jogadores podem usar celulares durante o jogo.",
            "O número 001 é o criador do jogo.",
            "O jogo da ponte envolvia vidro temperado e comum.",
            "Sae-byeok é uma desertora da Coreia do Norte.",
            "Jogadores vestem macacões vermelhos.",
            "Os guardas têm símbolos geométricos nas máscaras.",
            "O prêmio total é de 45.6 bilhões de won.",
            "Ali salva Gi-hun durante o jogo da corda.",
            "Gi-hun vence a última prova: o jogo do squid.",
            "Jogadores eliminados recebem outra chance.",
            "A moeda usada para recrutar é o won coreano.",
            "A prova do biscoito exige cortar com uma agulha.",
            "A série se passa numa ilha secreta.",
            "Todos os guardas são mulheres."
        ]



        if 'boxes6' not in st.session_state:
            total_caixas = 15
            
            #aqui o indice ta um pra frente, depois da pra trocar o tema tbm, de caixa pra alguma coisa q ela tenha que selecionar certo
            #premiadas_indices = [1, 4, 8, 11, 13]  # exemplo: caixas 2,5,9,12,14
            premiadas_indices = [0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13]


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
                    label = afirmacoes[idx]
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
                    st.balloons()
                    st.session_state.message6 = "🎉 Parabéns! Você acertou todas as caixas premiadas!"
                else:
                    st.session_state.message6 = "❌ Errou! Seleção incorreta."

                st.rerun()

        else:
            if st.session_state.result6:
                st.success(st.session_state.message6)
                st.balloons()
                if st.button("Avançar para a próxima fase"):
                    for key in ['boxes6', 'selected_boxes', 'finished6', 'result6', 'message6', 'fase6_iniciada']:
                        st.session_state.pop(key, None)
                    st.session_state.step += 1
                    st.rerun()
            else:
                st.error(st.session_state.message6)
                for key in ['boxes6', 'selected_boxes', 'finished6', 'result6', 'message6', 'fase6_iniciada']:
                    st.session_state.pop(key, None)
                st.session_state.step = 9
                st.rerun()



elif st.session_state.step == 7:

    aplicar_estilo_geral("https://images5.alphacoders.com/138/thumb-1920-1386261.jpg")
    if mostrar_intro_fase(7, "🎯 Desafio 6: Escolha Corrompida", """O jogo te testou física e mentalmente.  
    Agora, resta uma escolha.
    Três caixas misteriosas. Uma guarda a resposta.  
    Duas contêm o fim.
    O Front Man observa silenciosamente.  
    Ele quer saber: **você ainda é você?**
    📦 Você pode parar agora.  
    Mas quem abandona, sem saber o que havia dentro…  
    simplesmente desaparece. Sem glória, sem retorno.
    Escolher errado, é perder tudo.
    Escolher certo, é ganhar o jogo.  
    Mas a dúvida sempre permanecerá: **o que te moveu a abrir?**"""):

        tocar_audio("https://www.myinstants.com/media/sounds/salesman-squid-game-edit-audio-blah-phonk.mp3")


        if 'boxes' not in st.session_state:
            caixas = [True, False, False]
            random.shuffle(caixas)
            st.session_state.boxes = caixas
            st.session_state.opened = [False, False, False]
            st.session_state.game_over = False
            st.session_state.message = "Escolha uma caixa para abrir."
            st.session_state.result = None
            st.session_state.saiu_sem_jogar = False

        cols = st.columns(3)

        for i in range(3):
            with cols[i]:
                if st.session_state.opened[i]:
                    if st.session_state.boxes[i]:
                        st.success("🎉 Prêmio escondido! Você escolheu certo.")
                        st.session_state.result = True
                    else:
                        st.error("💥 Armadilha! Fim da linha.")
                        st.session_state.result = False
                        st.session_state.game_over = True
                else:
                    if not st.session_state.game_over and st.session_state.result is None:
                        if st.button(f"Abrir Caixa {i+1}", key=f"box_{i}"):
                            st.session_state.opened[i] = True
                            if st.session_state.boxes[i]:
                                st.session_state.message = "🎉 Você encontrou o prêmio. Pode avançar."
                            else:
                                st.session_state.message = "💥 Armadilha! Você perdeu tudo."
                            st.rerun()

        st.write(st.session_state.message)

        # Jogadora opta por sair sem abrir
        if st.session_state.result is None and not any(st.session_state.opened):
            if st.button("Desistir do jogo e sair"):
                st.session_state.saiu_sem_jogar = True
                st.rerun()

        if st.session_state.saiu_sem_jogar:
            st.error("🩸 Você lutou tanto… e escolheu desaparecer. Nenhuma resposta. Nenhum avanço.")
            
            for key in ['boxes', 'opened', 'game_over', 'message', 'result', 'saiu_sem_jogar', 'fase7_iniciada']:
                st.session_state.pop(key, None)
            st.session_state.step = 9
            st.rerun()

        # Se venceu
        if st.session_state.result is True:
            if st.button("Avançar para a próxima fase"):
                for key in ['boxes', 'opened', 'game_over', 'message', 'result', 'saiu_sem_jogar', 'fase7_iniciada']:
                    st.session_state.pop(key, None)
                st.session_state.step += 1
                st.rerun()

        # Se perdeu
        if st.session_state.result is False:
            st.error("Fim do jogo. Você perdeu tudo.")
            for key in ['boxes', 'opened', 'game_over', 'message', 'result', 'saiu_sem_jogar', 'fase7_iniciada']:
                st.session_state.pop(key, None)
            st.session_state.step = 9
            st.rerun()


elif st.session_state.step ==8:


    aplicar_estilo_geral("https://images.alphacoders.com/118/thumb-1920-1183834.jpg")

    def mostrar_intro_fase_ultima(step, titulo, descricao):
        flag = f"fase{step}_iniciada"
        if flag not in st.session_state:
            st.session_state[flag] = False

        if not st.session_state[flag]:
            st.markdown(f"## {titulo}")
            st.markdown(f"<p style='white-space:pre-line;'>{descricao}</p>", unsafe_allow_html=True)
            if st.button("🔓 MOSTRAR SENHA"):
                st.session_state[flag] = True
                st.rerun()
            return False
        return True

    if mostrar_intro_fase_ultima(8, "🎉 PARABÉNS!", """ Você enfrentou cada enigma, cada armadilha, e chegou até aqui.<br>
        Provou coragem, raciocínio e coração.<br><br>
        Agora, pegue seu premio:"""):
        tocar_audio("https://www.myinstants.com/media/sounds/congratulations-squid-game.mp3")
        st.image("static/imagens/Gaby_uniforme.png", use_container_width=True)
        st.markdown("<h2 style='text-align:center; color:white;'>Jogadora 097 venceu!</h2>", unsafe_allow_html=True)



        # Exibe os três números grandes centralizados
        numeros_cadeado = [4, 5, 6]  # Exemplo de chave — você pode trocar

        st.markdown(f"""
        <div style="text-align:center; margin-top:60px;">
            <span style="font-size:50px; font-weight:bold; color:#FFD700; letter-spacing:10px;">
                {numeros_cadeado[0]} &nbsp;&nbsp; {numeros_cadeado[1]} &nbsp;&nbsp; {numeros_cadeado[2]}
            </span><br><br>
            <span style="font-size:22px; color:#ffffff;">🔐 Essa é a chave. Use-a para abrir seu presente.</span>
        </div>
        """, unsafe_allow_html=True)


elif st.session_state.step == 9:

    # Fundo preto e estilo do botão
    st.markdown("""
        <style>
        .stApp {
            background-color: black;
        }
        div.stButton > button:first-child {
            background-color: #c71585;
            color: white;
            font-size: 20px;
            font-weight: bold;
            border: none;
            border-radius: 10px;
            padding: 12px 28px;
            box-shadow: 0px 0px 12px #c71585;
            transition: 0.3s ease;
        }
        div.stButton > button:first-child:hover {
            background-color: #d94bbb;
            box-shadow: 0px 0px 18px #d94bbb;
            transform: scale(1.05);
        }
        </style>
    """, unsafe_allow_html=True)

    # Define largura desejada
    botao_largura_px = 400

    # Container que centraliza tudo
    st.markdown(f'<div style="width: {botao_largura_px}px; margin: 0 auto; text-align: center;">', unsafe_allow_html=True)

    st.image("static/imagens/gaby_eliminada.png", width=botao_largura_px)
    st.markdown("<h2 style='color:white;'>Jogadora 097 eliminada</h2>", unsafe_allow_html=True)

    if st.button("🔁 Tentar de novo", key="botao_estilizado"):
        st.session_state.step = 1
        for k in list(st.session_state.keys()):
            if k != "step":
                del st.session_state[k]
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
