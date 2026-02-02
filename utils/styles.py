import streamlit as st

def apply_custom_styles():
    """Aplica estilos personalizados y muestra solo la flecha del menú de Streamlit"""
    st.markdown("""
    <style>
        /* === OCULTAR SOLO EL CONTENIDO DEL MENÚ AUTOMÁTICO === */
        /* Ocultar navegación automática pero mantener el toggle */
        [data-testid="stSidebarNav"] {
            display: none !important;
        }

        /* === MANTENER TODO LO DEMÁS VISIBLE === */
        /* Sidebar personalizado completamente visible */
        section[data-testid="stSidebar"] {
            display: block !important;
            visibility: visible !important;
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

        /* === ESTILOS PARA NAVEGACIÓN INFERIOR CENTRADA === */
        .navigation-container {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            gap: 1rem !important;
            margin: 2rem 0 !important;
            padding: 1.5rem !important;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%) !important;
            border-radius: 15px !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
            position: fixed !important;
            bottom: 0 !important;
            left: 50% !important;
            transform: translateX(-50%) !important;
            z-index: 1000 !important;
            width: auto !important;
            max-width: 90vw !important;
        }

        .navigation-container button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            border: 2px solid white !important;
            border-radius: 10px !important;
            padding: 0.75rem 1.5rem !important;
            font-size: 14px !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3) !important;
            min-width: 120px !important;
        }

        .navigation-container button:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0 6px 16px rgba(102, 126, 234, 0.5) !important;
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%) !important;
        }

        .navigation-container button:active {
            transform: translateY(-1px) !important;
        }

        /* Responsive para móvil */
        @media (max-width: 768px) {
            .navigation-container {
                flex-direction: column !important;
                gap: 0.5rem !important;
                padding: 1rem !important;
                width: 85vw !important;
            }

            .navigation-container button {
                width: 100% !important;
                min-width: unset !important;
                padding: 0.6rem 1rem !important;
                font-size: 13px !important;
            }
        }

        /* Responsive para tablet */
        @media (max-width: 1024px) and (min-width: 769px) {
            .navigation-container {
                width: 80vw !important;
                gap: 0.8rem !important;
            }

            .navigation-container button {
                min-width: 100px !important;
                padding: 0.6rem 1.2rem !important;
                font-size: 13px !important;
            }
        }

        /* Espacio para evitar que el contenido se solape con la navegación */
        .main-content {
            padding-bottom: 120px !important;
        }

        @media (max-width: 768px) {
            .main-content {
                padding-bottom: 180px !important;
            }
        }
    </style>
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
        st.caption("💡 Usa la flecha ☰ en la esquina superior izquierda para ocultar/mostrar este menú")


def create_navigation_buttons(prev_page=None, home_page="streamlit_app.py", next_page=None):
    """Crea botones de navegación centrados y responsive"""
    if prev_page or home_page or next_page:
        st.markdown("""
        <div class="navigation-container">
        """, unsafe_allow_html=True)

        # Determinar el número de botones y configurar columnas
        buttons_count = sum([bool(prev_page), bool(home_page), bool(next_page)])

        if buttons_count == 1:
            # Solo un botón - centrado
            cols = st.columns([1, 2, 1])
            col_index = 1  # Columna del centro
        elif buttons_count == 2:
            # Dos botones - distribuidos
            cols = st.columns([1, 1, 1])
            if prev_page and home_page:
                prev_col, home_col = cols[0], cols[1]
            elif prev_page and next_page:
                prev_col, next_col = cols[0], cols[2]
            else:  # home_page and next_page
                home_col, next_col = cols[1], cols[2]
        else:
            # Tres botones - distribuidos
            cols = st.columns([1, 1, 1])
            prev_col, home_col, next_col = cols[0], cols[1], cols[2]

        # Crear los botones según corresponda
        if buttons_count == 1:
            with cols[col_index]:
                if prev_page:
                    if st.button("⬅️ Anterior", key="nav_prev"):
                        st.switch_page(prev_page)
                elif home_page:
                    if st.button("🏠 Home", key="nav_home"):
                        st.switch_page(home_page)
                elif next_page:
                    if st.button("➡️ Siguiente", key="nav_next"):
                        st.switch_page(next_page)
        elif buttons_count == 2:
            if prev_page and home_page:
                with prev_col:
                    if st.button("⬅️ Anterior", key="nav_prev"):
                        st.switch_page(prev_page)
                with home_col:
                    if st.button("🏠 Home", key="nav_home"):
                        st.switch_page(home_page)
            elif prev_page and next_page:
                with prev_col:
                    if st.button("⬅️ Anterior", key="nav_prev"):
                        st.switch_page(prev_page)
                with next_col:
                    if st.button("➡️ Siguiente", key="nav_next"):
                        st.switch_page(next_page)
            else:  # home_page and next_page
                with home_col:
                    if st.button("🏠 Home", key="nav_home"):
                        st.switch_page(home_page)
                with next_col:
                    if st.button("➡️ Siguiente", key="nav_next"):
                        st.switch_page(next_page)
        else:  # buttons_count == 3
            with prev_col:
                if st.button("⬅️ Anterior", key="nav_prev"):
                    st.switch_page(prev_page)
            with home_col:
                if st.button("🏠 Home", key="nav_home"):
                    st.switch_page(home_page)
            with next_col:
                if st.button("➡️ Siguiente", key="nav_next"):
                    st.switch_page(next_page)

        st.markdown("""
        </div>
        <div class="main-content"></div>
        """, unsafe_allow_html=True)
