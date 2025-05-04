#criterio: Diversidad de uso de redes sociales por persona
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

#leer el archivo y organizar los datos:
df= pd.read_excel('datos_encuesta.xlsx')
redes_por_persona =df['¿Qué redes sociales son las que más utilizas en el día?'].tolist()
df = pd.DataFrame({'persona': [f'Persona {i+1}' for i in range(len(redes_por_persona))],
                   'redes': redes_por_persona})
#como tenemos más de una red social por persona, separamos las redes sociales y las ponemos en una lista
df_exploded = df.assign(redes=df['redes'].str.split(', ')).explode('redes')

persona_indices = {persona: i for i, persona in enumerate(df['persona'])}
redes_unicas = df_exploded['redes'].unique().tolist()
red_indices = {red: i + len(persona_indices) for i, red in enumerate(redes_unicas)}

source = []
target = []
value = []
#creacion de los links
for _, row in df_exploded.iterrows():
    source.append(persona_indices[row['persona']])
    target.append(red_indices[row['redes']])
    value.append(1)
#colores para las redes sociales y las personas
colores = {
    'Facebook': '#1877F2',
    'Youtube': '#FF0000',
    'Instagram': '#E4405F',
    'WhatsApp': '#25D366',
    'TikTok': '#000000',
    'LinkedIn': '#0A66C2',
    'Telegram': '#0088CC',
    'SnapChat': '#FFFC00',
    'X (Twitter)': '#666666',
    'WeChat': '#07C160'}

labels = list(persona_indices.keys()) + redes_unicas
node_colors = ['#A9A9A9'] * len(persona_indices)
node_colors += [colores.get(red, '#CCCCCC') for red in redes_unicas]

# Diagrama Sankey con Plotly, las sources serán grises
fig = go.Figure(data=[go.Sankey(
    node=dict(label=labels, color=node_colors),
    link=dict(source=source, target=target, value=value,
              color=["rgba(150,150,150,0.3)"] * len(source))
)])
fig.update_layout(title_text="Diversidad de uso de redes sociales por persona", font_size=10)
#La siquiente línea es para guardar el gráfico como un archivo HTML.
#fig.write_html("Grafico_Nayely.html") 
