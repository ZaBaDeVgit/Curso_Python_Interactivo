import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu

st.set_page_config(
    page_title="Clase 14 - Duck Typing Profundo",
    page_icon="🦆",
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

st.title("🦆 Clase 14: Duck Typing Profundo")

# Crear menú lateral personalizado
create_sidebar_menu()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea sistema de Procesamiento Universal</h3>
    <p>Crea:</p>
    <ul>
        <li>Función <b>procesar_datos(objeto)</b> que:</li>
        <li>• Si tiene <b>procesar()</b>, lo usa</li>
        <li>• Si tiene <b>transformar()</b>, lo usa</li>
        <li>• Si es <b>diccionario</b>, lo convierte</li>
        <li>• Si es <b>lista</b>, la procesa elemento por elemento</li>
        <li>• Si tiene <b>__iter__</b>, itera sobre él</li>
        <li>• Usa hasattr() y duck typing</li>
    </ul>
    <p><i>Pista: "Si parece un pato y suena como un pato..."</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🆘 Ver Solución"):
        st.code("""
def procesar_datos(objeto):
    \"\"\"Función universal que procesa cualquier objeto usando duck typing\"\"\"
    
    # 1. Si tiene método procesar(), usarlo
    if hasattr(objeto, 'procesar'):
        return objeto.procesar()
    
    # 2. Si tiene método transformar(), usarlo
    if hasattr(objeto, 'transformar'):
        return objeto.transformar()
    
    # 3. Si es diccionario, convertir a JSON
    if isinstance(objeto, dict):
        return f"Diccionario con {len(objeto)} items: {list(objeto.keys())}"
    
    # 4. Si es lista, procesar cada elemento
    if isinstance(objeto, list):
        return [procesar_datos(item) for item in objeto]
    
    # 5. Si es iterable (pero no string), iterar
    if hasattr(objeto, '__iter__') and not isinstance(objeto, (str, bytes)):
        return list(objeto)
    
    # 6. Si tiene __len__, mostrar longitud
    if hasattr(objeto, '__len__'):
        return f"Objeto con longitud {len(objeto)}"
    
    # 7. Por defecto, convertir a string
    return str(objeto)

# Clases de ejemplo
class Procesador:
    def procesar(self):
        return "🔧 Procesado con método procesar()"

class Transformador:
    def transformar(self):
        return "🔄 Transformado con método transformar()"

class Contenedor:
    def __init__(self, items):
        self.items = items
    
    def __iter__(self):
        return iter(self.items)
    
    def __len__(self):
        return len(self.items)

# Pruebas
datos = [
    Procesador(),
    Transformador(),
    {"nombre": "Ana", "edad": 25},
    [1, 2, 3, "hola"],
    Contenedor(["a", "b", "c"]),
    42,
    "texto simple"
]

for i, dato in enumerate(datos, 1):
    resultado = procesar_datos(dato)
    print(f"{i}. {resultado}")
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")
    
    codigo_default = """def procesar_datos(objeto):
    \"\"\"Función universal que procesa cualquier objeto usando duck typing\"\"\"
    
    # 1. Si tiene método procesar(), usarlo
    if hasattr(objeto, 'procesar'):
        return objeto.procesar()
    
    # 2. Si tiene método transformar(), usarlo
    # TODO: Implementar esta parte
    
    # 3. Si es diccionario, convertir a JSON
    # TODO: Implementar esta parte
    
    # 4. Si es lista, procesar cada elemento
    # TODO: Implementar esta parte
    
    # 5. Si es iterable (pero no string), iterar
    # TODO: Implementar esta parte
    
    # 6. Si tiene __len__, mostrar longitud
    # TODO: Implementar esta parte
    
    # 7. Por defecto, convertir a string
    return str(objeto)

# Clases de ejemplo
class Procesador:
    def procesar(self):
        return "🔧 Procesado con método procesar()"

class Transformador:
    def transformar(self):
        return "🔄 Transformado con método transformar()"

class Contenedor:
    def __init__(self, items):
        self.items = items
    
    def __iter__(self):
        return iter(self.items)
    
    def __len__(self):
        return len(self.items)

# Prueba tu código:
datos = [
    Procesador(),
    Transformador(),
    {"nombre": "Ana", "edad": 25},
    [1, 2, 3, "hola"],
    Contenedor(["a", "b", "c"]),
    42,
    "texto simple"
]

for i, dato in enumerate(datos, 1):
    resultado = procesar_datos(dato)
    print(f"{i}. {resultado}")"""

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
    <h3>🦆 ¿Qué es Duck Typing?</h3>
    <p>Principio de Python: "Si camina como pato y grazna como pato...":</p>
    <ul>
        <li>No importa el tipo de objeto</li>
        <li>Importa lo que puede hacer</li>
        <li>Usa hasattr() para verificar métodos</li>
        <li>Más flexible que herencia</li>
    </ul>
    <p><b>Famosa frase:</b></p>
    <p><i>"If it walks like a duck and quacks like a duck, then it's a duck"</i></p>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>🔍 hasattr() y getattr()</h3>
    <p>Herramientas clave para duck typing:</p>
    <ul>
        <li><b>hasattr(obj, 'metodo')</b> - ¿tiene el método?</li>
        <li><b>getattr(obj, 'metodo')</b> - obtener el método</li>
        <li><b>callable(metodo)</b> - ¿es ejecutable?</li>
        <li><b>isinstance()</b> - verificar tipo específico</li>
    </ul>
    <p><b>Ejemplo:</b></p>
    <pre><code>def saludar(objeto):
    if hasattr(objeto, 'hablar'):
        return objeto.hablar()
    return "No puedo hablar"</code></pre>
    </div>
    """, unsafe_allow_html=True)

# Ejemplos adicionales
st.markdown("---")
st.subheader("💡 Ejemplos Prácticos")

col_ej1, col_ej2 = st.columns(2)

with col_ej1:
    st.markdown("""
    <div class="explicacion">
    <h3>📝 Ejemplo: Editores de Texto</h3>
    <p>Cualquier objeto que pueda escribir texto:</p>
    <pre><code>def escribir(objeto, texto):
    if hasattr(objeto, 'write'):
        objeto.write(texto)
    elif hasattr(objeto, 'append'):
        objeto.append(texto)
    elif hasattr(objeto, 'send'):
        objeto.send(texto)
    else:
        print(texto)

# Funciona con archivos, listas, sockets, etc.
escribir(open_file, "Hola")
escribir(mi_lista, "Hola")
escribir(socket, "Hola")</code></pre>
    </div>
    """, unsafe_allow_html=True)

with col_ej2:
    st.markdown("""
    <div class="explicacion">
    <h3>🔄 Ejemplo: Procesadores</h3>
    <p>Cualquier objeto que pueda procesar datos:</p>
    <pre><code>def procesar(objeto, datos):
    if hasattr(objeto, 'process'):
        return objeto.process(datos)
    elif hasattr(objeto, 'handle'):
        return objeto.handle(datos)
    elif callable(objeto):
        return objeto(datos)
    else:
        return str(objeto) + str(datos)

# Funciona con funciones, objetos, etc.
procesar(mi_funcion, datos)
procesar(mi_clase, datos)
procesar(lambda x: x*2, datos)</code></pre>
    </div>
    """, unsafe_allow_html=True)

# Patrones avanzados
st.markdown("---")
st.subheader("🚀 Patrones Avanzados de Duck Typing")

st.markdown("""
<div class="explicacion">
<h3>🎯 Pattern Matching con Duck Typing</h3>
<p>Usar duck typing para seleccionar comportamiento:</p>
<pre><code>def smart_process(objeto):
    \"\"\"Procesamiento inteligente basado en capacidades\"\"\"
    
    # Pattern 1: Si puede guardar y cargar
    if hasattr(objeto, 'save') and hasattr(objeto, 'load'):
        objeto.save()
        return objeto.load()
    
    # Pattern 2: Si puede serializar
    if hasattr(objeto, 'serialize'):
        return objeto.serialize()
    
    # Pattern 3: Si es contenedor
    if hasattr(objeto, '__contains__'):
        return f"Contenedor con {len(objeto)} elementos"
    
    # Pattern 4: Si es numérico
    if hasattr(objeto, '__add__') and hasattr(objeto, '__mul__'):
        return objeto * 2
    
    return objeto</code></pre>

<h3>🔧 Fábricas Dinámicas</h3>
<p>Crear objetos basados en interfaces disponibles:</p>
<pre><code>def create_processor(source):
    \"\"\"Crea procesador basado en el tipo de fuente\"\"\"
    
    if hasattr(source, 'read'):
        return StreamReader(source)
    elif hasattr(source, 'execute'):
        return QueryProcessor(source)
    elif hasattr(source, 'connect'):
        return DatabaseProcessor(source)
    else:
        return GenericProcessor(source)</code></pre>

<h3>⚡ Adaptadores Universales</h3>
<p>Adaptar cualquier objeto a una interfaz común:</p>
<pre><code>class UniversalAdapter:
    def __init__(self, objeto):
        self.obj = objeto
    
    def process(self):
        if hasattr(self.obj, 'process'):
            return self.obj.process()
        elif hasattr(self.obj, 'handle'):
            return self.obj.handle()
        elif callable(self.obj):
            return self.obj()
        else:
            return str(self.obj)</code></pre>
</div>
""", unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/14_Clase_Interfaces.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/16_Clase_SobrecargaOperadores.py")
