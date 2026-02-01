import streamlit as st

st.set_page_config(
    page_title="Curso Python POO",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    /* === OCULTAR MENÚ AUTOMÁTICO DE STREAMLIT === */
    [data-testid="stSidebarNav"] {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        position: absolute !important;
    }

    /* Ocultar el contenedor del menú automático */
    section[data-testid="stSidebar"] > div:first-child > div:first-child {
        display: none !important;
    }

    /* Para versiones más recientes de Streamlit */
    section[data-testid="stSidebar"] ul {
        display: none !important;
    }

    /* Clases adicionales que puede usar Streamlit */
    .st-emotion-cache-1gwvy71,
    .st-emotion-cache-pkbazv {
        display: none !important;
    }

    /* === MANTENER VISIBLE EL SIDEBAR PERSONALIZADO === */
    section[data-testid="stSidebar"] {
        display: block !important;
        visibility: visible !important;
    }

    /* Asegurar que los expanders se vean */
    .st-expander,
    [data-testid="stExpander"] {
        display: block !important;
        visibility: visible !important;
    }

    /* === ESTILOS PERSONALIZADOS === */
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
        background-color: rgba(255, 255, 255, 0.05);
    }

    .class-card:hover {
        transform: translateX(10px);
        background-color: rgba(102, 126, 234, 0.1);
    }

    .class-card h3 {
        margin-top: 0;
        color: #667eea;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
<div class="main-header">
    <h1>🐍 Curso Completo: Programación Orientada a Objetos</h1>
    <p>Domina Python desde cero hasta crear aplicaciones reales</p>
</div>
""",
    unsafe_allow_html=True,
)

# Sidebar con menú desplegable personalizado
with st.sidebar:
    st.title("📚 Bienvenid@s al Curso")

    st.markdown("---")

    # Menú desplegable para módulos
    with st.expander("🎯 Módulo 1: Fundamentos POO", expanded=True):
        st.page_link("streamlit_app.py", label="🏠 Inicio del Curso")
        st.page_link("pages/01_Introduccion.py", label="01. Introducción")
        st.page_link("pages/02_Clase_Classes.py", label="02. Clase 1: Classes")
        st.page_link("pages/03_Clase_Metodos.py", label="03. Clase 2: Métodos")
        st.page_link("pages/04_Clase_Herencia.py", label="04. Clase 3: Herencia")
        st.page_link("pages/05_Clase_Polimorfismo.py", label="05. Clase 4: Polimorfismo")
        st.page_link("pages/06_Clase_Encapsulamiento.py", label="06. Clase 5: Encapsulamiento")
        st.page_link("pages/07_Clase_MetodosEspeciales.py", label="07. Clase 6: Métodos Especiales")
        st.page_link("pages/08_Clase_Propiedades.py", label="08. Clase 7: Propiedades")
        st.page_link("pages/09_Clase_MetodosClase.py", label="09. Clase 8: Métodos de Clase")
        st.page_link("pages/10_Clase_Composicion.py", label="10. Clase 9: Composición")
        st.page_link("pages/11_Clase_MiniCalc.py", label="11. Clase 10: Proyecto MiniCalc")

    with st.expander("🚀 Módulo 2: POO Avanzado", expanded=False):
        st.write("Próximamente...")

    with st.expander("🏗️ Módulo 3: Patrones de Diseño", expanded=False):
        st.write("Próximamente...")

    with st.expander("🌐 Módulo 4: POO en el Mundo Real", expanded=False):
        st.write("Próximamente...")

    with st.expander("⚡ Módulo 5: POO Moderna", expanded=False):
        st.write("Próximamente...")

    st.markdown("---")
    st.caption("💡 Navega usando los módulos")

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