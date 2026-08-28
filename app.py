import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Mapamundi Interactivo", page_icon="🌍", layout="centered")

st.title("🌍 Mapamundi Interactivo")

# Crear mapamundi 3D interactivo
fig = go.Figure(data=[go.Scattergeo(
    lon = [-180, -90, 0, 90, 180],
    lat = [0, 0, 0, 0, 0],
    mode = 'markers',
    marker = dict(
        size = 0,
        color = 'rgba(0,0,0,0)'
    )
)])

fig.update_layout(
    geo=dict(
        projection_type='orthographic',
        showland=True,
        landcolor='rgb(100, 150, 80)',
        showocean=True,
        oceancolor='rgb(30, 90, 150)',
        showlakes=True,
        lakecolor='rgb(50, 120, 180)',
        showcoastline=True,
        coastlinecolor='rgb(80, 120, 90)',
        coastlinewidth=1,
        countrywidth=0.5,
        countrycolor='rgb(200, 200, 200)',
        showframe=False,
        bgcolor='rgba(0, 0, 0, 0.1)'
    ),
    title="🌍 Planeta Tierra 3D",
    height=600,
    margin=dict(l=0, r=0, t=50, b=0),
    paper_bgcolor='rgba(10, 10, 30, 0.9)',
    font=dict(color='white', size=12)
)

st.plotly_chart(fig, use_container_width=True)

st.success("✨ Visualización interactiva del planeta tierra. ¡Haz clic y arrastra para rotar!")
