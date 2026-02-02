import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu, create_sidebar_toggle

st.set_page_config(
    page_title="Clase 20 - Proyecto Sistema Usuarios",
    page_icon="👥",
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

st.title("👥 Clase 20: Proyecto Sistema de Usuarios")

# Crear menú lateral personalizado
create_sidebar_menu()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del Día")
    st.markdown("""
    <div class="explicacion">
    <h3>Integra todos los conceptos del Módulo 2</h3>
    <p>Crea un sistema completo con:</p>
    <ul>
        <li><b>Herencia Múltiple</b>: UsuarioBase + Notificaciones</li>
        <li><b>Clases Abstractas</b>: Autenticable, Permisos</li>
        <li><b>Protocolos</b>: Almacenamiento, Validador</li>
        <li><b>Duck Typing</b>: ProcesadorUniversal</li>
        <li><b>Sobrecarga</b>: Usuario + Usuario = Grupo</li>
        <li><b>Iteradores</b>: IteradorUsuarios</li>
        <li><b>Context Managers</b>: SesionUsuario</li>
        <li><b>Data Classes</b>: Perfil, Configuracion</li>
        <li><b>Enums</b>: RolUsuario, EstadoSesion</li>
    </ul>
    <p><i>¡Este es el proyecto final del Módulo 2!</i></p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🆘 Ver Solución"):
        st.code("""
# Sistema Completo de Usuarios - Integración Módulo 2

from abc import ABC, abstractmethod
from typing import Protocol, Dict, List, Any, Optional, Iterator
from dataclasses import dataclass, field
from enum import Enum, IntEnum, unique, auto
from contextlib import contextmanager
import json
import hashlib
import time
from datetime import datetime, timedelta

# ===== ENUMS =====
@unique
class RolUsuario(IntEnum):
    VISITANTE = 1
    USUARIO = 2
    MODERADOR = 3
    ADMINISTRADOR = 4

    @property
    def permisos(self) -> List[str]:
        permisos_map = {
            RolUsuario.VISITANTE: ["leer"],
            RolUsuario.USUARIO: ["leer", "escribir"],
            RolUsuario.MODERADOR: ["leer", "escribir", "moderar"],
            RolUsuario.ADMINISTRADOR: ["leer", "escribir", "moderar", "administrar"]
        }
        return permisos_map[self]

@unique
class EstadoSesion(Enum):
    ACTIVA = "activa"
    INACTIVA = "inactiva"
    EXPIRADA = "expirada"
    CERRADA = "cerrada"

    @property
    def es_valida(self) -> bool:
        return self in [EstadoSesion.ACTIVA, EstadoSesion.INACTIVA]

# ===== DATA CLASSES =====
@dataclass(frozen=True)
class PerfilUsuario:
    nombre: str
    email: str
    bio: str = ""
    avatar_url: str = ""
    fecha_creacion: datetime = field(default_factory=datetime.now)

    @property
    def dominio_email(self) -> str:
        return self.email.split('@')[1] if '@' in self.email else ""

@dataclass
class ConfiguracionUsuario:
    tema: str = "claro"
    idioma: str = "es"
    notificaciones_email: bool = True
    notificaciones_push: bool = True
    sesion_recordar: bool = False
    tiempo_sesion_minutos: int = 30

    def __post_init__(self):
        if self.tiempo_sesion_minutos < 5:
            self.tiempo_sesion_minutos = 5

# ===== PROTOCOLOS =====
@runtime_checkable
class Almacenamiento(Protocol):
    def guardar(self, clave: str, datos: Any) -> bool: ...
    def leer(self, clave: str) -> Optional[Any]: ...
    def eliminar(self, clave: str) -> bool: ...
    def existe(self, clave: str) -> bool: ...

@runtime_checkable
class Validador(Protocol):
    def validar(self, datos: Any) -> bool: ...
    def mensaje_error(self) -> str: ...

# ===== CLASES ABSTRACTAS =====
class Autenticable(ABC):
    @abstractmethod
    def autenticar(self, credenciales: Dict[str, str]) -> bool:
        pass

    @abstractmethod
    def cambiar_password(self, password_actual: str, password_nuevo: str) -> bool:
        pass

class Permisos(ABC):
    @abstractmethod
    def tiene_permiso(self, permiso: str) -> bool:
        pass

    @abstractmethod
    def agregar_permiso(self, permiso: str) -> None:
        pass

# ===== CLASES BASE =====
class UsuarioBase:
    def __init__(self, id: int, perfil: PerfilUsuario, rol: RolUsuario):
        self.id = id
        self.perfil = perfil
        self.rol = rol
        self._configuracion = ConfiguracionUsuario()
        self._fecha_ultimo_acceso = datetime.now()

    @property
    def nombre_completo(self) -> str:
        return self.perfil.nombre

    @property
    def es_activo(self) -> bool:
        return (datetime.now() - self._fecha_ultimo_acesso).days < 30

    def actualizar_ultimo_acceso(self):
        self._fecha_ultimo_acceso = datetime.now()

    def __str__(self) -> str:
        return f"#{self.id} {self.perfil.nombre} ({self.rol.name})"

# ===== HERENCIA MÚLTIPLE =====
class Notificaciones:
    def __init__(self):
        self._notificaciones_pendientes: List[str] = []

    def agregar_notificacion(self, mensaje: str):
        self._notificaciones_pendientes.append(mensaje)

    def obtener_notificaciones(self) -> List[str]:
        notificaciones = self._notificaciones_pendientes.copy()
        self._notificaciones_pendientes.clear()
        return notificaciones

    def tiene_notificaciones(self) -> bool:
        return len(self._notificaciones_pendientes) > 0

class Usuario(UsuarioBase, Autenticable, Permisos, Notificaciones):
    def __init__(self, id: int, perfil: PerfilUsuario, rol: RolUsuario, password: str):
        super().__init__(id, perfil, rol)
        Notificaciones.__init__(self)
        self._password_hash = self._hash_password(password)
        self._sesiones: Dict[str, Dict] = {}

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def autenticar(self, credenciales: Dict[str, str]) -> bool:
        password = credenciales.get("password", "")
        password_hash = self._hash_password(password)

        if password_hash == self._password_hash:
            self.actualizar_ultimo_acceso()
            self.agregar_notificacion("Sesión iniciada exitosamente")
            return True
        return False

    def cambiar_password(self, password_actual: str, password_nuevo: str) -> bool:
        if self.autenticar({"password": password_actual}):
            self._password_hash = self._hash_password(password_nuevo)
            self.agregar_notificacion("Contraseña cambiada exitosamente")
            return True
        return False

    def tiene_permiso(self, permiso: str) -> bool:
        return permiso in self.rol.permisos

    def agregar_permiso(self, permiso: str) -> None:
        # Los permisos están definidos por el rol, no se pueden agregar individualmente
        pass

    # SOBRECARGA DE OPERADORES
    def __add__(self, otro: 'Usuario') -> 'GrupoUsuarios':
        return GrupoUsuarios([self, otro])

    def __eq__(self, otro: object) -> bool:
        if isinstance(otro, Usuario):
            return self.id == otro.id
        return False

    def __hash__(self) -> int:
        return hash(self.id)

    @property
    def configuracion(self) -> ConfiguracionUsuario:
        return self._configuracion

    def actualizar_configuracion(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self._configuracion, key):
                setattr(self._configuracion, key, value)

# ===== ITERADORES =====
class IteradorUsuarios:
    def __init__(self, usuarios: List[Usuario]):
        self._usuarios = usuarios
        self._indice = 0

    def __iter__(self) -> Iterator[Usuario]:
        self._indice = 0
        return self

    def __next__(self) -> Usuario:
        if self._indice >= len(self._usuarios):
            raise StopIteration
        usuario = self._usuarios[self._indice]
        self._indice += 1
        return usuario

    def __len__(self) -> int:
        return len(self._usuarios)

class GrupoUsuarios:
    def __init__(self, usuarios: List[Usuario]):
        self.usuarios = usuarios
        self._iterador = IteradorUsuarios(usuarios)

    def __iter__(self) -> Iterator[Usuario]:
        return self._iterador

    def __len__(self) -> int:
        return len(self.usuarios)

    def __add__(self, otro: 'GrupoUsuarios') -> 'GrupoUsuarios':
        return GrupoUsuarios(self.usuarios + otro.usuarios)

    def __str__(self) -> str:
        return f"Grupo({len(self.usuarios)} usuarios)"

# ===== CONTEXT MANAGER =====
@contextmanager
def SesionUsuario(usuario: Usuario, almacenamiento: Almacenamiento):
    \"\"\"Context manager para manejar sesión de usuario\"\"\"
    token = f"token_{usuario.id}_{int(time.time())}"
    datos_sesion = {
        "usuario_id": usuario.id,
        "token": token,
        "estado": EstadoSesion.ACTIVA.value,
        "inicio": datetime.now().isoformat()
    }

    # Guardar sesión
    almacenamiento.guardar(f"sesion_{token}", datos_sesion)
    usuario.agregar_notificacion("Sesión iniciada")

    try:
        yield datos_sesion
    except Exception as e:
        # Manejar error en sesión
        datos_sesion["estado"] = EstadoSesion.CERRADA.value
        datos_sesion["error"] = str(e)
        usuario.agregar_notificacion(f"Error en sesión: {e}")
        raise
    finally:
        # Cerrar sesión
        datos_sesion["estado"] = EstadoSesion.CERRADA.value
        datos_sesion["fin"] = datetime.now().isoformat()
        almacenamiento.guardar(f"sesion_{token}", datos_sesion)
        usuario.agregar_notificacion("Sesión cerrada")

# ===== DUCK TYPING =====
class ProcesadorUniversal:
    def procesar(self, objeto: Any) -> Dict[str, Any]:
        resultado = {"tipo": type(objeto).__name__, "procesado": False}

        # Duck typing: procesar según capacidades del objeto
        if hasattr(objeto, 'procesar_datos'):
            resultado.update(objeto.procesar_datos())
            resultado["procesado"] = True
        elif hasattr(objeto, 'id') and hasattr(objeto, 'perfil'):
            # Es un usuario
            resultado.update({
                "id": objeto.id,
                "nombre": objeto.perfil.nombre,
                "rol": objeto.rol.name,
                "email": objeto.perfil.email
            })
            resultado["procesado"] = True
        elif hasattr(objeto, '__iter__') and not isinstance(objeto, str):
            # Es iterable
            resultado["elementos"] = len(objeto)
            resultado["procesado"] = True

        return resultado

# ===== IMPLEMENTACIONES DE PROTOCOLOS =====
class AlmacenamientoMemoria:
    def __init__(self):
        self._datos: Dict[str, Any] = {}

    def guardar(self, clave: str, datos: Any) -> bool:
        self._datos[clave] = datos
        return True

    def leer(self, clave: str) -> Optional[Any]:
        return self._datos.get(clave)

    def eliminar(self, clave: str) -> bool:
        return self._datos.pop(clave, None) is not None

    def existe(self, clave: str) -> bool:
        return clave in self._datos

class ValidadorEmail:
    def __init__(self):
        self._error = ""

    def validar(self, datos: Any) -> bool:
        if isinstance(datos, str):
            if "@" in datos and "." in datos.split("@")[1]:
                return True
            self._error = "Email inválido: formato incorrecto"
        else:
            self._error = "Email debe ser un string"
        return False

    def mensaje_error(self) -> str:
        return self._error

# ===== SISTEMA COMPLETO =====
class SistemaUsuarios:
    def __init__(self, almacenamiento: Almacenamiento):
        self._almacenamiento = almacenamiento
        self._usuarios: Dict[int, Usuario] = {}
        self._procesador = ProcesadorUniversal()
        self._validador_email = ValidadorEmail()
        self._siguiente_id = 1

    def registrar_usuario(self, nombre: str, email: str, password: str, rol: RolUsuario = RolUsuario.USUARIO) -> Usuario:
        # Validar email
        if not self._validador_email.validar(email):
            raise ValueError(self._validador_email.mensaje_error())

        # Crear perfil
        perfil = PerfilUsuario(nombre=nombre, email=email)

        # Crear usuario
        usuario = Usuario(self._siguiente_id, perfil, rol, password)

        # Guardar usuario
        self._usuarios[usuario.id] = usuario
        self._almacenamiento.guardar(f"usuario_{usuario.id}", usuario)

        self._siguiente_id += 1
        usuario.agregar_notificacion("Usuario registrado exitosamente")

        return usuario

    def obtener_usuario(self, id: int) -> Optional[Usuario]:
        return self._usuarios.get(id)

    def listar_usuarios(self) -> GrupoUsuarios:
        return GrupoUsuarios(list(self._usuarios.values()))

    def procesar_datos_usuario(self, id: int) -> Dict[str, Any]:
        usuario = self.obtener_usuario(id)
        if usuario:
            return self._procesador.procesar(usuario)
        return {"error": "Usuario no encontrado"}

    def iniciar_sesion(self, email: str, password: str) -> Optional[Dict[str, Any]]:
        # Buscar usuario por email
        for usuario in self._usuarios.values():
            if usuario.perfil.email == email:
                if usuario.autenticar({"password": password}):
                    with SesionUsuario(usuario, self._almacenamiento) as sesion:
                        return sesion
                return None
        return None

    def obtener_estadisticas(self) -> Dict[str, Any]:
        total_usuarios = len(self._usuarios)
        usuarios_por_rol = {}

        for usuario in self._usuarios.values():
            rol_nombre = usuario.rol.name
            usuarios_por_rol[rol_nombre] = usuarios_por_rol.get(rol_nombre, 0) + 1

        return {
            "total_usuarios": total_usuarios,
            "usuarios_por_rol": usuarios_por_rol,
            "sesiones_activas": len([k for k in self._almacenamiento._datos.keys() if k.startswith("sesion_")])
        }

# ===== DEMOSTRACIÓN =====
def demostrar_sistema():
    print("🚀 INICIANDO SISTEMA DE USUARIOS COMPLETO")
    print("=" * 60)

    # Crear sistema
    almacenamiento = AlmacenamientoMemoria()
    sistema = SistemaUsuarios(almacenamiento)

    # Registrar usuarios
    print("\\n📝 Registrando usuarios...")
    ana = sistema.registrar_usuario("Ana García", "ana@email.com", "password123", RolUsuario.ADMINISTRADOR)
    juan = sistema.registrar_usuario("Juan Pérez", "juan@email.com", "pass456", RolUsuario.USUARIO)
    maria = sistema.registrar_usuario("María López", "maria@email.com", "abc789", RolUsuario.MODERADOR)

    print(f"✅ Usuarios registrados: {ana}, {juan}, {maria}")

    # Probar herencia múltiple y notificaciones
    print("\\n📧 Probando notificaciones...")
    ana.agregar_notificacion("Bienvenida al sistema")
    print(f"Notificaciones de Ana: {ana.obtener_notificaciones()}")

    # Probar sobrecarga de operadores
    print("\\n🔢 Probando sobrecarga de operadores...")
    grupo1 = ana + juan
    grupo2 = maria + ana
    grupo_total = grupo1 + grupo2
    print(f"Grupo 1: {grupo1}")
    print(f"Grupo 2: {grupo2}")
    print(f"Grupo total: {grupo_total}")

    # Probar iteradores
    print("\\n🔄 Probando iteradores...")
    print("Usuarios en el sistema:")
    for usuario in sistema.listar_usuarios():
        print(f"  - {usuario}")

    # Probar duck typing
    print("\\n🦆 Probando duck typing...")
    for usuario_id in [1, 2, 3]:
        datos = sistema.procesar_datos_usuario(usuario_id)
        print(f"Datos procesados usuario {usuario_id}: {datos}")

    # Probar context managers
    print("\\n📁 Probando context managers...")
    sesion = sistema.iniciar_sesion("ana@email.com", "password123")
    if sesion:
        print(f"Sesión iniciada: {sesion['token']}")

    # Probar permisos y roles
    print("\\n🔐 Probando permisos y roles...")
    print(f"Ana puede administrar: {ana.tiene_permiso('administrar')}")
    print(f"Juan puede administrar: {juan.tiene_permiso('administrar')}")
    print(f"María puede moderar: {maria.tiene_permiso('moderar')}")

    # Probar data classes
    print("\\n📊 Probando data classes...")
    config = ana.configuracion
    print(f"Configuración de Ana: {config}")
    ana.actualizar_configuracion(tema="oscuro", notificaciones_push=False)
    print(f"Configuración actualizada: {ana.configuracion}")

    # Probar enums
    print("\\n🏷️ Probando enums...")
    print(f"Roles disponibles: {[rol.name for rol in RolUsuario]}")
    print(f"Nivel de Ana: {ana.rol.value}")
    print(f"Permisos de Ana: {ana.rol.permisos}")

    # Estadísticas finales
    print("\\n📈 Estadísticas del sistema:")
    stats = sistema.obtener_estadisticas()
    for key, value in stats.items():
        print(f"  {key}: {value}")

    print("\\n✅ ¡Sistema demostrado exitosamente!")

# Ejecutar demostración
if __name__ == "__main__":
    demostrar_sistema()
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")

    codigo_default = """# Sistema de Usuarios - Integración Módulo 2
# Importa todas las clases necesarias y crea el sistema completo

from abc import ABC, abstractmethod
from typing import Protocol, Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum, IntEnum, unique
from contextlib import contextmanager
import hashlib
import time
from datetime import datetime

# TODO: Implementar todos los componentes del sistema:
# 1. Enums para roles y estados
# 2. Data classes para perfiles y configuración
# 3. Protocolos para almacenamiento y validación
# 4. Clases abstractas para autenticación y permisos
# 5. Herencia múltiple para Usuario
# 6. Sobrecarga de operadores
# 7. Iteradores para grupos de usuarios
# 8. Context managers para sesiones
# 9. Duck typing para procesamiento universal
# 10. Sistema completo que integre todo

class SistemaUsuarios:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, nombre, email, password):
        # TODO: Implementar registro completo
        pass

    def iniciar_sesion(self, email, password):
        # TODO: Implementar autenticación
        pass

# Prueba básica
sistema = SistemaUsuarios()
print("🚀 Sistema de Usuarios - Módulo 2")
print("Integra todos los conceptos aprendidos")"""

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
st.subheader("📚 Integración de Conceptos del Módulo 2")

col_exp1, col_exp2 = st.columns(2)

with col_exp1:
    st.markdown("""
    <div class="explicacion">
    <h3>🔀 Herencia Múltiple</h3>
    <p>Usuario hereda de:</p>
    <ul>
        <li><b>UsuarioBase</b> - datos básicos</li>
        <li><b>Autenticable</b> - login/password</li>
        <li><b>Permisos</b> - control de acceso</li>
        <li><b>Notificaciones</b> - mensajes</li>
    </ul>

    <h3>🎨 Clases Abstractas</h3>
    <p>Definen contratos:</p>
    <ul>
        <li><b>Autenticable</b> - métodos de login</li>
        <li><b>Permisos</b> - control de acceso</li>
        <li>Forzan implementación</li>
    </ul>

    <h3>🔌 Protocolos</h3>
    <p>Interfaces flexibles:</p>
    <ul>
        <li><b>Almacenamiento</b> - guardar/leer datos</li>
        <li><b>Validador</b> - validar información</li>
        <li>Permiten múltiples implementaciones</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>🦆 Duck Typing</h3>
    <p>ProcesadorUniversal:</p>
    <ul>
        <li>Procesa cualquier objeto</li>
        <li>Usa hasattr() para detectar capacidades</li>
        <li>Adapta según lo que puede hacer</li>
    </ul>

    <h3>⚡ Sobrecarga de Operadores</h3>
    <p>Operadores personalizados:</p>
    <ul>
        <li><b>usuario + usuario</b> → GrupoUsuarios</li>
        <li><b>grupo + grupo</b> → Grupo combinado</li>
        <li><b>usuario == usuario</b> → comparar IDs</li>
    </ul>

    <h3>🔄 Iteradores</h3>
    <p>IteradorUsuarios:</p>
    <ul>
        <li>Recorre lista de usuarios</li>
        <li>Implementa __iter__ y __next__</li>
        <li>Usable en bucles for</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Resumen del módulo
st.markdown("---")
st.subheader("🎯 Resumen del Módulo 2")

st.markdown("""
<div class="explicacion">
<h3>🏆 ¡Felicidades! Has completado el Módulo 2</h3>
<p>Este proyecto integra todos los conceptos avanzados de POO:</p>

<h4>✅ Conceptos Dominados:</h4>
<ul>
    <li><b>Herencia Múltiple</b> - Combinar funcionalidades de varias clases</li>
    <li><b>Clases Abstractas</b> - Definir contratos y estructuras</li>
    <li><b>Protocolos</b> - Interfaces flexibles y duck typing</li>
    <li><b>Duck Typing Profundo</b> - Procesamiento universal</li>
    <li><b>Sobrecarga de Operadores</b> - Comportamiento natural de objetos</li>
    <li><b>Iteradores y Generadores</b> - Secuencias eficientes</li>
    <li><b>Context Managers</b> - Gestión automática de recursos</li>
    <li><b>Data Classes</b> - Clases para datos simples</li>
    <li><b>Enums</b> - Constantes tipadas y seguras</li>
</ul>

<h4>🚀 Lo que aprendiste:</h4>
<ul>
    <li>Diseñar arquitecturas complejas y escalables</li>
    <li>Usar patrones avanzados de POO</li>
    <li>Integrar múltiples conceptos en un sistema real</li>
    <li>Aplicar las mejores prácticas de Python</li>
    <li>Crear código mantenible y extensible</li>
</ul>

<h4>🎯 Siguiente Paso:</h4>
<p>¡Estás listo para el <b>Módulo 3: Patrones de Diseño</b>!</p>
<p>Aprenderás patrones como Singleton, Factory, Observer, y más...</p>
</div>
""", unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/20_Clase_Enums.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("🎉 ¡Módulo 2 Completado!"):
        st.switch_page("streamlit_app.py")
