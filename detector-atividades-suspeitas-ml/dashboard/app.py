import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Configuração de página
st.set_page_config(
    page_title="Detector de Atividades Suspeitas",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tema escuro
st.markdown(
    """
    <style>
        body {
            background-color: #0e1117;
            color: #c9d1d9;
        }
        .main {
            background-color: #0e1117;
        }
        h1 {
            color: #58a6ff;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.title("🛡️ Dashboard de Detecção de Atividades Suspeitas")

# Simulando dados
dias = pd.date_range(end=pd.Timestamp.today(), periods=15)
dados_simulados = {
    "Data": dias,
    "Conexões Suspeitas": np.random.randint(5, 100, size=15),
    "Anomalias Detectadas": np.random.randint(0, 20, size=15)
}
df = pd.DataFrame(dados_simulados)

# Gráfico de conexões suspeitas
st.subheader("📈 Conexões Suspeitas (últimos 15 dias)")
chart1 = alt.Chart(df).mark_line(point=True).encode(
    x='Data:T',
    y='Conexões Suspeitas:Q',
    tooltip=['Data:T', 'Conexões Suspeitas']
).properties(
    width=800,
    height=300
).configure_mark(
    color='#58a6ff'
)

st.altair_chart(chart1)

# Gráfico de anomalias
st.subheader("🚨 Anomalias Detectadas")
chart2 = alt.Chart(df).mark_bar().encode(
    x='Data:T',
    y='Anomalias Detectadas:Q',
    tooltip=['Data:T', 'Anomalias Detectadas']
).properties(
    width=800,
    height=300
).configure_mark(
    color='#ff4b4b'
)

st.altair_chart(chart2)

# Mensagem final
st.info("Os dados acima são apenas uma simulação. Integrações com logs reais devem ser configuradas.")
