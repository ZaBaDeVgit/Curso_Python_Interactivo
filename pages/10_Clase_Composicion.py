import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu, create_sidebar_toggle

st.set_page_config(
    page_title="Clase 9 - Composición",
    page_icon="🧩",
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

st.title("🧩 Clase 9: Composición vs Herencia")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea sistema de Computadora</h3>
    <p>Usando composición:</p>
    <ul>
        <li>Clase <b>CPU</b> con marca y velocidad</li>
        <li>Clase <b>RAM</b> con capacidad</li>
        <li>Clase <b>Almacenamiento</b> con tipo y tamaño</li>
        <li>Clase <b>Computadora</b> que contiene CPU, RAM, Almacenamiento</li>
        <li>Método <b>mostrar_especificaciones()</b></li>
    </ul>
    <p><i>Pista: Computadora "tiene" CPU, no "es" CPU</i></p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🆘 Ver Solución"):
        st.code("""
class CPU:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad

    def __str__(self):
        return f"CPU {self.marca} {self.velocidad}GHz"

class RAM:
    def __init__(self, capacidad_gb):
        self.capacidad_gb = capacidad_gb

    def __str__(self):
        return f"RAM {self.capacidad_gb}GB"

class Almacenamiento:
    def __init__(self, tipo, capacidad_gb):
        self.tipo = tipo
        self.capacidad_gb = capacidad_gb

    def __str__(self):
        return f"{self.tipo} {self.capacidad_gb}GB"

class Computadora:
    def __init__(self, cpu, ram, almacenamiento):
        self.cpu = cpu
        self.ram = ram
        self.almacenamiento = almacenamiento

    def mostrar_especificaciones(self):
        return f"PC: {self.cpu}, {self.ram}, {self.almacenamiento}"
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")

    codigo_default = """class CPU:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad

class RAM:
    def __init__(self, capacidad_gb):
        self.capacidad_gb = capacidad_gb

class Almacenamiento:
    def __init__(self, tipo, capacidad_gb):
        self.tipo = tipo
        self.capacidad_gb = capacidad_gb

class Computadora:
    def __init__(self, cpu, ram, almacenamiento):
        # Asigna los componentes
        pass

    def mostrar_especificaciones(self):
        # Retorna string con todas las especificaciones
        pass

# Prueba tu código:
mi_cpu = CPU("Intel", 3.2)
mi_ram = RAM(16)
mi_almacenamiento = Almacenamiento("SSD", 512)

mi_pc = Computadora(mi_cpu, mi_ram, mi_almacenamiento)
print(mi_pc.mostrar_especificaciones())"""

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
    <h3>🧩 ¿Qué es Composición?</h3>
    <p>Relación "tiene-un" (has-a):</p>
    <ul>
        <li>Un objeto contiene otros objetos</li>
        <li>Los componentes son independientes</li>
        <li>Mayor flexibilidad que herencia</li>
        <li>Evita jerarquías profundas</li>
    </ul>
    <p><b>Ejemplo:</b> Auto tiene Motor, tiene Ruedas</p>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>⚖️ Composición vs Herencia</h3>
    <p><b>Herencia:</b> "es-un" (is-a)</p>
    <ul>
        <li>Perro es un Animal</li>
        <li>Estática en tiempo de ejecución</li>
        <li>Acoplamiento fuerte</li>
    </ul>
    <p><b>Composición:</b> "tiene-un" (has-a)</p>
    <ul>
        <li>Auto tiene Motor</li>
        <li>Dinámica en tiempo de ejecución</li>
        <li>Acoplamiento débil</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Ejemplo visual
st.markdown("---")
st.subheader("🎨 Ejemplo de Composición")

st.markdown("""
<div class="explicacion">
<h3>🏗️ Estructura de Composición</h3>
<pre>
    Computadora
    ├── CPU
    │   ├── marca: "Intel"
    │   └── velocidad: 3.2
    ├── RAM
    │   └── capacidad_gb: 16
    └── Almacenamiento
        ├── tipo: "SSD"
        └── capacidad_gb: 512
</pre>
<p>Computadora contiene objetos, no hereda de ellos</p>
</div>
""", unsafe_allow_html=True)

# Principio de composición
st.markdown("---")
st.subheader('🎯 Principio: "Favor Composition over Inheritance"')

st.markdown("""
<div class="explicacion">
<h3>✅ Ventajas de la Composición</h3>
<ul>
    <li><b>Flexibilidad:</b> Cambiar componentes en runtime</li>
    <li><b>Reutilización:</b> Mismos componentes en diferentes contextos</li>
    <li><b>Mantenimiento:</b> Cambios locales no afectan a toda la jerarquía</li>
    <li><b>Testing:</b> Más fácil de probar componentes individualmente</li>
</ul>

<h3>⚠️ Cuándo usar Herencia</h3>
<ul>
    <li>Cuando realmente hay relación "es-un"</li>
    <li>Para compartir comportamiento común</li>
    <li>En jerarquías bien definidas y estables</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Ejemplo práctico
if st.button("🔍 Ver Ejemplo Práctico"):
    st.code("""
# Composición: Biblioteca
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []  # Composición: tiene libros

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        return [libro.titulo for libro in self.libros]

# Uso:
biblio = Biblioteca("Central")
biblio.agregar_libro(Libro("1984", "Orwell"))
biblio.agregar_libro(Libro("Dune", "Herbert"))
print(biblio.mostrar_libros())
    """, language="python")

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/09_Clase_MetodosClase.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/11_Clase_MiniCalc.py")
