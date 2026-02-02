import streamlit as st
import streamlit.components.v1 as components

def apply_custom_styles():
    """Aplica estilos personalizados y modifica el menú automático de Streamlit"""
    st.markdown("""
    <style>
        /* === MODIFICAR MENÚ AUTOMÁTICO DE STREAMLIT === */
        /* Mostrar solo las flechas del toggle, ocultar todo lo demás */
        [data-testid="stSidebarNav"] {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            position: absolute !important;
        }

        /* Ocultar el contenedor principal del menú automático */
        section[data-testid="stSidebar"] > div:first-child > div:first-child {
            display: none !important;
        }

        /* Ocultar todos los enlaces y contenido del menú automático */
        section[data-testid="stSidebar"] ul,
        section[data-testid="stSidebar"] li,
        section[data-testid="stSidebar"] a,
        section[data-testid="stSidebar"] .st-emotion-cache-1gwvy71,
        section[data-testid="stSidebar"] .st-emotion-cache-pkbazv {
            display: none !important;
            visibility: hidden !important;
        }

        /* PERO MANTENER VISIBLE EL BOTÓN TOGGLE DE STREAMLIT */
        /* El botón de toggle del sidebar (flecha) */
        button[kind="header"],
        button[data-testid="baseButton-header"],
        .st-emotion-cache-1r6slb0,
        button[aria-label="View sidebar"] {
            display: block !important;
            visibility: visible !important;
            position: fixed !important;
            top: 10px !important;
            left: 10px !important;
            z-index: 99999 !important;
            background: #667eea !important;
            color: white !important;
            border: 2px solid white !important;
            border-radius: 8px !important;
            padding: 8px 12px !important;
            font-size: 18px !important;
            font-weight: bold !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3) !important;
            transition: all 0.3s ease !important;
        }

        button[kind="header"]:hover,
        button[data-testid="baseButton-header"]:hover,
        .st-emotion-cache-1r6slb0:hover,
        button[aria-label="View sidebar"]:hover {
            background: #764ba2 !important;
            transform: scale(1.1) !important;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.5) !important;
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
    </style>
    """, unsafe_allow_html=True)


def create_sidebar_toggle():
    """Crea el botón externo para toggle del sidebar usando components.html"""
    components.html(
        """
        <style>
            .toggle-btn-external {
                position: fixed;
                top: 70px;
                left: 20px;
                z-index: 999999;
                background: #667eea;
                color: white;
                border: 2px solid white;
                border-radius: 8px;
                padding: 12px 20px;
                cursor: pointer;
                font-size: 16px;
                font-weight: 700;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
                transition: all 0.3s ease;
                display: block;
                font-family: 'Source Sans Pro', sans-serif;
            }

            .toggle-btn-external:hover {
                background: #764ba2;
                transform: scale(1.05);
                box-shadow: 0 6px 16px rgba(102, 126, 234, 0.5);
            }

            .toggle-btn-external:active {
                transform: scale(0.98);
            }
        </style>

        <button id="toggleSidebarBtn" class="toggle-btn-external">
            <span id="toggleIcon">☰</span> Menú
        </button>

        <script>
            (function() {
                let sidebarCollapsed = false;

                function toggleSidebar() {
                    console.log('🔘 Toggle clicked');

                    // Buscar el sidebar en el documento padre (Streamlit)
                    const sidebar = window.parent.document.querySelector('section[data-testid="stSidebar"]');
                    const icon = document.getElementById('toggleIcon');

                    if (!sidebar) {
                        console.error('❌ Sidebar no encontrado');
                        return;
                    }

                    sidebarCollapsed = !sidebarCollapsed;
                    console.log('📊 Nuevo estado:', sidebarCollapsed ? 'COLAPSADO' : 'EXPANDIDO');

                    if (sidebarCollapsed) {
                        // Colapsar
                        sidebar.style.marginLeft = '-350px';
                        sidebar.style.opacity = '0.2';
                        sidebar.style.pointerEvents = 'none';
                        if (icon) icon.textContent = '→';
                        localStorage.setItem('sidebar-state', 'collapsed');
                    } else {
                        // Expandir
                        sidebar.style.marginLeft = '0px';
                        sidebar.style.opacity = '1';
                        sidebar.style.pointerEvents = 'auto';
                        if (icon) icon.textContent = '☰';
                        localStorage.setItem('sidebar-state', 'expanded');
                    }
                }

                function initSidebarToggle() {
                    console.log('🚀 Inicializando toggle del sidebar');

                    const savedState = localStorage.getItem('sidebar-state');
                    const sidebar = window.parent.document.querySelector('section[data-testid="stSidebar"]');
                    const icon = document.getElementById('toggleIcon');

                    console.log('💾 Estado guardado:', savedState);

                    // Restaurar estado guardado
                    if (sidebar && savedState === 'collapsed') {
                        sidebarCollapsed = true;
                        sidebar.style.marginLeft = '-350px';
                        sidebar.style.opacity = '0.2';
                        sidebar.style.pointerEvents = 'none';
                        if (icon) icon.textContent = '→';
                        console.log('📦 Sidebar restaurado como colapsado');
                    } else {
                        sidebarCollapsed = false;
                        if (icon) icon.textContent = '☰';
                        console.log('📂 Sidebar restaurado como expandido');
                    }
                }

                // Asignar evento al botón
                const btn = document.getElementById('toggleSidebarBtn');
                if (btn) {
                    btn.addEventListener('click', toggleSidebar);
                    console.log('✅ Evento click asignado al botón');
                }

                // Inicializar
                setTimeout(initSidebarToggle, 100);
                setTimeout(initSidebarToggle, 500);
                setTimeout(initSidebarToggle, 1000);

                // Observer para cuando el DOM del padre cambie
                if (window.MutationObserver) {
                    const observer = new MutationObserver(() => {
                        setTimeout(initSidebarToggle, 100);
                    });
                    observer.observe(window.parent.document.body, {childList: true, subtree: true});
                    console.log('👁️ Observer activado');
                }
            })();
        </script>
        """,
        height=0,  # Altura 0 para que no ocupe espacio
    )


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
        st.caption("💡 Usa la flecha ☰ en la esquina superior izquierda para ocultar/mostrar este menú")