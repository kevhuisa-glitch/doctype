import streamlit as st

# Configuración de la página simulando una pantalla móvil
st.set_page_config(page_title="App Educativa Esencial", page_icon="🎓", layout="centered")

# Inicializar variables de estado del usuario (Base de datos temporal)
if "puntos" not in st.session_state:
    st.session_state.puntos = 150
if "nivel" not in st.session_state:
    st.session_state.nivel = "Secundaria"
if "premium" not in st.session_state:
    st.session_state.premium = False
if "leccion_completada" not in st.session_state:
    st.session_state.leccion_completada = False

# CABECERA DE LA APP
st.title("🎓 Academia Esencial")
col_perfil, col_pts = st.columns([2, 1])
with col_perfil:
    st.write(f"👤 **Mi Perfil:** Nivel {st.session_state.nivel}")
with col_pts:
    st.subheader(f"🏆 {st.session_state.puntos} pts")

if st.session_state.premium:
    st.success("👑 Cuenta Premium Activa (Acceso Ilimitado)")

st.markdown("---")

# BARRA DE NAVEGACIÓN SIMULADA
menu = st.sidebar.radio("Navegación", ["🏠 Inicio / Materias", "👑 Hazte Premium", "📊 Mi Progreso"])

# PANTALLA 1: INICIO Y MATERIAS
if menu == "🏠 Inicio / Materias":
    st.markdown("### 🎯 Desafío del Día")
    progreso = 100 if st.session_state.leccion_completada else 40
    st.progress(progreso / 100)
    st.write(f"¡Llevas el {progreso}% del día completado!")
    
    st.markdown("### 📚 Elige tu Materia:")
    
    # MATERIA 1: CYT
    with st.expander("🔬 CIENCIA Y TECNOLOGÍA (Color: Verde)", expanded=True):
        st.write("Aprende el funcionamiento del mundo y tu salud.")
        estado_lec1 = "✅ Completada" if st.session_state.leccion_completada else "▶️ Iniciar"
        if st.button(f"Lección 1: El secreto de los octógonos ({estado_lec1})", key="cyt_l1"):
            st.session_state.pantalla_actual = "leccion_cyt"
            st.rerun()
        if st.button("🔒 Lección 2: Física del movimiento (Premium)", key="cyt_l2"):
            st.warning("Esta lección requiere suscripción mensual.")
            
    # MATERIA 2: MATEMÁTICAS
    with st.expander("📐 MATEMÁTICAS (Color: Azul)"):
        st.write("Domina los números en tus compras del día a día.")
        if st.button("▶️ Lección 1: Cálculo de vueltos en la tienda", key="mat_l1"):
            st.info("Próximamente disponible en la siguiente actualización.")
        if st.button("🔒 Lección 2: Ecuaciones del hogar (Premium)", key="mat_l2"):
            st.warning("Esta lección requiere suscripción mensual.")

    # MATERIA 3: COMUNICACIÓN
    with st.expander("✍️ COMUNICACIÓN (Color: Rojo)"):
        st.write("Expresate correctamente en redes y correos.")
        if st.button("▶️ Lección 1: El punto y la coma en WhatsApp", key="com_l1"):
            st.info("Próximamente disponible.")

    # CONTROL DE FLUJO INTERNO PARA MOSTRAR LA LECCIÓN DE OCTÓGONOS
    if "pantalla_actual" in st.session_state and st.session_state.pantalla_actual == "leccion_cyt":
        st.markdown("---")
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
                st.info("🤖 Tutor IA: Recuerda que Sodio significa Sal.")
                
            if st.button("Enviar Respuesta 🚀"):
                if respuesta == "Contiene mucha sal y debes moderar su consumo.":
                    st.success("¡Excelente respuesta! El sodio es sal. Ganaste +10 puntos.")
                    if not st.session_state.leccion_completada:
                        st.session_state.puntos += 10
                        st.session_state.leccion_completada = True
                    st.balloons()
                else:
                    st.error("Respuesta incorrecta. ¡Revisa la teoría o la pista e inténtalo de nuevo!")

# PANTALLA 2: PAYWALL (PAGO)
elif menu == "👑 Hazte Premium":
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
        st.success("¡Felicidades! Ahora tienes acceso a toda la experiencia Premium.")
        st.rerun()

# PANTALLA 3: PROGRESO
elif menu == "📊 Mi Progreso":
    st.subheader("Tus Logros Educativos")
    st.metric(label="Puntos Totales Acumulados", value=f"{st.session_state.puntos} PTS")
    st.write("✅ Lecciones terminadas hoy: 1" if st.session_state.leccion_completada else "❌ No has terminado lecciones hoy.")
    
    if st.session_state.premium:
        st.write("Suscripción gestionada mediante Google Play / App Store.")
        if st.button("Cancelar Suscripción (Demostración de un clic)"):
            st.session_state.premium = False
            st.info("Suscripción cancelada correctamente.")
            st.rerun()
