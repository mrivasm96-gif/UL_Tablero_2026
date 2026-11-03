"""L · Dirección común: una parvada donde algunos pájaros vuelan juntos."""

import streamlit as st

from componentes import TINTA, caja_juego, encabezado_principio, escenario, mensaje, pie_principio

PAJARO = ("M1 12 C8 4 15 5 20 12 C25 5 32 4 39 12 C32 11 26 14 22 19 L20 28 L18 19 "
          "C14 14 8 11 1 12 Z")
VOLADORES = {1, 3, 4, 8, 10}  # los pájaros que suben juntos


def dibujar_parvada(volar: bool) -> str:
    pajaros = []
    for i in range(12):
        x, y = (i % 6) * 46, (i // 6) * 44
        clase = ' class="ul-vuela"' if volar and i in VOLADORES else ""
        # El <g> de afuera coloca al pájaro; el de adentro es el que se anima
        pajaros.append(
            f'<g transform="translate({x},{y})"><g{clase}><path d="{PAJARO}" fill="{TINTA}"/></g></g>'
        )
    return (
        '<svg viewBox="-4 -52 280 128" width="290" height="132" role="img" '
        f'aria-label="Pájaros iguales; algunos vuelan hacia arriba juntos">{"".join(pajaros)}</svg>'
    )


p = encabezado_principio("direccion_comun")
dibujo, controles = caja_juego(p)

with controles:
    volar = st.toggle("¡A volar!")
    if volar:
        mensaje(p, "¡Los que volaron juntos parecen una parvada, aunque estuvieran separados!")
    else:
        mensaje(p, "Ahora todos los pájaros se ven iguales. Ningún grupo resalta.")

with dibujo:
    escenario(p, dibujar_parvada(volar))

pie_principio(p)
