#criterio:  Cantidad de personas que consumen redes sociales separadas por horas de consumo
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#preparación de datos:
df= pd.read_excel('datos_encuesta.xlsx')
contar_tiempos = df['¿Cuánto tiempo sueles pasar en estas redes sociales?'].value_counts()
tiempos_ordenados = ['0-1 hora', '2-3 horas', '4-5 horas', '6+ horas']
time_counts = contar_tiempos.reindex(tiempos_ordenados).fillna(0)

#gráfico de reloj: ocupe coordenadas polares
fig, ax = plt.subplots(figsize=(9,9), subplot_kw=dict(polar=True))
N = len(time_counts)
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
width = 2 * np.pi / N
#crear barras
bars = ax.bar(theta, time_counts.values, width=width, 
              color=plt.cm.viridis(np.linspace(0.2, 0.5, N)),
              edgecolor='white', linewidth=3)

#se añade etiquetas con porcentajes
total = time_counts.sum()
for bar, count, label in zip(bars, time_counts.values, time_counts.index):
    height = bar.get_height()
    #para que no se superponga encima, le doy otro color y más altura
    ax.text(bar.get_x() + bar.get_width()/2., height * 0.75,
            f'{count} ({count/total*100:.1f}%)',
            ha='center', va='bottom', fontsize=12, color="blue",fontweight="bold")
#el reloj gir en torno horario
ax.set_theta_offset(np.pi/2)
ax.set_theta_direction(-1)
ax.set_xticks(theta)
ax.set_xticklabels(time_counts.index, fontsize=12)
ax.set_yticks([])
ax.set_title('Cantidad de personas que consumen redes sociales separadas por horas de consumo\n', fontsize=16)

for t in np.linspace(0, 2*np.pi, 12, endpoint=False):
    ax.plot([t, t], [0, time_counts.max()*0.9], color='gray', alpha=0.3, ls=':')
plt.tight_layout()
plt.show()