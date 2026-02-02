import streamlit as st
from utils.styles import apply_custom_styles, create_sidebar_menu, create_navigation_buttons, create_navigation_buttons

st.set_page_config(
    page_title="Introducción",
    page_icon="🏠",
    layout="wide"
)

# Aplicar estilos personalizados y mostrar solo flecha del menú
apply_custom_styles()

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

# Navegación inferior centrada y responsive
create_navigation_buttons(next_page="pages/02_Clase_Classes.py")