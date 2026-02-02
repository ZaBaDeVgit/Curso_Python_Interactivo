import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu

st.set_page_config(
    page_title="Clase 15 - Sobrecarga de Operadores",
    page_icon="⚡",
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

st.title("⚡ Clase 15: Sobrecarga de Operadores")

# Crear menú lateral personalizado
create_sidebar_menu()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea clase Vector Matemático</h3>
    <p>Crea clase <b>Vector</b> con:</p>
    <ul>
        <li>Atributos: <b>x</b>, <b>y</b></li>
        <li><b>__add__</b> para suma de vectores</li>
        <li><b>__sub__</b> para resta de vectores</li>
        <li><b>__mul__</b> para multiplicación por escalar</li>
        <li><b>__eq__</b> para comparación de igualdad</li>
        <li><b>__str__</b> para representación</li>
        <li><b>__len__</b> para magnitud</li>
    </ul>
    <p><i>Pista: Vector(2,3) + Vector(1,1) = Vector(3,4)</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🆘 Ver Solución"):
        st.code("""
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)
    
    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y)
    
    def __mul__(self, escalar):
        return Vector(self.x * escalar, self.y * escalar)
    
    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __len__(self):
        # Magnitud del vector
        return int(math.sqrt(self.x**2 + self.y**2))
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Operador inverso para escalar * vector
    def __rmul__(self, escalar):
        return self.__mul__(escalar)
    
    # Operador de negación
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    # Magnitud como propiedad
    @property
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2)

# Pruebas
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"3 * v1 = {3 * v1}")
print(f"-v1 = {-v1}")
print(f"v1 == v2 = {v1 == v2}")
print(f"len(v1) = {len(v1)}")
print(f"magnitud de v1 = {v1.magnitud:.2f}")
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")
    
    codigo_default = """import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, otro):
        # Sumar componente por componente
        pass
    
    def __sub__(self, otro):
        # Restar componente por componente
        pass
    
    def __mul__(self, escalar):
        # Multiplicar por escalar
        pass
    
    def __eq__(self, otro):
        # Comparar igualdad
        pass
    
    def __str__(self):
        # Representación como string
        pass
    
    def __len__(self):
        # Retornar magnitud (entero)
        pass
    
    def __repr__(self):
        # Representación oficial
        pass
    
    def __rmul__(self, escalar):
        # Para escalar * vector
        pass
    
    def __neg__(self):
        # Para -vector
        pass

# Prueba tu código:
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"3 * v1 = {3 * v1}")
print(f"-v1 = {-v1}")
print(f"v1 == v2 = {v1 == v2}")
print(f"len(v1) = {len(v1)}")"""

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
    <h3>⚡ ¿Qué es Sobrecarga de Operadores?</h3>
    <p>Permite que tus clases usen operadores Python:</p>
    <ul>
        <li>Redefine el comportamiento de +, -, *, /</li>
        <li>Usa métodos especiales (dunder methods)</li>
        <li>Hace código más natural e intuitivo</li>
        <li>Sigue principios de Python</li>
    </ul>
    <p><b>Ejemplo:</b> <code>vector1 + vector2</code> en realidad llama <code>vector1.__add__(vector2)</code></p>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>🔧 Operadores Comunes</h3>
    <p><b>Aritméticos:</b></p>
    <ul>
        <li><code>__add__(self, otro)</code> → +</li>
        <li><code>__sub__(self, otro)</code> → -</li>
        <li><code>__mul__(self, otro)</code> → *</li>
        <li><code>__truediv__(self, otro)</code> → /</li>
    </ul>
    <p><b>Comparación:</b></p>
    <ul>
        <li><code>__eq__(self, otro)</code> → ==</li>
        <li><code>__lt__(self, otro)</code> → <</li>
        <li><code>__gt__(self, otro)</code> → ></li>
    </ul>
    <p><b>Inversos:</b></p>
    <ul>
        <li><code>__radd__(self, otro)</code> → otro + self</li>
        <li><code>__rmul__(self, otro)</code> → otro * self</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Ejemplos adicionales
st.markdown("---")
st.subheader("💡 Ejemplos Prácticos")

col_ej1, col_ej2 = st.columns(2)

with col_ej1:
    st.markdown("""
    <div class="explicacion">
    <h3>💰 Ejemplo: Dinero</h3>
    <p>Clase para manejar dinero con monedas:</p>
    <pre><code>class Dinero:
    def __init__(self, cantidad, moneda="USD"):
        self.cantidad = cantidad
        self.moneda = moneda
    
    def __add__(self, otro):
        if self.moneda != otro.moneda:
            raise ValueError("Monedas diferentes")
        return Dinero(self.cantidad + otro.cantidad, self.moneda)
    
    def __sub__(self, otro):
        return Dinero(self.cantidad - otro.cantidad, self.moneda)
    
    def __str__(self):
        return f"{self.cantidad:.2f} {self.moneda}"

