"""Piezas visuales que comparten todas las páginas."""

from pathlib import Path

import streamlit as st

from contenido import PAGINA_INICIO, PRINCIPIOS, buscar

RAIZ = Path(__file__).parent
TINTA = "#2E3A59"  # color del texto y de los animales


def cargar_estilos() -> None:
    """Agrega a la página los estilos de assets/estilos.css."""
    css = (RAIZ / "assets" / "estilos.css").read_text(encoding="utf-8")
    st.html(f"<style>{css}</style>")


def cuaderno(items: list[str], color: str, titulo: str = "¿PARA QUÉ TE SIRVE?") -> None:
    """Tarjeta con forma de hoja de cuaderno (renglones y margen rojo)."""
    lista = "".join(f"<li>{t}</li>" for t in items)
    st.html(
        f'<section class="ul-cuaderno">'
        f'<h2 class="ul-etiqueta" style="color:{color}">{titulo}</h2>'
        f"<ul>{lista}</ul></section>"
    )


# ---------------------------------------------------------------------------
# Página de un principio: encabezado → juego → vida real → navegación
# ---------------------------------------------------------------------------
def encabezado_principio(id_principio: str) -> dict:
    """Pinta la letra, el nombre, la idea y «¿Para qué te sirve?». Devuelve el principio."""
    p = buscar(id_principio)
    st.html(
        f'<header class="ul-encabezado">'
        f'<div class="ul-letra" style="background:{p["suave"]};color:{p["fuerte"]}">{p["letra"]}</div>'
        f'<div><p class="ul-etiqueta" style="color:{p["fuerte"]}">PRINCIPIO {p["n"]} DE 7</p>'
        f'<h1 class="ul-titulo">{p["nombre"]}</h1></div></header>'
        f'<p class="ul-idea">{p["idea"]}</p>'
    )
    cuaderno(p["sirve"], p["fuerte"])
    return p


def caja_juego(p: dict):
    """Crea la tarjeta «Juega y descubre» y devuelve sus dos columnas: (dibujo, controles)."""
    st.html(f"<style>.st-key-juego-{p['id']}{{border-color:{p['suave']} !important;}}</style>")
    caja = st.container(border=True, key=f"juego-{p['id']}")
    with caja:
        st.html(
            f'<h2 class="ul-etiqueta" style="color:{p["fuerte"]}">JUEGA Y DESCUBRE</h2>'
            f'<p class="ul-instruccion">{p["juego"]}</p>'
        )
        dibujo, controles = st.columns([1, 1.1], gap="large", vertical_alignment="center")
    return dibujo, controles


def escenario(p: dict, svg: str) -> None:
    """Caja de color donde va el dibujo del juego.

    Se usa st.markdown (y no st.html) porque st.html limpia las etiquetas <svg>.
    El SVG se junta en una sola línea para que Markdown no lo confunda con código.
    """
    svg = " ".join(svg.split())
    st.markdown(
        f'<div class="ul-escenario" style="background:{p["suave"]}">{svg}</div>',
        unsafe_allow_html=True,
    )


def mensaje(p: dict, texto: str) -> None:
    """Globo con lo que el niño acaba de descubrir."""
    st.html(f'<div class="ul-mensaje" style="background:{p["suave"]}">{texto}</div>')


def pie_principio(p: dict) -> None:
    """Pinta «En la vida real» y los botones Anterior / Siguiente."""
    st.html(
        f'<section class="ul-vida" style="background:{p["suave"]}">'
        f'<h2 class="ul-etiqueta" style="color:{p["fuerte"]}">EN LA VIDA REAL</h2>'
        f'<p>{p["vida"]}</p></section>'
    )

    i = p["n"] - 1
    if i == 0:
        anterior, txt_anterior = PAGINA_INICIO, "Inicio"
    else:
        anterior, txt_anterior = PRINCIPIOS[i - 1]["archivo"], f"Anterior: {PRINCIPIOS[i - 1]['nombre']}"
    if i == len(PRINCIPIOS) - 1:
        siguiente, txt_siguiente = PAGINA_INICIO, "Volver al inicio"
    else:
        siguiente, txt_siguiente = PRINCIPIOS[i + 1]["archivo"], f"Siguiente: {PRINCIPIOS[i + 1]['nombre']}"

    st.html(
        f"<style>.st-key-nav-siguiente a{{background:{p['fuerte']} !important;"
        f"border-color:{p['fuerte']} !important;}}</style>"
    )
    izq, der = st.columns(2)
    with izq, st.container(key="nav-anterior"):
        st.page_link(anterior, label=f"← {txt_anterior}")
    with der, st.container(key="nav-siguiente", horizontal_alignment="right"):
        st.page_link(siguiente, label=f"{txt_siguiente} →")
