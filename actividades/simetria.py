"""T · Simetría: una mariposa con y sin espejo."""

import streamlit as st

from componentes import TINTA, caja_juego, encabezado_principio, escenario, mensaje, pie_principio

ROSA, NARANJA = "#E0607E", "#F2A65A"

# Alas izquierdas (siempre iguales)
ALA_ARRIBA_IZQ = "M128 70 C110 30 60 20 48 50 C38 78 70 100 128 96 Z"
ALA_ABAJO_IZQ = "M128 100 C90 100 62 120 72 148 C82 170 115 150 128 120 Z"

# Alas derechas: reflejo exacto (con espejo) o diferentes (sin espejo)
ALAS_DERECHAS = {
    "Con espejo": ("M132 70 C150 30 200 20 212 50 C222 78 190 100 132 96 Z",
                   "M132 100 C170 100 198 120 188 148 C178 170 145 150 132 120 Z"),
    "Sin espejo": ("M132 70 C140 50 170 48 180 62 C188 76 165 95 132 92 Z",
                   "M132 100 C175 96 215 110 205 130 C195 146 150 140 132 118 Z"),
}


def dibujar_mariposa(tipo: str) -> str:
    ala_arriba_der, ala_abajo_der = ALAS_DERECHAS[tipo]
    return f"""
    <svg viewBox="0 0 260 200" width="260" height="200" role="img" aria-label="Mariposa">
      <path d="{ALA_ARRIBA_IZQ}" fill="{ROSA}"/>
      <path d="{ALA_ABAJO_IZQ}" fill="{NARANJA}"/>
      <path d="{ala_arriba_der}" fill="{ROSA}"/>
      <path d="{ala_abajo_der}" fill="{NARANJA}"/>
      <ellipse cx="130" cy="105" rx="6" ry="48" fill="{TINTA}"/>
      <path d="M128 62 C124 46 116 38 106 34" fill="none" stroke="{TINTA}" stroke-width="3" stroke-linecap="round"/>
      <path d="M132 62 C136 46 144 38 154 34" fill="none" stroke="{TINTA}" stroke-width="3" stroke-linecap="round"/>
    </svg>"""


p = encabezado_principio("simetria")
dibujo, controles = caja_juego(p)

with controles:
    tipo = st.segmented_control("Tipo de mariposa", list(ALAS_DERECHAS), default="Con espejo")
    tipo = tipo or "Con espejo"
    if tipo == "Con espejo":
        mensaje(p, "Igual de los dos lados: se ve ordenada, completa y tranquila.")
    else:
        mensaje(p, "Un lado es distinto al otro: se ve rara, como si algo estuviera mal.")

with dibujo:
    escenario(p, dibujar_mariposa(tipo))

pie_principio(p)
