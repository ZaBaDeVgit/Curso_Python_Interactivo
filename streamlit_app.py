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
    background-color: rgba(144, 238, 144, 0.15);
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
