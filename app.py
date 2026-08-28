import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.title("¡Hola, mundo!")

# Mostrar una animación de globos al cargar la aplicación
st.balloons()

# Opción "Ingresar"
if st.button("Ingresar"):
    st.write("Has presionado 'Ingresar'. ¡Bienvenido!")
    # Mostrar globos también al presionar "Ingresar"
    st.balloons()

    # Crear un planeta tierra 3D interactivo con Plotly
    fig = go.Figure(data=[go.Scattergeo(
        lon = [-180, -90, 0, 90, 180],
        lat = [0, 0, 0, 0, 0],
        mode = 'markers',
        marker = dict(
            size = 0,
            color = 'rgba(0,0,0,0)'
        )
    )])
    
    fig.update_layout(geo=dict(projection_type='orthographic', showland=True, landcolor='rgb(100, 150, 80)', showocean=True, oceancolor='rgb(30, 90, 150)'))(
        projection_type = "orthographic",
        showland = True,
        landcolor = 'rgb(100, 150, 80)',
        showocean = True,
        oceancolor = 'rgb(30, 90, 150)',
        showlakes = True,
        lakecolor = 'rgb(50, 120, 180)',
        showcoastline = True,
        coastlinecolor = 'rgb(80, 120, 90)',
        coastlinewidth = 1,
        countrywidth = 0.5,
        countrycolor = 'rgb(200, 200, 200)',
        showframe = False,
        bgcolor = 'rgba(0, 0, 0, 0.1)'
    )
    
    fig.update_layout(
        title = "🌍 Planeta Tierra 3D",
        height = 600,
        margin = dict(l=0, r=0, t=50, b=0),
        paper_bgcolor = 'rgba(10, 10, 30, 0.9)',
        font = dict(color = 'white', size = 12)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.success("✨ Visualización interactiva del planeta tierra. ¡Haz clic y arrastra para rotar!")
