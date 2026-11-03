"""UL Tablero 2026 · La Gestalt explicada para niños.

Ejecuta:  streamlit run app.py
"""

from pathlib import Path

import streamlit as st

from componentes import cargar_estilos
from contenido import PAGINA_INICIO, PRINCIPIOS

RAIZ = Path(__file__).parent

st.set_page_config(
    page_title="Gestalt para niños · UL",
    page_icon=":material/visibility:",
    layout="wide",
)

# Logotipo de la UL arriba del panel de control
st.logo(str(RAIZ / "assets" / "logo_ul.svg"), size="large")

# ---------------------------------------------------------------------------
# Panel de control (navegación a la izquierda)
# ---------------------------------------------------------------------------
inicio = st.Page(PAGINA_INICIO, title="Inicio", icon=":material/home:", default=True)
principios = [
    st.Page(p["archivo"], title=f"{p['letra']} · {p['nombre']}", url_path=p["id"])
    for p in PRINCIPIOS
]

pagina = st.navigation({"General": [inicio], "Principios": principios}, position="sidebar")

cargar_estilos()
pagina.run()
