import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu
st.set_page_config(
    page_title="Clase 12 - Clases Abstractas",
    page_icon="🎨",
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

st.title("🎨 Clase 12: Clases Abstractas (ABC)")

# Crear menú lateral personalizado
create_sidebar_menu()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea sistema de Figuras Geométricas</h3>
    <p>Crea:</p>
    <ul>
        <li>Clase abstracta <b>Figura</b> con:</li>
        <li>• Método abstracto <b>area()</b></li>
        <li>• Método abstracto <b>perimetro()</b></li>
        <li>Clase <b>Circulo</b> que hereda de Figura</li>
        <li>Clase <b>Rectangulo</b> que hereda de Figura</li>
        <li>Implementa los métodos abstractos</li>
    </ul>
    <p><i>Pista: usa @abstractmethod y hereda de ABC</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🆘 Ver Solución"):
        st.code("""
from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
    def describir(self):
        return f"Soy una figura con área {self.area():.2f} y perímetro {self.perimetro():.2f}"

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")
    
    codigo_default = """from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def area(self):
        # Método abstracto - debe ser implementado
        pass
    
    @abstractmethod
    def perimetro(self):
        # Método abstracto - debe ser implementado
        pass
    
    def describir(self):
        return f"Soy una figura con área {self.area():.2f}"

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        # Implementa el área del círculo
        pass
    
    def perimetro(self):
        # Implementa el perímetro del círculo
        pass

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        # Implementa el área del rectángulo
        pass
    
    def perimetro(self):
        # Implementa el perímetro del rectángulo
        pass

# Prueba tu código:
circ = Circulo(5)
rect = Rectangulo(4, 6)
print(circ.describir())
print(rect.describir())"""

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
    <h3>🎨 ¿Qué son Clases Abstractas?</h3>
    <p>Son plantillas que definen estructura pero no implementación:</p>
    <ul>
        <li>No se pueden instanciar directamente</li>
        <li>Definen métodos que deben implementar las hijas</li>
        <li>Usan el decorador @abstractmethod</li>
        <li>Herredan de ABC (Abstract Base Class)</li>
    </ul>
    <p><b>Propósito:</b> Forzar un contrato de implementación</p>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>📋 @abstractmethod</h3>
    <p>Decorador que marca métodos como abstractos:</p>
    <ul>
        <li>Las clases hijas DEBEN implementarlos</li>
        <li>Si no lo hacen, también serán abstractas</li>
        <li>Python lanza TypeError si no se implementan</li>
    </ul>
    <p><b>Reglas:</b></p>
    <ul>
        <li>Clase abstracta → hereda de ABC</li>
        <li>Método abstracto → @abstractmethod</li>
        <li>Clase concreta → implementa todos los abstractos</li>
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
    <h3>🎵 Ejemplo: Instrumentos Musicales</h3>
    <p>Todo instrumento debe poder:</p>
    <ul>
        <li><b>tocar()</b> - producir sonido</li>
        <li><b>afinar()</b> - ajustar tono</li>
    </ul>
    <pre><code>class Instrumento(ABC):
    @abstractmethod
    def tocar(self):
        pass
    
    @abstractmethod
    def afinar(self):
        pass

class Guitarra(Instrumento):
    def tocar(self):
        return "🎸 Strum strum"
    
    def afinar(self):
        return "🎵 Afintando cuerdas"</code></pre>
    </div>
    """, unsafe_allow_html=True)

with col_ej2:
    st.markdown("""
    <div class="explicacion">
    <h3>🚗 Ejemplo: Vehículos</h3>
    <p>Todo vehículo debe poder:</p>
    <ul>
        <li><b>arrancar()</b> - poner en marcha</li>
        <li><b>detener()</b> - frenar</li>
        <li><b>acelerar()</b> - aumentar velocidad</li>
    </ul>
    <pre><code>class Vehiculo(ABC):
    @abstractmethod
    def arrancar(self):
        pass
    
    @abstractmethod
    def detener(self):
        pass

class Coche(Vehiculo):
    def arrancar(self):
        return "🚗 Brum brum"
    
    def detener(self):
        return "🛑 Screech!"</code></pre>
    </div>
    """, unsafe_allow_html=True)

# Ventajas y casos de uso
st.markdown("---")
st.subheader("🎯 ¿Cuándo usar Clases Abstractas?")

st.markdown("""
<div class="explicacion">
<h3>✅ Ventajas:</h3>
<ul>
    <li><b>Contrato claro:</b> Define qué métodos deben existir</li>
    <li><b>Seguridad:</b> Evita olvidar implementar métodos</li>
    <li><b>Diseño:</b> Fuerza arquitectura consistente</li>
    <li><b>Documentación:</b> Sirve como plantilla</li>
</ul>

<h3>🎯 Casos de Uso:</h3>
<ul>
    <li><b>Plugins:</b> Definir interfaz común</li>
    <li><b>APIs:</b> Estandarizar implementaciones</li>
    <li><b>Frameworks:</b> Crear puntos de extensión</li>
    <li><b>Sistemas:</b> Múltiples tipos similares</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/12_Clase_HerenciaMultiple.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/14_Clase_Interfaces.py")
