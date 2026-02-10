import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração visual de SaaS moderno
st.set_page_config(page_title="MédicoGestão IA", layout="wide")

# Barra Lateral de Navegação
with st.sidebar:
    st.title("🏥 MédicoGestão")
    st.markdown("---")
    aba = st.radio("Módulos", ["Dashboard Geral", "IA Contábil", "IA Atuarial"])
    st.markdown("---")
    st.info("Versão 1.0 - Natassia Atuária")

# Conteúdo de cada módulo
if aba == "Dashboard Geral":
    st.title("📊 Painel de Controle Executivo")
    
    # Cards de métricas
    m1, m2, m3 = st.columns(3)
    m1.metric("Médicos na Base", "50.000", "+12%")
    m2.metric("Receita Estimada", "R$ 1.5M", "Atuarial")
    m3.metric("Economia Fiscal", "R$ 320k", "IA")

    # Gráfico interativo
    st.subheader("Evolução Mensal")
    dados = pd.DataFrame({
        "Mês": ["Jan", "Fev", "Mar", "Abr"],
        "Receita": [10000, 15000, 12000, 18000]
    })
    fig = px.line(dados, x="Mês", y="Receita", markers=True)
    st.plotly_chart(fig, use_container_width=True)

elif aba == "IA Atuarial":
    st.title("📉 Inteligência de Risco e Reservas")
    st.write("Aqui você poderá inserir suas fórmulas de tabelas biométricas e projeções de longo prazo.")
    st.warning("Módulo em desenvolvimento: cálculos de reserva matemática ativos.")
