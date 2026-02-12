import streamlit as st


def calcular_constancia(horas, logica, leitura, foco):
    pontos = (horas*2) + (logica*3) + (leitura*2) + foco
    return pontos


def gerar_mensagem(pontos):
    if pontos >= 20:
        return "Você está imparável! continue assim."
    elif pontos >= 10:
        return "Boa constância. Ajuste pequenos detalhes."
    else:
        return "Lembre-se: constância>pressa."


st.set_page_config(page_title="Constância IA", page_icon="")

st.title("Constância IA")
st.subheader("Seu assistente inteligente de disciplina.")

horas = st.number_input("Horas estudadas hoje", min_value=0.0, step=0.5)
logica = st.selectbox("Estudou lógica?", [0, 1])
leitura = st.selectbox("Fez leitura técnica? ", [0, 1])
foco = st.slider("Nível de foco", 0, 10)

if st.button("Calcula desempenho"):
    pontos = calcular_constancia(horas, logica, leitura, foco)
    mensagem = gerar_mensagem(pontos)
    st.metric("pontuação de constância", pontos)
    st.success(mensagem)
