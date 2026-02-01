import streamlit as st
from io import StringIO
import sys

st.set_page_config(
    page_title="Clase 6 - Métodos Especiales",
    page_icon="✨",
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
    st.title("✨ Clase 6: Métodos Especiales")
    st.markdown("""
    ### Objetivos:
    1. Entender métodos mágicos
    2. Implementar __str__ y __repr__
    3. Sobrecargar operadores
    4. Usar métodos de comparación
    
    ### Navegación:
    """)
    st.page_link("streamlit_app.py", label="🏠 Home")
    st.page_link("pages/06_Clase_Encapsulamiento.py", label="⬅️ Anterior")
    st.page_link("pages/08_Clase_Propiedades.py", label="➡️ Siguiente")

st.title("✨ Clase 6: Métodos Especiales (Dunder Methods)")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea clase Vector2D</h3>
    <p>Debe tener:</p>
    <ul>
        <li>Atributos: <b>x</b>, <b>y</b></li>
        <li><b>__str__()</b> para representación amigable</li>
        <li><b>__repr__()</b> para representación técnica</li>
        <li><b>__add__()</b> para sumar vectores</li>
        <li><b>__eq__()</b> para comparar vectores</li>
        <li><b>__len__()</b> para obtener magnitud</li>
    </ul>
    <p><i>Pista: usa __ antes y después del nombre</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🆘 Ver Solución"):
        st.code("""
import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False
    
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")
    
    codigo_default = """import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        # Retorna representación amigable: "Vector(x, y)"
        pass
    
    def __repr__(self):
        # Retorna representación técnica: "Vector2D(x, y)"
        pass
    
    def __add__(self, other):
        # Suma componente a componente
        pass
    
    def __eq__(self, other):
        # Compara si son iguales
        pass
    
    def __len__(self):
        # Retorna la magnitud como entero
        pass

# Prueba tu código:
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
v3 = Vector2D(3, 4)

print(str(v1))
print(repr(v1))
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == v3: {v1 == v3}")
print(f"Magnitud de v1: {len(v1)}")"""

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
    <h3>✨ ¿Qué son Métodos Especiales?</h3>
    <p>También llamados "dunder methods" (double underscore):</p>
    <ul>
        <li>Comienzan y terminan con __</li>
        <li>Python los llama automáticamente</li>
        <li>Permiten personalizar comportamiento</li>
        <li>Sobrecarga de operadores</li>
    </ul>
    <p><b>Ejemplos:</b> __init__, __str__, __add__</p>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>🎭 __str__ vs __repr__</h3>
    <p><b>__str__():</b> Representación amigable</p>
    <ul>
        <li>Para usuarios finales</li>
        <li>Usado por print() y str()</li>
        <li>Debe ser legible</li>
    </ul>
    <p><b>__repr__():</b> Representación técnica</p>
    <ul>
        <li>Para desarrolladores</li>
        <li>Para debugging</li>
        <li>Idealmente evaluable</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Tabla de métodos especiales
st.markdown("---")
st.subheader("📋 Métodos Especiales Comunes")

st.markdown("""
<div class="explicacion">
<h3>🔧 Operadores Aritméticos</h3>
<table style="width: 100%; border-collapse: collapse;">
    <tr style="background-color: #e8f4f8;">
        <th style="padding: 8px; border: 1px solid #ddd;">Método</th>
        <th style="padding: 8px; border: 1px solid #ddd;">Operador</th>
        <th style="padding: 8px; border: 1px solid #ddd;">Descripción</th>
    </tr>
    <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">__add__</td>
        <td style="padding: 8px; border: 1px solid #ddd;">+</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Suma</td>
    </tr>
    <tr style="background-color: #f8f8f8;">
        <td style="padding: 8px; border: 1px solid #ddd;">__sub__</td>
        <td style="padding: 8px; border: 1px solid #ddd;">-</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Resta</td>
    </tr>
    <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">__mul__</td>
        <td style="padding: 8px; border: 1px solid #td;">*</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Multiplicación</td>
    </tr>
</table>

<h3>⚖️ Comparación</h3>
<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <tr style="background-color: #e8f4f8;">
        <th style="padding: 8px; border: 1px solid #ddd;">Método</th>
        <th style="padding: 8px; border: 1px solid #ddd;">Operador</th>
        <th style="padding: 8px; border: 1px solid #ddd;">Descripción</th>
    </tr>
    <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">__eq__</td>
        <td style="padding: 8px; border: 1px solid #ddd;">==</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Igualdad</td>
    </tr>
    <tr style="background-color: #f8f8f8;">
        <td style="padding: 8px; border: 1px solid #ddd;">__lt__</td>
        <td style="padding: 8px; border: 1px solid #ddd;"><</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Menor que</td>
    </tr>
    <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">__len__</td>
        <td style="padding: 8px; border: 1px solid #ddd;">len()</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Longitud</td>
    </tr>
</table>
</div>
""", unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/06_Clase_Encapsulamiento.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/08_Clase_Propiedades.py")
