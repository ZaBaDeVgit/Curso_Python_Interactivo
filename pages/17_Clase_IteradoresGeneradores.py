import streamlit as st
from io import StringIO
import sys
from utils.styles import apply_custom_styles, create_sidebar_menu

st.set_page_config(
    page_title="Clase 16 - Iteradores y Generadores",
    page_icon="🔄",
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

st.title("🔄 Clase 16: Iteradores y Generadores en Clases")

# Crear menú lateral personalizado
create_sidebar_menu()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Reto del día")
    st.markdown("""
    <div class="explicacion">
    <h3>Crea clase Contador Personalizado</h3>
    <p>Crea clase <b>Contador</b> con:</p>
    <ul>
        <li>Atributos: <b>inicio</b>, <b>fin</b>, <b>paso</b></li>
        <li><b>__iter__</b> que retorne self</li>
        <li><b>__next__</b> que retorne siguiente número</li>
        <li>Método <b>generar_pares()</b> con yield</li>
        <li>Método <b>generar_primos()</b> con yield</li>
        <li>Use StopIteration cuando termine</li>
    </ul>
    <p><i>Pista: for num in Contador(1, 10, 2): print(num)</i></p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🆘 Ver Solución"):
        st.code("""
class Contador:
    def __init__(self, inicio, fin, paso=1):
        self.inicio = inicio
        self.fin = fin
        self.paso = paso
        self.actual = inicio

    def __iter__(self):
        self.actual = self.inicio
        return self

    def __next__(self):
        if self.actual > self.fin:
            raise StopIteration
        valor = self.actual
        self.actual += self.paso
        return valor

    def generar_pares(self, limite):
        \"\"\"Generador de números pares\"\"\"
        num = 0
        while num <= limite:
            yield num
            num += 2

    def generar_primos(self, limite):
        \"\"\"Generador de números primos\"\"\"
        def es_primo(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        num = 2
        while num <= limite:
            if es_primo(num):
                yield num
            num += 1

    def __repr__(self):
        return f"Contador({self.inicio}, {self.fin}, {self.paso})"

# Pruebas
print("=== Iterador Contador ===")
contador = Contador(1, 10, 2)
for num in contador:
    print(f"Número: {num}")

print("\\n=== Generador de Pares ===")
pares = Contador(0, 20)
for par in pares.generar_pares(20):
    print(f"Par: {par}")

print("\\n=== Generador de Primos ===")
primos = Contador(0, 30)
for primo in primos.generar_primos(30):
    print(f"Primo: {primo}")

print("\\n=== Usando next() manualmente ===")
contador2 = Contador(5, 15)
iterador = iter(contador2)
print(f"Next 1: {next(iterador)}")
print(f"Next 2: {next(iterador)}")
print(f"Next 3: {next(iterador)}")
        """, language="python")

with col2:
    st.subheader("💻 Editor de Código")

    codigo_default = """class Contador:
    def __init__(self, inicio, fin, paso=1):
        self.inicio = inicio
        self.fin = fin
        self.paso = paso
        self.actual = inicio

    def __iter__(self):
        # Reiniciar el contador y retornar self
        pass

    def __next__(self):
        # Retornar siguiente número o lanzar StopIteration
        pass

    def generar_pares(self, limite):
        \"\"\"Generador de números pares usando yield\"\"\"
        # TODO: Implementar generador de pares
        pass

    def generar_primos(self, limite):
        \"\"\"Generador de números primos usando yield\"\"\"
        # TODO: Implementar generador de primos
        pass

    def __repr__(self):
        return f"Contador({self.inicio}, {self.fin}, {self.paso})"

# Prueba tu código:
print("=== Iterador Contador ===")
contador = Contador(1, 10, 2)
for num in contador:
    print(f"Número: {num}")

print("\\n=== Generador de Pares ===")
pares = Contador(0, 20)
for par in pares.generar_pares(20):
    print(f"Par: {par}")

print("\\n=== Generador de Primos ===")
primos = Contador(0, 30)
for primo in primos.generar_primos(30):
    print(f"Primo: {primo}")"""

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
    <h3>🔄 ¿Qué son Iteradores?</h3>
    <p>Objetos que permiten recorrer elementos secuencialmente:</p>
    <ul>
        <li>Implementan protocolo de iteración</li>
        <li>Tienen <b>__iter__()</b> y <b>__next__()</b></li>
        <li>Se usan en bucles for</li>
        <li>Conservan estado entre llamadas</li>
    </ul>
    <p><b>Protocolo de Iteración:</b></p>
    <ol>
        <li>for llama a <code>iter(objeto)</code></li>
        <li>Python llama a <code>objeto.__iter__()</code></li>
        <li>for llama a <code>next(iterador)</code></li>
        <li>Python llama a <code>iterador.__next__()</code></li>
        <li>Se repite hasta <code>StopIteration</code></li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="explicacion">
    <h3>⚡ ¿Qué son Generadores?</h3>
    <p>Funciones que producen secuencias de valores:</p>
    <ul>
        <li>Usan <b>yield</b> en lugar de <b>return</b></li>
        <li>Guardan estado automáticamente</li>
        <li>Más eficientes que listas grandes</li>
        <li>Se pueden usar una sola vez</li>
    </ul>
    <p><b>Ventajas:</b></p>
    <ul>
        <li><b>Memoria:</b> No guardan todos los valores</li>
        <li><b>Velocidad:</b> Producen valores bajo demanda</li>
        <li><b>Lazy evaluation:</b> Solo cuando se necesitan</li>
    </ul>
    <p><b>Ejemplo simple:</b></p>
    <pre><code>def contar_hasta(n):
    for i in range(n):
        yield i

for num in contar_hasta(5):
    print(num)  # 0, 1, 2, 3, 4</code></pre>
    </div>
    """, unsafe_allow_html=True)

# Ejemplos adicionales
st.markdown("---")
st.subheader("💡 Ejemplos Prácticos")

col_ej1, col_ej2 = st.columns(2)

with col_ej1:
    st.markdown("""
    <div class="explicacion">
    <h3>📚 Ejemplo: Librería</h3>
    <p>Iterador para recorrer libros:</p>
    <pre><code>class Libreria:
    def __init__(self, libros):
        self.libros = libros
        self.indice = 0

    def __iter__(self):
        self.indice = 0
        return self

    def __next__(self):
        if self.indice >= len(self.libros):
            raise StopIteration
        libro = self.libros[self.indice]
        self.indice += 1
        return libro

    def libros_por_genero(self, genero):
        for libro in self.libros:
            if libro.genero == genero:
                yield libro

# Uso
libreria = Libreria([libro1, libro2, libro3])
for libro in libreria:
    print(libro.titulo)</code></pre>
    </div>
    """, unsafe_allow_html=True)

with col_ej2:
    st.markdown("""
    <div class="explicacion">
    <h3>📊 Ejemplo: Sensor de Datos</h3>
    <p>Generador para leer datos de sensor:</p>
    <pre><code>class SensorDatos:
    def __init__(self, datos):
        self.datos = datos

    def __iter__(self):
        return self.leer_datos()

    def leer_datos(self):
        for dato in self.datos:
            if self.es_valido(dato):
                yield self.procesar(dato)

    def es_valido(self, dato):
        return dato is not None and dato > 0

    def procesar(self, dato):
        return dato * 2  # Procesamiento simple

# Uso
sensor = SensorDatos([1, 2, None, 3, 0, 4])
for valor in sensor:
    print(f"Valor procesado: {valor}")</code></pre>
    </div>
    """, unsafe_allow_html=True)

# Patrones avanzados
st.markdown("---")
st.subheader("🚀 Patrones Avanzados")

st.markdown("""
<div class="explicacion">
<h3>🎯 Generadores vs Iteradores</h3>
<p><b>¿Cuándo usar cada uno?</b></p>
<ul>
    <li><b>Iterador:</b> Cuando necesitas control total sobre el estado</li>
    <li><b>Generador:</b> Cuando solo necesitas producir valores</li>
    <li><b>Iterador:</b> Para objetos complejos con múltiples métodos</li>
    <li><b>Generador:</b> Para secuencias simples de valores</li>
</ul>

<h3>🔧 Combinando Iteradores</h3>
<p>Puedes encadenar y combinar iteradores:</p>
<pre><code>class CadenaIteradores:
    def __init__(self, *iteradores):
        self.iteradores = iteradores
        self.actual = 0

    def __iter__(self):
        self.actual = 0
        return self

    def __next__(self):
        while self.actual < len(self.iteradores):
            try:
                return next(self.iteradores[self.actual])
            except StopIteration:
                self.actual += 1
        raise StopIteration

# Uso
numeros = iter([1, 2, 3])
letras = iter(['a', 'b', 'c'])
combinado = CadenaIteradores(numeros, letras)
for item in combinado:
    print(item)  # 1, 2, 3, a, b, c</code></pre>

<h3>⚡ Generadores Infinitos</h3>
<p>Generadores que nunca terminan:</p>
<pre><code>class FibonacciInfinito:
    def __iter__(self):
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

# Uso con cuidado
fib = FibonacciInfinito()
for i, num in enumerate(fib):
    if i > 10:  # Limitar para bucle infinito
        break
    print(num)</code></pre>
</div>
""", unsafe_allow_html=True)

# Navegación
st.markdown("---")
col_prev, col_home, col_next = st.columns(3)

with col_prev:
    if st.button("⬅️ Anterior"):
        st.switch_page("pages/16_Clase_SobrecargaOperadores.py")

with col_home:
    if st.button("🏠 Home"):
        st.switch_page("streamlit_app.py")

with col_next:
    if st.button("➡️ Siguiente"):
        st.switch_page("pages/18_Clase_ContextManagers.py")
