"""E · Proximidad: 18 pececitos que se separan en grupos."""

import streamlit as st

from componentes import TINTA, caja_juego, encabezado_principio, escenario, mensaje, pie_principio

PEZ = "M33 10 C27 2 15 1 9 8 L2 2 L4 10 L2 18 L9 12 C15 19 27 18 33 10 Z"
ANCHO_GRUPO = 74  # 2 columnas de peces


def dibujar_cardumenes(separacion: int) -> str:
    peces = []
    for grupo in range(3):
        for fila in range(3):
            for columna in range(2):
                x = grupo * (ANCHO_GRUPO + separacion) + columna * 40
                y = fila * 28
                peces.append(
                    f'<g transform="translate({x},{y})"><path d="{PEZ}" fill="{TINTA}"/>'
                    f'<circle cx="27" cy="8" r="1.8" fill="#FFFFFF"/></g>'
                )
    ancho = 3 * ANCHO_GRUPO + 2 * separacion
    alto = 76
    return (
        f'<svg viewBox="0 0 {ancho} {alto}" width="{ancho * 1.2:.0f}" height="{alto * 1.2:.0f}" '
        f'role="img" aria-label="Pececitos que se separan en grupos">{"".join(peces)}</svg>'
    )


p = encabezado_principio("proximidad")
dibujo, controles = caja_juego(p)

with controles:
    separacion = st.slider("Separación entre grupos", min_value=6, max_value=44, value=6)
    if separacion < 16:
        mensaje(p, "Parece un solo montón de peces.")
    else:
        mensaje(p, "¡Ahora ves 3 grupos de peces! Los que nadan cerca parecen equipo.")

with dibujo:
    escenario(p, dibujar_cardumenes(separacion))

pie_principio(p)
