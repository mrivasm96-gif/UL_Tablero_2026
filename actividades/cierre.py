"""G · Cierre: un pez punteado al que le crecen los huecos."""

import streamlit as st

from componentes import TINTA, caja_juego, encabezado_principio, escenario, mensaje, pie_principio


def dibujar_pez(hueco: int) -> str:
    trazo = f'fill="none" stroke="{TINTA}" stroke-width="8" stroke-linejoin="round" stroke-dasharray="14 {hueco}"'
    return f"""
    <svg viewBox="0 0 230 200" width="230" height="200" role="img" aria-label="Pez dibujado con una línea punteada">
      <path d="M205 100 C180 52 105 48 71 92 L33 62 L45 100 L33 138 L71 108 C105 152 180 148 205 100 Z" {trazo}/>
      <path d="M150 70 C138 88 138 112 150 130" {trazo}/>
      <circle cx="178" cy="90" r="7" fill="{TINTA}"/>
    </svg>"""


p = encabezado_principio("cierre")
dibujo, controles = caja_juego(p)

with controles:
    hueco = st.slider("Tamaño de los huecos", min_value=0, max_value=26, value=4)
    if hueco <= 8:
        mensaje(p, "¡Sigue siendo un pez! Tu cerebro rellena los huecos.")
    elif hueco <= 18:
        mensaje(p, "Ya tiene huecos grandes… pero tu cerebro todavía lo completa.")
    else:
        mensaje(p, "Ahora son rayitas sueltas. ¡Encontraste el límite de tu cerebro!")

with dibujo:
    escenario(p, dibujar_pez(hueco))

pie_principio(p)
