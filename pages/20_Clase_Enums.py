import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu

st.set_page_config(
    page_title="Clase 19 - Enums",
    page_icon="🏷️",
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

st.title("🏷️ Clase 19: Enums y Clases Enumeradas")

# Crear menú lateral personalizado
create_sidebar_menu()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea sistema de Estados de Pedido</h3>
    <p>Crea usando <b>Enum</b> y <b>IntEnum</b>:</p>
    <ul>
        <li><b>EstadoPedido</b> con PENDIENTE, PROCESANDO, ENVIADO, ENTREGADO</li>
        <li><b>Prioridad</b> con BAJA=1, MEDIA=2, ALTA=3, URGENTE=4</li>
        <li><b>TipoProducto</b> con valores y descripciones</li>
        <li>Usa <b>@unique</b> para evitar duplicados</li>
        <li>Agrega métodos personalizados a los enums</li>
        <li>Usa <b>auto()</b> para valores automáticos</li>
    </ul>
    <p><i>Pista: from enum import Enum, IntEnum, auto, unique</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🆘 Ver Solución"):
        st.code("""
from enum import Enum, IntEnum, auto, unique
from typing import Dict, Any

@unique
class EstadoPedido(Enum):
    PENDIENTE = "pendiente"
    PROCESANDO = "procesando"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"
    
    @property
    def es_final(self) -> bool:
        return self in [EstadoPedido.ENTREGADO, EstadoPedido.CANCELADO]
    
    @property
    def es_activo(self) -> bool:
        return self in [EstadoPedido.PENDIENTE, EstadoPedido.PROCESANDO, EstadoPedido.ENVIADO]
    
    @property
    def color(self) -> str:
        colores = {
            EstadoPedido.PENDIENTE: "🟡",
            EstadoPedido.PROCESANDO: "🟠",
            EstadoPedido.ENVIADO: "🔵",
            EstadoPedido.ENTREGADO: "🟢",
            EstadoPedido.CANCELADO: "🔴"
        }
        return colores[self]
    
    def siguiente_estado(self) -> 'EstadoPedido':
        transiciones = {
            EstadoPedido.PENDIENTE: EstadoPedido.PROCESANDO,
            EstadoPedido.PROCESANDO: EstadoPedido.ENVIADO,
            EstadoPedido.ENVIADO: EstadoPedido.ENTREGADO,
            EstadoPedido.ENTREGADO: EstadoPedido.ENTREGADO,  # Estado final
            EstadoPedido.CANCELADO: EstadoPedido.CANCELADO   # Estado final
        }
        return transiciones.get(self, self)
    
    def puede_transicionar_a(self, nuevo_estado: 'EstadoPedido') -> bool:
        transiciones_permitidas = {
            EstadoPedido.PENDIENTE: [EstadoPedido.PROCESANDO, EstadoPedido.CANCELADO],
            EstadoPedido.PROCESANDO: [EstadoPedido.ENVIADO, EstadoPedido.CANCELADO],
            EstadoPedido.ENVIADO: [EstadoPedido.ENTREGADO],
            EstadoPedido.ENTREGADO: [],  # No puede cambiar
            EstadoPedido.CANCELADO: []  # No puede cambiar
        }
        return nuevo_estado in transiciones_permitidas[self]
    
    def __str__(self):
        return f"{self.color} {self.value.title()}"

@unique
class Prioridad(IntEnum):
    BAJA = 1
    MEDIA = 2
    ALTA = 3
    URGENTE = 4
    
    @property
    def color(self) -> str:
        colores = {
            Prioridad.BAJA: "🟢",
            Prioridad.MEDIA: "🟡",
            Prioridad.ALTA: "🟠",
            Prioridad.URGENTE: "🔴"
        }
        return colores[self]
    
    @property
    def tiempo_estimado_horas(self) -> int:
        tiempos = {
            Prioridad.BAJA: 72,    # 3 días
            Prioridad.MEDIA: 48,   # 2 días
            Prioridad.ALTA: 24,    # 1 día
            Prioridad.URGENTE: 4   # 4 horas
        }
        return tiempos[self]
    
    def __str__(self):
        return f"{self.color} {self.name.title()} (Nivel {self.value})"

@unique
class TipoProducto(Enum):
    ELECTRONICA = ("electrónica", "Dispositivos electrónicos y gadgets")
    ROPA = ("ropa", "Vestimenta y accesorios")
    ALIMENTOS = ("alimentos", "Productos comestibles y bebidas")
    HOGAR = ("hogar", "Artículos para el hogar y decoración")
    LIBROS = ("libros", "Libros y material educativo")
    JUGUETES = ("juguetes", "Juguetes y juegos")
    
    def __init__(self, categoria: str, descripcion: str):
        self.categoria = categoria
        self.descripcion = descripcion
    
    @property
    def icono(self) -> str:
        iconos = {
            TipoProducto.ELECTRONICA: "📱",
            TipoProducto.ROPA: "👕",
            TipoProducto.ALIMENTOS: "🍔",
            TipoProducto.HOGAR: "🏠",
            TipoProducto.LIBROS: "📚",
            TipoProducto.JUGUETES: "🎮"
        }
        return iconos[self]
    
    @property
    def impuesto_porcentaje(self) -> float:
        impuestos = {
            TipoProducto.ELECTRONICA: 0.21,  # 21%
            TipoProducto.ROPA: 0.16,         # 16%
            TipoProducto.ALIMENTOS: 0.08,   # 8%
            TipoProducto.HOGAR: 0.16,       # 16%
            TipoProducto.LIBROS: 0.04,      # 4%
            TipoProducto.JUGUETES: 0.16      # 16%
        }
        return impuestos[self]
    
    def __str__(self):
        return f"{self.icono} {self.descripcion}"

# Clase que usa los enums
@dataclass
class Pedido:
    id: int
    estado: EstadoPedido
    prioridad: Prioridad
    tipo_producto: TipoProducto
    monto: float
    
    @property
    def impuesto(self) -> float:
        return self.monto * self.tipo_producto.impuesto_porcentaje
    
    @property
    def total_con_impuesto(self) -> float:
        return self.monto + self.impuesto
    
    @property
    def tiempo_entrega_estimado(self) -> str:
        base = self.prioridad.tiempo_estimado_horas
        if self.tipo_producto == TipoProducto.ALIMENTOS:
            base = min(base, 24)  # Los alimentos son más rápidos
        elif self.tipo_producto == TipoProducto.ELECTRONICA:
            base = max(base, 48)  # La electrónica tarda más
        
        if base >= 24:
            return f"{base // 24} días"
        else:
            return f"{base} horas"
    
    def avanzar_estado(self) -> bool:
        if self.estado.es_final:
            return False
        
        siguiente = self.estado.siguiente_estado()
        if self.estado.puede_transicionar_a(siguiente):
            self.estado = siguiente
            return True
        return False
    
    def resumen(self) -> str:
        return f"""
📦 Pedido #{self.id}
{self.estado} | {self.prioridad}
🛍️ {self.tipo_producto}
💰 Monto: ${self.monto:.2f}
🧾 Impuesto: ${self.impuesto:.2f}
💳 Total: ${self.total_con_impuesto:.2f}
⏰ Entrega estimada: {self.tiempo_entrega_estimado}
        """.strip()

# Pruebas
print("=== Estados de Pedido ===")
for estado in EstadoPedido:
    print(f"{estado} - Final: {estado.es_final} - Activo: {estado.es_activo}")

print("\\n=== Prioridades ===")
for prioridad in Prioridad:
    print(f"{prioridad} - Tiempo: {prioridad.tiempo_estimado_horas}h")

print("\\n=== Tipos de Producto ===")
for tipo in TipoProducto:
    print(f"{tipo} - Impuesto: {tipo.impuesto_porcentaje*100:.0f}%")

print("\\n=== Sistema de Pedidos ===")
pedido1 = Pedido(
    id=1,
    estado=EstadoPedido.PENDIENTE,
    prioridad=Prioridad.ALTA,
    tipo_producto=TipoProducto.ELECTRONICA,
    monto=999.99
)

pedido2 = Pedido(
    id=2,
    estado=EstadoPedido.PROCESANDO,
    prioridad=Prioridad.MEDIA,
    tipo_producto=TipoProducto.LIBROS,
    monto=49.99
)

print(pedido1.resumen())
print("\\n" + "="*40 + "\\n")
print(pedido2.resumen())

print("\\n=== Simulación de Cambios de Estado ===")
print(f"Estado inicial: {pedido1.estado}")
while pedido1.avanzar_estado():
    print(f"Estado avanzado a: {pedido1.estado}")
print(f"Estado final: {pedido1.estado}")

print("\\n=== Validación de Transiciones ===")
print(f"¿Puede pasar de PENDIENTE a PROCESANDO? {EstadoPedido.PENDIENTE.puede_transicionar_a(EstadoPedido.PROCESANDO)}")
print(f"¿Puede pasar de ENVIADO a PENDIENTE? {EstadoPedido.ENVIADO.puede_transicionar_a(EstadoPedido.PENDIENTE)}")
print(f"¿Puede pasar de ENTREGADO a CANCELADO? {EstadoPedido.ENTREGADO.puede_transicionar_a(EstadoPedido.CANCELADO)}")
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")
    
    codigo_default = """from enum import Enum, IntEnum, auto, unique
from dataclasses import dataclass

@unique
class EstadoPedido(Enum):
    PENDIENTE = "pendiente"
    PROCESANDO = "procesando"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"
    
    @property
    def es_final(self) -> bool:
        # Retornar True si es estado final
        pass
    
    @property
    def es_activo(self) -> bool:
        # Retornar True si está en proceso
        pass

@unique
class Prioridad(IntEnum):
    BAJA = 1
    MEDIA = 2
    ALTA = 3
    URGENTE = 4
    
    @property
    def tiempo_estimado_horas(self) -> int:
        # Retornar horas según prioridad
        pass

@unique
class TipoProducto(Enum):
    ELECTRONICA = ("electrónica", "Dispositivos electrónicos")
    ROPA = ("ropa", "Vestimenta y accesorios")
    ALIMENTOS = ("alimentos", "Productos comestibles")
    
    def __init__(self, categoria: str, descripcion: str):
        self.categoria = categoria
        self.descripcion = descripcion
    
    @property
    def impuesto_porcentaje(self) -> float:
        # Retornar porcentaje de impuesto según tipo
        pass

@dataclass
class Pedido:
    id: int
    estado: EstadoPedido
    prioridad: Prioridad
    tipo_producto: TipoProducto
    monto: float
    
    @property
    def impuesto(self) -> float:
        # Calcular impuesto
        pass
    
    @property
    def total_con_impuesto(self) -> float:
        # Calcular total con impuesto
        pass

# Prueba tu código:
pedido = Pedido(
    id=1,
    estado=EstadoPedido.PENDIENTE,
    prioridad=Prioridad.ALTA,
    tipo_producto=TipoProducto.ELECTRONICA,
    monto=999.99
)

print(f"Total con impuesto: ${pedido.total_con_impuesto:.2f}")
print(f"¿Es estado final? {pedido.estado.es_final}")"""

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
    <h3>🏷️ ¿Qué son Enums?</h3>
    <p>Clases que definen un conjunto de constantes con nombre:</p>
    <ul>
        <li>Valores fijos y predefinidos</li>
        <li>Evitan "magic numbers" o strings</li>
        <li>Proporcionan seguridad de tipos</li>
        <li>Mejoran legibilidad del código</li>
    </ul>
    <p><b>Tipos de Enums:</b></p>
    <ul>
        <li><b>Enum</b> - valores arbitrarios</li>
        <li><b>IntEnum</b> - valores enteros</li>
        <li><b>Flag</b> - combinaciones bit a bit</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>⚙️ Decoradores y Funciones</h3>
    <p><b>@unique:</b></p>
    <ul>
        <li>Evita valores duplicados</li>
        <li>Lanza ValueError si hay duplicados</li>
        <li>Útil para detectar errores temprano</li>
    </ul>
    <p><b>auto():</b></p>
    <ul>
        <li>Asigna valores automáticamente</li>
        <li>Comienza desde 1 y se incrementa</li>
        <li>Solo funciona con ciertos tipos</li>
    </ul>
    <p><b>Métodos útiles:</b></p>
    <ul>
        <li><b>Enum.value</b> - valor del miembro</li>
        <li><b>Enum.name</b> - nombre del miembro</li>
        <li><b>Enum.__members__</b> - diccionario de miembros</li>
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
    <p>Estados y tipos en un juego:</p>
    <pre><code>from enum import Enum, auto

@unique
class EstadoJuego(Enum):
    MENU = auto()
    JUGANDO = auto()
    PAUSADO = auto()
    GAME_OVER = auto()
    VICTORIA = auto()

@unique
class TipoEnemigo(Enum):
    GOBLIN = ("goblin", 10, 2)
    ORCO = ("orco", 20, 5)
    DRAGON = ("dragón", 100, 20)
    
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida_maxima = vida
        self.ataque_base = ataque
    
    @property
    def dificultad(self) -> str:
        if self.vida_maxima < 15:
            return "Fácil"
        elif self.vida_maxima < 50:
            return "Medio"
        else:
            return "Difícil"</code></pre>
    </div>
    """, unsafe_allow_html=True)

with col_ej2:
    st.markdown("""
    <div class="explicacion">
    <h3>🌐 Ejemplo: Protocolos de Red</h3>
    <p>Códigos de estado HTTP:</p>
    <pre><code>from enum import IntEnum

@unique
class CodigoHTTP(IntEnum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_ERROR = 500
    
    @property
    def es_exitoso(self) -> bool:
        return 200 <= self.value < 300
    
    @property
    def es_error_cliente(self) -> bool:
        return 400 <= self.value < 500
    
    @property
    def es_error_servidor(self) -> bool:
        return 500 <= self.value < 600
    
    @property
    def categoria(self) -> str:
        if self.es_exitoso:
            return "✅ Éxito"
        elif self.es_error_cliente:
            return "❌ Error Cliente"
        elif self.es_error_servidor:
            return "🔥 Error Servidor"
        else:
            return "❓ Desconocido"</code></pre>
    </div>
    """, unsafe_allow_html=True)

# Patrones avanzados
st.markdown("---")
st.subheader("🚀 Patrones Avanzados con Enums")

st.markdown("""
<div class="explicacion">
<h3>🎯 Enums con Métodos Complejos</h3>
<p>Los enums pueden tener lógica sofisticada:</p>
<pre><code>@unique
class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7
    
    @property
    def es_laboral(self) -> bool:
        return self.value <= 5
    
    @property
    def es_fin_de_semana(self) -> bool:
        return not self.es_laboral
    
    def siguiente(self) -> 'DiaSemana':
        if self == DiaSemana.DOMINGO:
            return DiaSemana.LUNES
        return DiaSemana(self.value + 1)
    
    def anterior(self) -> 'DiaSemana':
        if self == DiaSemana.LUNES:
            return DiaSemana.DOMINGO
        return DiaSemana(self.value - 1)
    
    def dias_hasta(self, otro: 'DiaSemana') -> int:
        if otro.value >= self.value:
            return otro.value - self.value
        else:
            return (7 - self.value) + otro.value
    
    @classmethod
    def desde_nombre(cls, nombre: str) -> 'DiaSemana':
        nombre_normalizado = nombre.upper().strip()
        for dia in cls:
            if dia.name == nombre_normalizado:
                return dia
        raise ValueError(f"Día '{nombre}' no válido")

# Uso
hoy = DiaSemina.MIERCOLES
print(f"Hoy es {hoy.name}, ¿es laboral? {hoy.es_laboral}")
print(f"Mañana será {hoy.siguiente().name}")
print(f"Faltan {hoy.dias_hasta(DiaSemana.SABADO)} días para sábado")</code></pre>

<h3>🔄 Enums para Máquinas de Estado</h3>
<p>Perfectos para representar estados y transiciones:</p>
<pre><code>@unique
class EstadoConexion(Enum):
    DESCONECTADO = "desconectado"
    CONECTANDO = "conectando"
    CONECTADO = "conectado"
    ERROR = "error"
    REINTENTANDO = "reintentando"
    
    def puede_transicionar_a(self, nuevo_estado: 'EstadoConexion') -> bool:
        transiciones = {
            self.DESCONECTADO: [self.CONECTANDO],
            self.CONECTANDO: [self.CONECTADO, self.ERROR],
            self.CONECTADO: [self.DESCONECTADO],
            self.ERROR: [self.REINTENTANDO, self.DESCONECTADO],
            self.REINTENTANDO: [self.CONECTANDO, self.ERROR]
        }
        return nuevo_estado in transiciones.get(self, [])
    
    def transiciones_permitidas(self) -> List['EstadoConexion']:
        todas = [EstadoConexion.DESCONECTADO, EstadoConexion.CONECTANDO,
                EstadoConexion.CONECTADO, EstadoConexion.ERROR, 
                EstadoConexion.REINTENTANDO]
        return [estado for estado in todas if self.puede_transicionar_a(estado)]</code></pre>

<h3>🏭 Enums para Configuración</h3>
<p>Centralizar configuraciones y constantes:</p>
<pre><code>@unique
class ConfiguracionDB(Enum):
    DESARROLLO = {
        "host": "localhost",
        "port": 5432,
        "database": "dev_db",
        "timeout": 30
    }
    PRUEBAS = {
        "host": "localhost",
        "port": 5433,
        "database": "test_db",
        "timeout": 10
    }
    PRODUCCION = {
        "host": "prod-server.com",
        "port": 5432,
        "database": "prod_db",
        "timeout": 60
    }
    
    @property
    def host(self) -> str:
        return self.value["host"]
    
    @property
    def port(self) -> int:
        return self.value["port"]
    
    @property
    def connection_string(self) -> str:
        return f"postgresql://user:pass@{self.host}:{self.port}/{self.value['database']}"</code></pre>
</div>
""", unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/19_Clase_DataClasses.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/21_Clase_ProyectoSistemaUsuarios.py")
