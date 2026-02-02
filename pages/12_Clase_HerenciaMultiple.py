import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu

st.set_page_config(
    page_title="Clase 11 - Herencia Múltiple",
    page_icon="🔀",
    layout="wide"
)

# Aplicar estilos personalizados y ocultar menú automático
apply_custom_styles()

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

st.title("🔀 Clase 11: Herencia Múltiple")

# Crear menú lateral personalizado
create_sidebar_menu()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea sistema de Personajes Multifunción</h3>
    <p>Crea:</p>
    <ul>
        <li>Clase <b>Volador</b> con método volar()</li>
        <li>Clase <b>Nadador</b> con método nadar()</li>
        <li>Clase <b>Caminante</b> con método caminar()</li>
        <li>Clase <b>SuperHeroe</b> que hereda de las tres</li>
        <li>Usa <b>super()</b> apropiadamente</li>
    </ul>
    <p><i>Pista: Python usa MRO para resolver conflictos</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🆘 Ver Solución"):
        st.code("""
class Volador:
    def __init__(self, altura_max=1000):
        self.altura_max = altura_max
    
    def volar(self):
        return "🦅 Estoy volando a {self.altura_max}m de altura!"

class Nadador:
    def __init__(self, profundidad_max=100):
        self.profundidad_max = profundidad_max
    
    def nadar(self):
        return "🐟 Estoy nadando a {self.profundidad_max}m de profundidad!"

class Caminante:
    def __init__(self, velocidad=10):
        self.velocidad = velocidad
    
    def caminar(self):
        return "🚶 Estoy caminando a {self.velocidad} km/h!"

class SuperHeroe(Volador, Nadador, Caminante):
    def __init__(self, nombre, altura_max=2000, profundidad_max=200, velocidad=20):
        self.nombre = nombre
        # Inicializar todas las clases padre
        Volador.__init__(self, altura_max)
        Nadador.__init__(self, profundidad_max)
        Caminante.__init__(self, velocidad)
    
    def presentar(self):
        return f"⚡ Soy {self.nombre} y puedo hacer todo!"
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")
    
    codigo_default = """class Volador:
    def __init__(self, altura_max=1000):
        self.altura_max = altura_max
    
    def volar(self):
        # Retorna mensaje de vuelo
        pass

class Nadador:
    def __init__(self, profundidad_max=100):
        self.profundidad_max = profundidad_max
    
    def nadar(self):
        # Retorna mensaje de nado
        pass

class Caminante:
    def __init__(self, velocidad=10):
        self.velocidad = velocidad
    
    def caminar(self):
        # Retorna mensaje de caminata
        pass

class SuperHeroe(Volador, Nadador, Caminante):
    def __init__(self, nombre, altura_max=2000, profundidad_max=200, velocidad=20):
        self.nombre = nombre
        # Inicializa las clases padre
        pass
    
    def presentar(self):
        # Retorna presentación del superhéroe
        pass

# Prueba tu código:
hero = SuperHeroe("Aquaman")
print(hero.presentar())
print(hero.volar())
print(hero.nadar())
print(hero.caminar())"""

    codigo = st.text_area("Escribe tu código:", value=codigo_default, height=350)
    
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
    <h3>🔀 ¿Qué es Herencia Múltiple?</h3>
    <p>Permite que una clase herede de múltiples clases padre:</p>
    <ul>
        <li>Una clase puede tener varios padres</li>
        <li>Python usa MRO (Method Resolution Order)</li>
        <li>Resuelve conflictos automáticamente</li>
    </ul>
    <p><b>Sintaxis:</b> <code>class Hija(Padre1, Padre2):</code></p>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>🔄 MRO (Method Resolution Order)</h3>
    <p>Python define el orden de búsqueda de métodos:</p>
    <ul>
        <li>Busca en la clase actual primero</li>
        <li>Luego en los padres en orden</li>
        <li>Usa algoritmo C3 linearización</li>
    </ul>
    <p><b>Ver MRO:</b> <code>Clase.__mro__</code></p>
    </div>
    """, unsafe_allow_html=True)

# Ejemplos adicionales
st.markdown("---")
st.subheader("💡 Ejemplos Prácticos")

col_ej1, col_ej2 = st.columns(2)

with col_ej1:
    st.markdown("""
    <div class="explicacion">
    <h3>🎮 Ejemplo: Videojuego</h3>
    <p>Un personaje puede ser:</p>
    <ul>
        <li><b>Atacante</b> - tiene ataque()</li>
        <li><b>Defensor</b> - tiene defender()</li>
        <li><b>Mago</b> - tiene hechizar()</li>
    </ul>
    <p>GuerreroMago hereda de todos:</p>
    <pre><code>class GuerreroMago(Atacante, Defensor, Mago):
    def __init__(self):
        # Puede atacar, defender y hechizar
        pass</code></pre>
    </div>
    """, unsafe_allow_html=True)

with col_ej2:
    st.markdown("""
    <div class="explicacion">
    <h3>🏢 Ejemplo: Sistema Empresarial</h3>
    <p>Un empleado puede ser:</p>
    <ul>
        <li><b>Trabajador</b> - tiene trabajar()</li>
        <li><b>Gerente</b> - tiene gestionar()</li>
        <li><b>Capacitador</b> - tiene enseñar()</li>
    </ul>
    <p>GerenteCapacitador hereda de ambos:</p>
    <pre><code>class GerenteCapacitador(Gerente, Capacitador):
    def __init__(self):
        # Puede gestionar y enseñar
        pass</code></pre>
    </div>
    """, unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/11_Clase_MiniCalc.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/13_Clase_Abstractas.py")
