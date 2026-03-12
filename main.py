import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN DE PÁGINA
# ==========================================
st.set_page_config(page_title="Elkarr AI zketa | Asier Dorronsoro", layout="centered")

# ==========================================
# 2. ESTILOS CSS Y CABECERA (NEÓN / DARK)
# ==========================================
html_estilos_y_cabecera = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@600&display=swap');

/* LIMPIEZA DE STREAMLIT */
#MainMenu, header, footer { visibility: hidden; display: none; }
.block-container { padding: 2rem 1rem 3rem 1rem !important; max-width: 800px !important; }
[data-testid="stAppViewContainer"], [data-testid="stApp"] { background-color: #0a0a0a !important; }

/* CABECERA PRINCIPAL */
.portfolio-wrapper { font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; width: 100%; margin-bottom: 30px;}

.black-block { 
    background-color: #000; 
    border-radius: 24px; 
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); 
    border: 1px solid rgba(255, 255, 255, 0.05); 
    padding: 40px 20px; 
    text-align: center;
}

.neon-title { 
    font-family: 'Quicksand', sans-serif; 
    font-size: clamp(32px, 5vw, 48px); 
    font-weight: 600; 
    color: transparent; 
    -webkit-text-stroke: 1.5px #ffcc66; 
    text-shadow: 0 0 15px rgba(255, 204, 102, 0.3); 
    margin-bottom: 10px; 
}

.subtitle {
    color: #aaaaaa;
    font-size: 16px;
    margin-bottom: 30px;
    line-height: 1.5;
}

/* BOTÓN DE VOLVER (Estilo elegante oscuro) */
.back-btn { 
    display: inline-block;
    background-color: #2b2b2b; 
    border: 1px solid rgba(255, 204, 102, 0.3); 
    border-radius: 10px; 
    padding: 10px 24px; 
    color: #ffffff !important; 
    text-decoration: none;
    font-size: 14px; 
    font-weight: 600; 
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    transition: all 0.3s ease; 
}

.back-btn:hover { 
    background-color: #333333;
    border-color: rgba(255, 204, 102, 0.6); 
    box-shadow: 0 0 12px rgba(255, 204, 102, 0.2);
}

/* =========================================
   SÚPER CORRECCIÓN DE LOS EXPANSORES 
   ========================================= */

/* 1. Fondo del contenedor general */
[data-testid="stExpander"] {
    background-color: #111111 !important;
    border: 1px solid rgba(255, 204, 102, 0.2) !important;
    border-radius: 12px !important;
    margin-bottom: 15px;
    overflow: hidden; 
}

/* 2. MAGIA: Forzamos la cabecera a ser negra SIEMPRE */
[data-testid="stExpander"] summary, 
[data-testid="stExpander"] summary:hover,
[data-testid="stExpander"] summary:focus {
    background-color: #111111 !important;
}

/* 3. Fondo de la parte de abajo cuando se abre */
[data-testid="stExpanderDetails"] {
    background-color: #111111 !important;
}

/* Estilo Neón para el texto */
[data-testid="stExpander"] summary p {
    font-family: 'Quicksand', sans-serif !important;
    font-size: 18px !important;
    font-weight: 600 !important;
    color: transparent !important;
    -webkit-text-stroke: 1px #ffcc66 !important;
    text-shadow: 0 0 10px rgba(255, 204, 102, 0.3) !important;
    transition: text-shadow 0.3s ease;
    margin: 0 !important;
}

[data-testid="stExpander"] summary:hover p {
    text-shadow: 0 0 15px rgba(255, 204, 102, 0.6) !important;
}

/* Flechita dorada y fondo negro para el icono */
[data-testid="stExpander"] summary svg {
    color: #ffcc66 !important;
    background-color: transparent !important;
}

/* EFECTO APAGADO PARA PREGUNTAS 2-6 */
.expander-apagado summary p {
    -webkit-text-stroke: 0.5px rgba(170, 170, 170, 0.4) !important;
    text-shadow: none !important;
    opacity: 0.6;
}

[data-testid="stExpander"] summary svg {
    color: #ffcc66 !important;
}

