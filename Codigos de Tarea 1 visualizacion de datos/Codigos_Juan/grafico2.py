import pandas as pd
import matplotlib.pyplot as plt
import squarify
import matplotlib.colors as mcolors

# Cargar archivo
df = pd.read_excel("Grupo-5-Visualizaci-n-de-Datos/Fuentes_datos/Datos_Grafico2_Juan.xlsx")

# Asegurar formato numérico
df['Porcentaje'] = df['Porcentaje'].replace('%', '', regex=True).astype(float)

# Colores base
colores = {
    'Facebook': '#1877F2',
    'YouTube': '#FF0000',
    'Instagram': '#E4405F',
    'WhatsApp': '#25D366',
    'TikTok': '#333333',         # gris oscuro en lugar de negro puro
    'LinkedIn': '#0A66C2',
    'Telegram': '#0088CC',
    'Snapchat': '#FFFC00',
    'X (Twitter)': '#444444',    # gris oscuro para mejor visibilidad
    'WeChat': '#07C160'
}

def aclarar_color(hex_color, factor):
    rgb = mcolors.to_rgb(hex_color)
    aclarado = [1 - (1 - c) * factor for c in rgb]
    return aclarado

# Crear figura
fig, ax = plt.subplots(figsize=(16, 9))
x_offset = 0
etiquetas = []

# Generar gráfico
for red in df['Red Social'].unique():
    sub_df = df[df['Red Social'] == red]
    sizes = sub_df['Porcentaje'].values
    labels = sub_df['Rango Etario'].values
    total = sizes.sum()
    norm_sizes = [s * 100 / total for s in sizes]

    max_norm = max(norm_sizes)
    min_norm = min(norm_sizes)

    rects = squarify.squarify(
        squarify.normalize_sizes(norm_sizes, 100, 100),
        x=x_offset, y=0, dx=100, dy=100
    )

    base_color = colores.get(red, "#CCCCCC")  # gris si no definido

    for j, r in enumerate(rects):
        if max_norm - min_norm != 0:
            val = (norm_sizes[j] - min_norm) / (max_norm - min_norm)
        else:
            val = 0.5

        color = aclarar_color(base_color, 0.4 + 0.6 * val)
        text_color = 'white' if sum(color) < 1.5 else 'black'  # texto blanco en fondo oscuro

        ax.add_patch(plt.Rectangle((r['x'], r['y']), r['dx'], r['dy'],
                                   facecolor=color, edgecolor='white', linewidth=2))
        ax.text(r['x'] + r['dx']/2, r['y'] + r['dy']/2,
                f"{labels[j]}\n{sizes[j]}%", ha='center', va='center',
                fontsize=9, color=text_color)

    etiquetas.append((x_offset + 50, -8, red))
    x_offset += 110

# Ajustes de ejes
ax.set_xlim(0, x_offset)
ax.set_ylim(-10, 100)
ax.axis('off')

for x, y, red in etiquetas:
    ax.text(x, y, red, ha='center', va='top', fontsize=11, weight='bold')

plt.title('Distribución de rangos etarios por red social', fontsize=16, weight='bold')
plt.tight_layout()
plt.show()
