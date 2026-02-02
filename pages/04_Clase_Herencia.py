import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu, create_sidebar_toggle

st.set_page_config(
    page_title="Clase 3 - Herencia",
    page_icon="🔗",
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

# Crear menú lateral personalizado
create_sidebar_menu()

st.title("🔗 Clase 3: Herencia y Clases Hijas")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea jerarquía de Animales</h3>
    <p>Crea:</p>
    <ul>
        <li>Clase base: <b>Animal</b> con nombre y edad</li>
        <li>Clase hija: <b>Perro</b> con raza</li>
        <li>Clase hija: <b>Gato</b> con vidas (7 por defecto)</li>
        <li>Método <b>hacer_sonido()</b> para cada uno</li>
        <li>Usa <b>super().__init__()</b></li>
    </ul>
    <p><i>Pista: class Perro(Animal):</i></p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🆘 Ver Solución"):
        st.code("""
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def __init__(self, nombre, edad, vidas=7):
        super().__init__(nombre, edad)
        self.vidas = vidas

    def hacer_sonido(self):
        return "¡Miau!"
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")

    codigo_default = """class Animal:
    def __init__(self, nombre, edad):
        # Completa los atributos base
        pass

    def hacer_sonido(self):
        # Retorna un sonido genérico
        pass

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llama al __init__ de Animal y agrega raza
        pass

    def hacer_sonido(self):
        # Retorna "¡Guau!"
        pass

class Gato(Animal):
    def __init__(self, nombre, edad, vidas=7):
        # Llama al __init__ de Animal y agrega vidas
        pass

    def hacer_sonido(self):
        # Retorna "¡Miau!"
        pass

# Prueba tu código:
perro = Perro("Fido", 3, "Labrador")
gato = Gato("Michi", 2)
print(f"{perro.nombre} dice: {perro.hacer_sonido()}")
print(f"{gato.nombre} dice: {gato.hacer_sonido()}")"""

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
    <h3>🔗 ¿Qué es Herencia?</h3>
    <p>Es un mecanismo para crear nuevas clases basadas en existentes:</p>
    <ul>
        <li><b>Clase Padre:</b> Contiene atributos y métodos comunes</li>
        <li><b>Clase Hija:</b> Hereda y puede extender funcionalidades</li>
        <li><b>Reutilización:</b> Evita duplicar código</li>
    </ul>
    <p><b>Sintaxis:</b> <code>class Hija(Padre):</code></p>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>⚡ super() y __init__</h3>
    <p><b>super():</b> Permite acceder a métodos de la clase padre</p>
    <ul>
        <li><code>super().__init__()</code> llama al constructor padre</li>
        <li>Útil para inicializar atributos heredados</li>
        <li>Puede usarse con otros métodos también</li>
    </ul>
    <p><b>Sobreescritura:</b> Una clase hija puede redefinir métodos del padre</p>
    </div>
    """, unsafe_allow_html=True)

# Ejemplo visual
st.markdown("---")
st.subheader("🎨 Ejemplo Visual")

st.markdown("""
<div class="explicacion">
<h3>📊 Jerarquía de Clases</h3>
<pre>
        Animal
       /      \\
    Perro     Gato
    (raza)   (vidas)
</pre>
<p>Animal es la clase base con atributos comunes (nombre, edad)</p>
<p>Perro y Gato heredan esos atributos y agregan los suyos</p>
</div>
""", unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/03_Clase_Metodos.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/05_Clase_Polimorfismo.py")
