"""Textos y colores de los 7 principios de la Gestalt.

Si quieres cambiar una frase, un color o un ejemplo, este es el único
archivo que necesitas tocar.
"""

PRINCIPIOS = [
    {
        "id": "cierre",
        "archivo": "actividades/cierre.py",
        "letra": "G",
        "nombre": "Cierre",
        "suave": "#FAD2DC",
        "fuerte": "#A3264D",
        "corto": "Tu cerebro completa lo que falta.",
        "idea": "Tu cerebro completa lo que falta. Si a un dibujo le faltan pedacitos, "
                "¡tú lo ves completo de todos modos!",
        "sirve": [
            "Puedes dibujar con menos líneas y aun así todos entienden tu dibujo.",
            "Te ayuda a leer letras medio borradas en el pizarrón o en un letrero viejo.",
        ],
        "juego": "Mueve la barra para hacer más grandes los huecos del pez. "
                 "¿Hasta dónde sigues viendo un pez?",
        "vida": "Cuando ves un dibujo a medio borrar en el pizarrón, sigues sabiendo qué es.",
    },
    {
        "id": "proximidad",
        "archivo": "actividades/proximidad.py",
        "letra": "E",
        "nombre": "Proximidad",
        "suave": "#FFDDBF",
        "fuerte": "#9A4410",
        "corto": "Lo que está cerca parece equipo.",
        "idea": "Las cosas que están cerquita parecen del mismo equipo.",
        "sirve": [
            "Si dejas espacio entre un tema y otro en tu cuaderno, tus apuntes se entienden mejor.",
            "En un cartel, pon cada foto junto a su texto para que se sepa que van juntos.",
        ],
        "juego": "Separa los pececitos con la barra. ¿Cuántos grupos de peces ves ahora?",
        "vida": "En el recreo, los niños que están juntos parecen un grupo de amigos.",
    },
    {
        "id": "continuidad",
        "archivo": "actividades/continuidad.py",
        "letra": "S",
        "nombre": "Continuidad",
        "suave": "#FFEDA8",
        "fuerte": "#6E5400",
        "corto": "Tus ojos siguen el camino suave.",
        "idea": "Tus ojos siguen el camino más suave, como si fuera una carretera.",
        "sirve": [
            "Te ayuda a seguir caminos en mapas y laberintos sin perderte.",
            "Puedes usar flechas y líneas para explicar los pasos de algo.",
        ],
        "juego": "Mira las serpientes. Luego activa el interruptor para ver de qué pedazos están hechas.",
        "vida": "Si una carretera pasa detrás de un árbol, sabes que del otro lado sigue.",
    },
    {
        "id": "semejanza",
        "archivo": "actividades/semejanza.py",
        "letra": "T",
        "nombre": "Semejanza",
        "suave": "#C8EBD6",
        "fuerte": "#1F6640",
        "corto": "Lo que se parece, se junta.",
        "idea": "Lo que se parece, se junta. Si tienen el mismo color, forma o tamaño, "
                "tu cerebro los agrupa.",
        "sirve": [
            "Usa un color por materia en tus cuadernos y encontrarás todo más rápido.",
            "En un juego, usar playeras del mismo color ayuda a saber quién es de tu equipo.",
        ],
        "juego": "Elige qué cambia: color, forma o tamaño. ¿Ves filas o columnas?",
        "vida": "En un partido, los jugadores con la misma playera son del mismo equipo.",
    },
    {
        "id": "figura_fondo",
        "archivo": "actividades/figura_fondo.py",
        "letra": "A",
        "nombre": "Figura y fondo",
        "suave": "#CFE5F7",
        "fuerte": "#2D5F9A",
        "corto": "Decides qué es la cosa y qué es el fondo.",
        "idea": "Tu cerebro decide qué es «la cosa» (la figura) y qué está atrás (el fondo).",
        "sirve": [
            "Para que un cartel se lea de lejos, usa letras oscuras sobre un fondo claro (o al revés).",
            "Así entiendes cómo se esconden los animales con su camuflaje.",
        ],
        "juego": "Activa el interruptor para cambiar los colores. "
                 "¿Qué ves primero: el gato o el bloque?",
        "vida": "Un búho del mismo color que el árbol casi no se ve: se confunde con el fondo.",
    },
    {
        "id": "direccion_comun",
        "archivo": "actividades/direccion_comun.py",
        "letra": "L",
        "nombre": "Dirección común",
        "suave": "#DED3F6",
        "fuerte": "#5B3FA8",
        "corto": "Lo que se mueve igual, va junto.",
        "idea": "Lo que se mueve hacia el mismo lado parece un grupo.",
        "sirve": [
            "En el fútbol, ver hacia dónde corre tu equipo te ayuda a saber a quién pasar el balón.",
            "Al cruzar la calle, notas hacia dónde avanzan los coches y la gente.",
        ],
        "juego": "Todos los pájaros son iguales. Activa «¡A volar!» y mira cuáles se vuelven parvada.",
        "vida": "Una parvada de pájaros que vuela junta parece un solo equipo en el cielo.",
    },
    {
        "id": "simetria",
        "archivo": "actividades/simetria.py",
        "letra": "T",
        "nombre": "Simetría",
        "suave": "#C6ECEC",
        "fuerte": "#165E5E",
        "corto": "Igual de los dos lados se ve ordenado.",
        "idea": "Cuando algo es igual de los dos lados, como en un espejo, se ve ordenado y completo.",
        "sirve": [
            "Doblar el papel a la mitad te ayuda a recortar figuras parejas.",
            "Te ayuda a dibujar caras, mariposas y casas que se vean bien.",
        ],
        "juego": "Cambia entre «Con espejo» y «Sin espejo». ¿Cuál mariposa se ve más ordenada?",
        "vida": "Las alas de una mariposa y tu cara son casi iguales de los dos lados.",
    },
]

# Número de cada principio (1 a 7), útil para «Principio 3 de 7».
for _n, _p in enumerate(PRINCIPIOS, start=1):
    _p["n"] = _n

PAGINA_INICIO = "actividades/inicio.py"


def buscar(id_principio: str) -> dict:
    """Devuelve el principio con ese id."""
    for p in PRINCIPIOS:
        if p["id"] == id_principio:
            return p
    raise KeyError(f"No existe el principio «{id_principio}»")
