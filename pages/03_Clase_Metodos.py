import streamlit as st

st.set_page_config(
    page_title="Clase 2 - Métodos",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Clase 2: Métodos y Self")

with st.sidebar:
    st.title("⚙️ Clase 2")
    st.page_link("streamlit_app.py", label="🏠 Home")
    st.page_link("pages/02_Clase_Classes.py", label="⬅️ Anterior")

st.write("Contenido de la clase 2...")

if st.button("⬅️ Volver a Clase 1"):
    st.switch_page("pages/02_Clase_Classes.py")