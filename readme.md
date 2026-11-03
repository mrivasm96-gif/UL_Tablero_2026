# UL_Tablero_2026

Ejemplo sobre cómo utilizar widgets en los tableros: la **Gestalt explicada para niños**, con un mini juego por cada letra de G-E-S-T-A-L-T.

## Cómo correrlo

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Estructura

```
app.py                  # configuración, logotipo y panel de control
contenido.py            # textos y colores de los 7 principios (edita aquí)
componentes.py          # piezas compartidas: encabezado, cuaderno, juego, navegación
actividades/
  inicio.py             # acróstico GESTALT
  cierre.py             # G · slider
  proximidad.py         # E · slider
  continuidad.py        # S · toggle
  semejanza.py          # T · segmented_control
  figura_fondo.py       # A · toggle
  direccion_comun.py    # L · toggle (con animación)
  simetria.py           # T · segmented_control
assets/
  logo_ul.svg
  estilos.css           # estilos de libro de texto
.streamlit/config.toml  # paleta pastel y tipografías
```
