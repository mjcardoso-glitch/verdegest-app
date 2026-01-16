import streamlit as st
import google.generativeai as genai

st.title("🔍 Diagnóstico VerdeGest")

# 1. Configurar a Chave
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    st.success("✅ Chave de API encontrada!")
except Exception as e:
    st.error(f"❌ Erro na Chave: {e}")

# 2. Listar Modelos Disponíveis
st.write("A perguntar à Google que modelos tens disponíveis...")

try:
    found_any = False
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            st.code(f"Nome Técnico: {m.name}")
            found_any = True
    
    if not found_any:
        st.warning("⚠️ Não encontrei nenhum modelo. Verifica se a API 'Generative Language' está ativada no Google Cloud.")

except Exception as e:
    st.error(f"❌ Erro Crítico: {e}")
    st.info("Dica: Isto costuma acontecer se a Chave de API não tiver permissões suficientes.")
