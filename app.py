import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="SPRING AI SHIFT", page_icon="🌱", layout="wide")

# REDISEÑO ESTÉTICO: Contraste alto y legibilidad
st.markdown("""
    <style>
    /* Fondo negro absoluto */
    .stApp { 
        background-color: #000000; 
        color: #FFFFFF; 
    }
    
    /* Sidebar con contraste: Fondo casi negro, texto blanco */
    [data-testid="stSidebar"] { 
        background-color: #0A0A0A; 
        border-right: 1px solid #333;
    }
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] label {
        color: #FFFFFF !important;
    }

    /* Glassmorphism real: Bordes sutiles, fondo translúcido */
    .glass-box {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        color: #FFFFFF;
    }

    /* BOTÓN REFORMADO: Fondo oscuro con borde luz para legibilidad */
    div.stButton > button {
        background-color: #1A1A1A !important;
        color: #FFFFFF !important;
        border: 1px solid #444 !important;
        border-radius: 8px;
        width: 100%;
        height: 3em;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        border-color: #FFFFFF !important;
        background-color: #333333 !important;
    }

    /* Inputs y Text Areas con contraste */
    .stTextArea textarea {
        background-color: #111 !important;
        color: #FFFFFF !important;
        border: 1px solid #333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica IA (Se mantiene tu modelo funcional)
def procesar_claridad(key, rol, texto):
    try:
        genai.configure(api_key=key)
        # Usamos el modelo estable que confirmaste
        model = genai.GenerativeModel('gemini-1.5-flash') 
        prompt = f"Experto en {rol}. Explica este texto con analogías y pasos accionables: {texto}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error en la conexión: {e}"

# --- INTERFAZ ---
with st.sidebar:
    st.markdown("## CONFIGURACIÓN")
    user_key = st.text_input("Introduce tu API Key:", type="password")
    st.divider()
    perfil = st.selectbox("Perfil de Análisis:", ["Marketing & Negocios", "Producto-servicio", "Estrategia Ejecutiva"])

st.markdown("# SPRING AI SHIFT™")
st.markdown("### Transformando la complejidad en pasos accionables.")
st.divider()

col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown('<div class="glass-box">', unsafe_allow_html=True)
    st.markdown("#### ENTRADA DE DATOS")
    tema = st.text_area("¿Qué concepto quieres analizar hoy?", placeholder="Ej: ¿Qué es el branding?", height=250)
    enviar = st.button("GENERAR ANÁLISIS")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if enviar:
        if not user_key:
            st.error("Acceso denegado: Introduce tu API Key en la barra lateral.")
        elif not tema:
            st.warning("Campo vacío: Escribe un concepto para analizar.")
        else:
            with st.spinner("Decodificando complejidad..."):
                resultado = procesar_claridad(user_key, perfil, tema)
                st.markdown('<div class="glass-box">', unsafe_allow_html=True)
                st.markdown(resultado)
                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="glass-box" style="text-align: center; color: #666;">Esperando concepto para procesar...</div>', unsafe_allow_html=True)

# Footer de Servicios
st.divider()
c1, c2, c3 = st.columns(3)
with c1: st.caption("**STRATEGY** \nGobernanza y velocidad.")
with c2: st.caption("**EDUCATION** \nFormación para líderes.")
with c3: st.caption("**IMPACT** \nAlianzas con propósito.")
