import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="Modelamiento Molecular",
    page_icon="🧬",
    layout="wide"
)

st.sidebar.image("imagenes_/colegioquimico.png",caption="Modelamiento Molecular y Mecanismo de Reacción")

# =========================================================
# PÁGINA HOME – GENERALIDADES
# =========================================================
def Home():
    #st.image("imagenes_/colegio_quimico_cusco.png")
    st.title("MODELAMIENTO MOLECULAR Y MECANISMO DE REACCIÓN")
    st.subheader("Curso Virtual Teórico–Práctico | Colegio Químico ")
    st.markdown("---")

    st.write("""
    Este curso introduce los fundamentos del **modelamiento molecular**
    aplicados al estudio de **estructuras moleculares, superficies de energía
    potencial y mecanismos de reacción química**, integrando teoría y
    herramientas computacionales.
    """)

    st.markdown("### Objetivo General")
    st.write("""
    Comprender y aplicar técnicas básicas de modelamiento molecular para analizar
    estructuras, estabilidad y mecanismos de reacción química.
    """)

    st.markdown("### Competencias")
    st.markdown("""
    - Interpretar superficies de energía potencial  
    - Analizar mecanismos de reacción desde un enfoque molecular  
    - Utilizar herramientas computacionales para estudiar reacciones químicas  
    - Evaluar críticamente resultados teóricos  
    """)

    st.markdown("---")
    st.markdown("## Temario del Curso")

    temario = {
        "Sesión 1": "Introducción al modelamiento molecular y química computacional",
        "Sesión 2": "Representación molecular y optimización geométrica",
        "Sesión 3": "Energía molecular y superficies de energía potencial",
        "Sesión 4": "Campos de fuerza y métodos de cálculo",
        "Sesión 5": "Introducción a mecanismos de reacción",
        "Sesión 6": "Coordenada de reacción y estados de transición",
        "Sesión 7": "Cálculo y análisis de barreras de energía",
        "Sesión 8": "Mecanismos de reacción orgánica",
        "Sesión 9": "Mecanismos en química inorgánica y de materiales",
        "Sesión 10": "Integración y estudio de casos"
    }

    for s, d in temario.items():
        st.markdown(f"### {s}")
        st.write(d)

    st.markdown("---")
    st.info("Curso organizado por el Colegio de Químicos del Perú – Región Cusco")
    st.write("Docente: **Dr. Jesús Antonio Alvarado Huayhuaz**")

# =========================================================
# SESIÓN 1
# =========================================================
def page2():
    st.header("Sesión 1: Introducción al Modelamiento Molecular", divider="rainbow")
    st.markdown("""
    - ¿Qué es el modelamiento molecular?
    - Niveles de teoría
    """)

    video1 = "https://youtu.be/5iVqq-indVw"
    st.markdown(f'<iframe src="{video1}" width="800" height="450"></iframe>',
                unsafe_allow_html=True)

# =========================================================
# SESIÓN 2
# =========================================================
def page3():
    st.header("Sesión 2: Representación Molecular y Optimización", divider="rainbow")

    st.markdown("""
    - Representación 2D y 3D
    - Coordenadas cartesianas e internas
    - Optimización geométrica
    """)

    st.info("Visualización molecular 3D (PubChem)")
    components.iframe(
        "https://pubchem.ncbi.nlm.nih.gov/compound/2244#section=3D-Conformer",
        width=800,
        height=600
    )

# =========================================================
# SESIÓN 3
# =========================================================
def page4():
    st.header("Sesión 3: Energía Molecular y Superficies de Energía Potencial",
              divider="rainbow")

    st.markdown("""
    - Energía electrónica
    - Mínimos y puntos silla
    - Superficies de energía potencial (SEP)
    """)

    st.image("img/pes_diagram.png", caption="Superficie de Energía Potencial")

# =========================================================
# SESIÓN 4
# =========================================================
def page5():
    st.header("Sesión 4: Campos de Fuerza y Métodos de Cálculo", divider="rainbow")

    st.markdown("""
    **Mecánica Molecular (MM)**
    - AMBER
    - CHARMM

    **Métodos Cuánticos (QM)**
    - Hartree–Fock
    - DFT
    - Métodos semiempíricos
    """)

# =========================================================
# SESIÓN 5
# =========================================================
def page6():
    st.header("Sesión 5: Introducción a Mecanismos de Reacción", divider="rainbow")

    st.markdown("""
    - Concepto de mecanismo
    - Reactivos, productos e intermediarios
    - Energía y reactividad
    """)

# =========================================================
# SESIÓN 6
# =========================================================
def page7():
    st.header("Sesión 6: Coordenada de Reacción y Estados de Transición",
              divider="rainbow")

    st.image("img/reaction_coordinate.png",
             caption="Coordenada de reacción y estado de transición")

# =========================================================
# SESIÓN 7
# =========================================================
def page8():
    st.header("Sesión 7: Barreras de Energía", divider="rainbow")

    st.latex(r"""
    E_a = E_{TS} - E_{Reactivos}
    """)

    st.markdown("""
    - Energía de activación
    - Comparación entre rutas de reacción
    """)

# =========================================================
# SESIÓN 8
# =========================================================
def page9():
    st.header("Sesión 8: Mecanismos de Reacción Orgánica", divider="rainbow")

    st.markdown("""
    - SN1 / SN2
    - E1 / E2
    - Reacciones pericíclicas
    """)

# =========================================================
# SESIÓN 9
# =========================================================
def page10():
    st.header("Sesión 9: Mecanismos en Química Inorgánica y Materiales",
              divider="rainbow")

    st.markdown("""
    - Complejos metálicos
    - Reacciones redox
    - Catálisis
    """)

# =========================================================
# SESIÓN 10
# =========================================================
def page11():
    st.header("Sesión 10: Integración y Estudio de Casos", divider="rainbow")
    st.write("Discusión crítica de mecanismos reales y análisis computacional.")

# =========================================================
# PÁGINAS
# =========================================================
page_names_to_funcs = {
    "Generalidades": Home,
    "Sesión 1: Introducción": page2,
    "Sesión 2: Representación molecular": page3,
    "Sesión 3: Energía molecular y SEP": page4,
    "Sesión 4: Campos de fuerza": page5,
    "Sesión 5: Mecanismos de reacción": page6,
    "Sesión 6: Coordenada de reacción": page7,
    "Sesión 7: Barreras de energía": page8,
    "Sesión 8: Mecanismos orgánicos": page9,
    "Sesión 9: Inorgánica y materiales": page10,
    "Sesión 10: Integración final": page11,
}

selected_page = st.sidebar.selectbox("📚 Temario", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

st.sidebar.markdown("---")
st.sidebar.info("Autor: Dr. Jesús Antonio Alvarado Huayhuaz")
st.sidebar.write("Laboratorio de Investigación en Biopolímeros y Metalofármacos")
st.sidebar.write("Universidad Nacional de Ingeniería")
st.sidebar.write("📧 inefable12@gmail.com")
