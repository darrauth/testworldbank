import streamlit as st
import pandas as pd
from utils import plots as u  # Importamos el módulo de gráficos

# Cargar datos
@st.cache_data
def cargar_datos():
    df = pd.read_csv("df_pivot.csv")
    return df

df = cargar_datos()

# Título
st.title("📈 Evolución de Indicadores por País")

# Opciones para eje Y
columnas_numericas = df.select_dtypes(include='number').columns.tolist()
opciones_eje_y = [col for col in columnas_numericas if col not in ['Year']]

# Selectores
indicador = st.selectbox("Selecciona el indicador para el eje Y:", opciones_eje_y)
paises = df['Country'].unique()
paises_seleccionados = st.multiselect(
    "Selecciona los países a mostrar:",
    paises,
    default=["Colombia", "Alemania", "Estados Unidos"]
)

# Crear gráfico
fig = u.crear_grafico_evolutivo(df, indicador, paises_seleccionados)

# Mostrar
st.plotly_chart(fig, use_container_width=True)
