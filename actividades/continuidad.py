"""S · Continuidad: dos serpientes que se cruzan (en realidad son 4 pedazos)."""

import streamlit as st

from componentes import TINTA, caja_juego, encabezado_principio, escenario, mensaje, pie_principio

# Cada serpiente está hecha de 2 mitades que se tocan en el centro (140, 100)
PEDAZOS = [
    "M20 150 C60 150 100 125 140 100",   # serpiente 1, cola
    "M140 100 C180 75 220 50 256 50",    # serpiente 1, cabeza
    "M20 50 C60 50 100 75 140 100",      # serpiente 2, cola
    "M140 100 C180 125 220 150 256 150", # serpiente 2, cabeza
]
COLORES_PEDAZOS = ["#A3264D", "#2D5F9A", "#1F6640", "#9A4410"]


def dibujar_serpientes(mostrar_pedazos: bool) -> str:
    colores = COLORES_PEDAZOS if mostrar_pedazos else [TINTA] * 4
    cuerpos = "".join(
        f'<path d="{d}" fill="none" stroke="{c}" stroke-width="16" stroke-linecap="round"/>'
        for d, c in zip(PEDAZOS, colores)
    )
    cabezas = (
        f'<ellipse cx="266" cy="50" rx="18" ry="13" fill="{colores[1]}"/>'
        f'<circle cx="272" cy="45" r="3" fill="#FFFFFF"/>'
        f'<ellipse cx="266" cy="150" rx="18" ry="13" fill="{colores[3]}"/>'
        f'<circle cx="272" cy="145" r="3" fill="#FFFFFF"/>'
    )
    return (
        '<svg viewBox="0 0 300 200" width="300" height="200" role="img" '
        f'aria-label="Dos serpientes que se cruzan">{cuerpos}{cabezas}</svg>'
    )


p = encabezado_principio("continuidad")
dibujo, controles = caja_juego(p)

with controles:
    mostrar = st.toggle("Mostrar los pedazos")
    if mostrar:
        mensaje(p, "¡Eran 4 pedazos! Pero tus ojos siguieron el camino suave y viste 2 serpientes.")
    else:
        mensaje(p, "¿Ves 2 serpientes que se cruzan? La mayoría de las personas sí.")

with dibujo:
    escenario(p, dibujar_serpientes(mostrar))

pie_principio(p)