/* CONTENEDOR YOUTUBE VERTICAL */
.yt-container {
    display: flex; 
    justify-content: center; 
    width: 100%; 
    padding: 10px 0 20px 0;
}

.yt-iframe {
    width: 100%; 
    max-width: 320px; 
    height: 569px; 
    border-radius: 16px; 
    box-shadow: 0 10px 25px rgba(0,0,0,0.5); 
    border: 1px solid rgba(255,255,255,0.1);
}
</style>

<div class="portfolio-wrapper">
    <div class="black-block">
        <div class="neon-title">Elkarr AI zketa 🎙️</div>
        <div class="subtitle">5 preguntas, 5 respuestas.<br>Descubre a Asier Dorronsoro a través de gemelos digitales.</div>
    </div>
</div>
"""
st.markdown(html_estilos_y_cabecera, unsafe_allow_html=True)


# ==========================================
# 3. FUNCIÓN PARA GENERAR EL REPRODUCTOR YOUTUBE
# ==========================================
def reproductor_youtube(video_id):
    return f"""
    <div class="yt-container">
        <iframe class="yt-iframe" 
                src="https://www.youtube.com/embed/{video_id}?rel=0" 
                title="YouTube video player" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen>
        </iframe>
    </div>
    """

# ==========================================
# 4. SECCIÓN DE PREGUNTAS E IDs DE YOUTUBE
# ==========================================

ID_VIDEO_1 = "dmhBFkPBHXc"
ID_VIDEO_2 = ""
ID_VIDEO_3 = ""
ID_VIDEO_4 = ""
ID_VIDEO_5 = ""
ID_VIDEO_6 = ""

# --- PREGUNTA 1 ---
with st.expander("Introducción - Iñaki Lopez Gabilondo & Asier Dorronsoro"):
    st.markdown("<p style='color: #ccc; font-size: 15px; text-align: center; margin-bottom: 20px;'>La inconfundible voz de Iñaki Gabilondo. La inmejorable percha de Iñaki López. Bienvenidos a Elkarr AI zketa. Un experimento digital nacido para sortear barreras y centrarnos, sin rodeos, en conocer a Asier Dorronsoro. En este primer vídeo, conocerás a los protagonistas de esta historia.</p>", unsafe_allow_html=True)
    if ID_VIDEO_1:
        st.markdown(reproductor_youtube(ID_VIDEO_1), unsafe_allow_html=True)
    else:
        st.warning("⚠️ Pon el ID de YouTube en el código para ver el vídeo.")

# --- PREGUNTAS 2 A 6 (APAGADAS) ---
# Usamos un div con la clase 'expander-apagado' para envolverlas
st.markdown('<div class="expander-apagado">', unsafe_allow_html=True)

with st.expander("1. Cuéntame algo sobre ti ¿Cómo es Asier Dorronsoro en lo personal?"):
    if ID_VIDEO_2: st.markdown(reproductor_youtube(ID_VIDEO_2), unsafe_allow_html=True)
    else: st.info("Próximamente... 🚧")

with st.expander("2. Cuéntame algo sobre ti ¿Cómo es Asier Dorronsoro en lo profesional?"):
    if ID_VIDEO_3: st.markdown(reproductor_youtube(ID_VIDEO_3), unsafe_allow_html=True)
    else: st.info("Próximamente... 🚧")

with st.expander("3. El regreso a Euskadi ¿Por qué?"):
    if ID_VIDEO_4: st.markdown(reproductor_youtube(ID_VIDEO_4), unsafe_allow_html=True)
    else: st.info("Próximamente... 🚧")

with st.expander("4. ¿Qué te hace único?"):
    if ID_VIDEO_5: st.markdown(reproductor_youtube(ID_VIDEO_5), unsafe_allow_html=True)
    else: st.info("Próximamente... 🚧")

with st.expander("5. ¿Qué buscas en tu próximo reto profesional en Euskadi?"):
    if ID_VIDEO_6: st.markdown(reproductor_youtube(ID_VIDEO_6), unsafe_allow_html=True)
    else: st.info("Próximamente... 🚧")