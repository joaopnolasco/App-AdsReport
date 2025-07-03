import streamlit as st
import pandas as pd

# senha definida
PASSWORD = "Prasoads@2025"

# sessão para controlar login
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    # tela de login
    senha = st.text_input("Digite a senha para acessar o app:", type="password")
    if st.button("Entrar"):
        if senha == PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Senha incorreta. Tente novamente.")
    st.stop()  # interrompe o resto do app até logar

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
