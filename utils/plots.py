import plotly.graph_objs as go
import pandas as pd
import plotly.express as px



def crear_grafico_evolutivo(df: pd.DataFrame, indicador: str, paises: list) -> go.Figure:
    df_filtrado = df[df['Country'].isin(paises)]

    fig = go.Figure()

    for pais in paises:
        datos_pais = df_filtrado[df_filtrado['Country'] == pais]
        fig.add_trace(go.Scatter(
            x=datos_pais['Year'],
            y=datos_pais[indicador],
            mode='lines+markers',
            name=pais
        ))

    fig.update_layout(
        title=f"Evolutivo de {indicador}",
        xaxis_title="Año",
        yaxis_title=indicador,
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        legend_title="País"
    )

    return fig



def create_scatterplot(df: pd.DataFrame, x: str, y: str):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        size="PIB, PPA (dólares internacionales constantes de 2021)",
        hover_name="Country",
        color="Country",
        size_max=60,
        title=f"Relación entre {x} y {y} (tamaño = PIB)"
    )
    fig.update_layout(
        xaxis_title=x,
        yaxis_title=y,
        hovermode='closest',
        showlegend=False
    )
    return fig




def create_histogram(data: pd.DataFrame, variable: str, year: int):
    df_year = data[data["Year"] == year]
    fig = px.histogram(
        df_year,
        x=variable,
        nbins=20,
        title=f'Distribución de "{variable}" en {year}',
        labels={variable: variable},
        opacity=0.75
    )
    fig.update_layout(bargap=0.1)
    return fig
