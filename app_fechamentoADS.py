import streamlit as st
import pandas as pd

st.set_page_config(page_title="Praso Ads - Reports de fechamento", layout="centered")

st.title("📊 Praso Ads - Reports de fechamento")

st.write("Faça o upload do CSV com os dados de fechamento:")

# Upload do CSV
arquivo = st.file_uploader("Arraste e solte o arquivo aqui", type=["csv"])
if arquivo is not None:
    df = pd.read_csv(arquivo)

    # Exibe os nomes disponíveis
    industrias_disponiveis = sorted(df["industria"].unique())
    
    # Dropdown com busca
    industria_selecionada = st.selectbox("Selecione a indústria:", industrias_disponiveis)

    # Filtra e mostra o texto
    texto = df[df["industria"] == industria_selecionada]["texto"].values
    if len(texto) > 0:
        st.subheader("Texto de fechamento:")
        st.code(texto[0], language="markdown")
    else:
        st.warning("Texto não encontrado para esta indústria.")
