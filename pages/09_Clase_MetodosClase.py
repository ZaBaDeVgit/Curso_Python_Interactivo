import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu

st.set_page_config(
    page_title="Clase 8 - Métodos de Clase",
    page_icon="🔧",
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
    st.page_link("pages/08_Clase_Propiedades.py", label="⬅️ Anterior")
    st.page_link("pages/10_Clase_Composicion.py", label="➡️ Siguiente")

st.title("🔧 Clase 8: Métodos de Clase y Estáticos")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea clase Usuario</h3>
    <p>Debe tener:</p>
    <ul>
        <li>Atributos: <b>nombre</b>, <b>email</b>, <b>activo</b></li>
        <li>Contador de clase: <b>total_usuarios</b></li>
        <li><b>@classmethod</b> crear_admin()</li>
        <li><b>@staticmethod</b> validar_email()</li>
        <li><b>@classmethod</b> from_dict()</li>
    </ul>
    <p><i>Pista: @classmethod recibe cls, @staticmethod no</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🆘 Ver Solución"):
        st.code("""
class Usuario:
    total_usuarios = 0
    
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.activo = True
        Usuario.total_usuarios += 1
    
    @classmethod
    def crear_admin(cls, nombre, email):
        admin = cls(nombre, email)
        admin.activo = True
        admin.es_admin = True
        return admin
    
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email
    
    @classmethod
    def from_dict(cls, datos):
        return cls(datos['nombre'], datos['email'])
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")
    
    codigo_default = """class Usuario:
    total_usuarios = 0
    
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.activo = True
        # Incrementa el contador de clase
        pass
    
    @classmethod
    def crear_admin(cls, nombre, email):
        # Crea un usuario admin
        pass
    
    @staticmethod
    def validar_email(email):
        # Valida formato de email
        pass
    
    @classmethod
    def from_dict(cls, datos):
        # Crea usuario desde diccionario
        pass

# Prueba tu código:
user1 = Usuario("Ana", "ana@email.com")
admin = Usuario.crear_admin("Admin", "admin@site.com")
datos = {"nombre": "Juan", "email": "juan@email.com"}
user2 = Usuario.from_dict(datos)

print(f"Total usuarios: {Usuario.total_usuarios}")
print(f"Email válido: {Usuario.validar_email('test@test.com')}")
print(f"Admin: {admin.nombre}, Activo: {admin.activo}")"""

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
    <h3>🔧 @classmethod</h3>
    <p>Método que recibe la clase como primer parámetro:</p>
    <ul>
        <li>Recibe <b>cls</b> en lugar de <b>self</b></li>
        <li>Puede acceder a atributos de clase</li>
        <li>Útil para factory methods</li>
        <li>Puede crear instancias</li>
    </ul>
    <p><b>Uso:</b> <code>Usuario.crear_admin()</code></p>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>⚡ @staticmethod</h3>
    <p>Método que no recibe ni self ni cls:</p>
    <ul>
        <li>Independiente de la clase</li>
        <li>No puede acceder a atributos</li>
        <li>Función utilitaria</li>
        <li>Organización lógica</li>
    </ul>
    <p><b>Uso:</b> <code>Usuario.validar_email()</code></p>
    </div>
    """, unsafe_allow_html=True)

# Tabla comparativa
st.markdown("---")
st.subheader("📋 Comparación de Métodos")

st.markdown("""
<div class="explicacion">
<h3>⚖️ Tipos de Métodos en Clases</h3>
<table style="width: 100%; border-collapse: collapse;">
    <tr style="background-color: #e8f4f8;">
        <th style="padding: 8px; border: 1px solid #ddd;">Tipo</th>
        <th style="padding: 8px; border: 1px solid #ddd;">Parámetro</th>
        <th style="padding: 8px; border: 1px solid #ddd;">Acceso</th>
        <th style="padding: 8px; border: 1px solid #ddd;">Uso</th>
    </tr>
    <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">Instancia</td>
        <td style="padding: 8px; border: 1px solid #ddd;">self</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Atributos de instancia</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Operaciones del objeto</td>
    </tr>
    <tr style="background-color: #f8f8f8;">
        <td style="padding: 8px; border: 1px solid #ddd;">Clase</td>
        <td style="padding: 8px; border: 1px solid #ddd;">cls</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Atributos de clase</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Factory methods</td>
    </tr>
    <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">Estático</td>
        <td style="padding: 8px; border: 1px solid #ddd;">ninguno</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Ninguno</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Funciones utilitarias</td>
    </tr>
</table>
</div>
""", unsafe_allow_html=True)

# Ejemplo de factory method
st.markdown("---")
st.subheader("🏭 Factory Methods")

st.markdown("""
<div class="explicacion">
<h3>🏗️ Patrones Factory con @classmethod</h3>
<pre>
class Figura:
    def __init__(self, tipo, dimensiones):
        self.tipo = tipo
        self.dimensiones = dimensiones
    
    @classmethod
    def crear_cuadrado(cls, lado):
        return cls("cuadrado", {"lado": lado})
    
    @classmethod
    def crear_circulo(cls, radio):
        return cls("circulo", {"radio": radio})

# Uso:
cuadrado = Figura.crear_cuadrado(5)
circulo = Figura.crear_circulo(3)
</pre>
<p>Los factory methods simplifican la creación de objetos complejos</p>
</div>
""", unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/08_Clase_Propiedades.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/10_Clase_Composicion.py")
