import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu

st.set_page_config(
    page_title="Clase 7 - Propiedades",
    page_icon="🏗️",
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

# Crear menú lateral personalizado
create_sidebar_menu()

st.title("🏗️ Clase 7: Propiedades y Decoradores")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea clase Temperatura</h3>
    <p>Debe tener:</p>
    <ul>
        <li>Atributo privado: <b>__celsius</b></li>
        <li>Property <b>celsius</b> con getter/setter</li>
        <li>Property <b>fahrenheit</b> (solo lectura)</li>
        <li>Validación: no permitir < -273.15°C</li>
        <li>Property <b>kelvin</b> (solo lectura)</li>
    </ul>
    <p><i>Pista: usa @property y @nombre.setter</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🆘 Ver Solución"):
        st.code("""
class Temperatura:
    def __init__(self, celsius=0):
        self.celsius = celsius
    
    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperatura inválida")
        self.__celsius = value
    
    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32
    
    @property
    def kelvin(self):
        return self.__celsius + 273.15
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")
    
    codigo_default = """class Temperatura:
    def __init__(self, celsius=0):
        # Usa el setter para inicializar
        pass
    
    @property
    def celsius(self):
        # Retorna el valor privado
        pass
    
    @celsius.setter
    def celsius(self, value):
        # Valida y asigna el valor
        pass
    
    @property
    def fahrenheit(self):
        # Calcula y retorna Fahrenheit
        pass
    
    @property
    def kelvin(self):
        # Calcula y retorna Kelvin
        pass

# Prueba tu código:
temp = Temperatura(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
print(f"Kelvin: {temp.kelvin}K")

temp.celsius = 100
print(f"Nuevo Celsius: {temp.celsius}°C")
print(f"Nuevo Fahrenheit: {temp.fahrenheit}°F")"""

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
    <h3>🏗️ ¿Qué es @property?</h3>
    <p>Un decorador que convierte métodos en propiedades:</p>
    <ul>
        <li>Se accede como atributo, no como método</li>
        <li>Permite validación automática</li>
        <li>Crea interfaz limpia</li>
        <li>Mantiene encapsulamiento</li>
    </ul>
    <p><b>Sintaxis:</b> <code>@property</code> antes del método</p>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>⚙️ Getter y Setter</h3>
    <p><b>Getter:</b> Obtiene el valor</p>
    <ul>
        <li><code>@property</code></li>
        <li>Se llama al leer: <code>obj.propiedad</code></li>
    </ul>
    <p><b>Setter:</b> Asigna el valor</p>
    <ul>
        <li><code>@propiedad.setter</code></li>
        <li>Se llama al escribir: <code>obj.propiedad = valor</code></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Ejemplo visual
st.markdown("---")
st.subheader("🎨 Ejemplo de Propiedades")

st.markdown("""
<div class="explicacion">
<h3>🔄 Propiedades vs Métodos Tradicionales</h3>
<pre>
# ❌ Sin propiedades (métodos tradicionales)
persona.set_edad(25)
print(persona.get_edad())

# ✅ Con propiedades (más pythonico)
persona.edad = 25
print(persona.edad)
</pre>
<p>Las propiedades hacen el código más limpio e intuitivo</p>
</div>
""", unsafe_allow_html=True)

# Demostración de validación
st.markdown("---")
st.subheader("🛡️ Validación con Propiedades")

st.markdown("""
<div class="explicacion">
<h3>✅ Ventajas de las Propiedades</h3>
<ul>
    <li><b>Validación automática:</b> Se ejecuta código al asignar</li>
    <li><b>Cálculo dinámico:</b> Propiedades calculadas al vuelo</li>
    <li><b>Read-only:</b> Sin setter = solo lectura</li>
    <li><b>Compatibilidad:</b> Mantiene interfaz consistente</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Ejemplo de propiedad calculada
if st.button("🔍 Ver Ejemplo de Propiedad Calculada"):
    st.code("""
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    @property
    def area(self):
        import math
        return math.pi * self.radio ** 2
    
    @property
    def perimetro(self):
        import math
        return 2 * math.pi * self.radio

c = Circulo(5)
print(f"Radio: {c.radio}")
print(f"Área: {c.area:.2f}")  # Calculada automáticamente
print(f"Perímetro: {c.perimetro:.2f}")  # Calculado automáticamente
    """, language="python")

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/07_Clase_MetodosEspeciales.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/09_Clase_MetodosClase.py")
