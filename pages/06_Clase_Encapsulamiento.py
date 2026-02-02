import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu, create_sidebar_toggle

st.set_page_config(
    page_title="Clase 5 - Encapsulamiento",
    page_icon="🔒",
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

st.title("🔒 Clase 5: Encapsulamiento y Modificadores de Acceso")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea clase CuentaBancaria</h3>
    <p>Debe tener:</p>
    <ul>
        <li>Atributo privado: <b>__saldo</b></li>
        <li>Atributo protegido: <b>_titular</b></li>
        <li>Método <b>depositar(cantidad)</b></li>
        <li>Método <b>retirar(cantidad)</b> con validación</li>
        <li>Getter <b>get_saldo()</b></li>
        <li>No permitir saldo negativo</li>
    </ul>
    <p><i>Pista: usa __ para privado y _ para protegido</i></p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🆘 Ver Solución"):
        st.code("""
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular  # protegido
        self.__saldo = saldo_inicial  # privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depositado: ${cantidad}"
        return "Cantidad inválida"

    def retirar(self, cantidad):
        if cantidad > 0 and self.__saldo >= cantidad:
            self.__saldo -= cantidad
            return f"Retirado: ${cantidad}"
        return "Fondos insuficientes o cantidad inválida"

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self._titular
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")

    codigo_default = """class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        # Define atributo protegido para el titular
        # Define atributo privado para el saldo
        pass

    def depositar(self, cantidad):
        # Valida y deposita cantidad
        pass

    def retirar(self, cantidad):
        # Valida y retira cantidad
        pass

    def get_saldo(self):
        # Retorna el saldo privado
        pass

    def get_titular(self):
        # Retorna el titular protegido
        pass

# Prueba tu código:
cuenta = CuentaBancaria("Juan", 1000)
print(f"Titular: {cuenta.get_titular()}")
print(f"Saldo inicial: ${cuenta.get_saldo()}")
print(cuenta.depositar(500))
print(cuenta.retirar(200))
print(f"Saldo final: ${cuenta.get_saldo()}")"""

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
    <h3>🔒 Modificadores de Acceso</h3>
    <p>Python usa convenciones de nombres:</p>
    <ul>
        <li><b>_atributo:</b> Protegido (convención)</li>
        <li><b>__atributo:</b> Privado (name mangling)</li>
        <li><b>atributo:</b> Público</li>
    </ul>
    <p><b>Name Mangling:</b> __saldo → _Clase__saldo</p>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>🛡️ ¿Por qué Encapsular?</h3>
    <p>Beneficios del encapsulamiento:</p>
    <ul>
        <li>Control de acceso a datos</li>
        <li>Validación de valores</li>
        <li>Ocultar implementación</li>
        <li>Mayor seguridad</li>
    </ul>
    <p><b>Principio:</b> "Ocultar datos, exponer comportamiento"</p>
    </div>
    """, unsafe_allow_html=True)

# Ejemplo visual
st.markdown("---")
st.subheader("🎨 Ejemplo de Encapsulamiento")

st.markdown("""
<div class="explicacion">
<h3>🔐 Niveles de Acceso</h3>
<pre>
class Persona:
    def __init__(self):
        self.nombre = "Público"      # Accesible desde fuera
        self._edad = 25              # Protegido (convención)
        self.__dni = "12345678"      # Privado (name mangling)

p = Persona()
print(p.nombre)  # ✅ Funciona
print(p._edad)    # ⚠️ Funciona pero no recomendado
print(p.__dni)    # ❌ Error: AttributeError
</pre>
<p>El encapsulamiento protege los datos internos del objeto</p>
</div>
""", unsafe_allow_html=True)

# Demostración de name mangling
st.markdown("---")
st.subheader("🔍 Demostración: Name Mangling")

if st.button("🧪 Ver Name Mangling en Acción"):
    st.code("""
class Demo:
    def __init__(self):
        self.publico = "Público"
        self._protegido = "Protegido"
        self.__privado = "Privado"

obj = Demo()
print(obj.publico)     # "Público"
print(obj._protegido)  # "Protegido"
print(obj.__privado)   # ❌ AttributeError
print(obj._Demo__privado)  # "Privado" (name mangling)
    """, language="python")

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/05_Clase_Polimorfismo.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/07_Clase_MetodosEspeciales.py")
