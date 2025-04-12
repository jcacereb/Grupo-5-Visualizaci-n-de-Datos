import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos desde Excel
df = pd.read_excel("Fuentes_datos/datosgrafico1Alejandro.xlsx", sheet_name="Empezar la investigación")

# Limpiar nombres de columnas
df.columns = [col.strip() for col in df.columns]

# Filtrar columnas con usuarios
columnas_usuarios = [col for col in df.columns if "Usuarios Activos Anuales" in col]

# Transformar a formato largo
df_long = df.melt(
    id_vars=["Nombre de la Red Social"],
    value_vars=columnas_usuarios,
    var_name="Año",
    value_name="Usuarios"
)

# Extraer el año como número
df_long["Año"] = df_long["Año"].str.extract(r"(\d{4})").astype(int)

# Pivotear para heatmap: filas = redes sociales, columnas = años
heatmap_data = df_long.pivot(index="Nombre de la Red Social", columns="Año", values="Usuarios")

# Crear Heatmap
plt.figure(figsize=(14, 8))
sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="YlGnBu", linewidths=0.5, linecolor='gray')

# Estética
plt.title("Usuarios Activos por Red Social y Año (En millones de personas)", fontsize=16)
plt.xlabel("Año")
plt.ylabel("Red Social")
plt.tight_layout()
plt.show()
