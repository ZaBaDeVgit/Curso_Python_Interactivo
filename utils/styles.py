import streamlit as st

def apply_custom_styles():
    """Aplica estilos personalizados y oculta el menú automático de Streamlit"""
    st.markdown("""
    <style>
        /* === OCULTAR MENÚ AUTOMÁTICO DE STREAMLIT === */
        [data-testid="stSidebarNav"] {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            position: absolute !important;
        }

        /* Ocultar el contenedor del menú automático */
        section[data-testid="stSidebar"] > div:first-child > div:first-child {
            display: none !important;
        }

        /* Para versiones más recientes de Streamlit */
        section[data-testid="stSidebar"] ul {
            display: none !important;
        }

        /* Clases adicionales que puede usar Streamlit */
        .st-emotion-cache-1gwvy71,
        .st-emotion-cache-pkbazv {
            display: none !important;
        }

        /* === MANTENER VISIBLE EL SIDEBAR PERSONALIZADO === */
        section[data-testid="stSidebar"] {
            display: block !important;
            visibility: visible !important;
            transition: all 0.3s ease !important;
        }

        /* Asegurar que los expanders se vean */
        .st-expander,
        [data-testid="stExpander"] {
            display: block !important;
            visibility: visible !important;
        }

        /* === ESTILOS PERSONALIZADOS === */
        .main-header {
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }

        .class-card {
            padding: 2rem;
            border-radius: 10px;
            border-left: 5px solid #667eea;
            margin: 1rem 0;
            transition: transform 0.3s;
            background-color: rgba(102, 126, 234, 0.1);
        }

        .class-card:hover {
            transform: translateX(10px);
            background-color: rgba(102, 126, 234, 0.2);
        }

        .class-card h3 {
            margin-top: 0;
            color: #667eea;
        }

        /* Mejorar contraste en modo oscuro */
        .stButton button {
            background-color: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            transition: all 0.3s;
        }

        .stButton button:hover {
            background-color: #764ba2;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(102, 126, 234, 0.3);
        }

        /* === ESTILOS PARA BOTÓN TOGGLE === */
        .toggle-container {
            background: #667eea;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.75rem 1rem;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
            font-weight: 600;
            transition: all 0.3s ease;
            margin-bottom: 1.5rem;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }

        .toggle-container:hover {
            background: #764ba2;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(102, 126, 234, 0.4);
        }

        .toggle-container:active {
            transform: translateY(0px);
        }

        /* === ESTILOS PARA BOTÓN TOGGLE EXTERNO === */
        .sidebar-toggle-external {
            position: fixed;
            top: 20px;
            left: 20px;
            z-index: 99999;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.75rem 1rem;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
            min-width: 180px;
        }

        .sidebar-toggle-external:hover {
            background: #764ba2;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }

        .sidebar-toggle-external:active {
            transform: translateY(0px);
        }

        /* Ocultar botón en modo móvil */
        @media (max-width: 768px) {
            .sidebar-toggle-external {
                display: none;
            }
        }

        /* Estilos para el sidebar colapsado */
        .sidebar-hidden {
            margin-left: -350px !important;
            opacity: 0.1 !important;
            pointer-events: none !important;
        }

        .sidebar-visible {
            margin-left: 0px !important;
            opacity: 1 !important;
            pointer-events: auto !important;
        }
    </style>
    """, unsafe_allow_html=True)


def create_sidebar_toggle():
    """Crea el botón externo para toggle del sidebar - POSICIÓN AJUSTADA"""
    st.markdown("""
    <div style="position: fixed; top: 60px; left: 20px; z-index: 99999;">
        <button onclick="toggleSidebar()" style="
            background: #667eea;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.75rem 1rem;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
            min-width: 180px;
            display: block !important;
            visibility: visible !important;
        " onmouseover="this.style.background='#764ba2'; this.style.transform='translateY(-2px)'"
           onmouseout="this.style.background='#667eea'; this.style.transform='translateY(0px)'"
           title="Ocultar/Mostrar Menú">
            ☰ Menú
        </button>
    </div>

    <script>
    // Función para toggle del sidebar
    function toggleSidebar() {
        console.log('Toggle clicked');
        const sidebar = document.querySelector('section[data-testid="stSidebar"]');
        if (sidebar) {
            console.log('Sidebar encontrado:', sidebar);
            if (sidebar.style.marginLeft === '-350px' || sidebar.style.marginLeft === '') {
                sidebar.style.marginLeft = '-350px';
                sidebar.style.opacity = '0.1';
                localStorage.setItem('sidebar-state', 'collapsed');
                console.log('Sidebar colapsado');
            } else {
                sidebar.style.marginLeft = '0px';
                sidebar.style.opacity = '1';
                localStorage.setItem('sidebar-state', 'expanded');
                console.log('Sidebar expandido');
            }
        } else {
            console.error('Sidebar no encontrado');
        }
    }

    // Inicializar estado guardado y asegurar que el botón esté visible
    function initToggle() {
        console.log('Inicializando toggle');
        const savedState = localStorage.getItem('sidebar-state');
        const sidebar = document.querySelector('section[data-testid="stSidebar"]');
        const button = document.querySelector('button[onclick="toggleSidebar()"]');

        console.log('Estado guardado:', savedState);
        console.log('Sidebar:', !!sidebar);
        console.log('Botón:', !!button);

        if (sidebar && savedState === 'collapsed') {
            sidebar.style.marginLeft = '-350px';
            sidebar.style.opacity = '0.1';
            console.log('Sidebar inicializado como colapsado');
        }

        // Asegurar que el botón sea visible
        if (button) {
            button.style.display = 'block';
            button.style.visibility = 'visible';
            console.log('Botón hecho visible');
        }
    }

    // Múltiples intentos para asegurar que funcione
    initToggle();
    setTimeout(initToggle, 100);
    setTimeout(initToggle, 500);
    setTimeout(initToggle, 1000);
    setTimeout(initToggle, 2000);

    // También cuando el DOM cambia
    if (window.MutationObserver) {
        const observer = new MutationObserver(function(mutations) {
            setTimeout(initToggle, 100);
        });
        observer.observe(document.body, {childList: true, subtree: true});
    }
    </script>
    """, unsafe_allow_html=True)


