import streamlit as st
from utils.styles import apply_custom_styles, create_sidebar_menu

st.set_page_config(
    page_title="Curso Python POO",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Aplicar estilos personalizados y ocultar menú automático
apply_custom_styles()

st.markdown(
    """
<div class="main-header">
    <h1>🐍 Curso Completo: Programación Orientada a Objetos</h1>
    <p>Domina Python desde cero hasta crear aplicaciones reales</p>
</div>
""",
    unsafe_allow_html=True,
)

# Crear menú lateral personalizado
create_sidebar_menu()

# Contenido principal
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📚 Contenido del Curso")

    clases = [
        ("01_Introduccion.py", "🏠", "Introducción", "Conceptos básicos y setup"),
        ("02_Clase_Classes.py", "📦", "Clase 1: Classes", "Creando tu primera clase"),
        ("03_Clase_Metodos.py", "⚙️", "Clase 2: Métodos", "__init__, self y métodos"),
        ("04_Clase_Herencia.py", "🔗", "Clase 3: Herencia", "Clases hijas y super()"),
        ("05_Clase_Polimorfismo.py", "🎭", "Clase 4: Polimorfismo", "Múltiples formas"),
        ("06_Clase_Encapsulamiento.py", "🔒", "Clase 5: Encapsulamiento", "Modificadores de acceso"),
        ("07_Clase_MetodosEspeciales.py", "✨", "Clase 6: Métodos Especiales", "__str__, __repr__ y más"),
        ("08_Clase_Propiedades.py", "🏗️", "Clase 7: Propiedades", "@property y decoradores"),
        ("09_Clase_MetodosClase.py", "🔧", "Clase 8: Métodos de Clase", "@classmethod y @staticmethod"),
        ("10_Clase_Composicion.py", "🧩", "Clase 9: Composición", "has-a vs is-a"),
        ("11_Clase_MiniCalc.py", "🧮", "Clase 10: Proyecto MiniCalc", "Integración de conceptos"),
    ]

    for filename, icon, titulo, desc in clases:
        st.markdown(
            f"""
        <div class="class-card">
            <h3>{icon} {titulo}</h3>
            <p>{desc}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Botón para ir a la clase
        if st.button(f"Ir a {titulo}", key=filename):
            st.switch_page(f"pages/{filename}")

with col2:
    st.subheader("📊 Tu Progreso")
    st.progress(0, text="0% Completado")

    st.info("💡 Usa el menú lateral para navegar entre clases")

    st.markdown("### 🎯 Objetivos del Curso")
    st.markdown("""
    - ✅ Dominar POO en Python
    - ✅ Crear aplicaciones reales
    - ✅ Buenas prácticas de código
    - ✅ Patrones de diseño
    """)

st.markdown("---")
st.markdown("### 🚀 ¿Listo para empezar?")
st.write("Selecciona una clase del menú lateral o haz clic en los botones de arriba para comenzar tu viaje en la Programación Orientada a Objetos.")

st.markdown("---")
st.caption("Curso creado por ZaBaDeV con ❤️ | © 2024")