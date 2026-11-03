"""T · Semejanza: peces y pájaros que forman filas por color, forma o tamaño."""

import streamlit as st

from componentes import TINTA, caja_juego, encabezado_principio, escenario, mensaje, pie_principio

ROSA = "#E58BA5"
PEZ = ("M39 12 C32 2 18 1 11 9 L2 2 L5 12 L2 22 L11 15 C18 23 32 22 39 12 Z", 40, 24)
PAJARO = ("M1 12 C8 4 15 5 20 12 C25 5 32 4 39 12 C32 11 26 14 22 19 L20 28 L18 19 "
          "C14 14 8 11 1 12 Z", 40, 30)

MENSAJES = {
    "Color": "Ves filas porque juntas los peces del mismo color.",
    "Forma": "Ves filas porque juntas peces con peces y pájaros con pájaros.",
    "Tamaño": "Ves filas porque juntas los peces grandes con los grandes y los chicos con los chicos.",
}


def dibujar_cuadricula(que_cambia: str) -> str:
    figuras = []
    for fila in range(4):
        impar = fila % 2 == 1
        for columna in range(4):
            forma, color, escala = PEZ, TINTA, 1.0
            if que_cambia == "Color" and impar:
                color = ROSA
            elif que_cambia == "Forma" and impar:
                forma = PAJARO
            elif que_cambia == "Tamaño":
                escala = 0.55 if impar else 1.2
            d, ancho, alto = forma
            x = columna * 56 + 28 - ancho * escala / 2
            y = fila * 52 + 26 - alto * escala / 2
            figuras.append(
                f'<path d="{d}" fill="{color}" transform="translate({x:.1f},{y:.1f}) scale({escala})"/>'
            )
    return (
        '<svg viewBox="0 0 224 208" width="250" height="232" role="img" '
        f'aria-label="Cuadrícula de peces y pájaros que forman filas">{"".join(figuras)}</svg>'
    )


p = encabezado_principio("semejanza")
dibujo, controles = caja_juego(p)

with controles:
    que_cambia = st.segmented_control("¿Qué cambia en cada fila?", list(MENSAJES), default="Color")
    que_cambia = que_cambia or "Color"  # si el niño quita la selección, volvemos a «Color»
    mensaje(p, MENSAJES[que_cambia])

with dibujo:
    escenario(p, dibujar_cuadricula(que_cambia))

pie_principio(p)
