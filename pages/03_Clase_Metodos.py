import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu
st.set_page_config(
    page_title="Clase 2 - Métodos",
    page_icon="⚙️",
    layout="wide"
)

# Aplicar estilos personalizados y mostrar solo flecha del menú
apply_custom_styles()

# Aplicar estilos personalizados y mostrar solo flecha del menú

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

st.title("⚙️ Clase 2: Métodos y el Parámetro Self")

# Crear menú lateral personalizado
create_sidebar_menu()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea la clase Estudiante</h3>
    <p>Debe tener:</p>
    <ul>
        <li>Atributos: <b>nombre</b>, <b>edad</b>, <b>notas</b> (lista vacía)</li>
        <li>Método: <b>agregar_nota(nota)</b> que añada a la lista</li>
        <li>Método: <b>promedio()</b> que calcule el promedio</li>
        <li>Método: <b>mostrar_info()</b> que retorne nombre y edad</li>
    </ul>
    <p><i>Pista: usa self para acceder a los atributos</i></p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🆘 Ver Solución"):
        st.code("""
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)
        return f"Nota {nota} agregada"

    def promedio(self):
        if not self.notas:
            return "No hay notas"
        return sum(self.notas) / len(self.notas)

    def mostrar_info(self):
        return f"{self.nombre}, {self.edad} años"
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")

    codigo_default = """class Estudiante:
    def __init__(self, nombre, edad):
        # Completa aquí los atributos
        pass

    def agregar_nota(self, nota):
        # Agrega la nota a la lista
        pass

    def promedio(self):
        # Calcula y retorna el promedio
        pass

    def mostrar_info(self):
        # Retorna la información del estudiante
        pass

# Prueba tu código:
est = Estudiante("Ana", 20)
print(est.mostrar_info())
print(est.agregar_nota(85))
print(est.agregar_nota(90))
print(f"Promedio: {est.promedio()}")"""

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

# Explicación adicional
st.markdown("---")
st.subheader("📚 Conceptos Clave")

col_exp1, col_exp2 = st.columns(2)

with col_exp1:
    st.markdown("""
    <div class="explicacion">
    <h3>🔍 ¿Qué es `self`?</h3>
    <p><b>Self</b> es una referencia al objeto actual:</p>
    <ul>
        <li>Siempre es el primer parámetro de un método</li>
        <li>Permite acceder a los atributos del objeto</li>
        <li>Python lo pasa automáticamente</li>
    </ul>
    <p><b>Ejemplo:</b> <code>self.nombre</code> accede al atributo nombre</p>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>⚡ Métodos vs Atributos</h3>
    <p><b>Atributos:</b> Datos del objeto (variables)</p>
    <ul>
        <li><code>self.nombre = "Juan"</code></li>
        <li>Almacenan información</li>
    </ul>
    <p><b>Métodos:</b> Acciones del objeto (funciones)</p>
    <ul>
        <li><code>def saludar(self):</code></li>
        <li>Realizan operaciones</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/02_Clase_Classes.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/04_Clase_Herencia.py")