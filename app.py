import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import requests

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="Curso Jesus Alvarado",
    page_icon="☢️",
    layout="wide"
)

st.sidebar.image("imagenes_/colegioquimico.png",
                 caption="Modelamiento Molecular y Mecanismo de Reacción", width=200)

# =========================================================
# PÁGINA HOME – GENERALIDADES
# =========================================================
def Home():
    #st.image("imagenes_/colegio_quimico_cusco.png")
    st.header("MODELAMIENTO MOLECULAR Y MECANISMO DE REACCIÓN", divider="rainbow")
    #st.markdown("---")
    st.text("Curso Virtual Teórico–Práctico")

    st.image("imagenes_/molecula2.png", caption = "Mapa de Potencial Electrostático. Fuente: Elaboración propia. Generada con Avogadro y POV-Ray")
             
    st.write("""
    Bienvenidos a la plataforma web del curso, en este espacio se irá compartiendo el contenido de las sesiones semana a semana: 
    slides, tutoriales, código y más.
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

    df_temario = pd.DataFrame({
        "Sesión": ["1","2","3","4","5","6","7","8","9","10"],
        "Tema": [
            "Introducción al modelamiento molecular y química computacional",
            "Representación molecular y optimización geométrica",
            "Energía molecular y superficies de energía potencial",
            "Campos de fuerza y métodos de cálculo",
            "Introducción a mecanismos de reacción",
            "Coordenada de reacción y estados de transición",
            "Cálculo y análisis de barreras de energía",
            "Mecanismos de reacción orgánica",
            "Mecanismos en química inorgánica y de materiales",
            "Integración y estudio de casos"],
        "Fecha": ["9FEB","16FEB","23FEB","2MAR","9MAR","16MAR","23MAR","30MAR","6ABR","13ABR"]
    })
    
    # ------------------ Layout ------------------
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.dataframe(
            df_temario[["Sesión","Tema","Fecha"]],
            hide_index=True,
            use_container_width=True
        )

        st.info("## IMPORTANTE:")

        st.write("""A lo largo del curso iremos sugiriendo la instalación de algunos programas de acceso gratuito, como por ejemplo, 
        Avogadro 1.2, ORCA 6.1, ChemCraft 1.8, PyMOL 3.1.4.1, sin embargo, constantemente se brindarán alternativas para trabajar desde la nube. 
        Así, recalcamos que no hay requerimientos mínimos de hardware para realizar el curso con normalidad.""")
        
        st.write("Las imágenes, videos, artículos y animaciones mostradas a continuación forman parte del contenido de ejercicios que veremos en el curso.")
        st.text("1. Videos resumiendo artículos o tutoriales, utilizando NotebookLM de Google")
        st.video("imagenes_/video2.mp4") 
        
        st.text("2. Literatura de la sesión (Flipped Classroom)")        
        st.pdf("imagenes_/Avogadro_como_herramienta_edu.pdf")
        
        url = "https://www.tiktok.com/@inefable12x/video/7604144200048741650?is_from_webapp=1&sender_device=pc&web_id=7537296124756968965"
        st.markdown("3. Videotutoriales cortos desde [TikTok](%s)" % url)       
        st.video("imagenes_/video3.mp4")
        st.text("4. Flashcards y cuestionarios interactivos con NotebookLM")
        st.image("imagenes_/flashcards1.PNG")       
    with col_right:
        st.write("5. Obtención de Frecuencia imaginaria para hallar el TS. Fuente de la imagen: Visualize Organic Chemistry (New Jersey Institute of Technology). Generado con el programa GaussView")
        st.markdown("![Alt Text](https://visualizeorgchem.com/images/tutorial-PES/SN2-freq.gif)")
        st.write("De Schlegel, HB J. Comput. Chem. 2003 , 24 , 1514-1527.")
        st.image("imagenes_/PES.jpg")
        st.image("imagenes_/tip4p.png") #, use_container_width=True)
        st.write("6. Uso de PyMOL para la visualización de modelos. En el ejemplo, modelos de agua para simulaciones de dinámica molecular: TIP4P (arriba) & TIP5P (abajo). Fuente: Elaboración propia.")
        st.image("imagenes_/tip5p.png") #, use_container_width=True)
        st.write("7. Uso de software especializado gratuito para el personalización de representaciones moleculares. Fuente: Elaboración propia.")
        st.image("imagenes_/WIZARD_3PL1_esquema.png") 
        st.text("8. Código para generación de gráficas. Fuente: https://joaquinbarroso.com/2022/05/18/dft-beyond-academia/")
        st.image("imagenes_/dft.png")

    def obtener_frase():
        try:
            res = requests.get(
                "https://api.quotable.io/random",
                timeout=5,
                verify=False
            )
            data = res.json()
            return f"{data['content']} — {data['author']}"
        except:
            return "La química también necesita paciencia."


    st.markdown("---")
    st.success("Cada vez que visites esta página te llevarás una frase 🙂")
    frase = obtener_frase()
    st.write(frase)

    st.markdown(
        f"""
        <div style='text-align: center; color: #555555;'>
            <small>🧬 Desarrollado por Jesus Alvarado H. </small>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# SESIÓN 1
# =========================================================
def page2():
    st.header("Sesión 1: Introducción al Modelamiento Molecular", divider="rainbow")
    st.markdown("""
    - ¿Qué es el modelamiento molecular?
    - Niveles de teoría
    """)

    st.video("imagenes_/video1.mp4")    

# =========================================================
# SESIÓN 2
# =========================================================
def page3():
    st.header("Sesión 2: Representación Molecular y Optimización", divider="rainbow")

    st.markdown("- Representación 2D y 3D")

    st.video("imagenes_/representaciones.mp4")

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

    st.image("https://ars.els-cdn.com/content/image/1-s2.0-S0019452224001559-gr8.jpg",
            caption = "https://www.sciencedirect.com/science/article/pii/S0019452224001559")

# =========================================================
# SESIÓN 4
# =========================================================
def page5():
    st.header("Sesión 4: Campos de Fuerza y Métodos de Cálculo", divider="rainbow")

    st.markdown("![Alt Text](https://i.makeagif.com/media/7-04-2020/zpBEQV.gif)")
    
    st.markdown("""
    **Mecánica Molecular (MM)**

    **Métodos Cuánticos (QM)**

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
st.sidebar.info("Autor: Dr. Jesus Alvarado H")
st.sidebar.write("Laboratorio de Investigación en Biopolímeros y Metalofármacos")
st.sidebar.write("Universidad Nacional de Ingeniería")
st.sidebar.write("📧 inefable12@gmail.com")
