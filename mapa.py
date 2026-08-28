```python
import plotly.express as px

# Usamos un dataset de ejemplo que viene con Plotly
df = px.data.gapminder().query("year == 2007")

fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp",
                    hover_name="country",
                    color_continuous_scale=px.colors.sequential.Plasma)

fig.show()
```
