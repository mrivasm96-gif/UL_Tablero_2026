"""A · Figura y fondo: un gato recortado en un bloque."""

import streamlit as st

from componentes import TINTA, caja_juego, encabezado_principio, escenario, mensaje, pie_principio

GATO = ("M78 52 L72 22 L92 40 C97 39 103 39 108 40 L128 22 L122 52 C130 62 130 78 120 88 "
        "C140 100 150 130 146 168 L54 168 C50 130 60 100 80 88 C70 78 70 62 78 52 Z")
COLA = "M144 162 C172 162 178 128 160 116"


def dibujar_gato(invertir: bool) -> str:
    fondo, figura = ("#FFFFFF", TINTA) if invertir else (TINTA, "#FFF8E8")
    return f"""
    <svg viewBox="0 0 200 200" width="200" height="200" role="img" aria-label="Bloque con la silueta de un gato sentado">
      <rect x="0" y="0" width="200" height="200" rx="18" fill="{fondo}"/>
      <path d="{GATO}" fill="{figura}"/>
      <path d="{COLA}" fill="none" stroke="{figura}" stroke-width="10" stroke-linecap="round"/>
    </svg>"""


p = encabezado_principio("figura_fondo")
dibujo, controles = caja_juego(p)

with controles:
    invertir = st.toggle("Cambiar colores")
    if invertir:
        mensaje(p, "Ahora el gato oscuro es la figura y lo blanco es el fondo.")
    else:
        mensaje(p, "El gato está hecho de «hueco». ¿Viste primero el gato o el bloque oscuro?")

with dibujo:
    escenario(p, dibujar_gato(invertir))

pie_principio(p)
