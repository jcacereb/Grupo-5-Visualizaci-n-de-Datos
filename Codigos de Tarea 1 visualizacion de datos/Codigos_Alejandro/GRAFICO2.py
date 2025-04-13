import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel
file_path = "Grupo-5-Visualizaci-n-de-Datos/Fuentes_datos/datosgrafico2Alejandro.xlsx"  # Asegúrate de que esté en el mismo directorio o proporciona la ruta completa
df = pd.read_excel(file_path, sheet_name='Empezar la investigación')

# Renombrar columnas para facilitar su uso
df.columns = ['Red_Social', 'Ingresos']

# Ordenar los datos por ingresos para una mejor visualización
df_sorted = df.sort_values('Ingresos')

# Crear el gráfico tipo Lollipop
plt.figure(figsize=(10, 6))
plt.hlines(y=df_sorted['Red_Social'], xmin=0, xmax=df_sorted['Ingresos'], color='skyblue')
plt.plot(df_sorted['Ingresos'], df_sorted['Red_Social'], "o", color='steelblue')

# Etiquetas y título
plt.xlabel('Ingresos Totales (en millones)')
plt.title('Ingresos por Red Social')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Ajustar el diseño y mostrar
plt.tight_layout()
plt.show()
