import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# Configurações da página
st.set_page_config(
    page_title="Shield IA - Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🔒"
)

# Título com estilo
st.markdown("""
    <h1 style='text-align: center; color: #1f77b4;'>🔒 Shield IA - Detecção de Atividades Suspeitas</h1>
    <p style='text-align: center;'>Dashboard com simulação de eventos de segurança e anomalias detectadas por Machine Learning</p>
""", unsafe_allow_html=True)

# Simulação de dados
np.random.seed(42)
dates = [datetime.now() - timedelta(minutes=i*5) for i in range(100)][::-1]
tipo_evento = ["Port Scan", "DDoS", "Access from TOR", "Botnet"]
data = pd.DataFrame({
    "timestamp": dates,
    "tipo_evento": np.random.choice(tipo_evento, size=100),
    "qtd_eventos": np.random.poisson(lam=5, size=100)
})

# Gráfico de linha com Plotly
fig = px.line(
    data,
    x="timestamp",
    y="qtd_eventos",
    color="tipo_evento",
    title="📈 Atividades suspeitas por tipo ao longo do tempo",
    template="plotly_dark",
    markers=True
)
fig.update_layout(
    font=dict(color="#B0C4DE"),
    title_font=dict(size=20),
    legend_title_text='Tipo de Evento',
    margin=dict(t=50, l=25, r=25, b=25)
)

# Exibir gráfico
st.plotly_chart(fig, use_container_width=True)

# Tabela de dados recentes
st.markdown("## 🧾 Últimos eventos registrados")
st.dataframe(data.tail(10), use_container_width=True)

# Footer estilizado
st.markdown("""
    <hr>
    <p style='text-align: center; color: gray;'>Projeto simulado - Shield IA - 2025</p>
""", unsafe_allow_html=True)

