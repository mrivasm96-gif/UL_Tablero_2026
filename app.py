import streamlit as st

# Configuración general de la app (debe ser la primera llamada de Streamlit)
st.set_page_config(
    page_title="UL Tablero 2026",
    page_icon="📊",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Catálogo de actividades
# Cambia aquí el nombre, el ícono y la descripción de cada actividad.
# ---------------------------------------------------------------------------
ACTIVIDADES = [
    {"titulo": "Actividad 1", "icono": "1️⃣", "descripcion": "Descripción de la actividad 1."},
    {"titulo": "Actividad 2", "icono": "2️⃣", "descripcion": "Descripción de la actividad 2."},
    {"titulo": "Actividad 3", "icono": "3️⃣", "descripcion": "Descripción de la actividad 3."},
    {"titulo": "Actividad 4", "icono": "4️⃣", "descripcion": "Descripción de la actividad 4."},
    {"titulo": "Actividad 5", "icono": "5️⃣", "descripcion": "Descripción de la actividad 5."},
    {"titulo": "Actividad 6", "icono": "6️⃣", "descripcion": "Descripción de la actividad 6."},
    {"titulo": "Actividad 7", "icono": "7️⃣", "descripcion": "Descripción de la actividad 7."},
]


# ---------------------------------------------------------------------------
# Páginas
# ---------------------------------------------------------------------------
def inicio():
    st.title("📊 UL Tablero 2026")
    st.write("Ejemplo sobre cómo utilizar widgets en los tableros.")
    st.info("Selecciona una actividad en el panel de la izquierda.")

    cols = st.columns(4)
    for i, act in enumerate(ACTIVIDADES):
        with cols[i % 4]:
            with st.container(border=True):
                st.markdown(f"**{act['icono']} {act['titulo']}**")
                st.caption(act["descripcion"])


def placeholder(act: dict):
    """Contenido provisional para una actividad. Reemplázalo con tus widgets."""
    st.title(f"{act['icono']} {act['titulo']}")
    st.caption(act["descripcion"])
    st.divider()
    st.warning("🚧 Esta actividad está en construcción.")
    # TODO: agrega aquí los widgets de la actividad


def crear_pagina(numero: int, act: dict) -> st.Page:
    return st.Page(
        lambda: placeholder(act),
        title=act["titulo"],
        icon=act["icono"],
        url_path=f"actividad-{numero}",
    )


# ---------------------------------------------------------------------------
# Navegación (panel de control a la izquierda)
# ---------------------------------------------------------------------------
paginas = {
    "General": [st.Page(inicio, title="Inicio", icon="🏠", default=True)],
    "Actividades": [crear_pagina(i, act) for i, act in enumerate(ACTIVIDADES, start=1)],
}

pg = st.navigation(paginas, position="sidebar")

with st.sidebar:
    st.divider()
    st.caption("UL Tablero 2026")

pg.run()
