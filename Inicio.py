"""Página de inicio: acróstico GESTALT."""

import streamlit as st

from componentes import cuaderno
from contenido import PRINCIPIOS

st.html(
    '<p class="ul-etiqueta" style="color:#A3264D">LOS 7 TRUCOS DE TU CEREBRO</p>'
    '<h1 class="ul-titulo ul-titulo-inicio">¿Cómo ve tu cerebro?</h1>'
    '<p class="ul-intro">Gestalt es una palabra alemana que significa «forma completa». '
    "Tu cerebro no ve pedacitos sueltos: los junta para entender el mundo. "
    "Aquí hay 7 trucos que usa todo el tiempo, ¡uno por cada letra!</p>"
)

cuaderno(
    [
        "Para hacer dibujos, carteles y tareas que todos entiendan a la primera.",
        "Para ordenar tus cuadernos y encontrar todo más rápido.",
        "Para descubrir los trucos que hay en juegos, mapas, anuncios y en la naturaleza.",
    ],
    color="#A3264D",
)

st.html('<p class="ul-etiqueta" style="color:#4F5B78">GESTALT, LETRA POR LETRA</p>')

# Un renglón por letra: se lee de arriba hacia abajo G-E-S-T-A-L-T
for p in PRINCIPIOS:
    st.html(f"<style>.st-key-fila-{p['id']}{{border-color:{p['suave']} !important;}}</style>")
    with st.container(border=True, key=f"fila-{p['id']}"):
        letra, texto, enlace = st.columns([0.9, 5, 1.2], vertical_alignment="center")
        with letra:
            st.html(
                f'<div class="ul-fila-letra" style="background:{p["suave"]};color:{p["fuerte"]}">'
                f'{p["letra"]}</div>'
            )
        with texto:
            st.html(
                f'<p class="ul-fila-nombre" style="color:{p["fuerte"]}">{p["nombre"]}</p>'
                f'<p class="ul-fila-corto">{p["corto"]}</p>'
            )
        with enlace:
            st.page_link(p["archivo"], label="Ver →")
