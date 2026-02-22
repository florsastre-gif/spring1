import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURACIÓN DE INTERFAZ ---
st.set_page_config(
    page_title="SPRING AI SHIFT", 
    page_icon="🌱", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- UI ENGINE (ESTÉTICA TECH PREMIUM) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=JetBrains+Mono:wght@400&display=swap');

    :root {
        --bg-deep: #050505;
        --bg-surface: #0F0F0F;
        --accent: #00FFAA;
        --text-main: #E0E0E0;
    }

    .stApp { background-color: var(--bg-deep); color: var(--text-main); font-family: 'Inter', sans-serif; }
    
    [data-testid="stSidebar"] { 
        background-color: var(--bg-surface); 
        border-right: 1px solid rgba(255,255,255,0.1);
    }

    /* Input Fields corregidos para legibilidad total */
    input, textarea, [data-baseweb="select"] > div {
        background-color: #000000 !important;
        color: var(--accent) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 8px !important;
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* Botón con Glow */
    div.stButton > button {
        background: linear-gradient(135deg, #00FFAA 0%, #00CC88 100%) !important;
        color: #000000 !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.8rem 2rem !important;
        width: 100%;
        box-shadow: 0 4px 15px rgba(0, 255, 170, 0.2);
    }

    .intel-card {
        background-color: var(--bg-surface);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 24px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CLASE DE ANÁLISIS ESTRATÉGICO ---
class ShiftAnalytic:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def process(self, role, prompt_text):
        system_instruction = (
            f"Actúa como un Consultor Estratégico Senior experto en {role}. "
            "Tu tarea es decodificar conceptos complejos. "
            "IDIOMA: Responde EXCLUSIVAMENTE en español. "
            "ESTRUCTURA: \n"
            "1. RESUMEN EJECUTIVO (Máximo 3 líneas).\n"
            "2. DESCONSTRUCCIÓN TÉCNICA.\n"
            "3. RUTA DE ACCIÓN (3 pasos).\n"
            "4. PREGUNTAS ESTRATÉGICAS (Genera 2 preguntas profundas para hacer reflexionar al usuario)."
        )
        try:
            response = self.model.generate_content(f"{system_instruction}\n\nAnaliza: {prompt_text}")
            return response.text
        except Exception as e:
            return f"ERROR_DE_SISTEMA: {str(e)}"

# --- INTERFAZ DE USUARIO ---
with st.sidebar:
    st.markdown("### AUTENTICACIÓN")
    user_key = st.text_input("TOKEN_DE_ACCESO", type="password", placeholder="Pega tu API Key aquí...")
    

st.markdown("# SPRING AI SHIFT™")
st.markdown("`ESTADO: ACTIVO // IDIOMA: ESPAÑOL`")

col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("### [ENTRADA_DE_DATOS]")
    tema = st.text_area("", placeholder="Describi cuál es HOY tu desafío comercial...", height=300)
    process_trigger = st.button("EJECUTAR ANÁLISIS ESTRATÉGICO")

with col2:
    st.markdown("### [INTELIGENCIA_DE_SALIDA]")
    if process_trigger:
        if not user_key:
            st.error("Error de Autenticación: Falta la API Key en el panel lateral.")
        elif not tema:
            st.warning("Error de Entrada: El flujo de datos está vacío.")
        else:
            engine = ShiftAnalytic(user_key)
            with st.spinner("Procesando a través del motor estratégico..."):
                time.sleep(1) 
                result = engine.process(perfil, tema)
                st.markdown(f'<div class="intel-card">{result}</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            '<div style="height:300px; display:flex; align-items:center; justify-content:center; border:1px dashed #333; border-radius:12px; color:#555;">'
            'Esperando flujo de datos...'
            '</div>', 
            unsafe_allow_html=True
        )

# --- PIE DE PÁGINA ---
st.markdown("<br><br>", unsafe_allow_html=True)
f1, f2, f3 = st.columns(3)
with f1: st.markdown("`ESTRATEGIA` / Gobernanza")
with f2: st.markdown("`EDUCACIÓN` / Liderazgo")
with f3: st.markdown("`IMPACTO` / Propósito")
