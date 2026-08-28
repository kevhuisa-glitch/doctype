import streamlit as st
import time

# Configuración de la página simulando una pantalla móvil
st.set_page_config(page_title="App Educativa Esencial", page_icon="🎓", layout="centered")

# CSS con animaciones
st.markdown("""
<style>
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes bounce {
        0%, 100% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-10px);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.5;
        }
    }
    
    @keyframes slideIn {
        from {
            transform: translateX(-50px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes glow {
        0%, 100% {
            box-shadow: 0 0 5px rgba(0, 200, 100, 0.3);
        }
        50% {
            box-shadow: 0 0 20px rgba(0, 200, 100, 0.8);
        }
    }
    
    @keyframes spinningIcon {
        from {
            transform: rotate(0deg);
        }
        to {
            transform: rotate(360deg);
        }
    }
    
    .title-animated {
        animation: fadeIn 0.8s ease-in-out;
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
    }
    
    .points-animated {
        animation: bounce 0.6s ease-in-out infinite;
        font-weight: bold;
        color: #FFD700;
    }
    
    .section-animated {
        animation: slideIn 0.6s ease-in-out;
    }
    
    .button-glow {
        animation: glow 2s ease-in-out infinite;
    }
    
    .icon-spin {
        display: inline-block;
        animation: spinningIcon 2s linear infinite;
    }
    
    .success-pulse {
        animation: pulse 1s ease-in-out;
    }
    
    .metric-card {
        animation: fadeIn 1s ease-in-out;
        padding: 20px;
        border-radius: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar variables de estado del usuario (Base de datos temporal)
if "puntos" not in st.session_state:
    st.session_state.puntos = 150
if "nivel" not in st.session_state:
    st.session_state.nivel = "Secundaria"
if "premium" not in st.session_state:
    st.session_state.premium = False
if "leccion_completada" not in st.session_state:
    st.session_state.leccion_completada = False

# CABECERA DE LA APP CON ANIMACIÓN
st.markdown('<div class="title-animated">🎓 Academia Esencial</div>', unsafe_allow_html=True)

col_perfil, col_pts = st.columns([2, 1])
with col_perfil:
    st.markdown('<div class="section-animated">', unsafe_allow_html=True)
    st.write(f"👤 **Mi Perfil:** Nivel {st.session_state.nivel}")
    st.markdown('</div>', unsafe_allow_html=True)
with col_pts:
    st.markdown(f'<div class="points-animated">🏆 {st.session_state.puntos} pts</div>', unsafe_allow_html=True)

if st.session_state.premium:
    st.markdown('<div class="success-pulse">', unsafe_allow_html=True)
    st.success("👑 Cuenta Premium Activa (Acceso Ilimitado)")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# BARRA DE NAVEGACIÓN SIMULADA
menu = st.sidebar.radio("Navegación", ["🏠 Inicio / Materias", "👑 Hazte Premium", "📊 Mi Progreso"])

# PANTALLA 1: INICIO Y MATERIAS
if menu == "🏠 Inicio / Materias":
    st.markdown('<div class="section-animated">', unsafe_allow_html=True)
    st.markdown("### 🎯 Desafío del Día")
    progreso = 100 if st.session_state.leccion_completada else 40
    st.progress(progreso / 100)
    st.write(f"¡Llevas el {progreso}% del día completado!")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("### 📚 Elige tu Materia:")
    
    # MATERIA 1: CYT
    with st.expander("🔬 CIENCIA Y TECNOLOGÍA (Color: Verde)", expanded=True):
        st.markdown('<div class="section-animated">', unsafe_allow_html=True)
        st.write("Aprende el funcionamiento del mundo y tu salud.")
        estado_lec1 = "✅ Completada" if st.session_state.leccion_completada else "▶️ Iniciar"
        if st.button(f"Lección 1: El secreto de los octógonos ({estado_lec1})", key="cyt_l1"):
            st.session_state.pantalla_actual = "leccion_cyt"
            st.rerun()
        if st.button("🔒 Lección 2: Física del movimiento (Premium)", key="cyt_l2"):
            st.warning("Esta lección requiere suscripción mensual.")
        st.markdown('</div>', unsafe_allow_html=True)
            
    # MATERIA 2: MATEMÁTICAS
    with st.expander("📐 MATEMÁTICAS (Color: Azul)"):
        st.markdown('<div class="section-animated">', unsafe_allow_html=True)
        st.write("Domina los números en tus compras del día a día.")
        if st.button("▶️ Lección 1: Cálculo de vueltos en la tienda", key="mat_l1"):
            st.info("Próximamente disponible en la siguiente actualización.")
        if st.button("🔒 Lección 2: Ecuaciones del hogar (Premium)", key="mat_l2"):
            st.warning("Esta lección requiere suscripción mensual.")
        st.markdown('</div>', unsafe_allow_html=True)

    # MATERIA 3: COMUNICACIÓN
    with st.expander("✍️ COMUNICACIÓN (Color: Rojo)"):
        st.markdown('<div class="section-animated">', unsafe_allow_html=True)
        st.write("Expresate correctamente en redes y correos.")
        if st.button("▶️ Lección 1: El punto y la coma en WhatsApp", key="com_l1"):
            st.info("Próximamente disponible.")
        st.markdown('</div>', unsafe_allow_html=True)

    # CONTROL DE FLUJO INTERNO PARA MOSTRAR LA LECCIÓN DE OCTÓGONOS
    if "pantalla_actual" in st.session_state and st.session_state.pantalla_actual == "leccion_cyt":
        st.markdown("---")
        st.markdown('<div class="section-animated">', unsafe_allow_html=True)
        st.subheader("🔬 Lección: El Secreto de los Octógonos Negros")
        
        tab1, tab2, tab3 = st.tabs(["📑 Teoría", "🎨 Ejemplo Real", "❓ El Reto"])
        
        with tab1:
            st.write("""
            ¿Te has fijado en los símbolos negros de cuatro lados en las envolturas? Se llaman **octógonos de advertencia**.
            Sirven para advertirte, de un solo vistazo, si ese producto tiene ingredientes en exceso:
            * 🧂 **Alto en Sodio:** Demasiada sal (afecta la presión).
            * 🍬 **Alto en Azúcar:** Exceso de dulce (causa diabetes).
            * 🥩 **Alto en Grasas Saturadas:** Grasas pesadas para el corazón.
            """)
            
        with tab2:
            st.write("""
            Imagina que vas a la bodega por una merienda:
            * **Cereal de caja:** Dice '¡Con Vitaminas!' pero tiene el octógono **'Alto en Azúcar'**.
            * **Yogur natural:** No tiene ningún octógono negro.
            
            **Regla de oro:** A menos octógonos, más saludable es el alimento. No te dejes llevar por la publicidad.
            """)
            
        with tab3:
            st.write("**Pregunta:** Encuentras una jamonada que dice **'Alto en Sodio'**. ¿Qué significa?")
            respuesta = st.radio("Selecciona tu respuesta:", [
                "Tiene demasiada azúcar y causa caries.",
                "Contiene mucha sal y debes moderar su consumo.",
                "Es 100% saludable porque el sodio es una vitamina."
            ])
            
            if st.button("💡 Solicitar Pista del Tutor"):
                st.markdown('<span class="icon-spin">🤖</span> Tutor IA: Recuerda que Sodio significa Sal.', unsafe_allow_html=True)
                
            if st.button("Enviar Respuesta 🚀"):
                if respuesta == "Contiene mucha sal y debes moderar su consumo.":
                    st.markdown('<div class="success-pulse">', unsafe_allow_html=True)
                    st.success("¡Excelente respuesta! El sodio es sal. Ganaste +10 puntos.")
                    st.markdown('</div>', unsafe_allow_html=True)
                    if not st.session_state.leccion_completada:
                        st.session_state.puntos += 10
                        st.session_state.leccion_completada = True
                    st.balloons()
                else:
                    st.error("Respuesta incorrecta. ¡Revisa la teoría o la pista e inténtalo de nuevo!")
        st.markdown('</div>', unsafe_allow_html=True)

# PANTALLA 2: PAYWALL (PAGO)
elif menu == "👑 Hazte Premium":
    st.markdown('<div class="section-animated">', unsafe_allow_html=True)
    st.subheader("🚀 Desbloquea Tu Máximo Potencial")
    st.write("Aprende lo esencial de la vida sin límites y prepárate al más alto nivel escolar.")
    
    st.markdown("""
    * 🌟 **Acceso ilimitado** a todos los temas avanzados y preuniversitarios.
    * 📶 **Modo Sin Internet** para estudiar donde quieras sin gastar tus datos.
    * 🤖 **Tutor de Inteligencia Artificial** 24/7 para resolver cualquier duda.
    * 🎓 **Certificados oficiales** firmados al terminar cada nivel.
    """)
    
    st.info("🎁 **Pruébalo GRATIS por 7 días.** Luego solo $3.99 USD / mes. Cancela cuando quieras.")
    
    if st.button("🌟 INICIAR MI PRUEBA GRATIS"):
        st.session_state.premium = True
        st.markdown('<div class="success-pulse">', unsafe_allow_html=True)
        st.success("¡Felicidades! Ahora tienes acceso a toda la experiencia Premium.")
        st.markdown('</div>', unsafe_allow_html=True)
        time.sleep(1)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# PANTALLA 3: PROGRESO
elif menu == "📊 Mi Progreso":
    st.markdown('<div class="section-animated">', unsafe_allow_html=True)
    st.subheader("Tus Logros Educativos")
    
    st.markdown(f"""
    <div class="metric-card">
        <h3>🏆 Puntos Totales Acumulados</h3>
        <h1>{st.session_state.puntos} PTS</h1>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.leccion_completada:
        st.markdown('<div class="success-pulse">', unsafe_allow_html=True)
        st.write("✅ Lecciones terminadas hoy: 1")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.write("❌ No has terminado lecciones hoy.")
    
    if st.session_state.premium:
        st.write("Suscripción gestionada mediante Google Play / App Store.")
        if st.button("Cancelar Suscripción (Demostración de un clic)"):
            st.session_state.premium = False
            st.info("Suscripción cancelada correctamente.")
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
