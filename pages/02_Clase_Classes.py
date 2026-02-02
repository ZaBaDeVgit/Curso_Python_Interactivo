import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu, create_sidebar_toggle

st.set_page_config(
    page_title="Clase 1 - Classes",
    page_icon="📦",
    layout="wide"
)

# Aplicar estilos personalizados y ocultar menú automático
apply_custom_styles()

# Crear botón de toggle para el sidebar
create_sidebar_toggle()

st.markdown("""
<style>
    .explicacion {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
        color: #000000 !important;
    }
    .explicacion h3, .explicacion p, .explicacion li, .explicacion b {
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("📦 Clase 1: Creando tu primera Clase")

# Crear menú lateral personalizado
create_sidebar_menu()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea la clase Coche</h3>
    <p>Debe tener:</p>
    <ul>
        <li>Atributos: <b>marca</b>, <b>modelo</b>, <b>encendido</b> (bool)</li>
        <li>Método: <b>arrancar()</b> que cambie encendido a True</li>
        <li>Método: <b>estado()</b> que diga si está encendido o apagado</li>
    </ul>
    <p><i>Pista: usa self.atributo = valor</i></p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🆘 Ver Solución"):
        st.code("""
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    def arrancar(self):
        self.encendido = True
        return "¡Brrrum!"

    def estado(self):
        if self.encendido:
            return f"{self.marca} está encendido"
        return f"{self.marca} está apagado"
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")

    codigo_default = """class Coche:
    def __init__(self, marca, modelo):
        # Completa aquí los atributos
        pass

    def arrancar(self):
        # Cambia encendido a True
        pass

    def estado(self):
        # Retorna el estado
        pass

# Prueba tu código:
mi_coche = Coche("Toyota", "Corolla")
print(mi_coche.arrancar())
print(mi_coche.estado())"""

    codigo = st.text_area("Escribe tu código:", value=codigo_default, height=300)

    if st.button("▶️ Ejecutar Código", type="primary"):
        old_stdout = sys.stdout
        sys.stdout = buffer = StringIO()

        try:
            exec(codigo, {"__name__": "__main__"})
            sys.stdout = old_stdout
            output = buffer.getvalue()

            if output:
                st.success("✅ Resultado:")
                st.code(output, language="text")
            else:
                st.warning("No hay salida. ¿Usaste print()?")
        except Exception as e:
            sys.stdout = old_stdout
            st.error(f"❌ Error: {e}")

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/01_Introduccion.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/03_Clase_Metodos.py")