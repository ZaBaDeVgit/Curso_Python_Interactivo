import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu, create_navigation_buttons
st.set_page_config(
    page_title="Clase 13 - Interfaces y Protocolos",
    page_icon="🔌",
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

st.title("🔌 Clase 13: Interfaces y Protocolos")

# Crear menú lateral personalizado
create_sidebar_menu()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea sistema de Almacenamiento</h3>
    <p>Crea:</p>
    <ul>
        <li>Protocolo <b>Almacenamiento</b> con:</li>
        <li>• Método <b>guardar(datos)</b></li>
        <li>• Método <b>leer(clave)</b></li>
        <li>• Método <b>eliminar(clave)</b></li>
        <li>Clase <b>BaseDatos</b> que implementa el protocolo</li>
        <li>Clase <b>Archivo</b> que implementa el protocolo</li>
        <li>Usa typing.Protocol y @runtime_checkable</li>
    </ul>
    <p><i>Pista: Los protocolos son como interfaces informales</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🆘 Ver Solución"):
        st.code("""
from typing import Protocol, Dict, Any, Optional
import json
import os

@runtime_checkable
class Almacenamiento(Protocol):
    def guardar(self, clave: str, datos: Any) -> bool:
        ...
    
    def leer(self, clave: str) -> Optional[Any]:
        ...
    
    def eliminar(self, clave: str) -> bool:
        ...

class BaseDatos:
    def __init__(self):
        self.datos: Dict[str, Any] = {}
    
    def guardar(self, clave: str, datos: Any) -> bool:
        self.datos[clave] = datos
        return True
    
    def leer(self, clave: str) -> Optional[Any]:
        return self.datos.get(clave)
    
    def eliminar(self, clave: str) -> bool:
        return self.datos.pop(clave, None) is not None

class Archivo:
    def __init__(self, ruta: str):
        self.ruta = ruta
        if not os.path.exists(ruta):
            with open(ruta, 'w') as f:
                json.dump({}, f)
    
    def guardar(self, clave: str, datos: Any) -> bool:
        try:
            with open(self.ruta, 'r') as f:
                contenido = json.load(f)
            contenido[clave] = datos
            with open(self.ruta, 'w') as f:
                json.dump(contenido, f)
            return True
        except:
            return False
    
    def leer(self, clave: str) -> Optional[Any]:
        try:
            with open(self.ruta, 'r') as f:
                contenido = json.load(f)
            return contenido.get(clave)
        except:
            return None
    
    def eliminar(self, clave: str) -> bool:
        try:
            with open(self.ruta, 'r') as f:
                contenido = json.load(f)
            if clave in contenido:
                del contenido[clave]
                with open(self.ruta, 'w') as f:
                    json.dump(contenido, f)
                return True
            return False
        except:
            return False
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")
    
    codigo_default = """from typing import Protocol, Dict, Any, Optional
import json
import os

@runtime_checkable
class Almacenamiento(Protocol):
    def guardar(self, clave: str, datos: Any) -> bool:
        # Implementar en clases concretas
        pass
    
    def leer(self, clave: str) -> Optional[Any]:
        # Implementar en clases concretas
        pass
    
    def eliminar(self, clave: str) -> bool:
        # Implementar en clases concretas
        pass

class BaseDatos:
    def __init__(self):
        self.datos: Dict[str, Any] = {}
    
    def guardar(self, clave: str, datos: Any) -> bool:
        # Guarda en memoria
        pass
    
    def leer(self, clave: str) -> Optional[Any]:
        # Lee de memoria
        pass
    
    def eliminar(self, clave: str) -> bool:
        # Elimina de memoria
        pass

class Archivo:
    def __init__(self, ruta: str):
        self.ruta = ruta
        # Crear archivo si no existe
        pass
    
    def guardar(self, clave: str, datos: Any) -> bool:
        # Guarda en archivo JSON
        pass
    
    def leer(self, clave: str) -> Optional[Any]:
        # Lee de archivo JSON
        pass
    
    def eliminar(self, clave: str) -> bool:
        # Elimina de archivo JSON
        pass

# Prueba tu código:
bd = BaseDatos()
archivo = Archivo("datos.json")

# Verificar si implementan el protocolo
print(f"BD implementa Almacenamiento: {isinstance(bd, Almacenamiento)}")
print(f"Archivo implementa Almacenamiento: {isinstance(archivo, Almacenamiento)}")

# Probar funcionalidad
bd.guardar("usuario1", {"nombre": "Ana", "edad": 25})
print(f"Leído de BD: {bd.leer('usuario1')}")"""

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
    <h3>🔌 ¿Qué son Protocolos?</h3>
    <p>Son interfaces informales de Python:</p>
    <ul>
        <li>Definen "contratos" de métodos</li>
        <li>No heredan de una clase base</li>
        <li>Usan typing.Protocol</li>
        <li>Pueden verificarse con @runtime_checkable</li>
    </ul>
    <p><b>Diferencia con ABC:</b></p>
    <ul>
        <li>ABC: obliga a implementar</li>
        <li>Protocolo: solo define estructura</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>🔍 @runtime_checkable</h3>
    <p>Permite verificar si una clase implementa un protocolo:</p>
    <ul>
        <li>Usa isinstance() para verificar</li>
        <li>Revisa si tiene los métodos necesarios</li>
        <li>No verifica tipos de parámetros</li>
        <li>Útil para type hints y validación</li>
    </ul>
    <p><b>Ejemplo:</b></p>
    <pre><code>@runtime_checkable
class Hablador(Protocol):
    def hablar(self) -> str: ...

class Perro:
    def hablar(self) -> str:
        return "Guau!"

print(isinstance(Perro(), Hablador))  # True</code></pre>
    </div>
    """, unsafe_allow_html=True)

# Ejemplos adicionales
st.markdown("---")
st.subheader("💡 Ejemplos Prácticos")

col_ej1, col_ej2 = st.columns(2)

with col_ej1:
    st.markdown("""
    <div class="explicacion">
    <h3>📝 Ejemplo: Procesadores de Texto</h3>
    <p>Todo procesador debe poder:</p>
    <ul>
        <li><b>procesar(texto)</b> - transformar texto</li>
        <li><b>formatear(texto)</b> - aplicar formato</li>
    </ul>
    <pre><code>@runtime_checkable
class ProcesadorTexto(Protocol):
    def procesar(self, texto: str) -> str: ...
    def formatear(self, texto: str) -> str: ...

class Mayusculas:
    def procesar(self, texto: str) -> str:
        return texto.upper()
    
    def formatear(self, texto: str) -> str:
        return f"[{texto}]"</code></pre>
    </div>
    """, unsafe_allow_html=True)

with col_ej2:
    st.markdown("""
    <div class="explicacion">
    <h3>🔄 Ejemplo: Convertidores</h3>
    <p>Todo convertidor debe poder:</p>
    <ul>
        <li><b>convertir(datos)</b> - transformar datos</li>
        <li><b>validar(datos)</b> - verificar formato</li>
    </ul>
    <pre><code>@runtime_checkable
class Convertidor(Protocol):
    def convertir(self, datos: Any) -> Dict: ...
    def validar(self, datos: Any) -> bool: ...

class JSONConvertidor:
    def convertir(self, datos: Any) -> Dict:
        return json.loads(datos)
    
    def validar(self, datos: Any) -> bool:
        try:
            json.loads(datos)
            return True
        except:
            return False</code></pre>
    </div>
    """, unsafe_allow_html=True)

# Ventajas y casos de uso
st.markdown("---")
st.subheader("🎯 ¿Cuándo usar Protocolos?")

st.markdown("""
<div class="explicacion">
<h3>✅ Ventajas:</h3>
<ul>
    <li><b>Flexibilidad:</b> No fuerza herencia</li>
    <li><b>Compatibilidad:</b> Clases existentes pueden cumplir</li>
    <li><b>Type hints:</b> Mejora autocompletado</li>
    <li><b>Duck typing:</b> "Si camina como pato y grazna como pato..."</li>
</ul>

<h3>🎯 Casos de Uso:</h3>
<ul>
    <li><b>Plugins:</b> Definir interfaces sin herencia</li>
    <li><b>APIs:</b> Estandarizar sin forzar estructura</li>
    <li><b>Librerías:</b> Permitir múltiples implementaciones</li>
    <li><b>Sistemas:</b> Componentes intercambiables</li>
</ul>

<h3>🆚 Protocolo vs Clase Abstracta:</h3>
<ul>
    <li><b>Protocolo:</b> "Si tiene estos métodos, puede usarse"</li>
    <li><b>ABC:</b> "Debe heredar de mí y implementar estos métodos"</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/13_Clase_Abstractas.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/15_Clase_DuckTyping.py")
