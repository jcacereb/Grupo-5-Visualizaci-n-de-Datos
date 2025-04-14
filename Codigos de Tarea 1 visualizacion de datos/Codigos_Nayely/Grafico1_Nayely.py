import pandas as pd
import plotly.express as px

df = pd.read_excel('Grupo-5-Visualizaci-n-de-Datos/Fuentes_datos/Datos_Grafico1_Nayely.xlsx')
df_long = df.melt(id_vars="Nombre de la Red Social", var_name="Continente", value_name="Usuarios (millones)")
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

#Grafico de barras por continente:
fig = px.bar(df_long, x="Continente", y="Usuarios (millones)", color="Nombre de la Red Social", title="Distribución geográfica de usuarios de Redes Sociales",
             text="Usuarios (millones)",
             color_discrete_map=colores)
fig.update_layout(barmode="stack", xaxis_title="Continente", yaxis_title="Usuarios (millones)", legend_title="Red Social")
fig.show()
#Al usar plotly, el grafico es interactivo por lo que es necesario descargarlo como un html si se quiere interactuar con la grafica
#fig.write_html("Grafico2_Nayely.html")  #Con esta linea se genera el html, aunque en GitHub igual estoy dejando el html listo.