import streamlit as st
import pandas as pd

st.title("¡Hola, mundo!")

# Mostrar una animación de globos al cargar la aplicación
st.balloons()

# Opción "Ingresar"
if st.button("Ingresar"):
    st.write("Has presionado 'Ingresar'. ¡Bienvenido!")
    # Mostrar globos también al presionar "Ingresar"
    st.balloons()

    # Mostrar un mapa mundi (centrado en 0,0) con algunos puntos representativos
    coords = pd.DataFrame({
        'lat': [0, 51.5074, 40.7128, -33.8688, 35.6895, -23.5505],
        'lon': [0, -0.1278, -74.0060, 151.2093, 139.6917, -46.6333]
    })
    # Zoom bajo para ver el mapa mundi completo
    st.map(coords, zoom=0)
