import streamlit as st
from io import StringIO
import sys

st.set_page_config(
    page_title="Clase 4 - Polimorfismo",
    page_icon="🎭",
    layout="wide"
)

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

# Sidebar
with st.sidebar:
    st.title("🎭 Clase 4: Polimorfismo")
    st.markdown("""
    ### Objetivos:
    1. Entender el polimorfismo
    2. Usar métodos con mismo nombre
    3. Crear interfaces comunes
    4. Aplicar duck typing
    
    ### Navegación:
    """)
    st.page_link("streamlit_app.py", label="🏠 Home")
    st.page_link("pages/04_Clase_Herencia.py", label="⬅️ Anterior")
    st.page_link("pages/06_Clase_Encapsulamiento.py", label="➡️ Siguiente")

st.title("🎭 Clase 4: Polimorfismo - Múltiples Formas")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea sistema de Figuras</h3>
    <p>Crea:</p>
    <ul>
        <li>Clase base: <b>Figura</b> con método <b>area()</b></li>
        <li>Clase <b>Cuadrado</b> con lado</li>
        <li>Clase <b>Círculo</b> con radio</li>
        <li>Clase <b>Triángulo</b> con base y altura</li>
        <li>Función <b>calcular_area(figura)</b></li>
    </ul>
    <p><i>Pista: todas deben tener método area()</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🆘 Ver Solución"):
        st.code("""
import math

class Figura:
    def area(self):
        raise NotImplementedError("Debe implementar area()")

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2

def calcular_area(figura):
    return figura.area()
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")
    
    codigo_default = """import math

class Figura:
    def area(self):
        # Implementa método base
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        # Calcula área del cuadrado
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        # Calcula área del círculo
        pass

def calcular_area(figura):
    # Llama al método area de cualquier figura
    pass

# Prueba tu código:
figuras = [
    Cuadrado(5),
    Circulo(3),
    Triangulo(4, 6)
]

for fig in figuras:
    print(f"Área: {calcular_area(fig):.2f}")"""

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
    <h3>🎭 ¿Qué es Polimorfismo?</h3>
    <p>Significa "muchas formas" en programación:</p>
    <ul>
        <li>Objetos diferentes responden al mismo mensaje</li>
        <li>Métodos con mismo nombre en clases distintas</li>
        <li>Permite tratar objetos de forma uniforme</li>
    </ul>
    <p><b>Ejemplo:</b> figura.area() funciona para cuadrados, círculos, etc.</p>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>🦆 Duck Typing</h3>
    <p>"Si camina como pato y grazna como pato..."</p>
    <ul>
        <li>No importa el tipo, solo los métodos</li>
        <li>Si tiene el método necesario, funciona</li>
        <li>Python es dinámicamente tipado</li>
    </ul>
    <p><b>Principio:</b> "Si tiene area(), es una figura"</p>
    </div>
    """, unsafe_allow_html=True)

# Ejemplo visual
st.markdown("---")
st.subheader("🎨 Ejemplo de Polimorfismo")

st.markdown("""
<div class="explicacion">
<h3>🔄 Mismo Método, Diferentes Comportamientos</h3>
<pre>
Cuadrado.area() → lado²
Círculo.area()   → π × radio²
Triángulo.area() → (base × altura) / 2
</pre>
<p>Todos tienen el método area() pero cada uno lo implementa a su manera</p>
<p>Esto permite escribir código genérico que funciona con cualquier figura</p>
</div>
""", unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/04_Clase_Herencia.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/06_Clase_Encapsulamiento.py")
