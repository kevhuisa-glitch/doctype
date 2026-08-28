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

    # Mostrar un mapa mundi completo como planeta tierra
    # Crear una cuadrícula de puntos alrededor del mundo
    latitudes = np.linspace(-90, 90, 19)  # Filas
    longitudes = np.linspace(-180, 180, 37)  # Columnas
    
    coords_list = []
    for lat in latitudes:
        for lon in longitudes:
            coords_list.append({'lat': lat, 'lon': lon})
    
    coords = pd.DataFrame(coords_list)
    
    # Mostrar el mapa mundi completo
    st.map(coords, zoom=0)
