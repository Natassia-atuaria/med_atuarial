import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="MédicoGestão IA", layout="wide")

# Menu Lateral
with st.sidebar:
    st.title("🏥 MédicoGestão")
    menu = st.radio("Navegação", ["Início", "Cálculo Atuarial", "IA Contábil"])

if menu == "Início":
    st.title("📊 Painel Executivo")
    c1, c2, c3 = st.columns(3)
    c1.metric("Médicos na Base", "50.000", "+12%")
    c2.metric("Receita Processada", "R$ 1.5M", "8%")
    c3.metric("Economia Gerada", "R$ 420k", "IA")
    
    # Gráfico de exemplo
    df = pd.DataFrame({"Mês": ["Jan", "Fev", "Mar"], "Valor": [10, 25, 20]})
    fig = px.line(df, x="Mês", y="Valor", title="Evolução de Contratos")
    st.plotly_chart(fig, use_container_width=True)

elif menu == "Cálculo Atuarial":
    st.title("📉 Inteligência de Risco")
    st.write("Módulo para projeção de reservas e tabelas biométricas.")
