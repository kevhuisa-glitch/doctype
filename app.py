import streamlit as st
import pandas as pd
import numpy as np

st.title("¡Hola, mundo!")

# Mostrar una animación de globos al cargar la aplicación
st.balloons()

# Opción "Ingresar"
if st.button("Ingresar"):
    st.write("Has presionado 'Ingresar'. ¡Bienvenido!")
    # Mostrar globos también al presionar "Ingresar"
    st.balloons()

    # Crear un mapa que representa el planeta tierra
    # Generar una malla densa de puntos para simular la forma del planeta
    latitudes = np.linspace(-90, 90, 36)
    longitudes = np.linspace(-180, 180, 72)
    
    coords_list = []
    for lat in latitudes:
        for lon in longitudes:
            coords_list.append({'lat': lat, 'lon': lon})
    
    coords = pd.DataFrame(coords_list)
    
    # Mostrar el mapa del planeta tierra
    st.map(coords, zoom=0, use_container_width=True)
    
    st.info("🌍 Este es el mapa del planeta tierra con una cuadrícula global de puntos")
