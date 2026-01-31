import streamlit as st

st.set_page_config(
    page_title="Introducción",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Introducción al Curso")

with st.sidebar:
    st.title("📚 Navegación")
    st.page_link("streamlit_app.py", label="🏠 Home")
    st.page_link("pages/02_Clase_Classes.py", label="📦 Siguiente: Classes")

st.markdown("""
## Bienvenido al curso de Python POO

En este curso aprenderás:
- Qué es la Programación Orientada a Objetos
- Cómo crear clases y objetos
- Métodos y atributos
- Herencia y polimorfismo

### ¿Qué necesitas?
- Python instalado
- Ganas de aprender
""")

st.info("👈 Haz clic en 'Siguiente: Classes' en el menú lateral para empezar")

# Navegación inferior
col1, col2, col3 = st.columns([1, 2, 1])
with col3:
    if st.button("➡️ Ir a Clase 1", type="primary"):
        st.switch_page("pages/02_Clase_Classes.py")