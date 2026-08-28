import streamlit as st

st.title("¡Hola, mundo!")

# Mostrar una animación de globos al cargar la aplicación
st.balloons()

# Opción "Ingresar"
if st.button("Ingresar"):
    st.write("Has presionado 'Ingresar'. ¡Bienvenido!")
    # Mostrar globos también al presionar "Ingresar"
    st.balloons()
