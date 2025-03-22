
import streamlit as st
import pandas as pd
from utils.plots import create_histogram

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("df_pivot.csv")  # o cambia al nombre real del archivo
    return df

st.title("Análisis de Datos: Histograma por Año")

# Datos
df = load_data()

# Selección de año
years = sorted(df["Year"].unique())
year = st.selectbox("Selecciona el año:", years)

# Selección de variable
variables_numericas = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
variables_numericas = [col for col in variables_numericas if col not in ['Year', 'PIB, PPA (dólares internacionales constantes de 2021)']]
var = st.selectbox("Selecciona la variable para el histograma:", variables_numericas)

# Crear histograma
fig = create_histogram(df, var, year)
st.plotly_chart(fig, use_container_width=True)
