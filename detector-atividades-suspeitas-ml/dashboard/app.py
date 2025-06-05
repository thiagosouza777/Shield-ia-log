import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="Detector de Atividades Suspeitas", layout="wide")

# Estilo escuro com azul
st.markdown("""
    <style>
        .main {
            background-color: #0f1117;
            color: #c0d6f9;
        }
        h1, h2, h3 {
            color: #4dabf7;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Dashboard de Detecção de Atividades Suspeitas")

# ======= Simulação de Dados =======
np.random.seed(42)
horas = pd.date_range(datetime.now() - timedelta(hours=23), periods=24, freq='H')
dados = pd.DataFrame({
    "Hora": horas,
    "Eventos Suspeitos": np.random.poisson(lam=20, size=24),
    "IPs Únicos": np.random.randint(5, 15, size=24),
    "Tipo de Evento": np.random.choice(["Port Scan", "Tentativa de Login", "Payload Suspeito"], size=24)
})

# ======= KPIs ==========
col1, col2, col3 = st.columns(3)
col1.metric("🚨 Total de Eventos", int(dados["Eventos Suspeitos"].sum()))
col2.metric("🌐 IPs únicos", dados["IPs Únicos"].sum())
col3.metric("🕒 Picos > 30 eventos", (dados["Eventos Suspeitos"] > 30).sum())

# ======= Gráfico de Linha =========
fig = px.line(dados, x="Hora", y="Eventos Suspeitos", title="Eventos Suspeitos por Hora", markers=True)
fig.update_layout(template="plotly_dark", title_font_color='lightblue')
st.plotly_chart(fig, use_container_width=True)

# ======= Alerta Simulado =========
if dados["Eventos Suspeitos"].iloc[-1] > 30:
    st.error("🚨 Alerta: Volume elevado de eventos na última hora!")

# ======= Tabela =========
with st.expander("🔍 Ver detalhes por hora"):
    st.dataframe(dados.style.background_gradient(cmap="Blues"))
