import streamlit as st
from utils.styles import apply_custom_styles, create_sidebar_menu, create_sidebar_toggle

st.set_page_config(
    page_title="Introducción",
    page_icon="🏠",
    layout="wide"
)

# Aplicar estilos personalizados y ocultar menú automático
apply_custom_styles()

# Crear botón de toggle para el sidebar
create_sidebar_toggle()

st.title("🏠 Introducción al Curso")

# Crear menú lateral personalizado
create_sidebar_menu()

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