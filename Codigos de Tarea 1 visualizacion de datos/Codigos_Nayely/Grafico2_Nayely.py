import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('Fuentes_datos/Datos_Grafico2_Nayely.xlsx')
colores={
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
redes_sociales = df['Nombre de la Red Social'].tolist()
horarios = {}
for _, row in df.iterrows():
    red_social = row['Nombre de la Red Social']
    #Separamos las horas para ponerlo en una lista
    horas = [int(h) for h in str(row['Horario de mayor uso']).split(',')]
    horarios[red_social] = horas

plt.figure(figsize=(12, 8))
posiciones_y = np.arange(len(redes_sociales))

#Hacemos bloques de 1 hora, para más que quede más genial a la vista
for i, red in enumerate(redes_sociales):
    for hora in horarios[red]:
        plt.barh(i, width=0.8, height=0.6, 
                left=hora, color=colores[red], alpha=0.7)

plt.yticks(posiciones_y, redes_sociales, fontsize=10)
plt.xlabel('Horario (24h)', fontsize=12)
plt.title('Horario de mayor actividad en cada Red Social', fontsize=16, pad=20)
plt.xlim(0, 24)
plt.xticks(range(0, 25), [f"{h:02d}:00" for h in range(0, 25)], rotation=45)
plt.grid(axis='x', linestyle=':', alpha=0.4)
for hora in range(0, 25):
    plt.axvline(hora, color='gray', linestyle=':', linewidth=0.5, alpha=0.3)

leyenda = [plt.Rectangle((0,0), 1, 1, color=colores[red]) for red in redes_sociales]
plt.legend(leyenda, redes_sociales, title='Redes Sociales', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()