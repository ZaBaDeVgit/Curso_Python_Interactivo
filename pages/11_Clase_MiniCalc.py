import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu

st.set_page_config(
    page_title="Clase 10 - MiniCalc",
    page_icon="🧮",
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
    .proyecto-final {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# Crear menú lateral personalizado
create_sidebar_menu()
    st.page_link("pages/10_Clase_Composicion.py", label="⬅️ Anterior")
    st.page_link("streamlit_app.py", label="➡️ Siguiente (Módulo 2)")

st.title("🧮 Clase 10: Proyecto Final - MiniCalculadora POO")

st.markdown("""
<div class="proyecto-final">
<h2>🎯 ¡Proyecto Integrador del Módulo 1!</h2>
<p>Aplica todo lo aprendido: clases, métodos, herencia, polimorfismo, encapsulamiento, propiedades y composición.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del Proyecto")
    st.markdown("""
    <div class="explicacion">
    <h3>🧮 Crea MiniCalculadora POO</h3>
    <p>Debe incluir:</p>
    <ul>
        <li><b>Operacion</b> (clase base abstracta)</li>
        <li><b>Suma, Resta, Multiplica, Divide</b> (heredan)</li>
        <li><b>Calculadora</b> (usa composición)</li>
        <li><b>Historial</b> (almacena operaciones)</li>
        <li>Propiedades para validación</li>
        <li>Métodos especiales (__str__, __call__)</li>
    </ul>
    <p><i>Integra todos los conceptos del módulo!</i></p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🆘 Ver Solución Completa"):
        st.code("""
from abc import ABC, abstractmethod

class Operacion(ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def ejecutar(self):
        pass

    def __str__(self):
        return f"{self.a} {self.simbolo} {self.b} = {self.ejecutar()}"

class Suma(Operacion):
    simbolo = "+"

    def ejecutar(self):
        return self.a + self.b

class Resta(Operacion):
    simbolo = "-"

    def ejecutar(self):
        return self.a - self.b

class Multiplica(Operacion):
    simbolo = "*"

    def ejecutar(self):
        return self.a * self.b

class Divide(Operacion):
    simbolo = "/"

    def ejecutar(self):
        if self.b == 0:
            raise ValueError("No se puede dividir por cero")
        return self.a / self.b

class Historial:
    def __init__(self):
        self._operaciones = []

    def agregar(self, operacion):
        self._operaciones.append(operacion)

    def mostrar(self):
        return [str(op) for op in self._operaciones]

class Calculadora:
    def __init__(self):
        self.historial = Historial()

    def sumar(self, a, b):
        op = Suma(a, b)
        self.historial.agregar(op)
        return op.ejecutar()

    def restar(self, a, b):
        op = Resta(a, b)
        self.historial.agregar(op)
        return op.ejecutar()

    def multiplicar(self, a, b):
        op = Multiplica(a, b)
        self.historial.agregar(op)
        return op.ejecutar()

    def dividir(self, a, b):
        op = Divide(a, b)
        self.historial.agregar(op)
        return op.ejecutar()

    def ver_historial(self):
        return self.historial.mostrar()
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")

    codigo_default = """from abc import ABC, abstractmethod

# Clase base abstracta
class Operacion(ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def ejecutar(self):
        pass

    def __str__(self):
        return f"{self.a} {self.simbolo} {self.b} = {self.ejecutar()}"

# Clases hijas
class Suma(Operacion):
    simbolo = "+"

    def ejecutar(self):
        # Implementa la suma
        pass

class Resta(Operacion):
    simbolo = "-"

    def ejecutar(self):
        # Implementa la resta
        pass

class Multiplica(Operacion):
    simbolo = "*"

    def ejecutar(self):
        # Implementa la multiplicación
        pass

class Divide(Operacion):
    simbolo = "/"

    def ejecutar(self):
        # Implementa la división con validación
        pass

# Clase de composición
class Calculadora:
    def __init__(self):
        self.historial = []

    def sumar(self, a, b):
        # Crea operación, agrega al historial y retorna resultado
        pass

    def ver_historial(self):
        # Retorna el historial de operaciones
        pass

# Prueba tu código:
calc = Calculadora()
print(f"5 + 3 = {calc.sumar(5, 3)}")
print(f"10 - 4 = {calc.restar(10, 4)}")
print("Historial:", calc.ver_historial())"""

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

# Explicación del proyecto
st.markdown("---")
st.subheader("📚 Conceptos Integrados")

col_exp1, col_exp2 = st.columns(2)

with col_exp1:
    st.markdown("""
    <div class="explicacion">
    <h3>🔗 Conceptos Aplicados</h3>
    <ul>
        <li><b>Clases y Objetos:</b> Operacion, Calculadora</li>
        <li><b>Herencia:</b> Suma, Resta heredan de Operacion</li>
        <li><b>Polimorfismo:</b> Todas tienen método ejecutar()</li>
        <li><b>Encapsulamiento:</b> Historial protegido</li>
        <li><b>Abstractas:</b> Operacion como clase base</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>⚡ Métodos Especiales</h3>
    <ul>
        <li><b>__str__:</b> Representación amigable</li>
        <li><b>__init__:</b> Inicialización</li>
        <li><b>@abstractmethod:</b> Fuerza implementación</li>
        <li><b>Composición:</b> Calculadora usa Historial</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Resumen del módulo
st.markdown("---")
st.markdown("""
<div class="proyecto-final">
<h2>🎉 ¡Felicidades! Módulo 1 Completado</h2>
<p>Has dominado los fundamentos de POO en Python:</p>
<ul>
    <li>✅ Creación de clases y objetos</li>
    <li>✅ Métodos y parámetro self</li>
    <li>✅ Herencia y clases hijas</li>
    <li>✅ Polimorfismo y múltiples formas</li>
    <li>✅ Encapsulamiento y modificadores</li>
    <li>✅ Métodos especiales y propiedades</li>
    <li>✅ Métodos de clase y estáticos</li>
    <li>✅ Composición vs herencia</li>
    <li>✅ Proyecto integrador</li>
</ul>
<p><b>🚀 Estás listo para el Módulo 2: POO Avanzado!</b></p>
</div>
""", unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/10_Clase_Composicion.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("🏠 Volver al Inicio"):
        st.switch_page("streamlit_app.py")
