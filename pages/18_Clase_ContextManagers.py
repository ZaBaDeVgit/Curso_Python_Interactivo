import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu, create_navigation_buttons
st.set_page_config(
    page_title="Clase 17 - Context Managers",
    page_icon="📁",
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

st.title("📁 Clase 17: Context Managers (__enter__, __exit__)")

# Crear menú lateral personalizado
create_sidebar_menu()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea clase GestorBaseDatos</h3>
    <p>Crea clase <b>GestorBaseDatos</b> con:</p>
    <ul>
        <li>Atributos: <b>nombre_db</b>, <b>conexion</b></li>
        <li><b>__enter__</b> que conecte a la BD</li>
        <li><b>__exit__</b> que desconecte y maneje errores</li>
        <li>Método <b>ejecutar_query()</b></li>
        <li>Método <b>commit()</b> y <b>rollback()</b></li>
        <li>Maneje excepciones y limpieza automática</li>
    </ul>
    <p><i>Pista: with GestorBaseDatos("mi_db") as db:</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🆘 Ver Solución"):
        st.code("""
import sqlite3
import time

class GestorBaseDatos:
    def __init__(self, nombre_db):
        self.nombre_db = nombre_db
        self.conexion = None
        self.cursor = None
    
    def __enter__(self):
        \"\"\"Se ejecuta al entrar al context manager\"\"\"
        print(f"🔌 Conectando a la base de datos: {self.nombre_db}")
        self.conexion = sqlite3.connect(self.nombre_db)
        self.cursor = self.conexion.cursor()
        # Crear tabla si no existe
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                email TEXT
            )
        ''')
        self.conexion.commit()
        print("✅ Conexión establecida")
        return self  # Este objeto se asigna a 'as db'
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        \"\"\"Se ejecuta al salir del context manager\"\"\"
        print("🔌 Cerrando conexión a la base de datos")
        if exc_type is not None:
            print(f"❌ Error ocurrido: {exc_type.__name__}: {exc_val}")
            if self.conexion:
                self.conexion.rollback()
                print("🔄 Rollback realizado")
        else:
            if self.conexion:
                self.conexion.commit()
                print("✅ Commit realizado")
        
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
        print("✅ Conexión cerrada")
        
        # Retornar False para no suprimir excepciones
        return False
    
    def ejecutar_query(self, query, params=None):
        \"\"\"Ejecuta un query SQL\"\"\"
        if self.cursor:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        return None
    
    def insertar_usuario(self, nombre, email):
        \"\"\"Inserta un usuario en la tabla\"\"\"
        query = "INSERT INTO usuarios (nombre, email) VALUES (?, ?)"
        self.cursor.execute(query, (nombre, email))
        print(f"👤 Usuario {nombre} insertado")
    
    def obtener_usuarios(self):
        \"\"\"Obtiene todos los usuarios\"\"\"
        query = "SELECT * FROM usuarios"
        return self.ejecutar_query(query)

# Pruebas
print("=== Uso Correcto ===")
with GestorBaseDatos("test.db") as db:
    db.insertar_usuario("Ana", "ana@email.com")
    db.insertar_usuario("Juan", "juan@email.com")
    usuarios = db.obtener_usuarios()
    print("Usuarios:", usuarios)

print("\\n=== Manejo de Errores ===")
try:
    with GestorBaseDatos("test.db") as db:
        db.insertar_usuario("Error", "error@email.com")
        # Provocar un error
        db.cursor.execute("SELECT * FROM tabla_inexistente")
except Exception as e:
    print(f"Excepción capturada fuera: {e}")

print("\\n=== Uso Anidado ===")
with GestorBaseDatos("test.db") as db1:
    with GestorBaseDatos("otro.db") as db2:
        print("📁 Dos bases de datos abiertas simultáneamente")
        db1.insertar_usuario("Usuario1", "user1@test.com")
        db2.insertar_usuario("Usuario2", "user2@otro.com")
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")
    
    codigo_default = """import sqlite3
import time

class GestorBaseDatos:
    def __init__(self, nombre_db):
        self.nombre_db = nombre_db
        self.conexion = None
        self.cursor = None
    
    def __enter__(self):
        \"\"\"Se ejecuta al entrar al context manager\"\"\"
        # TODO: Conectar a la base de datos
        print(f"🔌 Conectando a: {self.nombre_db}")
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        \"\"\"Se ejecuta al salir del context manager\"\"\"
        # TODO: Cerrar conexión y manejar errores
        print("🔌 Cerrando conexión")
        pass
    
    def ejecutar_query(self, query, params=None):
        \"\"\"Ejecuta un query SQL\"\"\"
        if self.cursor:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        return None
    
    def insertar_usuario(self, nombre, email):
        \"\"\"Inserta un usuario en la tabla\"\"\"
        query = "INSERT INTO usuarios (nombre, email) VALUES (?, ?)"
        self.cursor.execute(query, (nombre, email))
        print(f"👤 Usuario {nombre} insertado")
    
    def obtener_usuarios(self):
        \"\"\"Obtiene todos los usuarios\"\"\"
        query = "SELECT * FROM usuarios"
        return self.ejecutar_query(query)

# Prueba tu código:
print("=== Uso del Context Manager ===")
with GestorBaseDatos("test.db") as db:
    db.insertar_usuario("Ana", "ana@email.com")
    db.insertar_usuario("Juan", "juan@email.com")
    usuarios = db.obtener_usuarios()
    print("Usuarios:", usuarios)"""

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
    <h3>📁 ¿Qué son Context Managers?</h3>
    <p>Objetos que gestionan recursos automáticamente:</p>
    <ul>
        <li>Implementan protocolo de context manager</li>
        <li>Tienen <b>__enter__()</b> y <b>__exit__()</b></li>
        <li>Se usan con la declaración <b>with</b></li>
        <li>Garantizan limpieza de recursos</li>
    </ul>
    <p><b>Protocolo:</b></p>
    <ol>
        <li>with llama a <code>objeto.__enter__()</code></li>
        <li>Retorno se asigna a variable <b>as</b></li>
        <li>Se ejecuta código dentro del with</li>
        <li>Python llama a <code>objeto.__exit__()</code></li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>🔧 __enter__ y __exit__</h3>
    <p><b>__enter__(self):</b></p>
    <ul>
        <li>Se ejecuta al entrar al bloque with</li>
        <li>Debe retornar el objeto a usar</li>
        <li>Prepara recursos (conexiones, archivos)</li>
        <li>Retorna self usualmente</li>
    </ul>
    <p><b>__exit__(self, exc_type, exc_val, exc_tb):</b></p>
    <ul>
        <li>Se ejecuta al salir del bloque with</li>
        <li>Recibe info de excepción si ocurrió</li>
        <li>Limpia recursos (cierra conexiones)</li>
        <li>Retorna True para suprimir excepción</li>
    </ul>
    <p><b>Parámetros de __exit__:</b></p>
    <ul>
        <li><b>exc_type:</b> tipo de excepción (None si no hay)</li>
        <li><b>exc_val:</b> valor de la excepción</li>
        <li><b>exc_tb:</b> traceback de la excepción</li>
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
    <h3>⏱️ Ejemplo: Temporizador</h3>
    <p>Mide tiempo de ejecución automáticamente:</p>
    <pre><code>import time

class Temporizador:
    def __init__(self, nombre="Operación"):
        self.nombre = nombre
        self.inicio = None
        self.fin = None
    
    def __enter__(self):
        self.inicio = time.time()
        print(f"⏱️ Iniciando {self.nombre}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fin = time.time()
        duracion = self.fin - self.inicio
        print(f"✅ {self.nombre} completada en {duracion:.2f}s")
        return False

# Uso
with Temporizador("Cálculo complejo"):
    resultado = sum(i**2 for i in range(1000000))
print(f"Resultado: {resultado}")</code></pre>
    </div>
    """, unsafe_allow_html=True)

with col_ej2:
    st.markdown("""
    <div class="explicacion">
    <h3>🔐 Ejemplo: Gestor de Seguridad</h3>
    <p>Controla acceso y permisos:</p>
    <pre><code>class GestorSeguridad:
    def __init__(self, usuario, permiso):
        self.usuario = usuario
        self.permiso = permiso
        self.autorizado = False
    
    def __enter__(self):
        if self.tiene_permiso():
            self.autorizado = True
            print(f"🔓 {self.usuario} autorizado")
            return self
        else:
            raise PermissionError(f"❌ {self.usuario} no tiene permiso {self.permiso}")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.autorizado:
            print(f"🔒 Cerrando sesión de {self.usuario}")
            self.autorizado = False
        return False
    
    def tiene_permiso(self):
        # Lógica de verificación
        return self.usuario == "admin"

# Uso
try:
    with GestorSeguridad("admin", "escribir") as seg:
        print("📝 Realizando operación segura")
except PermissionError as e:
    print(e)</code></pre>
    </div>
    """, unsafe_allow_html=True)

# Context Manager con @contextmanager
st.markdown("---")
st.subheader("🎯 Alternativa: @contextmanager")

st.markdown("""
<div class="explicacion">
<h3>📦 Usando contextlib.contextmanager</h3>
<p>Python ofrece una forma más simple de crear context managers:</p>
<pre><code>from contextlib import contextmanager

@contextmanager
def mi_context_manager():
    # Código de __enter__
    print("🔌 Iniciando recurso")
    recurso = "Recurso creado"
    
    try:
        yield recurso  # Equivale a return en __enter__
    finally:
        # Código de __exit__
        print("🔌 Limpiando recurso")
        # Limpieza automática

# Uso
with mi_context_manager() as recurso:
    print(f"Usando: {recurso}")
    # Salida: 🔌 Iniciando recurso
    #         Usando: Recurso creado
    #         🔌 Limpiando recurso</code></pre>

<h3>⚡ Ventajas de @contextmanager</h3>
<ul>
    <li><b>Más simple:</b> No necesita clase completa</li>
    <li><b>Menos código:</b> Solo función con yield</li>
    <li><b>Automático:</b> try/finally maneja excepciones</li>
    <li><b>Flexibilidad:</b> Ideal para casos simples</li>
</ul>

<h3>🔄 Cuándo usar cada uno</h3>
<ul>
    <li><b>Clase con __enter__/__exit__:</b> Para objetos complejos con estado</li>
    <li><b>@contextmanager:</b> Para recursos simples sin estado persistente</li>
    <li><b>Clase:</b> Cuando necesitas métodos adicionales</li>
    <li><b>Función:</b> Cuando solo necesitas setup/teardown</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/17_Clase_IteradoresGeneradores.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/19_Clase_DataClasses.py")
