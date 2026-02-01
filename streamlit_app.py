import streamlit as st

st.set_page_config(
    page_title="Curso Python POO",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
    .main-header {
        text-align: center;
        padding: 3rem 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    .class-card {
        padding: 2rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
        transition: transform 0.3s;
    }
  .class-card:hover {
    transform: translateX(10px);
    background-color: rgba(200, 255, 200, 0.2);
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="main-header">
    <h1>🐍 Curso Completo: Programación Orientada a Objetos</h1>
    <p>Domina Python desde cero hasta crear aplicaciones reales</p>
</div>
""",
    unsafe_allow_html=True,
)

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
    st.info("💡 Usa el menú lateral (arriba a la izquierda) para navegar entre clases")

st.markdown("---")
st.caption("Curso creado por ZaBaDeV ❤️")
