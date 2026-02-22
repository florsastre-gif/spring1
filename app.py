import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURACIÓN DE MARCA ---
st.set_page_config(
    page_title="SPRING AI SHIFT", 
    page_icon="🌱", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- UI ARCHITECTURE (ELVATED TECH) ---
# Implementación de capas de profundidad y suavizado de contraste
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=JetBrains+Mono:wght@400&display=swap');

    /* Variables de diseño Senior */
    :root {
        --bg-deep: #050505;
        --bg-surface: #0F0F0F;
        --accent: #00FFAA;
        --border-subtle: rgba(255, 255, 255, 0.1);
        --text-main: #E0E0E0;
        --text-dim: #888888;
    }

    .stApp { background-color: var(--bg-deep); color: var(--text-main); font-family: 'Inter', sans-serif; }
    
    /* Sidebar Profesional: Reducción de ruido visual */
    [data-testid="stSidebar"] { 
        background-color: var(--bg-surface); 
        border-right: 1px solid var(--border-subtle);
    }

    /* Input Fields: Legibilidad garantizada y estética premium */
    input, textarea, [data-baseweb="select"] > div {
        background-color: #000000 !important;
        color: var(--accent) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: 8px !important;
        font-family: 'JetBrains Mono', monospace !important;
        padding: 12px !important;
    }
    
    input:focus, textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 10px rgba(0, 255, 170, 0.1) !important;
    }

    /* Acción Principal: Botón con jerarquía clara */
    div.stButton > button {
        background: linear-gradient(135deg, #00FFAA 0%, #00CC88 100%) !important;
        color: #000000 !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 2rem !important;
        width: 100%;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 15px rgba(0, 255, 170, 0.3);
    }

    /* Cards de Salida con profundidad */
    .intel-card {
        background-color: var(--bg-surface);
        border: 1px solid var(--border-subtle);
        border-radius: 12px;
        padding: 24px;
        margin-top: 10px;
    }

    /* Footer Estratégico */
    .footer-item {
        color: var(--text-dim);
        font-size: 0.8rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        border-top: 1px solid var(--border-subtle);
        padding-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIC LAYER (ENCAPSULADA) ---
class ShiftAnalytic:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def process(self, role, prompt_text):
        full_prompt = (
            f"You are a Senior Strategic Consultant in {role}. "
            f"Analyze the following and provide a high-level executive summary: {prompt_text}"
        )
        try:
            return self.model.generate_content(full_prompt).text
        except Exception as e:
            return f"PROCESS_ERROR: {str(e)}"

# --- INTERFACE DESIGN ---
with st.sidebar:
    st.markdown("<h3 style='color:white;'>SYSTEM_AUTH</h3>", unsafe_allow_html=True)
    user_key = st.text_input("ACCESS_TOKEN", type="password", placeholder="Paste API Key here...")
    st.divider()
    st.markdown("<h3 style='color:white;'>OPERATIONAL_SCOPE</h3>", unsafe_allow_html=True)
    perfil = st.selectbox("ROLE", ["Executive Strategy", "Product Innovation", "Marketing Intelligence"])

st.markdown("# SPRING AI SHIFT™")
st.markdown("<p style='color:#888;'>Bridging the gap between raw data and strategic execution.</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("### [INPUT_STREAM]")
    tema = st.text_area("", placeholder="Describe the concept or challenge to analyze...", height=300)
    process_trigger = st.button("RUN STRATEGIC ANALYSIS")

with col2:
    st.markdown("### [OUTPUT_INTEL]")
    if process_trigger:
        if not user_key:
            st.error("Authentication Error: API Key missing in sidebar.")
        elif not tema:
            st.warning("Input Error: Data stream is empty.")
        else:
            engine = ShiftAnalytic(user_key)
            with st.spinner("Processing through strategic engine..."):
                # Simulación de latencia para feedback visual premium
                time.sleep(1) 
                result = engine.process(perfil, tema)
                st.markdown(f'<div class="intel-card">{result}</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            '<div style="height:300px; display:flex; align-items:center; justify-content:center; border:1px dashed #333; border-radius:12px; color:#555;">'
            'Awaiting Strategic Input...'
            '</div>', 
            unsafe_allow_html=True
        )

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
f1, f2, f3 = st.columns(3)
with f1: st.markdown('<div class="footer-item">STRATEGY / Governance</div>', unsafe_allow_html=True)
with f2: st.markdown('<div class="footer-item">EDUCATION / Leadership</div>', unsafe_allow_html=True)
with f3: st.markdown('<div class="footer-item">IMPACT / Purpose</div>', unsafe_allow_html=True)