# Uso
d1 = Dinero(100, "EUR")
d2 = Dinero(50, "EUR")
total = d1 + d2  # Dinero(150, "EUR")</code></pre>
    </div>
    """, unsafe_allow_html=True)

with col_ej2:
    st.markdown("""
    <div class="explicacion">
    <h3>📅 Ejemplo: Fecha</h3>
    <p>Clase para manejar fechas personalizadas:</p>
    <pre><code>class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
    
    def __add__(self, dias):
        # Sumar días (simplificado)
        nueva_fecha = Fecha(self.dia + dias, self.mes, self.año)
        # Ajustar si pasa de mes
        return nueva_fecha
    
    def __sub__(self, otra):
        # Calcular diferencia de días
        return abs(self.dia - otra.dia)
    
    def __eq__(self, otra):
        return self.dia == otra.dia and self.mes == otra.mes

# Uso
f1 = Fecha(15, 6, 2024)
f2 = f1 + 10  # Fecha(25, 6, 2024)</code></pre>
    </div>
    """, unsafe_allow_html=True)

# Tabla de operadores
st.markdown("---")
st.subheader("📋 Tabla Completa de Operadores")

st.markdown("""
<div class="explicacion">
<h3>🔢 Operadores Aritméticos</h3>
<table style="width: 100%; border-collapse: collapse;">
    <tr style="background: #f0f0f0;">
        <th style="border: 1px solid #ddd; padding: 8px;">Operador</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Método</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Ejemplo</th>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px;">+</td>
        <td style="border: 1px solid #ddd; padding: 8px;">__add__</td>
        <td style="border: 1px solid #ddd; padding: 8px;">a + b</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px;">-</td>
        <td style="border: 1px solid #ddd; padding: 8px;">__sub__</td>
        <td style="border: 1px solid #ddd; padding: 8px;">a - b</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px;">*</td>
        <td style="border: 1px solid #ddd; padding: 8px;">__mul__</td>
        <td style="border: 1px solid #ddd; padding: 8px;">a * b</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px;">/</td>
        <td style="border: 1px solid #ddd; padding: 8px;">__truediv__</td>
        <td style="border: 1px solid #ddd; padding: 8px;">a / b</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px;">//</td>
        <td style="border: 1px solid #ddd; padding: 8px;">__floordiv__</td>
        <td style="border: 1px solid #ddd; padding: 8px;">a // b</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px;">%</td>
        <td style="border: 1px solid #ddd; padding: 8px;">__mod__</td>
        <td style="border: 1px solid #ddd; padding: 8px;">a % b</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px;">**</td>
        <td style="border: 1px solid #ddd; padding: 8px;">__pow__</td>
        <td style="border: 1px solid #ddd; padding: 8px;">a ** b</td>
    </tr>
</table>

<h3>⚖️ Operadores de Comparación</h3>
<table style="width: 100%; border-collapse: collapse;">
    <tr style="background: #f0f0f0;">
        <th style="border: 1px solid #ddd; padding: 8px;">Operador</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Método</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Ejemplo</th>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px;">==</td>
        <td style="border: 1px solid #ddd; padding: 8px;">__eq__</td>
        <td style="border: 1px solid #ddd; padding: 8px;">a == b</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px;">!=</td>
        <td style="border: 1px solid #ddd; padding: 8px;">__ne__</td>
        <td style="border: 1px solid #ddd; padding: 8px;">a != b</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><</td>
        <td style="border: 1px solid #ddd; padding: 8px;">__lt__</td>
        <td style="border: 1px solid #ddd; padding: 8px;">a < b</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><=</td>
        <td style="border: 1px solid #ddd; padding: 8px;">__le__</td>
        <td style="border: 1px solid #ddd; padding: 8px;">a <= b</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px;">></td>
        <td style="border: 1px solid #ddd; padding: 8px;">__gt__</td>
        <td style="border: 1px solid #ddd; padding: 8px;">a > b</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px;">>=</td>
        <td style="border: 1px solid #ddd; padding: 8px;">__ge__</td>
        <td style="border: 1px solid #ddd; padding: 8px;">a >= b</td>
    </tr>
</table>
</div>
""", unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/15_Clase_DuckTyping.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/17_Clase_IteradoresGeneradores.py")
