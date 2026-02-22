import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- CONFIGURACIÓN DE NÚCLEO ---
load_dotenv()
st.set_page_config(page_title="SPRING AI SHIFT", page_icon="🌱", layout="wide")

# --- UI ENGINE (TECH MINIMALISM) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;700&display=swap');

    /* Reset Global */
    .stApp { background-color: #050505; color: #E0E0E0; font-family: 'JetBrains Mono', monospace; }
    [data-testid="stSidebar"] { background-color: #000000; border-right: 1px solid #1A1A1A; }
    
    /* Typography */
    h1, h2, h3 { color: #FFFFFF !important; letter-spacing: -1px; font-weight: 700; }
    .stMarkdown p { font-weight: 300; line-height: 1.6; color: #A0A0A0; }

    /* Containers */
    .tech-card {
        background: #0A0A0A;
        border: 1px solid #1A1A1A;
        border-radius: 4px;
        padding: 2rem;
        margin-bottom: 1rem;
        transition: border 0.3s ease;
    }
    .tech-card:hover { border-color: #00FFAA; }

    /* Inputs */
    .stTextArea textarea {
        background-color: #000000 !important;
        color: #00FFAA !important;
        border: 1px solid #1A1A1A !important;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Primary Action Button */
    div.stButton > button {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: none !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        width: 100%;
        border-radius: 2px !important;
        padding: 0.75rem 0 !important;
        letter-spacing: 1px;
    }
    div.stButton > button:hover { background-color: #00FFAA !important; }

    /* Info Boxes */
    .stAlert { background-color: #0A0A0A !important; border: 1px solid #1A1A1A !important; color: #A0A0A0 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIC LAYER ---
class ShiftEngine:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analyze(self, role: str, text: str) -> str:
        prompt = f"""
        Role: Senior Expert in {role}
        Objective: Decodify complexity into actionable intelligence.
        Format: 
        1. CORE CONCEPT (1 sentence)
        2. SYSTEM ANALOGY
        3. EXECUTION PATH (3 clear steps)
        4. STRATEGIC QUESTION
        
        Input: {text}
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"SYSTEM_ERROR: {str(e)}"

# --- INTERFACE ---
with st.sidebar:
    st.markdown("### SYSTEM_AUTH")
    user_key = st.text_input("API_KEY_TOKEN", type="password")
    st.divider()
    st.markdown("### OPERATIONAL_PROFILE")
    perfil = st.selectbox("ROLE_SELECT", ["Marketing & Business", "Product-Service", "Executive Strategy"])

st.markdown("# SPRING AI SHIFT™")
st.markdown("`v2.0 // HIGH_CONTRAST_EDITION`")
st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="tech-card">', unsafe_allow_html=True)
    st.markdown("### INPUT_STREAM")
    tema = st.text_area("", placeholder="Enter concept to deconstruct...", height=250)
    process_btn = st.button("RUN_ANALYSIS")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if process_btn:
        if not user_key:
            st.error("ERR: MISSING_API_KEY")
        elif not tema:
            st.warning("ERR: EMPTY_INPUT")
        else:
            engine = ShiftEngine(user_key)
            with st.spinner("PROCESSING_DATA..."):
                output = engine.analyze(perfil, tema)
                st.markdown('<div class="tech-card">', unsafe_allow_html=True)
                st.markdown("### OUTPUT_INTEL")
                st.markdown(output)
                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="opacity: 0.3; padding: 2rem; border: 1px dashed #333;">SYSTEM_IDLE: Awaiting input stream...</div>', unsafe_allow_html=True)


