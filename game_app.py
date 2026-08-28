import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Juegos Simples 🎮", page_icon="🕹️", layout="centered")

# Inicializar variables de estado
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_active" not in st.session_state:
    st.session_state.game_active = False
if "game_selected" not in st.session_state:
    st.session_state.game_selected = None
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# CABECERA
st.title("🎮 Juegos Simples")
col1, col2 = st.columns([2, 1])
with col1:
    st.write("¡Diviértete con estos juegos sencillos!")
with col2:
    st.subheader(f"🏆 {st.session_state.score} pts")

st.markdown("---")

# MENÚ PRINCIPAL
menu = st.sidebar.radio("Selecciona un Juego", [
    "🏠 Inicio",
    "🎯 Adivina el Número",
    "🎲 Piedra, Papel o Tijera",
    "💡 Trivia Rápida",
    "🎪 Memoria"
])

# PANTALLA INICIO
if menu == "🏠 Inicio":
    st.markdown("### 🎯 Elige tu Juego:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🎯 Adivina el Número")
        st.write("Adivina un número entre 1 y 100 en menos intentos.")
        if st.button("Jugar →", key="btn_numeros"):
            st.session_state.game_selected = "numeros"
            st.session_state.game_active = True
            st.session_state.numero_secreto = random.randint(1, 100)
            st.session_state.attempts = 0
            st.rerun()
    
    with col2:
        st.markdown("#### 🎲 Piedra, Papel, Tijera")
        st.write("Juega contra la máquina. ¡Gana 3 de 5!")
        if st.button("Jugar →", key="btn_ppt"):
            st.session_state.game_selected = "ppt"
            st.session_state.game_active = True
            st.session_state.ppt_rounds = 0
            st.session_state.ppt_wins = 0
            st.rerun()
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("#### 💡 Trivia Rápida")
        st.write("Responde preguntas y acumula puntos.")
        if st.button("Jugar →", key="btn_trivia"):
            st.session_state.game_selected = "trivia"
            st.session_state.game_active = True
            st.session_state.trivia_count = 0
            st.rerun()
    
    with col4:
        st.markdown("#### 🎪 Memoria")
        st.write("Recuerda la secuencia de colores.")
        if st.button("Jugar →", key="btn_memoria"):
            st.session_state.game_selected = "memoria"
            st.session_state.game_active = True
            st.session_state.memoria_sequence = [random.choice(['🔴', '🟢', '🔵', '🟡'])]
            st.session_state.memoria_level = 1
            st.rerun()

# JUEGO 1: ADIVINA EL NÚMERO
elif menu == "🎯 Adivina el Número":
    st.subheader("🎯 Adivina el Número (1-100)")
    
    if not st.session_state.game_active:
        if st.button("Comenzar Juego"):
            st.session_state.game_active = True
            st.session_state.numero_secreto = random.randint(1, 100)
            st.session_state.attempts = 0
            st.rerun()
    else:
        st.write(f"**Intentos:** {st.session_state.attempts}")
        
        numero = st.number_input("Ingresa tu número:", min_value=1, max_value=100, step=1, key="num_input")
        
        if st.button("Enviar", key="btn_check_num"):
            st.session_state.attempts += 1
            
            if numero == st.session_state.numero_secreto:
                points = max(0, 50 - st.session_state.attempts * 5)
                st.session_state.score += points
                st.success(f"🎉 ¡Ganaste! ¡Adivinaste en {st.session_state.attempts} intentos! +{points} puntos")
                st.balloons()
                st.session_state.game_active = False
                
                if st.button("Volver al Inicio"):
                    st.session_state.game_selected = None
                    st.rerun()
            elif numero < st.session_state.numero_secreto:
                st.warning("⬆️ El número es más ALTO")
            else:
                st.warning("⬇️ El número es más BAJO")
            
            if st.session_state.attempts >= 10:
                st.error(f"😢 Perdiste. El número era {st.session_state.numero_secreto}")
                st.session_state.game_active = False
                if st.button("Volver al Inicio"):
                    st.session_state.game_selected = None
                    st.rerun()

# JUEGO 2: PIEDRA, PAPEL, TIJERA
elif menu == "🎲 Piedra, Papel o Tijera":
    st.subheader("🎲 Piedra, Papel o Tijera")
    
    if not st.session_state.game_active:
        if st.button("Comenzar Juego"):
            st.session_state.game_active = True
            st.session_state.ppt_rounds = 0
            st.session_state.ppt_wins = 0
            st.rerun()
    else:
        st.write(f"**Rondas:** {st.session_state.ppt_rounds}/5 | **Victorias:** {st.session_state.ppt_wins}")
        
        if st.session_state.ppt_rounds < 5:
            opciones = ["🪨 Piedra", "📄 Papel", "✂️ Tijera"]
            eleccion_jugador = st.radio("Elige tu opción:", opciones, key=f"ppt_{st.session_state.ppt_rounds}")
            
            if st.button("Jugar", key=f"btn_ppt_{st.session_state.ppt_rounds}"):
                eleccion_maquina = random.choice(opciones)
                st.session_state.ppt_rounds += 1
                
                st.write(f"🤖 Máquina eligió: {eleccion_maquina}")
                st.write(f"👤 Tú elegiste: {eleccion_jugador}")
                
                # Lógica del juego
                if eleccion_jugador == eleccion_maquina:
                    st.info("🤝 ¡Empate!")
                elif (eleccion_jugador == "🪨 Piedra" and eleccion_maquina == "✂️ Tijera") or \
                     (eleccion_jugador == "📄 Papel" and eleccion_maquina == "🪨 Piedra") or \
                     (eleccion_jugador == "✂️ Tijera" and eleccion_maquina == "📄 Papel"):
                    st.success("🎉 ¡Ganaste esta ronda! +10 puntos")
                    st.session_state.ppt_wins += 1
                    st.session_state.score += 10
                else:
                    st.error("😢 Perdiste esta ronda")
                
                if st.session_state.ppt_rounds >= 5:
                    if st.session_state.ppt_wins >= 3:
                        st.success(f"🏆 ¡Ganaste el juego! {st.session_state.ppt_wins}/5 victorias. +30 puntos")
                        st.session_state.score += 30
                        st.balloons()
                    else:
                        st.error(f"😢 Perdiste el juego. Solo {st.session_state.ppt_wins}/5 victorias.")
                    
                    st.session_state.game_active = False
                    if st.button("Volver al Inicio"):
                        st.session_state.game_selected = None
                        st.rerun()

