import plotly.express as px
import pandas as pd

# Colores de las redes sociales
colores = {
    'Facebook': '#1877F2',
    'YouTube': '#FF0000',
    'Instagram': '#E4405F',
    'WhatsApp': '#25D366',
    'TikTok': '#000000',
    'LinkedIn': '#0A66C2',
    'Telegram': '#0088CC',
    'Snapchat': '#FFFC00',
    'X (Twitter)': '#666666',
    'WeChat': '#07C160'
}
df = pd.read_excel('datos_mapa_Nayely.xlsx')
#print(df)
'''# Renombrar columnas para coincidir con tu código original
df = df.rename(columns={
    'Pais': 'País',
    'TOP 1': 'TOP 1',
    'TOP 2': 'TOP 2',
    'TOP 3': 'TOP 3'
})
'''
# Texto personalizado para el hover
df['texto'] = df.apply(
    lambda x: f"<b>{x['País']}</b><br>"
              f"TOP 1:{x['TOP 1']}<br>"
              f"TOP 2:{x['TOP 2']}<br>"
              f"TOP 3:{x['TOP 3']}", 
    axis=1
)
#MAPA Coroplético
fig = px.choropleth(df, 
                    locations='País',
                    locationmode='country names',
                    color='TOP 1',
                    scope='south america', #SOLO AMERICA DEL SUR
                    color_discrete_map=colores,
                    hover_name='texto',
                    title='TOP 3 de Redes Sociales por País en Sudamérica')
fig.update_traces(
    marker=dict(
        line=dict(width=1, color='black')
    )
)

fig.update_geos(
    showcountries=True,
    countrycolor="white",
    showsubunits=True,
    subunitcolor="gray"
)

fig.update_layout(
    margin={"r":0,"t":40,"l":0,"b":0},
    font_family="Montserrat",
    hoverlabel=dict(
        bgcolor="white",
        font_size=14,
        font_family="Montserrat"
    ),
    legend_title_text='Red Social TOP 1'
)
#fig.show()
fig.write_html("Grafico_mapa_Nayely.html") 