def create_sidebar_menu():
    """Crea el menú lateral personalizado con todos los módulos y clases"""
    with st.sidebar:
        st.title("📚 Bienvenid@s al Curso")
        st.markdown("---")

        # Menú desplegable para módulos
        with st.expander("🎯 Módulo 1: Fundamentos POO", expanded=True):
            st.page_link("streamlit_app.py", label="🏠 Inicio del Curso")
            st.page_link("pages/01_Introduccion.py", label="01. Introducción")
            st.page_link("pages/02_Clase_Classes.py", label="02. Clase 1: Classes")
            st.page_link("pages/03_Clase_Metodos.py", label="03. Clase 2: Métodos")
            st.page_link("pages/04_Clase_Herencia.py", label="04. Clase 3: Herencia")
            st.page_link("pages/05_Clase_Polimorfismo.py", label="05. Clase 4: Polimorfismo")
            st.page_link("pages/06_Clase_Encapsulamiento.py", label="06. Clase 5: Encapsulamiento")
            st.page_link("pages/07_Clase_MetodosEspeciales.py", label="07. Clase 6: Métodos Especiales")
            st.page_link("pages/08_Clase_Propiedades.py", label="08. Clase 7: Propiedades")
            st.page_link("pages/09_Clase_MetodosClase.py", label="09. Clase 8: Métodos de Clase")
            st.page_link("pages/10_Clase_Composicion.py", label="10. Clase 9: Composición")
            st.page_link("pages/11_Clase_MiniCalc.py", label="11. Clase 10: Proyecto MiniCalc")

        with st.expander("🚀 Módulo 2: POO Avanzado", expanded=True):
            st.page_link("pages/12_Clase_HerenciaMultiple.py", label="12. Clase 11: Herencia Múltiple")
            st.page_link("pages/13_Clase_Abstractas.py", label="13. Clase 12: Clases Abstractas")
            st.page_link("pages/14_Clase_Interfaces.py", label="14. Clase 13: Interfaces y Protocolos")
            st.page_link("pages/15_Clase_DuckTyping.py", label="15. Clase 14: Duck Typing Profundo")
            st.page_link("pages/16_Clase_SobrecargaOperadores.py", label="16. Clase 15: Sobrecarga de Operadores")
            st.page_link("pages/17_Clase_IteradoresGeneradores.py", label="17. Clase 16: Iteradores y Generadores")
            st.page_link("pages/18_Clase_ContextManagers.py", label="18. Clase 17: Context Managers")
            st.page_link("pages/19_Clase_DataClasses.py", label="19. Clase 18: Data Classes")
            st.page_link("pages/20_Clase_Enums.py", label="20. Clase 19: Enums")
            st.page_link("pages/21_Clase_ProyectoSistemaUsuarios.py", label="21. Clase 20: Proyecto Sistema Usuarios")

        with st.expander("🏗️ Módulo 3: Patrones de Diseño", expanded=False):
            st.write("🔄 Próximamente...")
            st.write("• Singleton")
            st.write("• Factory Method")
            st.write("• Observer")
            st.write("• Strategy")
            st.write("• Decorator")
            st.write("• Adapter")
            st.write("• Command")
            st.write("• State")
            st.write("• Template Method")
            st.write("• Proyecto: Gestor de Tareas")

        with st.expander("🌐 Módulo 4: POO en el Mundo Real", expanded=False):
            st.write("🔄 Próximamente...")
            st.write("• APIs REST con POO")
            st.write("• Bases de Datos ORM")
            st.write("• Testing con POO")
            st.write("• Logging y Monitoreo")
            st.write("• Configuración y Settings")
            st.write("• Validación de Datos")
            st.write("• Serialización")
            st.write("• Caching")
            st.write("• Proyecto: Microservicios")

        with st.expander("⚡ Módulo 5: POO Moderna", expanded=False):
            st.write("🔄 Próximamente...")
            st.write("• Type Hints Avanzados")
            st.write("• Async/Await con POO")
            st.write("• Metaprogramación")
            st.write("• Descriptores")
            st.write("• Mixins y Traits")
            st.write("• Inyección de Dependencias")
            st.write("• Domain-Driven Design")
            st.write("• Clean Architecture")
            st.write("• Proyecto: Framework Web")

        st.markdown("---")
        st.caption("💡 Usa el botón ☰ Menú para ocultar/mostrar este menú")