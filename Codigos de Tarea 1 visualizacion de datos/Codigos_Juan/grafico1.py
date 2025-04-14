import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# Cargar archivo
df = pd.read_excel("Grupo-5-Visualizaci-n-de-Datos/Fuentes_datos/Datos_Grafico1_Juan.xlsx")
df = df[["Red Social", "Tiempo promedio de uso diario (en minutos)"]].dropna()
df = df.sort_values(by="Tiempo promedio de uso diario (en minutos)")

# Datos
N = len(df)
values = df["Tiempo promedio de uso diario (en minutos)"].values
labels = df["Red Social"].values
angles = np.linspace(0, 2 * np.pi, N, endpoint=False)

# Colormap azul (claro a oscuro)
norm = mcolors.Normalize(vmin=min(values), vmax=max(values))
cmap = cm.Blues
colors = cmap(norm(values))

# Crear gráfico
fig, ax = plt.subplots(figsize=(12, 12), subplot_kw={'projection': 'polar'})

# Bordes
bars = ax.bar(
    angles,
    values,
    width=2 * np.pi / N,
    color=colors,
    alpha=0.9,
    edgecolor='black',  # borde negro
    linewidth=1.5       # borde más grueso
)

# Etiquetas y valores
for angle, label, height in zip(angles, labels, values):
    rotation = np.rad2deg(angle)
    align = "right" if np.pi/2 <= angle <= 3*np.pi/2 else "left"
    
    if label.lower() in ["linkedin", "telegram"]:
        label_text = f"{label} ({height:.1f} min)"
    else:
        label_text = label

    ax.text(angle, height + 6, label_text, ha=align, va='center',
            rotation=rotation if align == "left" else rotation + 180,
            rotation_mode='anchor', fontsize=11, fontweight='bold')

    if label.lower() not in ["linkedin", "telegram"]:
        ax.text(angle, height / 2, f"{height:.1f}", ha='center', va='center',
                fontsize=10, color='white', fontweight='bold')

# Ajustes
ax.set_ylim(0, max(values) + 25)
ax.yaxis.grid(True, linestyle='--', alpha=0.25)
ax.xaxis.grid(False)
ax.set_axis_off()

# Título
plt.title("Cantidad de minutos diarios usados por red social", y=1.08, fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
