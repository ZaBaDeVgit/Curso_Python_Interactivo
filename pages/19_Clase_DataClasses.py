import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu
st.set_page_config(
    page_title="Clase 18 - Data Classes",
    page_icon="📊",
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

st.title("📊 Clase 18: Data Classes")

# Crear menú lateral personalizado
create_sidebar_menu()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea sistema de Gestión de Productos</h3>
    <p>Crea usando <b>@dataclass</b>:</p>
    <ul>
        <li><b>Producto</b> con id, nombre, precio, stock</li>
        <li><b>Cliente</b> con id, nombre, email, vip</li>
        <li><b>Pedido</b> con id, cliente, productos, total</li>
        <li>Usa <b>field(default_factory=list)</b></li>
        <li>Usa <b>__post_init__</b> para calcular total</li>
        <li>Usa <b>frozen=True</b> donde sea apropiado</li>
    </ul>
    <p><i>Pista: from dataclasses import dataclass, field</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🆘 Ver Solución"):
        st.code("""
from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class Producto:
    id: int
    nombre: str
    precio: float
    stock: int = 0
    
    def __post_init__(self):
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo")
    
    @property
    def disponible(self) -> bool:
        return self.stock > 0
    
    def actualizar_stock(self, cantidad: int):
        self.stock += cantidad
    
    def __str__(self):
        return f"#{self.id} {self.nombre} - ${self.precio:.2f} (Stock: {self.stock})"

@dataclass(frozen=True)
class Cliente:
    id: int
    nombre: str
    email: str
    vip: bool = False
    fecha_registro: datetime = field(default_factory=datetime.now)
    
    @property
    def descuento(self) -> float:
        return 0.15 if self.vip else 0.0
    
    def __str__(self):
        vip_str = "VIP" if self.vip else "Regular"
        return f"{self.nombre} ({vip_str}) - {self.email}"

@dataclass
class Pedido:
    id: int
    cliente: Cliente
    productos: List[Producto] = field(default_factory=list)
    total: float = field(init=False)
    fecha: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        self.calcular_total()
    
    def agregar_producto(self, producto: Producto, cantidad: int = 1):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if not producto.disponible:
            raise ValueError(f"Producto {producto.nombre} no disponible")
        if producto.stock < cantidad:
            raise ValueError(f"Stock insuficiente. Disponible: {producto.stock}")
        
        # Agregar productos al pedido
        for _ in range(cantidad):
            self.productos.append(producto)
        
        # Actualizar stock del producto
        producto.actualizar_stock(-cantidad)
        self.calcular_total()
    
    def calcular_total(self):
        subtotal = sum(p.precio for p in self.productos)
        descuento = subtotal * self.cliente.descuento
        self.total = subtotal - descuento
    
    def resumen(self) -> str:
        resumen = f"📦 Pedido #{self.id}\\n"
        resumen += f"👤 Cliente: {self.cliente.nombre}\\n"
        resumen += f"📅 Fecha: {self.fecha.strftime('%d/%m/%Y')}\\n"
        resumen += f"🛍️ Productos ({len(self.productos)}):\\n"
        
        # Contar productos por nombre
        productos_contados = {}
        for p in self.productos:
            productos_contados[p.nombre] = productos_contados.get(p.nombre, 0) + 1
        
        for nombre, cantidad in productos_contados.items():
            resumen += f"  - {nombre} x{cantidad}\\n"
        
        resumen += f"💰 Total: ${self.total:.2f}"
        return resumen
    
    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nombre} - ${self.total:.2f}"

# Pruebas
print("=== Creando Productos ===")
p1 = Producto(1, "Laptop", 999.99, 10)
p2 = Producto(2, "Mouse", 29.99, 50)
p3 = Producto(3, "Teclado", 79.99, 25)

print(p1)
print(p2)
print(p3)

print("\\n=== Creando Clientes ===")
c1 = Cliente(1, "Ana García", "ana@email.com", vip=True)
c2 = Cliente(2, "Juan Pérez", "juan@email.com")

print(c1)
print(f"Descuento de {c1.nombre}: {c1.descuento*100:.0f}%")
print(f"Descuento de {c2.nombre}: {c2.descuento*100:.0f}%")

print("\\n=== Creando Pedidos ===")
pedido1 = Pedido(1, c1)
pedido1.agregar_producto(p1, 1)
pedido1.agregar_producto(p2, 2)

pedido2 = Pedido(2, c2)
pedido2.agregar_producto(p3, 1)
pedido2.agregar_producto(p2, 1)

print(pedido1)
print(pedido2)

print("\\n=== Resúmenes ===")
print(pedido1.resumen())
print("\\n" + "="*40 + "\\n")
print(pedido2.resumen())

print("\\n=== Stock Actualizado ===")
print(f"Stock Laptop: {p1.stock}")
print(f"Stock Mouse: {p2.stock}")
print(f"Stock Teclado: {p3.stock}")
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")
    
    codigo_default = """from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class Producto:
    id: int
    nombre: str
    precio: float
    stock: int = 0
    
    def __post_init__(self):
        # Validar que precio y stock no sean negativos
        pass
    
    @property
    def disponible(self) -> bool:
        # Retornar True si hay stock
        pass
    
    def actualizar_stock(self, cantidad: int):
        # Actualizar stock (positivo o negativo)
        pass

@dataclass(frozen=True)
class Cliente:
    id: int
    nombre: str
    email: str
    vip: bool = False
    fecha_registro: datetime = field(default_factory=datetime.now)
    
    @property
    def descuento(self) -> float:
        # Retornar 15% si es VIP, 0% si no
        pass

@dataclass
class Pedido:
    id: int
    cliente: Cliente
    productos: List[Producto] = field(default_factory=list)
    total: float = field(init=False)
    fecha: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        # Calcular total inicial
        pass
    
    def agregar_producto(self, producto: Producto, cantidad: int = 1):
        # Validar y agregar productos al pedido
        pass
    
    def calcular_total(self):
        # Calcular total con descuento
        pass

# Prueba tu código:
p1 = Producto(1, "Laptop", 999.99, 10)
c1 = Cliente(1, "Ana", "ana@email.com", vip=True)
pedido = Pedido(1, c1)
pedido.agregar_producto(p1, 1)
print(f"Total del pedido: ${pedido.total:.2f}")"""

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
    <h3>📊 ¿Qué son Data Classes?</h3>
    <p>Clases diseñadas para almacenar datos:</p>
    <ul>
        <li>Usan decorador @dataclass</li>
        <li>Generan automáticamente __init__, __repr__, etc.</li>
        <li>Ideales para objetos que solo contienen datos</li>
        <li>Disponibles desde Python 3.7</li>
    </ul>
    <p><b>Métodos generados automáticamente:</b></p>
    <ul>
        <li><b>__init__()</b> - constructor</li>
        <li><b>__repr__()</b> - representación oficial</li>
        <li><b>__eq__()</b> - comparación de igualdad</li>
        <li><b>__hash__()</b> - para usar como clave (si frozen)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>⚙️ Parámetros del Decorador</h3>
    <p><b>@dataclass(opciones):</b></p>
    <ul>
        <li><b>init=True</b> - generar __init__</li>
        <li><b>repr=True</b> - generar __repr__</li>
        <li><b>eq=True</b> - generar __eq__</li>
        <li><b>order=False</b> - generar métodos de comparación</li>
        <li><b>unsafe_hash=False</b> - generar __hash__</li>
        <li><b>frozen=False</b> - hacer inmutable</li>
    </ul>
    <p><b>field():</b> para configuración avanzada</p>
    <ul>
        <li><b>default=valor</b> - valor por defecto</li>
        <li><b>default_factory=func</b> - función para valor</li>
        <li><b>init=False</b> - no incluir en __init__</li>
        <li><b>repr=True</b> - incluir en __repr__</li>
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
    <h3>🎮 Ejemplo: Juego</h3>
    <p>Personajes y items del juego:</p>
    <pre><code>@dataclass
class Personaje:
    nombre: str
    vida: int = 100
    nivel: int = 1
    experiencia: int = 0
    
    def ganar_experiencia(self, exp: int):
        self.experiencia += exp
        if self.experiencia >= self.nivel * 100:
            self.subir_nivel()
    
    def subir_nivel(self):
        self.nivel += 1
        self.vida += 20
        print(f"🎉 ¡Nivel {self.nivel}!")

@dataclass
class Item:
    nombre: str
    tipo: str
    poder: int
    
    def usar(self, personaje: Personaje):
        if self.tipo == "pocion":
            personaje.vida += self.poder
        elif self.tipo == "arma":
            personaje.nivel += 1</code></pre>
    </div>
    """, unsafe_allow_html=True)

with col_ej2:
    st.markdown("""
    <div class="explicacion">
    <h3>📈 Ejemplo: Finanzas</h3>
    <p>Transacciones y cuentas:</p>
    <pre><code>@dataclass
class Transaccion:
    id: str
    monto: float
    tipo: str  # "ingreso" o "egreso"
    categoria: str
    fecha: datetime = field(default_factory=datetime.now)
    
    @property
    def es_ingreso(self) -> bool:
        return self.tipo == "ingreso"
    
    @property
    def es_egreso(self) -> bool:
        return self.tipo == "egreso"

@dataclass
class Cuenta:
    titular: str
    saldo: float = 0.0
    transacciones: List[Transaccion] = field(default_factory=list)
    
    def agregar_transaccion(self, trans: Transaccion):
        self.transacciones.append(trans)
        if trans.es_ingreso:
            self.saldo += trans.monto
        else:
            self.saldo -= trans.monto</code></pre>
    </div>
    """, unsafe_allow_html=True)

# Comparación y mejores prácticas
st.markdown("---")
st.subheader("🎯 Data Classes vs Clases Tradicionales")

st.markdown("""
<div class="explicacion">
<h3>📊 Cuándo usar Data Classes</h3>
<p><b>✅ Ideal para:</b></p>
<ul>
    <li>Objetos que principalmente almacenan datos</li>
    <li>Estructuras de datos simples</li>
    <li>DTOs (Data Transfer Objects)</li>
    <li>Configuraciones y settings</li>
    <li>Registros de base de datos</li>
    <li>API responses</li>
</ul>

<p><b>❌ No ideal para:</b></p>
<ul>
    <li>Clases con mucha lógica compleja</li>
    <li>Objetos que necesitan herencia múltiple</li>
    <li>Clases con comportamiento polimórfico</li>
    <li>Sistemas que requieren control total sobre __init__</li>
</ul>

<h3>⚡ Mejores Prácticas</h3>
<ul>
    <li><b>Usa type hints</b> - Mejora documentación y validación</li>
    <li><b>__post_init__</b> - Para validación y cálculos iniciales</li>
    <li><b>frozen=True</b> - Para objetos inmutables</li>
    <li><b>field(default_factory=list)</b> - Para valores mutables por defecto</li>
    <li><b>Propiedades</b> - Para datos calculados</li>
    <li><b>Métodos simples</b> - Para lógica relacionada con los datos</li>
</ul>

<h3>🔧 Ejemplo Completo</h3>
<pre><code>@dataclass(frozen=True)
class Coordenada:
    x: float
    y: float
    z: float = 0.0
    
    @property
    def magnitud(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5
    
    def distancia_a(self, otra: 'Coordenada') -> float:
        dx = self.x - otra.x
        dy = self.y - otra.y
        dz = self.z - otra.z
        return (dx**2 + dy**2 + dz**2) ** 0.5
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

# Uso
p1 = Coordenada(1, 2, 3)
p2 = Coordenada(4, 6, 8)
print(f"Distancia: {p1.distancia_a(p2):.2f}")
print(f"Magnitud de p1: {p1.magnitud:.2f}")</code></pre>
</div>
""", unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/18_Clase_ContextManagers.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/20_Clase_Enums.py")
