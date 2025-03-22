# app.py
import streamlit as st
import pandas as pd
from utils.plots import create_scatterplot

# Cargar datos
df = pd.read_csv("df_pivot.csv")

st.title("Visualización de Indicadores Mundiales")

# Filtros
st.sidebar.header("Opciones de visualización")

x_var = st.sidebar.selectbox("Variable en eje X:", [
    col for col in df.columns if col not in ["Country", "Year", "PIB, PPA (dólares internacionales constantes de 2021)", "Country", "Year", "PIB, PPA (dólares internacionales constantes de 2021)_log"]
])
y_var = st.sidebar.selectbox("Variable en eje Y:", [
    col for col in df.columns if col not in ["Country", "Year", "PIB, PPA (dólares internacionales constantes de 2021)", "PIB, PPA (dólares internacionales constantes de 2021)_log"]
])
year = st.sidebar.slider("Seleccionar año:", int(df["Year"].min()), int(df["Year"].max()), step=1)

# Filtrar por año
df_year = df[df["Year"] == year]

# Gráfico
st.plotly_chart(create_scatterplot(df_year, x_var, y_var))
