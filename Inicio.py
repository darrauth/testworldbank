import streamlit as st

st.title("📊 Bienvenido al Explorador de Indicadores Macroeconómicos")

st.markdown("""
Esta aplicación te permitirá visualizar y analizar distintos **indicadores macroeconómicos** relevantes para entender el contexto de los países a lo largo del tiempo.

A continuación, se presentan los indicadores transformados que usaremos en los análisis:

---

### 🧮 Indicadores incluidos:

- **PIB, PPA (dólares internacionales constantes de 2021)** 
  - Representa el Producto Interno Bruto ajustado por Paridad de Poder Adquisitivo. Se aplica logaritmo base 10 para estabilizar la escala.
  
- **Población urbana (% de la población total)** 
  - Proporción de la población que vive en zonas urbanas. Normalizada entre 0 y 1.

- **Efectividad del gobierno: estimación** 
  - Mide la calidad de los servicios públicos y la capacidad del gobierno para implementarlos. Estandarizada mediante Z-score.

- **Calidad regulatoria: estimación** 
  - Evalúa la capacidad del gobierno para formular y aplicar políticas y regulaciones sólidas. También estandarizada por Z-score.

---

Puedes avanzar por las pestañas del menú lateral para explorar visualizaciones, correlaciones y más análisis interactivos.
""")