# JUEGO 3: TRIVIA
elif menu == "💡 Trivia Rápida":
    st.subheader("💡 Trivia Rápida")
    
    preguntas = [
        {
            "pregunta": "¿Cuál es la capital de Francia?",
            "opciones": ["Londres", "París", "Berlín", "Madrid"],
            "correcta": "París"
        },
        {
            "pregunta": "¿Cuántos lados tiene un triángulo?",
            "opciones": ["2", "3", "4", "5"],
            "correcta": "3"
        },
        {
            "pregunta": "¿En qué año llegó el hombre a la Luna?",
            "opciones": ["1965", "1969", "1972", "1975"],
            "correcta": "1969"
        },
        {
            "pregunta": "¿Cuál es el planeta más grande del Sistema Solar?",
            "opciones": ["Saturno", "Júpiter", "Neptuno", "Marte"],
            "correcta": "Júpiter"
        },
        {
            "pregunta": "¿Cuál es el idioma más hablado del mundo?",
            "opciones": ["Español", "Inglés", "Mandarín", "Hindi"],
            "correcta": "Mandarín"
        }
    ]
    
    if not st.session_state.game_active:
        if st.button("Comenzar Trivia"):
            st.session_state.game_active = True
            st.session_state.trivia_count = 0
            st.rerun()
    else:
        if st.session_state.trivia_count < len(preguntas):
            pregunta_actual = preguntas[st.session_state.trivia_count]
            st.write(f"**Pregunta {st.session_state.trivia_count + 1}/{len(preguntas)}: {pregunta_actual['pregunta']}**")
            
            respuesta = st.radio("Elige tu respuesta:", pregunta_actual['opciones'], key=f"trivia_{st.session_state.trivia_count}")
            
            if st.button("Confirmar", key=f"btn_trivia_{st.session_state.trivia_count}"):
                if respuesta == pregunta_actual['correcta']:
                    st.success("✅ ¡Correcto! +15 puntos")
                    st.session_state.score += 15
                else:
                    st.error(f"❌ Incorrecto. La respuesta era: {pregunta_actual['correcta']}")
                
                st.session_state.trivia_count += 1
                st.rerun()
        else:
            st.success(f"🎉 ¡Completaste la trivia! Total ganado: {len(preguntas) * 15} puntos")
            st.balloons()
            st.session_state.game_active = False
            if st.button("Volver al Inicio"):
                st.session_state.game_selected = None
                st.rerun()

# JUEGO 4: MEMORIA
elif menu == "🎪 Memoria":
    st.subheader("🎪 Juego de Memoria")
    
    if not st.session_state.game_active:
        if st.button("Comenzar Juego"):
            st.session_state.game_active = True
            st.session_state.memoria_sequence = [random.choice(['🔴', '🟢', '🔵', '🟡'])]
            st.session_state.memoria_level = 1
            st.session_state.memoria_user_sequence = []
            st.rerun()
    else:
        st.write(f"**Nivel: {st.session_state.memoria_level}**")
        st.write(f"**Secuencia de la máquina:** {' '.join(st.session_state.memoria_sequence)}")
        
        st.info(f"Tienes que recordar y reproducir la secuencia.")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("🔴", key="btn_red", use_container_width=True):
                st.session_state.memoria_user_sequence.append('🔴')
        with col2:
            if st.button("🟢", key="btn_green", use_container_width=True):
                st.session_state.memoria_user_sequence.append('🟢')
        with col3:
            if st.button("🔵", key="btn_blue", use_container_width=True):
                st.session_state.memoria_user_sequence.append('🔵')
        with col4:
            if st.button("🟡", key="btn_yellow", use_container_width=True):
                st.session_state.memoria_user_sequence.append('🟡')
        
        if st.session_state.memoria_user_sequence:
            st.write(f"**Tu secuencia:** {' '.join(st.session_state.memoria_user_sequence)}")
            
            # Validar
            if len(st.session_state.memoria_user_sequence) == len(st.session_state.memoria_sequence):
                if st.session_state.memoria_user_sequence == st.session_state.memoria_sequence:
                    st.success(f"✅ ¡Correcto! Nivel {st.session_state.memoria_level} completado. +20 puntos")
                    st.session_state.score += 20
                    
                    # Siguiente nivel
                    st.session_state.memoria_level += 1
                    st.session_state.memoria_sequence.append(random.choice(['🔴', '🟢', '🔵', '🟡']))
                    st.session_state.memoria_user_sequence = []
                    st.rerun()
                else:
                    st.error(f"❌ Perdiste en el nivel {st.session_state.memoria_level}. Game Over.")
                    st.session_state.game_active = False
                    if st.button("Volver al Inicio"):
                        st.session_state.game_selected = None
                        st.rerun()

# REINICIAR PUNTOS
st.markdown("---")
if st.sidebar.button("🔄 Reiniciar Puntos"):
    st.session_state.score = 0
    st.success("Puntos reiniciados")
    st.rerun()
