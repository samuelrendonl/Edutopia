"""Catálogo curricular de Edutopia y generadores de práctica por grado."""

import sys
from pathlib import Path


# ``juegos`` vive en la raíz del proyecto para poder reutilizar su catálogo.
# Añadimos esa raíz también cuando este módulo se ejecuta directamente desde
# ``Backend`` (por ejemplo, al lanzar sus pruebas unitarias).
PROJECT_ROOT = str(Path(__file__).resolve().parents[2])
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

BASE_ACTIVITIES = [
    {
        "key": "math-counting", "subject": "Matemáticas", "kind": "Aprendizaje",
        "title": "Contamos hasta 20", "description": "Cuenta colecciones, reconoce los números y descubre cuántos objetos hay.",
        "curriculum": "counting", "color": "#4f61d8", "icon": "calculator", "points": 100, "minutes": 7,
        "lesson": [], "questions": [],
    },
    {
        "key": "math-sums", "subject": "Matemáticas", "kind": "Aprendizaje",
        "title": "Operaciones y problemas", "description": "Aprende estrategias para calcular y resolver situaciones cotidianas.",
        "curriculum": "operations", "color": "#5b5ce2", "icon": "calculator", "points": 100, "minutes": 7,
        "lesson": [
            "Primero lee el problema completo y piensa qué está pasando: ¿se juntan cantidades, se quitan, se repiten o se reparten? Esa historia te da una pista sobre la operación.",
            "Para sumar, puedes separar los números en decenas y unidades. Por ejemplo, 28 + 15 es (20 + 10) + (8 + 5). Luego juntas los resultados. Si una unidad pasa de diez, cambia diez unidades por una decena.",
            "Para restar, compara las cantidades o piensa cuánto falta para llegar de un número al otro. En una resta con préstamo, una decena se convierte en diez unidades. Comprueba el resultado sumando la diferencia al número menor.",
            "En grados mayores aparecen números más grandes y decimales. La multiplicación permite sumar grupos iguales; la división sirve para repartir o descubrir cuántos grupos caben. Dibuja, separa los números por partes y revisa si el resultado tiene sentido antes de marcarlo.",
        ],
        "questions": [],
    },
    {
        "key": "reading-story", "subject": "Lengua Castellana", "kind": "Aprendizaje",
        "title": "Leemos entre líneas", "description": "Comprende una historia, identifica sus pistas y explica tus ideas.",
        "color": "#f28c28", "icon": "book", "points": 100, "minutes": 8,
        "passage": "El sábado, Tomás encontró una caja pequeña junto al viejo limonero de su abuela. No tenía candado, pero una cinta azul rodeaba la tapa. Dentro había semillas, una nota y una fotografía de un jardín lleno de girasoles. La nota decía: «Las cosas bonitas crecen cuando alguien las cuida». Tomás miró el patio, que llevaba meses vacío, y llamó a su prima Sara. Juntos llenaron varias macetas con tierra. Separaron las semillas, las cubrieron con cuidado y escribieron el nombre de cada planta en una etiqueta. Durante las semanas siguientes se turnaron para regarlas. Un día, Sara llegó corriendo: entre la tierra asomaba un brote verde. Tomás sonrió. La caja ya no guardaba un misterio; ahora guardaba una promesa que los dos habían empezado a cumplir.",
        "passage_by_grade": {
            "early": "El sábado, Tomás encontró una caja junto al limonero de su abuela. Tenía una cinta azul. Adentro había semillas, una nota y una foto de girasoles. Tomás llamó a su prima Sara. Juntos pusieron tierra en unas macetas y sembraron las semillas. Cada día se turnaron para regarlas. Una mañana apareció un brote verde. Los dos sonrieron: ahora tenían plantas para cuidar.",
            "upper": "El sábado, Tomás descubrió una caja sin candado junto al limonero de su abuela; una cinta azul mantenía cerrada la tapa. Encontró semillas, una nota y una fotografía de un jardín repleto de girasoles. «Las cosas bonitas crecen cuando alguien las cuida», decía el mensaje. Como el patio llevaba meses vacío, invitó a su prima Sara a sembrar. Organizaron las semillas en macetas, pusieron etiquetas y se turnaron para regarlas durante varias semanas. Cuando un brote verde asomó entre la tierra, Tomás entendió que la nota no escondía un secreto mágico: les proponía un proyecto que ambos podían hacer realidad con paciencia y colaboración.",
        },
        "lesson": [
            "Comprender un texto es construir su sentido, no solo pronunciar sus palabras. Mientras lees, imagina la escena y pregúntate qué quiere cada personaje.",
            "Las respuestas explícitas aparecen directamente en el texto. Para encontrarlas, busca nombres, lugares, acciones y palabras que se repiten.",
            "A veces el texto no dice todo de forma directa. Puedes inferir algo juntando varias pistas. Una inferencia debe apoyarse en lo que leíste, no en una suposición sin evidencia.",
            "Al final, resume la historia con tus propias palabras: quién participó, qué problema o situación apareció y cómo terminó. Volver a leer una frase también es una buena estrategia.",
        ],
        "questions": [
            {"prompt": "¿Qué encontró Tomás junto al limonero?", "options": ["Una caja pequeña", "Una pelota", "Un libro grande"], "answer": 0},
            {"prompt": "¿De qué color era la cinta?", "options": ["Roja", "Azul", "Verde"], "answer": 1},
            {"prompt": "¿Qué había dentro de la caja?", "options": ["Semillas, una nota y una foto", "Juguetes y dulces", "Una regadera y una pala"], "answer": 0},
            {"prompt": "¿A quién llamó Tomás para ayudarle?", "options": ["A su abuela", "A su prima Sara", "A su vecino"], "answer": 1},
            {"prompt": "¿Qué hicieron con las semillas?", "options": ["Las guardaron en un cajón", "Las plantaron en macetas", "Se las regalaron a la abuela"], "answer": 1},
            {"prompt": "¿Por qué se turnaban para regarlas?", "options": ["Para cuidar las plantas entre los dos", "Para llenar la caja", "Para limpiar el patio"], "answer": 0},
            {"prompt": "¿Qué apareció entre la tierra?", "options": ["Una flor amarilla", "Un brote verde", "Una piedra azul"], "answer": 1},
            {"prompt": "¿Qué significa aquí «las cosas bonitas crecen cuando alguien las cuida»?", "options": ["Que cuidar algo ayuda a que se desarrolle", "Que las cajas deben cerrarse", "Que las plantas crecen sin agua"], "answer": 0},
            {"prompt": "¿Cómo cambió el patio durante la historia?", "options": ["De vacío empezó a tener macetas cuidadas", "Se convirtió en una caja", "Dejó de recibir luz"], "answer": 0},
            {"prompt": "¿Cuál es la idea principal del relato?", "options": ["Tomás perdió una fotografía", "Tomás y Sara cuidaron juntos unas semillas", "La abuela compró un limonero"], "answer": 1},
        ],
    },
    {
        "key": "words-syllables", "subject": "Lengua Castellana", "kind": "Aprendizaje",
        "title": "Palabras, sílabas y acentos", "description": "Escucha cómo suenan las palabras y reconoce dónde llevan tilde.",
        "color": "#e66a9b", "icon": "book", "points": 100, "minutes": 7,
        "lesson": [
            "Las sílabas son grupos de sonidos que pronunciamos en un solo impulso de voz. Pronuncia una palabra despacio y acompaña cada golpe de voz con una palmada.",
            "Una palabra puede tener una sílaba, como sol; dos, como ca-sa; tres, como ven-ta-na; o más, como ma-ri-po-sa. Las vocales ayudan a formar el centro de cada sílaba.",
            "Todas las palabras tienen una sílaba que suena con más fuerza: la sílaba tónica. En algunas palabras se escribe una tilde para señalar esa fuerza y seguir las reglas de acentuación.",
            "Lee cada opción en voz alta, sepárala en sílabas y escucha dónde recae la voz. Después revisa la tilde: practicar con ejemplos ayuda a escribir con más seguridad.",
        ],
        "questions": [
            {"prompt": "¿Cuántas sílabas tiene «casa»?", "options": ["Una", "Dos", "Tres"], "answer": 1},
            {"prompt": "¿Cómo se separa «mariposa»?", "options": ["ma-ri-po-sa", "mar-ip-osa", "ma-rip-osa"], "answer": 0},
            {"prompt": "¿Qué palabra empieza con el sonido de M?", "options": ["Luna", "Mesa", "Rana"], "answer": 1},
            {"prompt": "¿Cuál palabra tiene tres sílabas?", "options": ["Pan", "Camino", "Flor"], "answer": 1},
            {"prompt": "¿En qué sílaba suena más fuerte «pelota»?", "options": ["pe", "lo", "ta"], "answer": 1},
            {"prompt": "¿Cuál palabra lleva tilde escrita?", "options": ["Arbol", "Árbol", "Arból"], "answer": 1},
            {"prompt": "¿Cuántas sílabas tiene «mar»?", "options": ["Una", "Dos", "Tres"], "answer": 0},
            {"prompt": "¿Cuál separación es correcta para «ventana»?", "options": ["ven-ta-na", "ve-nta-na", "vent-ana"], "answer": 0},
            {"prompt": "¿Qué palabra rima con «canción»?", "options": ["Balón", "Casa", "Lápiz"], "answer": 0},
            {"prompt": "¿Cuál opción está escrita correctamente?", "options": ["camión", "camíon", "camion"], "answer": 0},
        ],
        "grade_questions": {
            "upper": [
                {"prompt": "¿Cuántas sílabas tiene «extraordinario»?", "options": ["Cuatro", "Seis", "Ocho"], "answer": 1},
                {"prompt": "¿Cuál palabra es esdrújula?", "options": ["Brújula", "Papel", "Reloj"], "answer": 0},
                {"prompt": "¿Cuál palabra presenta hiato?", "options": ["País", "Cuidado", "Puerta"], "answer": 0},
                {"prompt": "¿Cuál palabra aguda debe llevar tilde?", "options": ["Compás", "Papel", "Reloj"], "answer": 0},
                {"prompt": "¿Cuál palabra llana está bien escrita y no necesita tilde?", "options": ["Joven", "Jóven", "Jovén"], "answer": 0},
                {"prompt": "¿Cuál palabra contiene un triptongo?", "options": ["Buey", "País", "Maíz"], "answer": 0},
                {"prompt": "¿Cómo se separa «murciélago»?", "options": ["mur-cié-la-go", "murcié-la-go", "mur-ciél-ago"], "answer": 0},
                {"prompt": "¿Cuál palabra aguda lleva tilde?", "options": ["Café", "Mesa", "Lunes"], "answer": 0},
                {"prompt": "¿Qué palabra está tildada correctamente?", "options": ["también", "tambièn", "támbien"], "answer": 0},
                {"prompt": "En «biblioteca», ¿cuál es la sílaba tónica?", "options": ["bi", "te", "ca"], "answer": 1},
            ],
        },
    },
    {
        "key": "math-fractions-geometry", "subject": "Matemáticas", "kind": "Aprendizaje",
        "title": "Formas y posiciones", "description": "Reconoce figuras, cuerpos y posiciones en el espacio.",
        "curriculum": "shapes", "color": "#7c65d9", "icon": "calculator", "points": 100, "minutes": 8,
        "lesson": [
            "Una fracción representa partes iguales de un todo. El número de abajo indica en cuántas partes se divide y el de arriba cuántas partes tomamos.",
            "Para comparar fracciones con el mismo denominador, observa sus numeradores: más partes tomadas significa una fracción mayor.",
            "Las figuras tienen lados, vértices y propiedades que puedes observar. Medir con cuidado y dibujar ayuda a resolver problemas de geometría.",
            "Lee cada problema, identifica los datos y representa la situación antes de elegir una respuesta. Después comprueba si el resultado tiene sentido."
        ],
        "questions": [
            {"prompt": "¿Qué fracción representa una de cuatro partes iguales?", "options": ["1/4", "4/1", "1/2"], "answer": 0},
            {"prompt": "¿Cuál es mayor?", "options": ["2/8", "5/8", "1/8"], "answer": 1},
            {"prompt": "¿Cuántos lados tiene un pentágono?", "options": ["4", "5", "6"], "answer": 1},
            {"prompt": "La mitad de 12 es…", "options": ["4", "6", "8"], "answer": 1},
            {"prompt": "¿Qué figura tiene todos sus lados iguales y cuatro vértices?", "options": ["Círculo", "Cuadrado", "Triángulo"], "answer": 1},
            {"prompt": "Si una pizza se divide en 8 partes y comes 3, ¿qué fracción comes?", "options": ["3/8", "8/3", "5/8"], "answer": 0},
            {"prompt": "¿Cuántos centímetros hay en un metro?", "options": ["10", "50", "100"], "answer": 2},
            {"prompt": "¿Qué fracción equivale a la mitad?", "options": ["1/3", "2/4", "3/4"], "answer": 1},
            {"prompt": "Un rectángulo tiene…", "options": ["3 lados", "4 lados", "5 lados"], "answer": 1},
            {"prompt": "Si recorres 3 metros y luego 2 metros, recorres…", "options": ["1 metro", "5 metros", "6 metros"], "answer": 1}
        ]
    },
    {
        "key": "language-write-create", "subject": "Lengua Castellana", "kind": "Aprendizaje",
        "title": "Construimos historias", "description": "Ordena ideas, mejora frases y escribe con intención.",
        "color": "#d7659a", "icon": "book", "points": 100, "minutes": 8,
        "lesson": [
            "Toda historia necesita personajes, un lugar y algo que sucede. Ordenar esos elementos ayuda a que el lector entienda lo que quieres contar.",
            "Una oración comienza con mayúscula y termina con un signo adecuado. El punto separa ideas completas y la coma ayuda a organizar enumeraciones.",
            "Los conectores como primero, luego, porque y finalmente unen las ideas y muestran el orden o la causa de los acontecimientos.",
            "Antes de entregar un texto, léelo en voz alta: revisa mayúsculas, tildes, signos y si cada oración comunica una idea clara."
        ],
        "questions": [
            {"prompt": "¿Cuál oración comienza correctamente?", "options": ["mañana iremos al parque.", "Mañana iremos al parque.", "mañana Iremos al parque."], "answer": 1},
            {"prompt": "¿Qué signo termina una pregunta?", "options": ["¿ ?", ".", ","], "answer": 0},
            {"prompt": "¿Cuál palabra es un personaje?", "options": ["Valentina", "Ayer", "Rápido"], "answer": 0},
            {"prompt": "¿Qué conector indica el final?", "options": ["Primero", "Porque", "Finalmente"], "answer": 2},
            {"prompt": "¿Cuál oración tiene sentido completo?", "options": ["El perro corre.", "Porque la lluvia.", "En el jardín y."], "answer": 0},
            {"prompt": "Elige la palabra escrita correctamente.", "options": ["árbol", "arbol", "árból"], "answer": 0},
            {"prompt": "¿Qué palabra describe cómo corre alguien?", "options": ["Rápidamente", "Casa", "Ayer"], "answer": 0},
            {"prompt": "¿Cuál orden cuenta mejor una receta?", "options": ["Finalmente, primero, luego", "Primero, luego, finalmente", "Luego, finalmente, primero"], "answer": 1},
            {"prompt": "¿Para qué sirve la coma en una lista?", "options": ["Separar elementos", "Terminar siempre el texto", "Cambiar una palabra"], "answer": 0},
            {"prompt": "¿Cuál es un buen título para una historia de un viaje?", "options": ["Mi aventura en la montaña", "Palabra", "El"], "answer": 0}
        ]
    },

]


def _language_question(prompt, correct, wrong1, wrong2, index=0):
    """Construye una pregunta de Lengua con la respuesta en una posición variable."""
    options = [str(correct), str(wrong1), str(wrong2)]
    offset = index % 3
    if offset:
        options = options[-offset:] + options[:-offset]
    return {"prompt": prompt, "options": options, "answer": offset}


# La planificación curricular define para 2.º: lectura fluida y literal,
# párrafo narrativo con conectores, artículo/adjetivo/género/número y tilde en
# agudas, además de fábulas, leyendas y recitado. Estos contenidos son
# específicos del grado para no mostrar a 2.º las actividades genéricas de
# 1.º que tenía el catálogo anterior.
LANGUAGE_GRADE_CONTENT = {
    "reading-story": {
        "title": "Leemos con fluidez y comprendemos",
        "description": "Lee un relato breve con fluidez, identifica información literal y ordena sus acontecimientos.",
        "objective": "Leer con fluidez y practicar la comprensión literal de un texto narrativo.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "lesson": [
            "Lee en voz alta por grupos de palabras, sin detenerte en cada sílaba. Respeta los puntos y las comas para que el texto suene claro.",
            "La comprensión literal consiste en encontrar información que aparece directamente: personajes, lugar, acciones y momentos.",
            "Después de leer, vuelve al texto para comprobar tus respuestas. Ordenar los hechos ayuda a contar la historia con precisión.",
            "Para resumir, menciona quién participa, qué sucede primero, qué ocurre después y cómo termina.",
        ],
        "passage": "El sábado, Julia llevó una caja de cartón a la escuela. Con sus compañeros construyó un comedero para los pájaros del patio. Primero hicieron agujeros en los lados; después colocaron una cuerda y llenaron la caja con semillas. La maestra puso el comedero bajo un árbol. Al día siguiente, Julia observó dos gorriones y anotó lo que vio en su cuaderno.",
        "passage_by_grade": {
            "early": "El sábado, Julia llevó una caja de cartón a la escuela. Con sus compañeros construyó un comedero para los pájaros. Primero hicieron agujeros, después pusieron una cuerda y semillas. Al día siguiente, Julia vio dos gorriones y lo anotó en su cuaderno.",
            "middle": "El sábado, Julia llevó una caja de cartón a la escuela. Con sus compañeros construyó un comedero para los pájaros del patio. Primero hicieron agujeros en los lados; después colocaron una cuerda y llenaron la caja con semillas. La maestra puso el comedero bajo un árbol. Al día siguiente, Julia observó dos gorriones y anotó lo que vio en su cuaderno.",
            "upper": "El sábado, Julia llevó una caja de cartón a la escuela y, con sus compañeros, construyó un comedero para los pájaros del patio. Después de hacer los agujeros, colocaron una cuerda y semillas. La maestra lo puso bajo un árbol. Al día siguiente, Julia observó dos gorriones y registró sus observaciones en un cuaderno.",
        },
        "questions": [
            _language_question("¿Qué llevó Julia a la escuela?", "Una caja de cartón", "Una bolsa de libros", "Una maceta", 0),
            _language_question("¿Con quién construyó el comedero?", "Con sus compañeros", "Con su abuela", "Con un vecino", 1),
            _language_question("¿Para quién era el comedero?", "Para los pájaros", "Para los peces", "Para los conejos", 2),
            _language_question("¿Qué hicieron primero?", "Hicieron agujeros en los lados", "Llenaron la caja con semillas", "Observaron dos gorriones", 0),
            _language_question("¿Qué colocaron después?", "Una cuerda", "Una ventana", "Una bandera", 1),
            _language_question("¿Dónde puso la maestra el comedero?", "Bajo un árbol", "En la biblioteca", "Sobre una mesa", 2),
            _language_question("¿Qué pusieron dentro de la caja?", "Semillas", "Agua", "Piedras", 0),
            _language_question("¿Qué observó Julia al día siguiente?", "Dos gorriones", "Tres mariposas", "Un gato", 1),
            _language_question("¿Dónde anotó Julia lo que vio?", "En su cuaderno", "En una cartelera", "En una carta", 2),
            _language_question("¿Cuál es el orden correcto?", "Construir, colocar y observar", "Observar, construir y guardar", "Guardar, observar y construir", 0),
        ],
    },
    "words-syllables": {
        "title": "Leemos y escribimos palabras agudas",
        "description": "Mejora tu fluidez, reconoce la sílaba tónica y aplica la tilde en palabras agudas.",
        "objective": "Leer palabras con seguridad y usar la tilde en palabras agudas frecuentes.",
        "learning_order": 4,
        "learning_phase": "Practicar",
        "lesson": [
            "Lee las palabras completas y marca con la voz la sílaba que suena más fuerte.",
            "Las palabras agudas tienen la fuerza en la última sílaba: papel, canción y reloj.",
            "Las agudas llevan tilde cuando terminan en vocal, n o s: café, camión y compás.",
            "Separa las palabras en sílabas para leerlas con fluidez y revisa la tilde antes de escribir.",
        ],
        "questions": [
            _language_question("¿Cuál palabra es aguda?", "canción", "árbol", "lápiz", 0),
            _language_question("¿Dónde está la sílaba tónica de papel?", "pel", "pa", "pe", 1),
            _language_question("¿Cuál palabra aguda lleva tilde?", "café", "pared", "reloj", 2),
            _language_question("¿Por qué camión lleva tilde?", "Porque es aguda y termina en n", "Porque tiene tres sílabas", "Porque empieza con c", 0),
            _language_question("¿Cómo se separa canción?", "can-ción", "ca-nció-n", "canc-ión", 1),
            _language_question("¿Cuál palabra está escrita correctamente?", "compás", "compas", "cómpas", 2),
            _language_question("¿Cuál palabra no necesita tilde?", "papel", "sofá", "también", 0),
            _language_question("¿Qué palabra rima con canción?", "balón", "mesa", "árbol", 1),
            _language_question("¿Cuántas sílabas tiene teléfono?", "cuatro", "dos", "tres", 2),
            _language_question("¿Qué debes hacer para leer con fluidez?", "Leer respetando pausas y grupos de palabras", "Leer cada letra por separado siempre", "Ignorar los signos", 0),
        ],
    },
    "language-write-create": {
        "title": "Escribimos un párrafo narrativo",
        "description": "Organiza un párrafo con inicio, desarrollo y final usando conectores.",
        "objective": "Escribir y ordenar un párrafo narrativo breve con primero, luego, después y finalmente.",
        "learning_order": 2,
        "learning_phase": "Construir",
        "lesson": [
            "Un párrafo narrativo cuenta un hecho relacionado. Debe tener una idea principal y varias oraciones que la desarrollan.",
            "Usa conectores para ordenar: primero indica el inicio, luego o después continúan los hechos y finalmente presenta el cierre.",
            "Cada oración comienza con mayúscula y termina con punto. Lee el párrafo completo para comprobar que las ideas se entienden.",
            "Antes de escribir, piensa quién participa, dónde ocurre y qué sucede en cada momento.",
        ],
        "questions": [
            _language_question("¿Qué conector presenta el inicio?", "Primero", "Finalmente", "Aunque", 0),
            _language_question("¿Qué conector indica que algo ocurre después?", "Luego", "Porque", "Nunca", 1),
            _language_question("¿Qué conector cierra una narración?", "Finalmente", "Primero", "Mientras", 2),
            _language_question("¿Cuál oración puede iniciar un párrafo?", "Primero, Ana encontró una semilla.", "Finalmente, y.", "Porque la semilla.", 0),
            _language_question("Ordena: 1 sembró, 2 regó, 3 brotó.", "Primero sembró, luego regó y finalmente brotó.", "Finalmente sembró y primero brotó.", "Luego brotó, finalmente regó y primero sembró.", 1),
            _language_question("¿Qué elemento ayuda a saber de quién trata el párrafo?", "El personaje", "La coma solamente", "El número de páginas", 2),
            _language_question("¿Cuál oración está bien escrita?", "Después, Luis volvió a casa.", "después, Luis volvió a casa", "Después Luis volvió a casa", 0),
            _language_question("¿Qué signo termina una oración narrativa?", "El punto", "La coma", "El guion", 1),
            _language_question("¿Cuál grupo forma un párrafo coherente?", "Llegó la lluvia. Primero guardamos los libros y luego cerramos la ventana.", "Ventana. porque y libro.", "Finalmente primero la lluvia.", 2),
            _language_question("¿Qué conviene hacer antes de entregar el texto?", "Leerlo y revisar el orden de las ideas", "Borrar todos los puntos", "Escribir sin volver a leer", 0),
        ],
    },
    "language-vocabulary": {
        "title": "Sinónimos y antónimos",
        "description": "Amplía tu vocabulario y distingue palabras parecidas u opuestas dentro de una oración.",
        "objective": "Reconocer sinónimos y antónimos usando el significado y el contexto.",
        "learning_order": 5,
        "learning_phase": "Aplicar",
    },
    "language-grammar": {
        "title": "Artículos, adjetivos y concordancia",
        "description": "Identifica artículos y adjetivos, y haz concordar género y número al escribir.",
        "objective": "Usar artículos, adjetivos y palabras agudas con concordancia correcta.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
    },
    "language-adventure": {
        "title": "Fábulas, leyendas y recitado",
        "description": "Reconoce las características de fábulas y leyendas y practica un recitado claro.",
        "objective": "Distinguir fábulas y leyendas, identificar su enseñanza y leer con entonación.",
        "learning_order": 6,
        "learning_phase": "Aplicar",
    },
}


# Adaptación específica de 3.º según el plan curricular: comprender
# inferencias, escribir una narración de tres párrafos con diálogo, analizar
# sujeto/predicado y acercarse a mitos y novelas gráficas. Se mantiene
# separada de la adaptación de 2.º para que cada grado conserve su progresión.
THIRD_GRADE_LANGUAGE_CONTENT = {
    "reading-story": {
        "title": "Inferimos y encontramos la idea principal",
        "description": "Lee una historia, relaciona pistas y explica su idea principal con evidencias.",
        "objective": "Comprender información explícita e inferida y resumir la idea principal.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "lesson": [
            "Comprender un relato significa recuperar lo que dice y relacionar las pistas que ofrece.",
            "Una inferencia es una conclusión que construyes con varias pistas del texto. No es inventar: debe poder demostrarse.",
            "La idea principal resume lo más importante del texto; los detalles la explican o la apoyan.",
            "Para resumir, menciona el personaje, la situación, las acciones principales y el desenlace sin agregar información nueva.",
        ],
        "passage": "El viernes, Inés llegó temprano a la biblioteca del barrio. Sobre una mesa encontró un cuaderno con una etiqueta que decía: «Ideas para mejorar el parque». En sus páginas había dibujos de un banco, una papelera y un jardín de mariposas.\n\nInés leyó las propuestas y notó que varias personas habían escrito sus nombres al lado de una tarea. Sin embargo, la página del jardín estaba en blanco. Entonces dibujó unas plantas nativas y escribió: «Podemos sembrarlas y cuidarlas entre todos».\n\nLa semana siguiente, Inés llevó el cuaderno a la reunión vecinal. Los vecinos eligieron un lugar soleado, repartieron responsabilidades y comenzaron a trabajar. Al terminar la jornada, el cuaderno ya no estaba lleno solo de ideas: tenía un plan compartido.",
        "questions": [
            _language_question("¿Dónde encontró Inés el cuaderno?", "En la biblioteca del barrio", "En su salón", "En una tienda", 0),
            _language_question("¿Qué ideas aparecían dibujadas?", "Un banco, una papelera y un jardín", "Una cancha y una piscina", "Una casa y un puente", 1),
            _language_question("¿Por qué Inés escribió una propuesta para el jardín?", "Porque esa página estaba vacía y quería aportar", "Porque no le gustaban los bancos", "Porque quería llevarse el cuaderno", 2),
            _language_question("¿Qué se puede inferir de los nombres junto a las tareas?", "Que varias personas querían colaborar", "Que nadie conocía el parque", "Que las tareas ya estaban terminadas", 0),
            _language_question("¿Qué significa que el cuaderno tenía un plan compartido?", "Que los vecinos acordaron cómo trabajar juntos", "Que el cuaderno se repartió entre los vecinos", "Que Inés escribió todas las ideas", 1),
            _language_question("¿Cuál es la idea principal del relato?", "Una comunidad convierte ideas en un proyecto para mejorar el parque", "Una niña perdió un cuaderno en la biblioteca", "Los jardines solo necesitan dibujos", 2),
            _language_question("¿Qué ocurrió primero?", "Inés encontró el cuaderno", "Los vecinos eligieron un lugar", "Comenzaron a sembrar", 0),
            _language_question("¿Qué característica demuestra Inés con sus acciones?", "Iniciativa", "Descuido", "Impaciencia", 1),
            _language_question("¿Qué detalle apoya la idea de colaboración?", "Los vecinos repartieron responsabilidades", "La biblioteca abrió temprano", "El cuaderno tenía una etiqueta", 2),
            _language_question("¿Cuál es el mejor resumen?", "Inés propone cuidar un jardín y los vecinos organizan un proyecto común", "Inés dibuja un parque y guarda el cuaderno", "Los vecinos visitan una biblioteca para buscar dibujos", 0),
        ],
    },
    "language-write-create": {
        "title": "Escribimos una narración en tres párrafos",
        "description": "Planifica una historia con inicio, desarrollo, desenlace y un diálogo breve.",
        "objective": "Escribir una narración de tres párrafos con secuencia, personajes, diálogo y revisión.",
        "learning_order": 2,
        "learning_phase": "Construir",
        "lesson": [
            "Una narración de tres párrafos puede organizarse así: inicio (personajes y lugar), desarrollo (problema o acontecimiento) y desenlace (solución o cierre).",
            "El diálogo muestra lo que dicen los personajes. En un texto breve puedes introducirlo con dos puntos y marcar cada intervención con raya.",
            "Usa conectores como primero, mientras, después, entonces y finalmente para que el lector siga la secuencia.",
            "Revisa tu borrador: cada párrafo debe aportar una idea, las oraciones deben concordar y el final debe relacionarse con el problema.",
        ],
        "questions": [
            _language_question("¿Qué presenta normalmente el primer párrafo?", "Los personajes, el lugar y la situación inicial", "La solución de todos los problemas", "Una lista de palabras", 0),
            _language_question("¿Qué desarrolla el segundo párrafo?", "El problema o los acontecimientos principales", "Solo el título", "La despedida del lector", 1),
            _language_question("¿Qué debe mostrar el tercer párrafo?", "El desenlace o cierre", "El nombre del autor únicamente", "Un nuevo problema sin relación", 2),
            _language_question("¿Cuál oración introduce un diálogo correctamente?", "Marta dijo: —Podemos intentarlo.", "Marta dijo podemos intentarlo", "Marta: dijo —podemos intentarlo.", 0),
            _language_question("¿Qué conector indica que una acción ocurre después?", "Entonces", "Aunque", "Nunca", 1),
            _language_question("¿Cuál secuencia forma una narración coherente?", "Encontró la llave, abrió la puerta y entró.", "Entró, encontró la llave y abrió la puerta.", "Abrió la puerta, entró y buscó una puerta.", 2),
            _language_question("¿Qué elemento ayuda a que el problema tenga solución?", "Las acciones de los personajes", "Un título muy largo", "Repetir el inicio", 0),
            _language_question("¿Cuál oración mantiene el pasado?", "Lucía caminó y encontró una carta.", "Lucía camina y encontró una carta.", "Lucía caminará y encontró una carta.", 1),
            _language_question("¿Qué conviene hacer al revisar el borrador?", "Comprobar orden, diálogo, mayúsculas y puntos", "Eliminar todos los párrafos", "Cambiar cada palabra por un dibujo", 2),
            _language_question("¿Cuál título anuncia mejor una narración sobre una llave perdida?", "La llave del jardín", "Palabras sueltas", "El", 0),
        ],
    },
    "words-syllables": {
        "title": "Sujeto, predicado y tiempos verbales",
        "description": "Reconoce quién realiza la acción, qué se dice de esa persona y cuándo ocurre.",
        "objective": "Identificar sujeto y predicado, y reconocer verbos en presente, pasado y futuro.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "lesson": [
            "El sujeto indica de quién se habla. El predicado expresa qué hace, qué siente o qué le ocurre.",
            "Para encontrar el sujeto, pregunta quién realiza la acción. El verbo suele ser la palabra central del predicado.",
            "El verbo cambia según el tiempo: presente (hoy canta), pasado (ayer cantó) y futuro (mañana cantará).",
            "Lee la oración completa antes de responder y comprueba que sujeto, verbo y complementos tengan sentido juntos.",
        ],
        "questions": [
            _language_question("En «El equipo prepara una exposición», ¿cuál es el sujeto?", "El equipo", "prepara", "una exposición", 0),
            _language_question("En «Las abejas construyen su colmena», el predicado es…", "construyen su colmena", "Las abejas", "abejas", 1),
            _language_question("¿Cuál verbo está en pasado?", "leyeron", "leen", "leerán", 2),
            _language_question("Completa: Mañana Sofía ___ una carta.", "escribirá", "escribió ayer", "escribe ayer", 0),
            _language_question("¿Cuál oración tiene sujeto y predicado?", "El río atraviesa el valle.", "Por la mañana.", "Aunque llueva.", 1),
            _language_question("En «Mi hermano y yo visitamos el museo», el sujeto es…", "Mi hermano y yo", "visitamos", "el museo", 2),
            _language_question("¿En qué tiempo está «juegan»?", "Presente", "Pasado", "Futuro", 0),
            _language_question("¿Cuál oración está en futuro?", "Los niños leerán el cuento.", "Los niños leyeron el cuento.", "Los niños leen el cuento.", 1),
            _language_question("¿Qué pregunta ayuda a localizar el sujeto?", "¿Quién realiza la acción?", "¿Cuántas letras tiene?", "¿Dónde está el título?", 2),
            _language_question("¿Cuál oración concuerda correctamente?", "Las exploradoras encontraron una pista.", "Las exploradoras encontró una pista.", "La exploradoras encontraron una pista.", 0),
        ],
    },
    "language-adventure": {
        "title": "Mitos, novela gráfica y club de lectura",
        "description": "Reconoce rasgos de mitos y novelas gráficas y comparte interpretaciones de una lectura.",
        "objective": "Distinguir mitos y novelas gráficas, interpretar sus recursos y conversar sobre lo leído.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "lesson": [
            "Un mito es un relato tradicional que explica un origen o un fenómeno mediante personajes y hechos extraordinarios.",
            "La novela gráfica cuenta una historia con viñetas, imágenes, globos de diálogo y cartelas que orientan la lectura.",
            "En un club de lectura escuchamos interpretaciones, damos opiniones y las apoyamos con detalles del texto o de las imágenes.",
            "Distingue lo que el texto muestra de lo que tú infieres y respeta las ideas de quienes leen de otra manera.",
        ],
        "questions": [
            _language_question("¿Qué suele explicar un mito?", "El origen de un fenómeno o una tradición", "El precio de un producto", "Las reglas de un deporte", 0),
            _language_question("¿Qué elemento es propio de una novela gráfica?", "Las viñetas", "Las tablas de multiplicar", "Las recetas", 1),
            _language_question("¿Para qué sirve un globo de diálogo?", "Para mostrar lo que dice un personaje", "Para indicar el número de páginas", "Para describir el clima real", 2),
            _language_question("¿Qué es una cartela?", "Un recuadro con información del narrador o del tiempo", "El nombre de una viñeta", "Un dibujo sin relación", 0),
            _language_question("¿Qué actitud favorece un club de lectura?", "Escuchar y justificar las opiniones", "Interrumpir siempre", "Decir que solo existe una interpretación", 1),
            _language_question("¿Cuál situación podría aparecer en un mito?", "Un río que nace de la lágrima de una diosa", "Una lista de materiales escolares", "Un horario de clases", 2),
            _language_question("¿Cómo se organiza una novela gráfica?", "En imágenes secuenciadas que cuentan acciones", "En números sin orden", "En palabras aisladas sin personajes", 0),
            _language_question("¿Cuál comentario está apoyado en una evidencia?", "La heroína es valiente porque ayuda a su pueblo.", "Es el mejor relato porque sí.", "El final es azul aunque no aparece.", 1),
            _language_question("¿Qué diferencia hay entre un mito y una noticia?", "El mito es tradicional y puede incluir hechos extraordinarios; la noticia informa hechos", "La noticia siempre tiene viñetas", "El mito solo presenta datos comprobables", 2),
            _language_question("¿Qué conviene hacer al recomendar una lectura?", "Mencionar qué te gustó y explicar por qué", "Contar un final inventado", "No decir nada sobre el texto", 0),
        ],
    },
    "language-vocabulary": {
        "title": "Familias léxicas y palabras relacionadas",
        "description": "Descubre palabras que comparten raíz y organiza vocabulario por significado.",
        "objective": "Reconocer familias léxicas y usar relaciones de significado para comprender palabras nuevas.",
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "lesson": [
            "Una familia léxica reúne palabras que comparten una raíz y se relacionan por su significado: pan, panadero y panadería.",
            "No basta con que dos palabras empiecen igual; comprueba si conservan una parte de significado común.",
            "Los prefijos se colocan delante de una palabra y pueden cambiar su significado: re-leer significa leer otra vez.",
            "Usa el contexto y la raíz para deducir el significado de palabras desconocidas.",
        ],
        "questions": [
            _language_question("¿Cuál palabra pertenece a la familia de mar?", "marino", "mariposa", "martes", 0),
            _language_question("¿Cuál palabra pertenece a la familia de flor?", "florista", "flota", "flauta", 1),
            _language_question("¿Qué palabra comparte raíz con pan?", "panadería", "pantalón", "pantalla", 2),
            _language_question("¿Qué indica el prefijo re- en releer?", "Repetir la acción", "Negar la acción", "Hacer la acción antes", 0),
            _language_question("¿Cuál grupo pertenece al campo semántico de la escuela?", "cuaderno, aula y recreo", "río, montaña y nube", "tenedor, plato y sartén", 1),
            _language_question("¿Cuál palabra no pertenece a la familia de zapato?", "zapatero", "zapatilla", "zapallo", 2),
            _language_question("¿Qué palabra tiene la misma raíz que útil?", "utilidad", "último", "unidad", 0),
            _language_question("En «reconstruir», re- significa…", "volver a construir", "construir por primera vez", "dejar de construir", 1),
            _language_question("¿Qué estrategia ayuda a comprender «submarino»?", "Relacionar sub- con debajo y mar con el lugar", "Separarla en letras al azar", "Ignorar el contexto", 2),
            _language_question("¿Cuál pareja pertenece a la misma familia léxica?", "nación / nacional", "casa / camino", "sol / silla", 0),
        ],
    },
    "language-grammar": {
        "title": "Detectives del sujeto, predicado y prefijos",
        "description": "Analiza oraciones y reconoce cómo los prefijos forman palabras nuevas.",
        "objective": "Identificar sujeto y predicado, reconocer tiempos verbales y comprender prefijos frecuentes.",
        "learning_order": 6,
        "learning_phase": "Consolidar",
        "lesson": [
            "Para analizar una oración, localiza primero el verbo; luego pregunta quién realiza la acción para encontrar el sujeto.",
            "El predicado incluye el verbo y la información que se dice del sujeto. Puede tener más de una palabra.",
            "Los prefijos se unen a una palabra para formar otra: des- puede indicar negación o inversión y re- repetición.",
            "Comprueba tus respuestas leyendo la oración completa y observando si la nueva palabra conserva sentido.",
        ],
        "questions": [
            _language_question("En «La científica observa el cielo», el predicado es…", "observa el cielo", "La científica", "científica", 0),
            _language_question("¿Cuál es el sujeto de «Mis amigos prepararán la obra»?", "Mis amigos", "prepararán", "la obra", 1),
            _language_question("¿Qué expresa el prefijo des- en desordenar?", "Quitar o invertir el orden", "Repetir el orden", "Ordenar por primera vez", 2),
            _language_question("¿Qué palabra significa volver a leer?", "releer", "desleer", "leerán", 0),
            _language_question("¿Cuál verbo está en presente?", "observa", "observó", "observará", 1),
            _language_question("¿Qué oración tiene sujeto plural?", "Los músicos ensayan.", "El músico ensaya.", "Ensaya con cuidado.", 2),
            _language_question("En «El tren llegó temprano», ¿qué palabra es el verbo?", "llegó", "tren", "temprano", 0),
            _language_question("Completa: Ayer nosotros ___ el museo.", "visitamos", "visitaremos", "visitamos mañana", 1),
            _language_question("¿Cuál palabra tiene un prefijo?", "invisible", "ventana", "camino", 2),
            _language_question("¿Cuál análisis es correcto para «Las niñas cantan»?", "Sujeto: Las niñas; predicado: cantan", "Sujeto: cantan; predicado: Las niñas", "Sujeto: niñas; no hay predicado", 0),
        ],
    },
}


FOURTH_GRADE_LANGUAGE_CONTENT = {
    "reading-story": {
        "title": "Analizamos personajes y ambientes",
        "description": "Interpreta cómo el personaje y el ambiente —lugar y tiempo— construyen el sentido de un relato.",
        "objective": "Analizar personajes y ambientes, relacionar sus características y justificar interpretaciones.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "lesson": [
            "El personaje se conoce por lo que dice, piensa y hace. También puedes inferir sus características a partir de sus decisiones.",
            "El ambiente incluye el lugar, el tiempo y la atmósfera. Una noche silenciosa puede crear misterio; una plaza llena puede transmitir actividad.",
            "Observa cómo el ambiente influye en el conflicto y en las acciones de los personajes.",
            "Para justificar una interpretación, formula una idea y apóyala con una frase o un detalle del relato.",
        ],
        "passage": "Cuando comenzó a oscurecer, Amalia llegó al antiguo observatorio de la colina. El viento movía las ramas y las nubes cubrían la luna, pero desde la cúpula se veía una línea de luces en el valle.\n\nSu abuelo le había pedido recuperar el cuaderno de observaciones antes de la tormenta. Amalia sintió miedo al escuchar un golpe en la escalera, aunque decidió continuar porque sabía que el cuaderno guardaba los registros de varias generaciones. Encontró una ventana abierta y la cerró para proteger los mapas.\n\nAl salir, la lluvia empezó a caer. Amalia bajó abrazando el cuaderno y comprendió que no había vencido el miedo por ignorarlo, sino por actuar con cuidado a pesar de sentirlo.",
        "questions": [
            _language_question("¿Dónde ocurre principalmente el relato?", "En un observatorio de la colina", "En una estación de tren", "En una plaza del valle", 0),
            _language_question("¿Qué ambiente se describe al inicio?", "Oscuro, ventoso y con nubes", "Soleado y silencioso", "Caluroso y lleno de personas", 1),
            _language_question("¿Por qué Amalia fue al observatorio?", "Para recuperar el cuaderno de observaciones", "Para mirar las luces del valle", "Para visitar a sus amigos", 2),
            _language_question("¿Qué se puede inferir de que Amalia cerrara la ventana?", "Que cuida los mapas y actúa con responsabilidad", "Que quería esconderse de su abuelo", "Que no le interesaban las observaciones", 0),
            _language_question("¿Qué conflicto enfrenta Amalia?", "Debe completar una tarea aunque siente miedo y se acerca una tormenta", "No encuentra el camino al valle", "Quiere aprender a mover las nubes", 1),
            _language_question("¿Cuál es la característica principal de Amalia?", "Valiente y cuidadosa", "Descuidada y distraída", "Egoísta y agresiva", 2),
            _language_question("¿Qué detalle muestra que el observatorio es antiguo?", "El cuaderno reúne registros de varias generaciones", "La lluvia comenzó al salir", "Se veían luces en el valle", 0),
            _language_question("¿Cómo influye el ambiente en la historia?", "La oscuridad y la tormenta aumentan la tensión", "La luz del valle resuelve el problema", "El viento impide que exista un conflicto", 1),
            _language_question("¿Qué significa que actuó a pesar del miedo?", "Que reconoció el miedo y siguió con cuidado", "Que nunca sintió miedo", "Que ignoró todos los peligros", 2),
            _language_question("¿Cuál es la mejor síntesis?", "Amalia enfrenta una noche difícil, protege un cuaderno valioso y descubre que la valentía también implica actuar con cuidado.", "Amalia visita un observatorio para contemplar las luces del valle.", "Una tormenta destruye los mapas de un observatorio antiguo.", 0),
        ],
    },
    "language-write-create": {
        "title": "Escribimos textos expositivos y hacemos síntesis",
        "description": "Organiza información, explica un tema y resume sus ideas principales con claridad.",
        "objective": "Planificar un texto expositivo y elaborar una síntesis objetiva con ideas relacionadas.",
        "learning_order": 2,
        "learning_phase": "Construir",
        "lesson": [
            "Un texto expositivo explica un tema. Su propósito principal es informar, no contar una historia inventada ni convencer con opiniones.",
            "Organízalo en introducción, desarrollo y cierre. Presenta el tema, explica sus aspectos importantes y retoma lo esencial.",
            "Usa definiciones, ejemplos y conectores como además, por eso, sin embargo y finalmente para relacionar la información.",
            "Una síntesis conserva las ideas principales con palabras propias y elimina repeticiones, detalles secundarios y opiniones que no aparecen en la fuente.",
        ],
        "questions": [
            _language_question("¿Cuál es el propósito de un texto expositivo?", "Informar y explicar un tema", "Crear suspenso con personajes", "Expresar solo una opinión", 0),
            _language_question("¿Qué presenta la introducción?", "El tema que se va a explicar", "Todos los detalles finales", "Una lista sin relación", 1),
            _language_question("¿Qué suele incluir el desarrollo?", "Datos, explicaciones y ejemplos", "Solo el título", "La firma del lector", 2),
            _language_question("¿Qué debe conservar una síntesis?", "Las ideas principales", "Cada palabra de la fuente", "Detalles repetidos", 0),
            _language_question("¿Qué conector agrega información?", "Además", "Sin embargo", "Por eso", 1),
            _language_question("¿Cuál oración es más apropiada para informar?", "El agua cambia de estado cuando recibe o pierde calor.", "El agua es la cosa más maravillosa del mundo.", "¡Qué aburrido es estudiar el agua!", 2),
            _language_question("¿Qué conviene hacer antes de redactar?", "Seleccionar el tema y ordenar las ideas", "Copiar frases sin comprender", "Escribir el cierre primero sin propósito", 0),
            _language_question("¿Qué recurso ayuda a explicar un concepto?", "Una definición o un ejemplo", "Una palabra repetida muchas veces", "Un dato inventado", 1),
            _language_question("¿Qué información debe eliminarse de una síntesis?", "Repeticiones y detalles secundarios", "La idea principal", "La relación entre las ideas", 2),
            _language_question("¿Qué revisión mejora un texto expositivo?", "Comprobar claridad, orden, conectores y datos", "Agregar opiniones a cada oración", "Quitar todos los títulos", 0),
        ],
    },
    "words-syllables": {
        "title": "Oraciones compuestas y puntuación",
        "description": "Une ideas con sentido y utiliza la puntuación para escribir textos claros.",
        "objective": "Reconocer oraciones compuestas, usar conectores y aplicar coma, punto y dos puntos.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "lesson": [
            "Una oración compuesta reúne dos o más ideas relacionadas, generalmente con más de un verbo: «Leo y tomo notas».",
            "Los conectores expresan relaciones: y suma, pero contraste, porque causa, por eso consecuencia.",
            "La coma separa elementos de una lista y puede marcar una pausa; no se escribe entre el sujeto y el predicado.",
            "La puntuación organiza el texto: el punto cierra una idea completa y los dos puntos pueden introducir una enumeración o una explicación.",
        ],
        "questions": [
            _language_question("¿Cuál es una oración compuesta?", "Leo el texto y subrayo las ideas principales.", "El texto interesante.", "En la biblioteca.", 0),
            _language_question("¿Qué conector expresa contraste?", "Pero", "Y", "Porque", 1),
            _language_question("Completa: No salimos ___ estaba lloviendo.", "porque", "pero", "y", 2),
            _language_question("¿Cuál oración usa correctamente la coma en una lista?", "Llevé lápiz, regla y colores.", "Llevé, lápiz regla y colores.", "Llevé lápiz regla, y colores.", 0),
            _language_question("¿Qué signo puede introducir una lista?", "Los dos puntos", "El punto y coma siempre", "El signo de interrogación", 1),
            _language_question("¿Cuál oración no separa sujeto y predicado con una coma?", "Las niñas de cuarto prepararon la exposición.", "Las niñas de cuarto, prepararon la exposición.", "Las niñas, de cuarto prepararon la exposición.", 2),
            _language_question("¿Qué relación expresa «por eso»?", "Consecuencia", "Contraste", "Duda", 0),
            _language_question("¿Cuál grupo tiene dos ideas unidas correctamente?", "Terminó la clase y guardamos los materiales.", "Terminó la clase y.", "Porque guardamos los materiales.", 1),
            _language_question("¿Qué signo termina una oración declarativa?", "El punto", "La coma", "Los dos puntos", 2),
            _language_question("¿Cuál oración está puntuada correctamente?", "El experimento terminó; por eso, anotamos los resultados.", "El experimento, terminó por eso anotamos los resultados.", "El experimento terminó por eso, anotamos los resultados", 0),
        ],
    },
    "language-adventure": {
        "title": "Géneros, retórica y teatro leído",
        "description": "Reconoce recursos de distintos géneros y participa en una lectura teatral expresiva.",
        "objective": "Distinguir géneros literarios, identificar recursos retóricos y leer teatro con intención.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "lesson": [
            "Los géneros literarios organizan las obras según su forma y propósito: narrativo, lírico y dramático.",
            "La comparación relaciona dos elementos usando como o parece; la personificación atribuye acciones humanas a seres no humanos.",
            "El teatro presenta personajes, parlamentos y acotaciones. Las acotaciones orientan movimientos, tono y ambiente.",
            "En el teatro leído, la voz, el ritmo y las pausas ayudan a que el público comprenda las emociones y las acciones.",
        ],
        "questions": [
            _language_question("¿Qué género cuenta hechos con personajes y narrador?", "El narrativo", "El lírico", "El dramático únicamente", 0),
            _language_question("¿Qué género expresa emociones con ritmo o versos?", "El lírico", "El informativo", "El instructivo", 1),
            _language_question("¿Qué elemento es propio del teatro?", "Los parlamentos y las acotaciones", "La tabla de datos", "La bibliografía científica", 2),
            _language_question("¿Qué es una acotación?", "Una indicación sobre acciones, tono o escenario", "El título de la obra", "Una opinión del público", 0),
            _language_question("¿Cuál expresión contiene una comparación?", "La luna brilla como una moneda.", "La luna apareció.", "La luna es un satélite.", 1),
            _language_question("¿Cuál ejemplo tiene personificación?", "El viento susurró entre los árboles.", "El viento sopló a diez kilómetros por hora.", "El viento es aire en movimiento.", 2),
            _language_question("¿Qué ayuda a una lectura teatral?", "Cambiar la voz según el personaje y respetar las pausas", "Leer todas las líneas con el mismo tono", "Ignorar las acotaciones", 0),
            _language_question("¿Qué información aparece en un parlamento?", "Lo que dice un personaje", "El número de páginas", "La fecha de publicación solamente", 1),
            _language_question("¿Qué recurso retórico exagera una característica?", "La hipérbole", "La definición", "La enumeración alfabética", 2),
            _language_question("¿Qué conviene hacer después de leer una obra?", "Comentar el género y apoyar la interpretación con ejemplos", "Cambiar el final sin explicar", "Memorizar palabras aisladas", 0),
        ],
    },
    "language-vocabulary": {
        "title": "Polisemia y significado en contexto",
        "description": "Distingue los sentidos de una palabra y usa el contexto para interpretar mensajes.",
        "objective": "Reconocer palabras polisémicas y seleccionar su significado según el contexto.",
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "lesson": [
            "Una palabra polisémica tiene varios significados relacionados. El contexto indica cuál corresponde en cada oración.",
            "Compara las palabras que acompañan al término y la situación en que aparece antes de elegir un significado.",
            "Los diccionarios ofrecen varias acepciones; la acepción adecuada depende del uso concreto.",
            "Explicar una palabra con tus propias palabras y crear un ejemplo demuestra que comprendiste su sentido.",
        ],
        "questions": [
            _language_question("En «Me senté en el banco», banco significa…", "Un asiento", "Una entidad financiera", "Un grupo de peces", 0),
            _language_question("En «El banco aprobó el préstamo», banco significa…", "Una entidad financiera", "Un asiento", "Una mesa escolar", 1),
            _language_question("En «La copa del árbol está llena de hojas», copa es…", "La parte superior del árbol", "Un vaso", "Un premio", 2),
            _language_question("En «Ganó la copa del torneo», copa es…", "Un trofeo", "Una rama", "Un recipiente para beber", 0),
            _language_question("¿Qué pista ayuda a elegir el significado de una palabra?", "Las palabras y la situación que la rodean", "Solo la primera letra", "El número de sílabas", 1),
            _language_question("En «El ratón se escondió», ratón se refiere a…", "El animal", "El dispositivo del computador", "Una herramienta", 2),
            _language_question("En «Mueve el ratón para abrir el archivo», ratón es…", "Un dispositivo del computador", "Un animal", "Una parte de una casa", 0),
            _language_question("¿Qué significa «claro» en «El cielo está claro»?", "Sin nubes", "Fácil de comprender", "Un tono de pintura", 1),
            _language_question("¿Qué estrategia confirma una acepción?", "Sustituirla por un significado y comprobar si la oración tiene sentido", "Elegir siempre la primera acepción", "Ignorar las palabras cercanas", 2),
            _language_question("¿Cuál par muestra una palabra con sentidos diferentes según el contexto?", "llave: abre una puerta / resuelve un problema", "mesa / silla", "rojo / azul", 0),
        ],
    },
    "language-grammar": {
        "title": "Conectores y cohesión textual",
        "description": "Relaciona oraciones con conectores y evita repeticiones para construir textos cohesionados.",
        "objective": "Usar conectores de causa, contraste, consecuencia y orden para enlazar ideas.",
        "learning_order": 6,
        "learning_phase": "Consolidar",
        "lesson": [
            "La cohesión hace que las oraciones de un texto se relacionen. Los conectores muestran cómo se conectan las ideas.",
            "Usa primero, después y finalmente para ordenar; porque y ya que para explicar causas; por eso para consecuencias.",
            "Sin embargo y pero introducen contraste. Escoge el conector que exprese la relación real entre las ideas.",
            "También puedes evitar repeticiones usando pronombres o palabras equivalentes, sin perder claridad.",
        ],
        "questions": [
            _language_question("¿Qué conector introduce una causa?", "Porque", "Sin embargo", "Finalmente", 0),
            _language_question("¿Qué conector expresa consecuencia?", "Por eso", "Aunque", "Primero", 1),
            _language_question("Completa: Estudié mucho; ___, comprendí el tema.", "por eso", "sin embargo", "mientras", 2),
            _language_question("¿Qué conector ordena el inicio?", "Primero", "Aunque", "Por eso", 0),
            _language_question("¿Cuál oración expresa contraste?", "Quería salir, pero empezó a llover.", "Quería salir porque hacía sol.", "Primero salió y después volvió.", 1),
            _language_question("¿Qué palabra puede evitar repetir «Laura»?", "Ella", "Aquel", "Aquí", 2),
            _language_question("Completa: ___ terminamos la lectura, comentamos nuestras ideas.", "Después de que", "Sin embargo", "Por eso", 0),
            _language_question("¿Cuál grupo de oraciones es más cohesionado?", "Ana leyó el texto. Luego subrayó las ideas principales.", "Ana leyó el texto. Texto ideas libro.", "Ana texto y luego.", 1),
            _language_question("¿Qué relación expresa «aunque»?", "Contraste o dificultad", "Causa segura", "Orden temporal", 2),
            _language_question("¿Qué conviene revisar para mejorar la cohesión?", "Que los conectores y las referencias unan las ideas con claridad", "Que cada oración cambie de tema", "Que todas las palabras se repitan", 0),
        ],
    },
}


FIFTH_GRADE_LANGUAGE_CONTENT = {
    "reading-story": {
        "title": "Leemos críticamente: sesgos y fuentes",
        "description": "Contrasta fuentes, identifica sesgos y construye interpretaciones basadas en evidencias.",
        "objective": "Distinguir hechos, opiniones y sesgos, y valorar la confiabilidad de distintas fuentes.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "lesson": [
            "Leer críticamente significa comprender un texto y preguntarse quién lo escribió, para qué y con qué evidencias.",
            "Un hecho puede comprobarse; una opinión expresa una valoración. Un sesgo aparece cuando se presentan solo algunas perspectivas o se usan palabras que favorecen una postura.",
            "Para valorar una fuente revisa autoría, fecha, propósito, datos y coincidencias con otras fuentes confiables.",
            "Al resumir una información controvertida, diferencia lo que la fuente afirma de tus propias conclusiones.",
        ],
        "passage": "En la escuela, el comité ambiental investigó si convenía recuperar el humedal cercano. Un folleto de una empresa afirmaba: «El proyecto convertirá el lugar abandonado en el parque más moderno de la ciudad». No indicaba quién había realizado el estudio ni mostraba datos.\n\nEl grupo también consultó un informe de la universidad, firmado y fechado, que incluía mediciones del agua, mapas y entrevistas a los vecinos. El informe señalaba beneficios y dificultades: recuperar el humedal protegería aves y reduciría inundaciones, pero exigiría varios años de cuidado.\n\nDespués de comparar las fuentes, los estudiantes escribieron una propuesta. No repitieron que el proyecto sería «perfecto»; explicaron qué evidencias apoyaban la recuperación y qué preguntas debían responder antes de decidir.",
        "questions": [
            _language_question("¿Qué investigó el comité ambiental?", "Si convenía recuperar el humedal", "Cómo construir una empresa", "Qué aves migraban a otro país", 0),
            _language_question("¿Qué problema tenía el folleto de la empresa?", "Afirmaba mucho, pero no mostraba autor ni datos", "Tenía demasiados mapas y mediciones", "Presentaba varias perspectivas con fechas", 1),
            _language_question("¿Qué fuente ofrece más elementos para comprobar la información?", "El informe firmado y fechado de la universidad", "El folleto publicitario", "Un comentario sin autor", 2),
            _language_question("¿Qué posible sesgo tiene la frase «el parque más moderno»?", "Usa una valoración positiva y exagerada", "Presenta una medición exacta", "Explica una dificultad del proyecto", 0),
            _language_question("¿Qué beneficio aparece en el informe?", "Proteger aves y reducir inundaciones", "Construir el parque en un día", "Eliminar todas las dificultades", 1),
            _language_question("¿Qué dificultad reconoce el informe?", "El cuidado exigiría varios años", "No se pueden medir las inundaciones", "Los vecinos no fueron entrevistados", 2),
            _language_question("¿Qué actitud demostraron los estudiantes?", "Compararon fuentes antes de proponer una decisión", "Aceptaron la primera publicidad", "Rechazaron todos los datos", 0),
            _language_question("¿Cuál afirmación es un hecho verificable?", "El informe incluye mediciones del agua", "El proyecto será maravilloso", "El humedal es el lugar más bonito", 1),
            _language_question("¿Qué pregunta ayudaría a continuar la investigación?", "¿Quién financia y cómo se cuidará el humedal?", "¿Qué palabra suena más emocionante?", "¿Cómo hacer que el folleto parezca perfecto?", 2),
            _language_question("¿Cuál es la mejor síntesis?", "Los estudiantes comparan una publicidad y un informe para proponer recuperar el humedal con evidencias y reconocer sus retos.", "Una empresa promete construir un parque moderno junto a la escuela.", "El informe universitario demuestra que todos los proyectos ambientales son fáciles.", 0),
        ],
    },
    "language-write-create": {
        "title": "Escribimos un ensayo argumentativo",
        "description": "Presenta una tesis, desarrolla argumentos y utiliza citas para sostener una postura.",
        "objective": "Planificar un ensayo argumentativo con tesis, razones, evidencias, citas y conclusión.",
        "learning_order": 2,
        "learning_phase": "Construir",
        "lesson": [
            "Un ensayo argumentativo presenta una postura o tesis sobre un tema y busca sostenerla con razones y evidencias.",
            "Cada argumento debe explicar por qué apoya la tesis. Puedes usar datos, ejemplos o una cita breve de una fuente confiable.",
            "Las citas deben distinguirse de tus palabras y mencionar de dónde provienen. No presentes como propio lo que escribió otra persona.",
            "La conclusión retoma la tesis y muestra qué se puede deducir; no añade un argumento completamente nuevo.",
        ],
        "questions": [
            _language_question("¿Qué es la tesis de un ensayo?", "La postura principal que se defenderá", "El nombre de la fuente", "La lista de conectores", 0),
            _language_question("¿Qué función cumple un argumento?", "Explicar por qué la tesis es razonable", "Repetir el título sin explicar", "Cambiar de tema", 1),
            _language_question("¿Cuál es una evidencia?", "Un dato o ejemplo relacionado con la tesis", "Una opinión sin fundamento", "Una palabra llamativa", 2),
            _language_question("¿Para qué sirve una cita?", "Apoyar una idea con palabras de una fuente identificada", "Ocultar quién escribió la idea", "Reemplazar todo el ensayo", 0),
            _language_question("¿Qué conector introduce una razón?", "Porque", "Sin embargo", "Finalmente", 1),
            _language_question("¿Cuál tesis es clara?", "La escuela debería crear un huerto porque favorece el aprendizaje y el cuidado ambiental.", "El huerto y otras cosas.", "Me gusta mucho, muchísimo, el huerto.", 2),
            _language_question("¿Qué debe hacer una conclusión?", "Retomar la postura y las ideas más importantes", "Presentar un tema sin relación", "Copiar la introducción palabra por palabra", 0),
            _language_question("¿Cuál expresión introduce una cita?", "Según el informe de la universidad, «el humedal reduce inundaciones».", "El informe de la universidad y muchas palabras.", "Yo cito porque sí el humedal.", 1),
            _language_question("¿Qué conviene hacer antes de escribir?", "Investigar, definir la tesis y organizar los argumentos", "Elegir primero una conclusión sin tema", "Copiar una fuente completa", 2),
            _language_question("¿Qué revisión protege la honestidad del texto?", "Comprobar las fuentes y diferenciar citas de ideas propias", "Eliminar los nombres de los autores", "Presentar todos los datos como opiniones", 0),
        ],
    },
    "words-syllables": {
        "title": "Morfología, subordinación y registro",
        "description": "Analiza cómo se forman las palabras, relaciona oraciones y adapta el lenguaje a cada situación.",
        "objective": "Reconocer morfemas, oraciones subordinadas y diferencias entre registros formal e informal.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "lesson": [
            "La morfología estudia cómo se forman las palabras. La raíz aporta el significado principal y los prefijos o sufijos pueden modificarlo.",
            "Una oración subordinada depende de otra y cumple una función dentro de ella: «Me alegra que participes».",
            "El registro formal se usa en contextos académicos o institucionales; el informal es apropiado para conversaciones cercanas.",
            "Elige las palabras y la estructura según el destinatario, el propósito y la situación comunicativa.",
        ],
        "questions": [
            _language_question("¿Cuántas sílabas tiene «extraordinario»?", "Seis", "Cuatro", "Ocho", 0),
            _language_question("¿Qué palabra contiene un prefijo?", "deshacer", "mesa", "cantar", 1),
            _language_question("¿Cuál oración contiene una subordinada?", "Espero que llegues temprano.", "Llegué temprano.", "El camino largo.", 2),
            _language_question("En «Me alegra que participes», la parte subordinada es…", "que participes", "Me alegra", "alegra", 0),
            _language_question("¿Qué registro conviene en una carta dirigida a la rectoría?", "Formal", "Coloquial con muchos apodos", "Familiar", 1),
            _language_question("¿Cuál saludo es más formal?", "Estimada señora directora:", "¡Hola, parce!", "¿Qué más, amiga?", 2),
            _language_question("¿Qué expresa el sufijo -ero en panadero?", "Relación con una actividad u oficio", "Negación", "Repetición", 0),
            _language_question("¿Qué palabra introduce con frecuencia una causa subordinada?", "Aunque", "Porque", "Después", 1),
            _language_question("¿Cuál oración usa un registro académico adecuado?", "Los resultados indican una disminución de residuos.", "Los resultados están súper chéveres.", "Eso quedó rebueno, ¿sí o qué?", 2),
            _language_question("¿Qué debes considerar para elegir un registro?", "El destinatario, el propósito y la situación", "Solo la longitud de las palabras", "La cantidad de letras del título", 0),
        ],
    },
    "language-adventure": {
        "title": "Literatura universal y voz narrativa",
        "description": "Relaciona obras de distintas tradiciones y reconoce quién cuenta una historia y desde qué perspectiva.",
        "objective": "Reconocer rasgos de la literatura universal y analizar la voz narrativa y sus efectos.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "lesson": [
            "La literatura universal reúne obras de diferentes épocas y culturas que pueden dialogar con lectores de muchos lugares.",
            "El narrador en primera persona participa o recuerda los hechos; el narrador en tercera persona los cuenta desde fuera de la historia.",
            "La voz narrativa influye en la información que conocemos y en la cercanía que sentimos con los personajes.",
            "Comparar textos permite reconocer temas comunes y valorar distintas tradiciones sin borrar sus contextos culturales.",
        ],
        "questions": [
            _language_question("¿Qué se entiende por literatura universal?", "Obras de distintas culturas y épocas que pueden dialogar con lectores diversos", "Textos escritos en un solo país", "Una lista de autores actuales", 0),
            _language_question("¿Qué caracteriza al narrador en primera persona?", "Usa yo y participa o recuerda los hechos", "Solo describe datos científicos", "Nunca expresa lo que sabe", 1),
            _language_question("¿Qué pronombre suele identificar la tercera persona?", "Él o ella", "Yo", "Nosotros siempre", 2),
            _language_question("¿Qué efecto puede producir un narrador protagonista?", "Acerca al lector a sus pensamientos y experiencia", "Cuenta lo que todos ignoran", "Elimina a los personajes", 0),
            _language_question("¿Qué conviene considerar al comparar obras de culturas distintas?", "Su contexto y los temas que comparten", "Que una cultura sea superior", "Solo la extensión de los textos", 1),
            _language_question("¿Cuál fragmento está narrado en primera persona?", "Caminé hasta el río y guardé la carta.", "El viajero caminó hasta el río.", "La carta fue guardada por alguien.", 2),
            _language_question("¿Cuál fragmento está narrado en tercera persona?", "Maya observó la estrella desde la ventana.", "Observé la estrella desde la ventana.", "Creí que la estrella me llamaba.", 0),
            _language_question("¿Qué puede cambiar al cambiar la voz narrativa?", "La información y la perspectiva sobre los hechos", "El número de páginas automáticamente", "El idioma de todos los personajes", 1),
            _language_question("¿Qué actitud favorece leer literatura de otras tradiciones?", "Curiosidad y respeto por su contexto", "Rechazarla antes de leer", "Juzgarla con una sola costumbre", 2),
            _language_question("¿Qué actividad ayuda a analizar una obra?", "Comparar narrador, personajes, tema y contexto", "Contar solo cuántos párrafos tiene", "Cambiar todos los nombres", 0),
        ],
    },
    "language-vocabulary": {
        "title": "Lenguaje figurado y sentido crítico",
        "description": "Interpreta metáforas, ironías y expresiones figuradas según el contexto.",
        "objective": "Distinguir lenguaje literal y figurado y analizar la intención de recursos expresivos.",
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "lesson": [
            "El lenguaje literal comunica un significado directo; el figurado crea imágenes o relaciones para expresar una idea de otra manera.",
            "Una metáfora relaciona dos elementos sin usar necesariamente como: «sus palabras fueron flechas».",
            "La ironía puede decir lo contrario de lo que se quiere comunicar. El tono y el contexto son necesarios para reconocerla.",
            "No interpretes una expresión aislada: observa quién la dice, a quién, en qué situación y con qué intención.",
        ],
        "questions": [
            _language_question("¿Qué significa «sus palabras fueron flechas»?", "Sus palabras fueron muy hirientes o directas", "Lanzó flechas de verdad", "No dijo ninguna palabra", 0),
            _language_question("¿Cuál expresión está en sentido literal?", "La ventana está abierta.", "Tiene un corazón de piedra.", "El tiempo vuela.", 1),
            _language_question("En «El tiempo vuela», se quiere decir que…", "Pasa muy rápido", "Tiene alas", "Se quedó quieto", 2),
            _language_question("¿Qué recurso relaciona dos elementos sin decir «como»?", "La metáfora", "La definición", "La instrucción", 0),
            _language_question("¿Qué ayuda a reconocer una ironía?", "El contexto, el tono y la intención", "Solo el número de palabras", "La primera letra", 1),
            _language_question("Si alguien llega una hora tarde y oye «¡Qué puntualidad!», probablemente hay…", "Ironía", "Una definición", "Una instrucción literal", 2),
            _language_question("¿Qué significa «la ciudad despertó» en un texto?", "La ciudad comenzó a llenarse de actividad", "La ciudad durmió literalmente", "La ciudad cambió de lugar", 0),
            _language_question("¿Cuál expresión contiene una comparación?", "Brilla como una estrella.", "Es una estrella.", "La estrella apareció.", 1),
            _language_question("¿Qué pregunta ayuda a interpretar lenguaje figurado?", "¿Qué idea comunica en este contexto?", "¿Cuántas letras tiene?", "¿Está al principio del libro?", 2),
            _language_question("¿Cuál lectura evita una interpretación literal equivocada?", "«Tengo un mar de dudas» significa que tengo muchas dudas.", "La persona está nadando en un mar de dudas.", "La persona no tiene ninguna duda.", 0),
        ],
    },
    "language-grammar": {
        "title": "Cohesión textual y subordinación",
        "description": "Construye textos cohesionados con referencias, conectores y oraciones subordinadas.",
        "objective": "Analizar relaciones entre oraciones y usar recursos de cohesión para escribir con precisión.",
        "learning_order": 6,
        "learning_phase": "Consolidar",
        "lesson": [
            "La cohesión conecta las partes de un texto mediante pronombres, repeticiones controladas, sinónimos y conectores.",
            "Las oraciones subordinadas completan o explican una idea principal y suelen introducirse con que, porque, aunque o cuando.",
            "Los conectores organizan la argumentación: además suma, sin embargo contrasta, por lo tanto expresa consecuencia.",
            "Revisa que cada pronombre tenga un referente claro y que cada conector exprese la relación que realmente quieres comunicar.",
        ],
        "questions": [
            _language_question("¿Qué recurso evita repetir un nombre?", "Un pronombre o un sinónimo adecuado", "Un signo al azar", "Una palabra sin relación", 0),
            _language_question("¿Cuál oración contiene una subordinada?", "Pienso que la propuesta es posible.", "La propuesta clara.", "La propuesta llegó.", 1),
            _language_question("¿Qué relación expresa «sin embargo»?", "Contraste", "Suma", "Orden", 2),
            _language_question("Completa: El equipo investigó; ___, presentó sus resultados.", "por lo tanto", "aunque", "porque", 0),
            _language_question("¿Cuál texto evita una repetición innecesaria?", "El informe llegó. Este documento incluye datos.", "El informe llegó. El informe incluye datos del informe.", "Llegó informe documento dato.", 1),
            _language_question("¿Qué palabra introduce una condición?", "Si", "Además", "Por eso", 2),
            _language_question("Completa: ___ termines el borrador, revisa las citas.", "Cuando", "Sin embargo", "Por lo tanto", 0),
            _language_question("¿Cuál relación expresa «además»?", "Adición", "Causa", "Contraste", 1),
            _language_question("¿Qué hace que una referencia sea clara?", "Que podamos identificar a qué palabra o idea se refiere", "Que aparezca muchas veces", "Que no tenga antecedente", 2),
            _language_question("¿Qué revisión mejora la cohesión?", "Comprobar referentes, conectores y relaciones entre ideas", "Eliminar todos los conectores", "Repetir el mismo sustantivo en cada oración", 0),
        ],
    },
}


LANGUAGE_GRADE_CONTENT_BY_GRADE = {
    2: LANGUAGE_GRADE_CONTENT,
    3: THIRD_GRADE_LANGUAGE_CONTENT,
    4: FOURTH_GRADE_LANGUAGE_CONTENT,
    5: FIFTH_GRADE_LANGUAGE_CONTENT,
}


# Adaptación inicial de Sociales para 1.º. Las preguntas parten de la
# experiencia cercana del niño y avanzan desde reconocer espacios y vínculos
# hasta ordenar hechos y tomar decisiones responsables.
FIRST_GRADE_SOCIAL_CONTENT = {
    "social-identity": {
        "title": "Mi familia, mi escuela y la convivencia",
        "description": "Reconoce grupos cercanos, emociones y reglas para convivir con respeto.",
        "objective": "Identificar vínculos, emociones, espacios y acuerdos de convivencia en la vida cotidiana.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "project": "Árbol genealógico familiar",
        "lesson": [
            "Las familias pueden ser diferentes. Lo importante es que las personas se cuidan, se acompañan y se respetan.",
            "La escuela es un espacio para aprender, jugar y convivir con otros niños y adultos.",
            "Las reglas indican acuerdos para cuidarnos: escuchar, esperar turnos y usar los espacios sin lastimar.",
            "Nombrar cómo nos sentimos y escuchar a los demás ayuda a resolver pequeños conflictos.",
        ],
        "questions": [
            _language_question("¿Qué hace una familia?", "Cuida y acompaña a sus integrantes", "Es solo una casa", "Es un mapa", 0),
            _language_question("¿Qué hacemos en la escuela?", "Aprendemos y convivimos", "Dormimos todo el día", "Compramos alimentos siempre", 1),
            _language_question("¿Para qué sirven las reglas?", "Para cuidarnos y convivir mejor", "Para excluir a alguien", "Para lastimar", 2),
            _language_question("¿Qué muestra respeto?", "Escuchar cuando otra persona habla", "Interrumpir siempre", "Burlarse", 0),
            _language_question("¿Qué emoción podemos sentir al recibir ayuda?", "Alegría", "Una moneda", "Un continente", 1),
            _language_question("¿Qué hacemos cuando estamos enojados?", "Respiramos y hablamos con calma", "Golpeamos a otros", "Gritamos sin escuchar", 2),
            _language_question("¿Qué acuerdo ayuda durante un juego?", "Esperar el turno", "Quitar los materiales", "Cambiar las reglas sin avisar", 0),
            _language_question("¿Quiénes pueden formar parte de una familia?", "Personas que se quieren y se cuidan", "Solo personas con la misma apariencia", "Solo quienes viven en una escuela", 1),
            _language_question("¿Qué espacio usamos para aprender con compañeros?", "El salón de clase", "La Luna", "El océano", 2),
            _language_question("¿Qué hacemos si hay un conflicto?", "Pedimos ayuda y buscamos un acuerdo", "Escondemos el problema siempre", "Empujamos", 0),
        ],
    },
    "social-geography": {
        "title": "Mi casa, mi escuela y mi barrio",
        "description": "Representa lugares cercanos con dibujos, recorridos y puntos de referencia.",
        "objective": "Reconocer espacios cercanos, orientarse con referencias y representar un recorrido sencillo.",
        "learning_order": 2,
        "learning_phase": "Explorar",
        "lesson": [
            "El espacio cercano incluye lugares que visitamos: casa, escuela, parque, tienda y calles del barrio.",
            "Un mapa es un dibujo que representa un lugar visto desde arriba. Los símbolos ayudan a ubicar cada sitio.",
            "Los puntos de referencia, como un árbol grande o una esquina, nos ayudan a explicar por dónde vamos.",
            "Cuidar las calles, los parques y las señales hace que el barrio sea más seguro para todos.",
        ],
        "questions": [
            _language_question("¿Qué es un mapa?", "Un dibujo que representa un lugar", "Una receta", "Una canción", 0),
            _language_question("¿Qué puede representar un dibujo de una casa en un mapa?", "El lugar donde está la casa", "Una emoción", "El tiempo que hace", 1),
            _language_question("¿Qué es un punto de referencia?", "Un lugar u objeto que ayuda a orientarnos", "Un juguete que se pierde", "Una comida", 2),
            _language_question("¿Qué lugar puede estar en un barrio?", "Un parque", "La Luna", "El fondo del océano", 0),
            _language_question("¿Qué muestra un recorrido?", "Por dónde vamos de un lugar a otro", "Qué sentimos al despertar", "La edad de una persona", 1),
            _language_question("Si la escuela está junto al parque, el parque es…", "Un punto de referencia", "Una emoción", "Una regla", 2),
            _language_question("¿Qué debemos cuidar en el barrio?", "Calles, parques y señales", "La basura en el suelo", "Las paredes con rayones", 0),
            _language_question("¿Cómo podemos representar la ruta a la escuela?", "Con un dibujo y lugares de referencia", "Con una receta", "Con una lista de emociones", 1),
            _language_question("¿Qué símbolo podría representar una biblioteca?", "Un dibujo de un libro", "Un dibujo de una nube sin explicación", "Un número al azar", 2),
            _language_question("¿Qué hacemos para caminar con seguridad?", "Respetamos las señales y cruzamos acompañados", "Corremos entre los carros", "Ignoramos las calles", 0),
        ],
    },
    "social-history": {
        "title": "Ayer, hoy y mi línea de vida",
        "description": "Ordena experiencias y reconoce cambios entre ayer, hoy y otros momentos.",
        "objective": "Diferenciar ayer y hoy, ordenar hechos y reconocer cambios en la historia personal.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "lesson": [
            "Ayer es el día anterior, hoy es el día que estamos viviendo y mañana es el día que vendrá.",
            "Una línea de tiempo ordena hechos desde el primero hasta el último. Puedes usar dibujos y fechas sencillas.",
            "Las fotografías, los objetos y los relatos familiares ayudan a recordar experiencias del pasado.",
            "Comparar cómo éramos antes con cómo somos ahora permite reconocer cambios y aprendizajes.",
        ],
        "questions": [
            _language_question("¿Qué significa ayer?", "El día anterior", "El día que viene", "Ahora mismo", 0),
            _language_question("¿Qué significa hoy?", "El día que estamos viviendo", "El año pasado", "El próximo mes", 1),
            _language_question("¿Para qué sirve una línea de tiempo?", "Para ordenar hechos", "Para medir una mesa", "Para dibujar un mapa", 2),
            _language_question("¿Qué ocurrió primero en una rutina de la mañana?", "Despertarse", "Llegar a casa por la tarde", "Dormirse por la noche", 0),
            _language_question("¿Cuál puede ser una fuente de recuerdos?", "Una fotografía", "Una sombra sin historia", "Un número solo", 1),
            _language_question("¿Qué puede cambiar con el tiempo?", "La estatura y lo que aprendemos", "Nada nunca", "Solo el color del cielo", 2),
            _language_question("¿Qué podemos ordenar en una línea de vida?", "Momentos importantes de nuestra historia", "Los colores de una caja", "Los sonidos de una canción", 0),
            _language_question("¿Qué ayuda a conocer cómo era antes un familiar?", "Preguntarle y escuchar su relato", "Inventar una respuesta", "Borrar sus fotografías", 1),
            _language_question("¿Qué palabra indica un momento que todavía no llega?", "Mañana", "Ayer", "Hoy", 2),
            _language_question("¿Qué aprendemos al comparar antes y ahora?", "Reconocemos cambios y avances", "Que todo permanece igual", "Que los recuerdos no sirven", 0),
        ],
    },
    "social-economy": {
        "title": "Necesidades, deseos y ahorro",
        "description": "Distingue lo necesario de lo que deseas y toma decisiones responsables al usar recursos.",
        "objective": "Diferenciar necesidades y deseos, reconocer el ahorro y elegir compras responsables.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "lesson": [
            "Una necesidad es algo básico para vivir y estar bien, como agua, alimento, vivienda y cuidado.",
            "Un deseo es algo que nos gustaría tener, aunque podemos vivir sin ello, como un juguete nuevo.",
            "Ahorrar significa guardar una parte de los recursos para usarla después en una meta o necesidad.",
            "Antes de elegir, piensa si lo necesitas, cuánto cuesta y cómo puedes cuidar o compartir lo que tienes.",
        ],
        "questions": [
            _language_question("¿Cuál es una necesidad?", "Agua para beber", "Un juguete nuevo", "Una pegatina", 0),
            _language_question("¿Cuál es un deseo?", "Querer una pelota nueva", "Respirar aire", "Tener agua para beber", 1),
            _language_question("¿Qué hace una alcancía?", "Ayuda a guardar dinero", "Produce comida", "Mide el tiempo", 2),
            _language_question("¿Qué usamos para comprar algo?", "Dinero", "Una nube", "Una regla", 0),
            _language_question("¿Qué significa ahorrar?", "Guardar una parte para usarla después", "Gastar todo de inmediato", "Romper las monedas", 1),
            _language_question("¿Cuál decisión es responsable?", "Comparar y pensar antes de comprar", "Comprar todo sin mirar", "Desperdiciar los materiales", 2),
            _language_question("Si tienes sed, ¿qué necesitas?", "Agua", "Un juguete", "Una calcomanía", 0),
            _language_question("¿Qué puedes hacer si ya tienes muchos juguetes?", "Cuidarlos y compartirlos", "Botarlos todos", "Pedir más sin usarlos", 1),
            _language_question("¿Para qué sirve una meta de ahorro?", "Para saber qué queremos alcanzar", "Para gastar sin plan", "Para esconder las necesidades", 2),
            _language_question("¿Qué hacemos con los útiles escolares?", "Los cuidamos y usamos responsablemente", "Los desperdiciamos", "Los dejamos tirados", 0),
        ],
    },
    "social-explorer": {
        "title": "Mapa del tesoro del barrio",
        "description": "Sigue pistas, reconoce referencias y cuida los lugares de tu comunidad.",
        "objective": "Consolidar la orientación y la representación de espacios cercanos mediante un juego de pistas.",
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "prerequisites": ["social-geography"],
        "related_activity": "social-geography",
    },
}


SECOND_GRADE_SOCIAL_CONTENT = {
    "social-identity": {
        "title": "Mi comunidad y su diversidad",
        "description": "Reconoce roles, costumbres y derechos en comunidades diversas.",
        "objective": "Identificar personas, roles, derechos y formas de participación en la comunidad.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "lesson": [
            "Una comunidad reúne personas que comparten un lugar, necesidades o intereses. Cada persona puede cumplir distintos roles.",
            "La diversidad se observa en las familias, costumbres, lenguas, capacidades y formas de participar.",
            "Los niños tienen derechos, como recibir educación, ser cuidados y expresar sus ideas con respeto.",
            "Participar significa colaborar, escuchar a otros y ayudar a construir acuerdos para el bien común.",
        ],
        "questions": [
            _language_question("¿Qué es una comunidad?", "Personas que comparten un lugar o intereses", "Un objeto sin personas", "Un solo edificio", 0),
            _language_question("¿Qué significa diversidad?", "Variedad de personas, costumbres y formas de vivir", "Que todos sean idénticos", "Que nadie participe", 1),
            _language_question("¿Qué hace un bombero en la comunidad?", "Ayuda en emergencias", "Vende frutas siempre", "Organiza todos los juegos", 2),
            _language_question("¿Cuál es un derecho de los niños?", "Recibir educación y cuidado", "Trabajar sin descanso", "No ser escuchados", 0),
            _language_question("¿Qué actitud favorece la inclusión?", "Permitir que todos participen con los apoyos necesarios", "Dejar fuera a quien es diferente", "Burlarse de otra costumbre", 1),
            _language_question("¿Qué responsabilidad acompaña al derecho a aprender?", "Cuidar los materiales y participar", "Impedir que otros estudien", "Romper los libros", 2),
            _language_question("¿Cómo participamos en una decisión escolar?", "Dando ideas y escuchando propuestas", "Gritando para imponer una idea", "Ignorando a todos", 0),
            _language_question("¿Qué puede aportar una persona mayor a la comunidad?", "Experiencias y conocimientos", "Ninguna idea", "Solo objetos", 1),
            _language_question("¿Qué hacemos ante una diferencia?", "Dialogamos y respetamos", "Discriminamos", "Dejamos de escuchar", 2),
            _language_question("¿Qué ayuda a una comunidad a convivir?", "Acuerdos, colaboración y respeto", "Exclusión y silencio", "Competir siempre", 0),
        ],
    },
    "social-geography": {
        "title": "Mi municipio: mapas, leyendas y clima",
        "description": "Lee mapas sencillos, reconoce servicios del municipio y observa el clima de tu lugar.",
        "objective": "Interpretar mapas con leyenda, ubicar servicios y relacionar el clima con la vida cotidiana.",
        "learning_order": 2,
        "learning_phase": "Explorar",
        "lesson": [
            "El municipio es una comunidad organizada que ofrece servicios y administra lugares cercanos.",
            "Los mapas usan símbolos y una leyenda para representar parques, escuelas, hospitales, caminos y otros espacios.",
            "El clima describe condiciones habituales, como lluvia, temperatura y viento, durante un tiempo y lugar.",
            "Observar un mapa y el clima ayuda a planear recorridos y comprender actividades de la comunidad.",
        ],
        "questions": [
            _language_question("¿Qué es un municipio?", "Una comunidad con una organización local", "Un planeta", "Un animal", 0),
            _language_question("¿Para qué sirve la leyenda de un mapa?", "Explica el significado de los símbolos", "Cuenta una historia inventada", "Mide la temperatura", 1),
            _language_question("¿Qué puede representar un símbolo de una cruz en un mapa?", "Un centro de salud", "Una montaña siempre", "Una tienda de juguetes", 2),
            _language_question("¿Qué describe el clima?", "Condiciones habituales de la atmósfera", "El precio de un producto", "El tamaño de una familia", 0),
            _language_question("¿Qué servicio puede ofrecer una biblioteca?", "Libros y espacios para leer", "Lluvia", "Construcción de todos los caminos", 1),
            _language_question("¿Qué dato ayuda a decidir si llevamos paraguas?", "La posibilidad de lluvia", "El nombre del municipio", "La cantidad de ventanas", 2),
            _language_question("¿Qué muestra un mapa de recorridos?", "Cómo llegar de un lugar a otro", "Qué siente una persona", "Cuánto pesa un edificio", 0),
            _language_question("Si el parque está al norte de la escuela, ¿qué indica norte?", "Una dirección", "Un servicio", "Un tipo de clima", 1),
            _language_question("¿Qué acción cuida un espacio municipal?", "Usar las canecas y respetar las plantas", "Romper las señales", "Dejar basura", 2),
            _language_question("¿Qué podemos hacer para leer mejor un mapa?", "Observar el título, los símbolos y la leyenda", "Ignorar la leyenda", "Cambiar todos los símbolos", 0),
        ],
    },
    "social-history": {
        "title": "La historia de mi comunidad",
        "description": "Investiga cambios locales mediante generaciones, entrevistas, objetos y museos.",
        "objective": "Reconocer cambios y permanencias de la comunidad usando testimonios y fuentes locales.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "project": "Entrevista a un abuelo o vecino",
        "lesson": [
            "La historia local cuenta cómo han cambiado los lugares y las personas de nuestra comunidad.",
            "Una generación reúne personas que viven una época parecida. Comparar generaciones permite reconocer cambios y permanencias.",
            "Las entrevistas, fotografías, objetos y museos son fuentes que ayudan a conocer el pasado.",
            "Al investigar, pregunta con respeto, anota las respuestas y diferencia lo que alguien recuerda de lo que puedes comprobar en otras fuentes.",
        ],
        "questions": [
            _language_question("¿Qué es la historia local?", "El estudio de cambios y experiencias de una comunidad", "Una lista de compras", "El pronóstico del tiempo", 0),
            _language_question("¿Qué es una generación?", "Personas de edades cercanas que viven una época", "Un solo edificio", "Una moneda antigua", 1),
            _language_question("¿Cuál es una fuente oral?", "Una entrevista", "Un mapa sin explicación", "Una piedra sin contexto", 2),
            _language_question("¿Qué puede mostrar una fotografía antigua?", "Cómo era un lugar o una actividad", "El futuro con seguridad", "El precio de todos los productos", 0),
            _language_question("¿Qué conserva un museo?", "Objetos y recuerdos importantes", "Solo alimentos", "El clima de mañana", 1),
            _language_question("¿Cuál pregunta sirve para entrevistar a un vecino?", "¿Cómo era este barrio cuando usted era niño?", "¿Qué color tiene el silencio?", "¿Cuánto pesa un recuerdo?", 2),
            _language_question("¿Qué muestra una fecha en una fotografía?", "Cuándo pudo haber ocurrido el hecho", "Quién tomó todas las fotos", "Qué clima habrá mañana", 0),
            _language_question("¿Por qué comparamos fuentes?", "Para encontrar coincidencias y diferencias", "Para borrar los recuerdos", "Para inventar una historia", 1),
            _language_question("¿Qué puede cambiar en una comunidad?", "Sus calles, transportes y formas de trabajo", "Nada nunca", "Solo el color del cielo", 2),
            _language_question("¿Qué actitud necesitamos al escuchar un testimonio?", "Respeto y atención", "Interrumpir y burlarse", "Cambiar las respuestas", 0),
        ],
    },
    "social-economy": {
        "title": "Bienes, servicios y decisiones en el mercado",
        "description": "Distingue bienes y servicios, comprende el mercado y analiza mensajes publicitarios.",
        "objective": "Reconocer bienes, servicios, intercambios y decisiones responsables frente a la publicidad.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "lesson": [
            "Un bien es un objeto que satisface una necesidad; un servicio es una actividad que ayuda a las personas.",
            "En el mercado se intercambian bienes y servicios. Las personas eligen según sus necesidades, recursos y prioridades.",
            "La publicidad intenta informar o convencer. Puede destacar beneficios, pero no siempre cuenta toda la información.",
            "Antes de comprar, compara precios, revisa si lo necesitas y pregunta a una persona adulta cuando tengas dudas.",
        ],
        "questions": [
            _language_question("¿Qué es un bien?", "Un objeto que satisface una necesidad", "Una actividad sin producto", "Una emoción", 0),
            _language_question("¿Qué es un servicio?", "Una actividad que ayuda a alguien", "Una montaña", "Una moneda sin uso", 1),
            _language_question("¿Cuál es un bien?", "Un cuaderno", "Una clase de música", "Una consulta médica", 2),
            _language_question("¿Cuál es un servicio?", "El transporte público", "Un pan", "Un lápiz", 0),
            _language_question("¿Qué hacemos en un mercado?", "Intercambiamos o compramos bienes y servicios", "Observamos planetas", "Ordenamos las estaciones", 1),
            _language_question("¿Qué intenta hacer la publicidad?", "Informar o convencer sobre un producto o servicio", "Medir la lluvia", "Contar siempre toda la historia", 2),
            _language_question("¿Qué decisión es responsable?", "Comparar opciones antes de comprar", "Comprar por cualquier anuncio", "Gastar sin preguntar", 0),
            _language_question("¿Qué pregunta ayuda ante un anuncio?", "¿Realmente lo necesito y qué información falta?", "¿Cómo compro todo inmediatamente?", "¿Cómo escondo el precio?", 1),
            _language_question("¿Quién ofrece un servicio de salud?", "Una enfermera o un centro de salud", "Un mapa", "Una montaña", 2),
            _language_question("¿Qué ayuda a cuidar los recursos de la familia?", "Planear gastos y evitar desperdicios", "Comprar sin revisar", "Botar lo que todavía sirve", 0),
        ],
    },
    "social-explorer": {
        "title": "Ruta comunitaria con códigos QR",
        "description": "Sigue una ruta, interpreta símbolos y descubre servicios de tu municipio mediante códigos QR.",
        "objective": "Consolidar la lectura de mapas y la identificación de servicios mediante pistas comunitarias.",
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "prerequisites": ["social-geography"],
        "related_activity": "social-geography",
        "questions": [
            _language_question("¿Qué indica un código ubicado junto a una biblioteca?", "Una pista para conocer ese lugar", "El clima de todo el país", "El precio de un juguete", 0),
            _language_question("¿Qué debemos mirar antes de seguir una ruta?", "El mapa, la leyenda y las señales", "Solo el color del cielo", "Un anuncio cualquiera", 1),
            _language_question("Si la plaza está después del puente, ¿qué hacemos?", "Seguimos el recorrido hasta el puente y luego buscamos la plaza", "Volvemos sin mirar el mapa", "Cambiamos el nombre de la plaza", 2),
            _language_question("¿Qué lugar ofrece libros y lectura?", "La biblioteca", "El hospital", "La estación meteorológica", 0),
            _language_question("¿Qué acción cuida la ruta comunitaria?", "Respetar señales y no dejar basura", "Arrancar los códigos", "Dañar las plantas", 1),
            _language_question("¿Qué representa un símbolo acordado?", "Un lugar o servicio", "Una emoción secreta", "Un ruido", 2),
            _language_question("¿Qué ayuda a orientarnos en una ruta?", "Un punto de referencia", "Cerrar los ojos", "Cambiar de camino sin avisar", 0),
            _language_question("¿Qué servicio puede estar en el municipio?", "Un centro de salud", "Una nube", "Una estrella", 1),
            _language_question("¿Qué hacemos si no entendemos una pista?", "Pedimos ayuda y consultamos la leyenda", "La inventamos", "La rompemos", 2),
            _language_question("¿Qué aprendemos con una ruta comunitaria?", "A leer espacios y reconocer servicios cercanos", "A comprar todo lo que vemos", "A ignorar el municipio", 0),
        ],
    },
}


THIRD_GRADE_SOCIAL_CONTENT = {
    "social-identity": {
        "title": "Derechos y democracia escolar",
        "description": "Reconoce derechos de la niñez, responsabilidades y formas de participar en decisiones escolares.",
        "objective": "Relacionar derechos y responsabilidades y practicar el diálogo democrático en la escuela.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "lesson": [
            "Los derechos protegen la dignidad y el bienestar de los niños: aprender, ser cuidados, opinar y jugar son algunos ejemplos.",
            "Cada derecho se relaciona con responsabilidades, como respetar a los demás, cuidar los espacios y cumplir acuerdos.",
            "La democracia permite participar en decisiones mediante propuestas, diálogo, votaciones y acuerdos.",
            "Escuchar a quien piensa diferente y aceptar resultados justos fortalece la convivencia escolar.",
        ],
        "questions": [
            _language_question("¿Qué es un derecho?", "Una protección que corresponde a todas las personas", "Un premio secreto", "Una deuda", 0),
            _language_question("¿Cuál es un derecho de la niñez?", "Recibir educación y cuidado", "Trabajar sin descanso", "No poder opinar", 1),
            _language_question("¿Qué responsabilidad acompaña el derecho a jugar?", "Respetar las reglas y cuidar los materiales", "Impedir jugar a otros", "Romper los espacios", 2),
            _language_question("¿Qué hace una votación?", "Recoge preferencias para tomar una decisión", "Borra todas las opiniones", "Decide quién tiene más fuerza", 0),
            _language_question("¿Qué actitud ayuda a un diálogo democrático?", "Escuchar razones y hablar por turnos", "Gritar hasta ganar", "No dejar participar", 1),
            _language_question("¿Qué es una responsabilidad?", "Cumplir un compromiso", "Quitar derechos a otros", "Ignorar acuerdos", 2),
            _language_question("¿Cómo se presenta una propuesta escolar?", "Explicando una idea y sus razones", "Imponiéndola sin escuchar", "Ocultándola al grupo", 0),
            _language_question("¿Qué significa incluir?", "Permitir la participación de todos con los apoyos necesarios", "Dejar fuera a quien necesita ayuda", "Tratar peor a una persona", 1),
            _language_question("¿Qué ocurre después de una votación justa?", "Se respeta el resultado y se continúa dialogando", "Se castiga a quien pensó diferente", "Se eliminan las propuestas", 2),
            _language_question("¿Qué protege la convivencia democrática?", "Derechos, responsabilidades y acuerdos", "Silencio obligatorio", "Competencia sin reglas", 0),
        ],
    },
    "social-geography": {
        "title": "Mi región: recursos y actividades",
        "description": "Ubica tu región, reconoce sus recursos y relaciona paisajes con actividades de sus habitantes.",
        "objective": "Interpretar una región como espacio compartido y reconocer el uso responsable de sus recursos.",
        "learning_order": 2,
        "learning_phase": "Explorar",
        "project": "Mapa temático de la región",
        "lesson": [
            "Una región es un espacio que comparte características, como paisajes, clima, recursos o actividades de sus habitantes.",
            "Los mapas temáticos muestran un tema específico: ríos, cultivos, población, vías o actividades económicas.",
            "Los recursos naturales, como agua, suelo y bosques, ayudan a la vida y al trabajo, pero no son infinitos.",
            "Usar los recursos responsablemente significa aprovecharlos sin destruirlos y pensar en las personas del futuro.",
        ],
        "questions": [
            _language_question("¿Qué es una región?", "Un espacio con características comunes", "Una sola calle", "Un objeto escolar", 0),
            _language_question("¿Qué muestra un mapa temático?", "Un tema específico de un territorio", "Todas las historias de una familia", "El precio de un producto", 1),
            _language_question("¿Cuál es un recurso natural?", "El agua", "Un edificio", "Una aplicación", 2),
            _language_question("¿Qué actividad usa el suelo para cultivar alimentos?", "La agricultura", "La astronomía", "La programación", 0),
            _language_question("¿Qué paisaje tiene abundante agua salada?", "La costa", "El desierto sin oasis", "Una oficina", 1),
            _language_question("¿Qué actividad puede realizarse en una región de montañas?", "Turismo y agricultura de altura", "Pesca en mar abierto siempre", "Construcción de submarinos en toda ocasión", 2),
            _language_question("¿Qué representa la escala de un mapa?", "La relación entre una distancia dibujada y la real", "El clima de una ciudad", "La opinión de un habitante", 0),
            _language_question("¿Qué acción protege un recurso natural?", "Ahorrar agua y evitar contaminarla", "Desperdiciarla", "Arrojar residuos al río", 1),
            _language_question("¿Qué información puede tener un mapa de actividades?", "Lugares donde se cultiva, pesca o comercia", "Solo nombres de personas", "Únicamente fechas familiares", 2),
            _language_question("¿Por qué debemos cuidar los recursos de la región?", "Porque sostienen la vida actual y futura", "Porque nunca se terminan", "Porque solo pertenecen a una persona", 0),
        ],
    },
    "social-history": {
        "title": "Línea de tiempo y fuentes de mi comunidad",
        "description": "Ordena procesos comunitarios y compara fuentes para comprender cómo ha cambiado la localidad.",
        "objective": "Construir una línea de tiempo y usar fuentes para explicar cambios y permanencias de la comunidad.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "lesson": [
            "Una línea de tiempo organiza hechos en orden cronológico y ayuda a observar cuánto tiempo pasó entre ellos.",
            "Las fuentes históricas pueden ser orales, escritas, visuales o materiales: testimonios, cartas, fotografías, edificios y objetos.",
            "Comparar fuentes permite encontrar coincidencias, diferencias y preguntas que necesitan más investigación.",
            "Una explicación histórica debe distinguir lo que la fuente muestra de lo que nosotros inferimos.",
        ],
        "questions": [
            _language_question("¿Qué orden es cronológico?", "Antes, durante y después", "Después, antes y sin fechas", "Al azar, sin momentos", 0),
            _language_question("¿Qué es una fuente histórica?", "Una evidencia que ayuda a conocer el pasado", "Una predicción del futuro", "Un juguete nuevo sin contexto", 1),
            _language_question("¿Cuál es una fuente oral?", "El testimonio de un vecino", "Una fotografía", "Una carta", 2),
            _language_question("¿Qué puede mostrar una fotografía antigua?", "Cómo era un lugar o una actividad en otro momento", "Lo que ocurrirá mañana", "La opinión de todas las personas", 0),
            _language_question("¿Por qué comparamos fuentes?", "Para reconocer coincidencias y diferencias", "Para borrar datos", "Para inventar fechas", 1),
            _language_question("¿Qué pregunta ayuda a estudiar un cambio?", "¿Cómo era antes y cómo es ahora?", "¿Qué color tiene el silencio?", "¿Cuánto pesa una fecha?", 2),
            _language_question("¿Qué institución puede conservar objetos de la historia local?", "Un museo", "Una nube", "Una tienda sin archivos", 0),
            _language_question("¿Qué hace un historiador?", "Investiga el pasado usando evidencias", "Adivina sin consultar fuentes", "Cambia las fechas", 1),
            _language_question("¿Qué muestra una línea de tiempo?", "Relaciones de orden y duración entre hechos", "Solo los lugares de un mapa", "El precio de los bienes", 2),
            _language_question("¿Qué debemos hacer al usar un testimonio?", "Escucharlo, registrarlo y compararlo con otras fuentes", "Tomarlo como verdad sin preguntar", "Borrar quién lo contó", 0),
        ],
    },
    "social-economy": {
        "title": "Trabajo, sectores e impuestos",
        "description": "Relaciona trabajos y sectores económicos con los servicios que sostienen la comunidad.",
        "objective": "Distinguir sectores económicos, valorar el trabajo y comprender el propósito de los impuestos.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "lesson": [
            "El trabajo produce bienes, ofrece servicios y ayuda a satisfacer necesidades de las personas y la comunidad.",
            "El sector primario obtiene recursos de la naturaleza; el secundario transforma materiales y el terciario ofrece servicios.",
            "Los impuestos son aportes que se recaudan para financiar servicios y obras públicas, como escuelas, hospitales y vías.",
            "Todas las labores dignas merecen respeto. Comprender cómo se relacionan ayuda a tomar decisiones responsables.",
        ],
        "questions": [
            _language_question("¿Qué es un sector económico?", "Un grupo de actividades productivas relacionadas", "Un barrio", "Un continente", 0),
            _language_question("¿Qué actividad pertenece al sector primario?", "La agricultura", "La fabricación de zapatos", "La atención bancaria", 1),
            _language_question("¿Qué actividad pertenece al sector secundario?", "Transformar madera en muebles", "Cultivar café", "Enseñar en una escuela", 2),
            _language_question("¿Qué actividad pertenece al sector terciario?", "Ofrecer transporte", "Extraer minerales", "Cosechar frutas", 0),
            _language_question("¿Qué produce una fábrica?", "Bienes elaborados", "Solo ideas", "Lluvia", 1),
            _language_question("¿Para qué sirven los impuestos?", "Para financiar servicios y obras públicas", "Para comprar objetos de una sola persona", "Para ocultar ingresos", 2),
            _language_question("¿Cuál es un servicio público?", "La atención de un hospital público", "Un juguete privado", "Una fruta", 0),
            _language_question("¿Qué relación hay entre trabajo y comunidad?", "Los trabajos ofrecen bienes o servicios que necesitamos", "Ningún trabajo ayuda a otros", "Solo importa el trabajo de una persona", 1),
            _language_question("¿Qué debe recibir un trabajador?", "Respeto y condiciones dignas", "Ninguna protección", "Trabajo sin descanso", 2),
            _language_question("¿Qué decisión ayuda a la economía familiar?", "Planear gastos y evitar desperdicios", "Comprar sin comparar", "Gastar todos los recursos", 0),
        ],
    },
    "social-explorer": {
        "title": "Simulador de alcalde: presupuesto",
        "description": "Distribuye un presupuesto sencillo y decide cómo mejorar servicios de la comunidad.",
        "objective": "Aplicar nociones de servicios públicos, recursos y decisiones colectivas mediante un presupuesto.",
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "prerequisites": ["social-economy"],
        "related_activity": "social-economy",
        "questions": [
            _language_question("¿Qué debe hacer primero un alcalde responsable?", "Escuchar necesidades y revisar recursos", "Gastar todo sin plan", "Elegir solo lo que le gusta", 0),
            _language_question("¿En qué puede invertirse un presupuesto público?", "Escuelas, salud y vías", "Juguetes personales", "Objetos de una sola familia", 1),
            _language_question("Si una calle es peligrosa, ¿qué servicio necesita atención?", "La seguridad y el mantenimiento vial", "Un museo de pinturas únicamente", "Una tienda privada", 2),
            _language_question("¿Qué significa priorizar?", "Elegir primero lo más necesario", "Comprar todo al mismo tiempo", "Ignorar las necesidades", 0),
            _language_question("¿Por qué se consulta a la comunidad?", "Para conocer necesidades y participar en decisiones", "Para evitar escuchar opiniones", "Para gastar más sin explicación", 1),
            _language_question("¿Qué hace transparente un presupuesto?", "Explicar cuánto hay y en qué se usará", "Ocultar los gastos", "Cambiar las cifras sin avisar", 2),
            _language_question("¿Qué obra beneficia a muchas personas?", "Reparar una escuela pública", "Comprar un objeto personal", "Decorar una sola casa", 0),
            _language_question("¿Qué hacemos si no alcanza el presupuesto?", "Priorizamos y buscamos alternativas", "Prometemos todo sin calcular", "Gastamos sin revisar", 1),
            _language_question("¿Qué valor se practica al decidir juntos?", "Participación y responsabilidad", "Indiferencia", "Exclusión", 2),
            _language_question("¿Qué aprendemos con el simulador?", "Que los recursos son limitados y las decisiones tienen consecuencias", "Que el dinero público es infinito", "Que solo una persona debe opinar", 0),
        ],
    },
}


FOURTH_GRADE_SOCIAL_CONTENT = {
    "social-identity": {
        "title": "Ciudadanía, Constitución e inclusión",
        "description": "Comprende derechos, deberes e inclusión para participar responsablemente en la sociedad.",
        "objective": "Relacionar ciudadanía, Constitución, derechos, deberes e inclusión en situaciones cotidianas.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "lesson": [
            "La ciudadanía implica derechos, deberes y participación en las decisiones que afectan a la comunidad.",
            "La Constitución reúne principios y normas fundamentales que organizan el Estado y protegen derechos.",
            "Incluir significa eliminar barreras y ofrecer apoyos para que todas las personas puedan participar.",
            "Los conflictos ciudadanos se resuelven mejor con diálogo, respeto por las normas y búsqueda de acuerdos.",
        ],
        "questions": [
            _language_question("¿Qué implica ser ciudadano?", "Tener derechos, deberes y posibilidad de participar", "Solo recibir beneficios", "Obedecer sin poder opinar", 0),
            _language_question("¿Qué es la Constitución?", "La norma fundamental que organiza el Estado y protege derechos", "Un horario escolar", "Una lista de compras", 1),
            _language_question("¿Cuál es un deber ciudadano?", "Respetar los derechos y cumplir las normas", "Impedir la participación", "Desconocer todos los acuerdos", 2),
            _language_question("¿Qué significa incluir?", "Eliminar barreras para que todos participen", "Dejar fuera a quien necesita apoyo", "Tratar a las personas de forma injusta", 0),
            _language_question("¿Qué institución puede proteger derechos?", "Las autoridades y los organismos de justicia", "Un juguete", "Una montaña", 1),
            _language_question("¿Qué acción es democrática?", "Escuchar propuestas y participar en decisiones", "Imponer una idea por la fuerza", "No permitir opiniones", 2),
            _language_question("¿Qué ayuda a resolver un conflicto ciudadano?", "Dialogar y buscar acuerdos justos", "Usar violencia", "Ignorar a las personas afectadas", 0),
            _language_question("¿Qué ejemplo muestra inclusión?", "Adaptar un espacio para que pueda usarlo una persona con discapacidad", "Cerrar la entrada a una persona", "Burlarse de una diferencia", 1),
            _language_question("¿Por qué son importantes los derechos?", "Protegen la dignidad y el bienestar de las personas", "Permiten excluir a otros", "Solo sirven para algunas familias", 2),
            _language_question("¿Qué relación hay entre derechos y deberes?", "Ejercer derechos implica respetar los derechos de los demás", "Los deberes eliminan los derechos", "No tienen ninguna relación", 0),
        ],
    },
    "social-geography": {
        "title": "Mi país: relieve, clima y regiones",
        "description": "Interpreta mapas políticos y físicos y relaciona regiones con sus paisajes y climas.",
        "objective": "Distinguir mapas políticos y físicos y explicar cómo relieve y clima influyen en las regiones.",
        "learning_order": 2,
        "learning_phase": "Explorar",
        "project": "Mapa temático de una región del país",
        "lesson": [
            "Un mapa político muestra fronteras, departamentos, municipios y otras divisiones administrativas.",
            "Un mapa físico representa formas del relieve, como montañas, llanuras, valles, ríos y costas.",
            "El clima se relaciona con factores como altitud, relieve, cercanía al mar y ubicación geográfica.",
            "Las regiones tienen paisajes y actividades diferentes. Los mapas, la escala, la orientación y la leyenda ayudan a interpretarlas.",
        ],
        "questions": [
            _language_question("¿Qué muestra un mapa político?", "Divisiones administrativas y fronteras", "Solo montañas", "El menú de una región", 0),
            _language_question("¿Qué representa un mapa físico?", "Formas de la superficie terrestre", "Los resultados de una elección", "Los precios de un mercado", 1),
            _language_question("¿Qué es el relieve?", "Las formas de la superficie terrestre", "Una ley del país", "Una profesión", 2),
            _language_question("¿Qué puede influir en el clima de un lugar?", "La altitud y la cercanía al mar", "El color de las casas", "El nombre de una calle", 0),
            _language_question("¿Qué paisaje tiene terrenos planos y extensos?", "Una llanura", "Una cordillera únicamente", "Un acantilado siempre", 1),
            _language_question("¿Qué elemento ayuda a calcular distancias en un mapa?", "La escala", "El título de una canción", "El color de una bandera", 2),
            _language_question("¿Qué información puede mostrar un mapa temático?", "Distribución de cultivos, población o climas", "Todos los recuerdos familiares", "Solo nombres sin ubicación", 0),
            _language_question("¿Qué relación puede existir entre clima y actividades?", "El clima influye en cultivos, transporte y formas de vida", "El clima no afecta ninguna actividad", "Solo cambia el idioma", 1),
            _language_question("¿Qué indica la leyenda de un mapa?", "El significado de sus símbolos", "La edad del mapa solamente", "El precio del papel", 2),
            _language_question("¿Por qué es útil comparar regiones?", "Para reconocer sus características y necesidades diferentes", "Para afirmar que todas son iguales", "Para eliminar sus nombres", 0),
        ],
    },
    "social-history": {
        "title": "Historia nacional: etapas y personajes",
        "description": "Ordena procesos de la historia nacional y comprende las acciones de sus protagonistas en contexto.",
        "objective": "Reconocer etapas, cambios, continuidades y personajes de la historia nacional mediante fuentes.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "project": "Investiga un personaje histórico",
        "lesson": [
            "La historia nacional se estudia como un proceso con etapas, cambios y continuidades, no como una lista aislada de fechas.",
            "Los personajes históricos actuaron en circunstancias concretas. Para comprenderlos, revisa sus decisiones, intereses y consecuencias.",
            "Las fuentes pueden ser documentos, objetos, imágenes, testimonios y lugares. Cada fuente ofrece una perspectiva.",
            "Una línea de tiempo y la comparación de fuentes ayudan a explicar relaciones entre causas, hechos y consecuencias.",
        ],
        "questions": [
            _language_question("¿Qué es una etapa histórica?", "Un periodo con características y procesos relacionados", "Un día sin relación con otros", "Un lugar del mapa", 0),
            _language_question("¿Qué ayuda a ordenar etapas nacionales?", "Una línea de tiempo", "Una receta", "Una lista de colores", 1),
            _language_question("¿Qué es una fuente histórica?", "Una evidencia del pasado", "Una predicción sin datos", "Un rumor actual", 2),
            _language_question("¿Por qué debemos estudiar a un personaje en su contexto?", "Para comprender sus decisiones y circunstancias", "Para juzgarlo sin conocer la época", "Para olvidar a las demás personas", 0),
            _language_question("¿Qué puede ser una fuente primaria?", "Una carta escrita durante el acontecimiento", "Un resumen escolar posterior siempre", "Una opinión sin fecha", 1),
            _language_question("¿Qué relación muestra una explicación histórica?", "Causas, hechos y consecuencias", "Colores y tamaños sin sentido", "Solo nombres repetidos", 2),
            _language_question("¿Por qué comparar dos fuentes?", "Para reconocer coincidencias, diferencias y perspectivas", "Para borrar una de ellas", "Para evitar investigar", 0),
            _language_question("¿Qué pregunta sirve para investigar un personaje?", "¿Qué hizo, en qué contexto y qué consecuencias tuvo?", "¿Qué color le gustaba sin consultar fuentes?", "¿Por qué debemos inventar su historia?", 1),
            _language_question("¿Qué muestra una continuidad histórica?", "Algo que permanece o se transforma lentamente", "Un hecho que nunca ocurrió", "Un dato sin fecha", 2),
            _language_question("¿Qué debe incluir una investigación histórica?", "Fuentes, contexto y una explicación propia", "Solo una opinión", "Datos copiados sin indicar origen", 0),
        ],
    },
    "social-economy": {
        "title": "Empresa, banco, presupuesto y comercio",
        "description": "Comprende cómo se organizan empresas, bancos y presupuestos en la economía cotidiana.",
        "objective": "Distinguir ingresos, gastos, ahorro, crédito y comercio en decisiones económicas responsables.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "lesson": [
            "Una empresa organiza personas, recursos y actividades para producir bienes o prestar servicios.",
            "Un banco ofrece servicios financieros, como guardar dinero, facilitar pagos o conceder préstamos bajo condiciones.",
            "Un presupuesto registra ingresos y gastos para planear decisiones y evitar gastar más de lo disponible.",
            "El comercio conecta productores y consumidores. Comparar precios, calidad e impacto ayuda a elegir responsablemente.",
        ],
        "questions": [
            _language_question("¿Qué hace una empresa?", "Organiza recursos para producir bienes o servicios", "Solo guarda recuerdos", "Mide el relieve", 0),
            _language_question("¿Qué servicio puede ofrecer un banco?", "Guardar dinero y facilitar pagos", "Cultivar todos los alimentos", "Organizar el clima", 1),
            _language_question("¿Qué es un presupuesto?", "Un plan de ingresos y gastos", "Una lista de deseos sin recursos", "Un mapa físico", 2),
            _language_question("¿Qué es un ingreso?", "Dinero que recibimos", "Dinero que gastamos", "Una deuda siempre", 0),
            _language_question("¿Qué es un gasto?", "Dinero que usamos para adquirir algo", "Un ingreso", "Un recurso natural", 1),
            _language_question("¿Qué ayuda a evitar deudas innecesarias?", "Planear y comparar antes de comprar", "Gastar sin revisar", "Ocultar los precios", 2),
            _language_question("¿Qué es el comercio?", "Intercambio de bienes y servicios", "Una forma de medir montañas", "Una actividad sin personas", 0),
            _language_question("¿Qué debe considerar una empresa responsable?", "Su impacto en las personas y el ambiente", "Solo vender más sin consecuencias", "Ignorar a sus trabajadores", 1),
            _language_question("¿Para qué sirve ahorrar?", "Para alcanzar una meta o afrontar una necesidad futura", "Para gastar sin plan", "Para evitar registrar gastos", 2),
            _language_question("¿Qué decisión económica es responsable?", "Comparar calidad, precio y necesidad", "Comprar por impulso siempre", "Gastar todo el ingreso", 0),
        ],
    },
    "social-explorer": {
        "title": "Comercio internacional: misión barco",
        "description": "Relaciona países, productos, rutas y decisiones responsables en un reto de comercio.",
        "objective": "Consolidar la comprensión de intercambio, rutas, presupuesto y cooperación entre territorios.",
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "prerequisites": ["social-economy", "social-geography"],
        "related_activity": "social-economy",
        "questions": [
            _language_question("¿Qué es el comercio internacional?", "Intercambio de bienes y servicios entre países", "Una actividad dentro de una sola casa", "Un mapa sin rutas", 0),
            _language_question("¿Qué puede transportar un barco comercial?", "Productos entre puertos", "Solo emociones", "El clima de un país", 1),
            _language_question("¿Qué es una ruta comercial?", "Un recorrido por el que se transportan productos", "Una lista de deseos", "Una frontera sin lugares", 2),
            _language_question("¿Qué debe revisar una empresa antes de enviar mercancía?", "Costos, ruta, normas y seguridad", "Solo el color del barco", "Ningún dato", 0),
            _language_question("¿Qué significa importar?", "Comprar productos de otro país", "Vender dentro de la misma tienda", "Guardar productos sin usarlos", 1),
            _language_question("¿Qué significa exportar?", "Vender productos a otro país", "Comprar en el barrio", "Destruir una mercancía", 2),
            _language_question("¿Qué valor favorece el comercio entre países?", "Cooperación y respeto por los acuerdos", "Engaño", "Incumplimiento permanente", 0),
            _language_question("¿Qué decisión hace más responsable un envío?", "Reducir residuos y planear la ruta", "Desperdiciar combustible", "Ocultar el origen del producto", 1),
            _language_question("¿Por qué se usa un presupuesto en la misión?", "Para organizar recursos y evitar gastos excesivos", "Porque el dinero es infinito", "Para no registrar decisiones", 2),
            _language_question("¿Qué aprendemos con el juego?", "Que el comercio conecta territorios y requiere decisiones responsables", "Que comerciar no tiene consecuencias", "Que un país no depende de ningún otro", 0),
        ],
    },
}


FIFTH_GRADE_SOCIAL_CONTENT = {
    "social-identity": {
        "title": "Ciudadanía global y derechos humanos",
        "description": "Relaciona derechos humanos, cooperación internacional y responsabilidades frente a desafíos comunes.",
        "objective": "Comprender la ciudadanía global, los derechos humanos y el papel de la cooperación internacional.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "lesson": [
            "Los derechos humanos pertenecen a todas las personas por su dignidad, sin importar nacionalidad, origen, género o condición.",
            "La ciudadanía global reconoce que nuestras decisiones afectan a otras personas y al planeta, aunque vivan lejos.",
            "La ONU y otros organismos promueven cooperación, diálogo y acuerdos para afrontar problemas compartidos.",
            "Participar responsablemente implica informarse, respetar la diversidad y actuar frente a las desigualdades.",
        ],
        "questions": [
            _language_question("¿Qué son los derechos humanos?", "Derechos de todas las personas por su dignidad", "Privilegios de un solo grupo", "Premios para algunos países", 0),
            _language_question("¿Qué significa ciudadanía global?", "Asumir responsabilidades con una comunidad mundial", "Vivir sin relacionarse con otros", "Ignorar los problemas de otros países", 1),
            _language_question("¿Qué promueve la ONU?", "Cooperación y diálogo entre países", "Aislamiento total", "Competencia sin acuerdos", 2),
            _language_question("¿Qué valor protege los derechos humanos?", "La dignidad", "El desprecio", "La indiferencia", 0),
            _language_question("¿Qué situación vulnera un derecho?", "Impedir la educación por el origen de una persona", "Garantizar atención médica", "Escuchar distintas opiniones", 1),
            _language_question("¿Qué ayuda a combatir un prejuicio?", "Informarse y escuchar experiencias diversas", "Repetir estereotipos", "Excluir a un grupo", 2),
            _language_question("¿Por qué un problema ambiental puede ser global?", "Porque sus efectos atraviesan fronteras", "Porque solo ocurre en una casa", "Porque no afecta a nadie", 0),
            _language_question("¿Qué acción muestra solidaridad internacional?", "Cooperar para responder a una emergencia", "Ocultar información", "Negarse a dialogar", 1),
            _language_question("¿Qué relación hay entre derechos y deberes?", "Respetar los derechos propios y ajenos exige responsabilidades", "Los derechos eliminan toda responsabilidad", "Los deberes solo pertenecen a otros", 2),
            _language_question("¿Qué hace un ciudadano global responsable?", "Se informa, participa y respeta la diversidad", "Comparte rumores", "Decide sin escuchar", 0),
        ],
    },
    "social-geography": {
        "title": "Continentes, husos horarios y globalización",
        "description": "Interpreta relaciones entre continentes, horarios, territorios y procesos de globalización.",
        "objective": "Ubicar continentes, comprender husos horarios y analizar conexiones globales y geopolíticas.",
        "learning_order": 2,
        "learning_phase": "Explorar",
        "lesson": [
            "Los continentes son grandes extensiones de tierra con territorios, pueblos y paisajes diversos.",
            "Los husos horarios organizan la hora del planeta según la rotación de la Tierra y la posición este-oeste.",
            "La globalización conecta países mediante comercio, tecnología, migraciones, información y cultura.",
            "La geopolítica estudia cómo se relacionan poder, territorio, recursos y decisiones entre países y regiones.",
        ],
        "questions": [
            _language_question("¿Qué es un continente?", "Una gran extensión de tierra con diversos territorios", "Un barrio", "Un río pequeño", 0),
            _language_question("¿Para qué sirven los husos horarios?", "Para organizar las horas según la ubicación del planeta", "Para medir la altura de una montaña", "Para dividir una ciudad en barrios", 1),
            _language_question("¿Por qué cambia la hora entre lugares del mundo?", "Por la rotación de la Tierra y la posición este-oeste", "Por el color de las banderas", "Porque todos los relojes están dañados", 2),
            _language_question("¿Qué facilita la globalización?", "Intercambios, comunicaciones y conexiones entre países", "El aislamiento completo", "La desaparición de los territorios", 0),
            _language_question("¿Qué estudia la geopolítica?", "Relaciones de poder, territorio y recursos", "La ortografía de una lengua", "El crecimiento de una planta", 1),
            _language_question("¿Qué puede circular entre países?", "Bienes, información, personas y conocimientos", "Solo fronteras", "Únicamente montañas", 2),
            _language_question("¿Qué muestra un mapa político mundial?", "Países, fronteras y capitales", "Solo la profundidad del océano", "Los sentimientos de una población", 0),
            _language_question("¿Qué riesgo puede tener la globalización?", "Aumentar desigualdades si los beneficios no se distribuyen justamente", "Eliminar toda comunicación", "Hacer iguales todos los paisajes", 1),
            _language_question("¿Qué actitud favorece las relaciones internacionales?", "Cooperar y respetar acuerdos", "Imponer decisiones siempre", "Desinformar a otros países", 2),
            _language_question("¿Qué debemos considerar al estudiar un territorio?", "Sus personas, recursos, historia y relaciones de poder", "Solo su tamaño", "Únicamente el nombre de su capital", 0),
        ],
    },
    "social-history": {
        "title": "Historia mundial: civilizaciones y revoluciones",
        "description": "Relaciona civilizaciones, revoluciones y procesos históricos con sus causas y consecuencias.",
        "objective": "Explicar cambios de la historia mundial usando causas, consecuencias, fuentes y distintas perspectivas.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "lesson": [
            "Una civilización organiza formas de vida, gobierno, economía, conocimientos y cultura en un periodo histórico.",
            "Las revoluciones son procesos de cambios profundos que pueden transformar la política, la economía y la sociedad.",
            "Los hechos históricos tienen causas y consecuencias. Una explicación completa relaciona varias razones y efectos.",
            "Las fuentes ofrecen perspectivas; compararlas permite evitar explicaciones únicas y comprender voces diferentes.",
        ],
        "questions": [
            _language_question("¿Qué es una civilización?", "Una sociedad con formas organizadas de vida y cultura", "Una sola persona", "Un fenómeno meteorológico", 0),
            _language_question("¿Qué puede producir una revolución?", "Cambios profundos en una sociedad", "Solo un cambio de estación", "Una operación matemática", 1),
            _language_question("¿Qué relación ayuda a explicar un proceso histórico?", "Causas y consecuencias", "Colores y tamaños", "Rumores y adivinanzas", 2),
            _language_question("¿Qué aspecto puede estudiarse de una civilización?", "Su organización, conocimientos y cultura", "Solo el clima de un día", "Únicamente el nombre de una persona", 0),
            _language_question("¿Qué es una fuente histórica?", "Una evidencia que permite conocer e interpretar el pasado", "Una predicción sin datos", "Una opinión anónima sin contexto", 1),
            _language_question("¿Por qué puede haber distintas perspectivas históricas?", "Porque las personas y grupos viven los hechos de maneras diferentes", "Porque no existen hechos", "Porque las fechas no importan", 2),
            _language_question("¿Qué pregunta ayuda a analizar una revolución?", "¿Qué causas tuvo y qué cambios produjo?", "¿Qué color era más popular?", "¿Cómo borrar sus consecuencias?", 0),
            _language_question("¿Qué hace una línea de tiempo?", "Ordena procesos y muestra su duración", "Reemplaza todas las fuentes", "Mide la economía actual", 1),
            _language_question("¿Qué debemos hacer con una fuente histórica?", "Ubicarla en su contexto y compararla con otras", "Creerla sin analizar", "Cambiarle la fecha", 2),
            _language_question("¿Qué aprendemos al estudiar la historia mundial?", "Comprendemos cambios, conexiones y decisiones humanas", "Que todas las sociedades fueron iguales", "Que el pasado no influye en el presente", 0),
        ],
    },
    "social-economy": {
        "title": "Emprendimiento, finanzas y desigualdad",
        "description": "Analiza proyectos, decisiones financieras y desigualdades desde una perspectiva responsable y sostenible.",
        "objective": "Comprender emprendimiento, finanzas, desigualdad e impacto social y ambiental de las decisiones económicas.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "project": "Proyecto ODS local",
        "lesson": [
            "Emprender significa identificar una necesidad y diseñar una solución que genere valor, no solo ganar dinero.",
            "La educación financiera ayuda a planear ingresos, gastos, ahorro, crédito y riesgos antes de decidir.",
            "La desigualdad aparece cuando las oportunidades o los recursos se distribuyen de manera injusta entre personas o grupos.",
            "Un proyecto sostenible considera el impacto social, económico y ambiental y se relaciona con los Objetivos de Desarrollo Sostenible.",
        ],
        "questions": [
            _language_question("¿Qué significa emprender?", "Crear una solución o proyecto para una necesidad", "Gastar sin plan", "Copiar sin propósito", 0),
            _language_question("¿Qué ayuda a tomar una decisión financiera?", "Comparar ingresos, gastos, riesgos y metas", "Ignorar los costos", "Comprar siempre a crédito", 1),
            _language_question("¿Qué es la desigualdad?", "Distribución injusta de oportunidades o recursos", "Que todos tengan lo mismo", "Una actividad comercial", 2),
            _language_question("¿Qué puede hacer responsable a un emprendimiento?", "Considerar a las personas y el ambiente", "Ignorar residuos y trabajadores", "Buscar ganancias sin límites", 0),
            _language_question("¿Qué es el ahorro?", "Guardar recursos para una meta o necesidad futura", "Gastar todo el ingreso", "Una deuda obligatoria", 1),
            _language_question("¿Qué significa pedir un crédito?", "Recibir dinero que debe devolverse según unas condiciones", "Recibir dinero sin compromiso", "Intercambiar un mapa", 2),
            _language_question("¿Qué busca un proyecto ODS local?", "Aportar a un problema social o ambiental de la comunidad", "Resolver todos los problemas del mundo en un día", "Vender sin analizar necesidades", 0),
            _language_question("¿Qué decisión reduce la desigualdad?", "Ampliar oportunidades de educación y participación", "Excluir a quien tiene menos recursos", "Ocultar información", 1),
            _language_question("¿Qué debe analizar un presupuesto?", "Ingresos, gastos y prioridades", "Solo deseos", "Únicamente el color de una moneda", 2),
            _language_question("¿Qué criterio ayuda a elegir un producto?", "Necesidad, precio, calidad e impacto", "La publicidad más llamativa siempre", "Comprar sin comparar", 0),
        ],
    },
    "social-explorer": {
        "title": "Modelo ONU: decisiones globales",
        "description": "Representa países, escucha posturas y negocia acuerdos sobre un desafío mundial.",
        "objective": "Consolidar ciudadanía global mediante diálogo, argumentos, negociación y acuerdos internacionales.",
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "prerequisites": ["social-identity", "social-geography"],
        "related_activity": "social-identity",
        "questions": [
            _language_question("¿Qué se hace en un Modelo ONU?", "Se representan países y se dialoga sobre problemas globales", "Se compite sin reglas", "Se estudia solo un mapa", 0),
            _language_question("¿Qué debe investigar una delegación?", "La postura, necesidades y propuestas del país que representa", "Solo el nombre de su capital", "Una opinión sin datos", 1),
            _language_question("¿Qué ayuda a construir un argumento?", "Evidencias y razones claras", "Gritos y amenazas", "Rumores", 2),
            _language_question("¿Qué significa negociar?", "Buscar un acuerdo entre distintas posiciones", "Obligar a todos a aceptar una idea", "Evitar escuchar", 0),
            _language_question("¿Qué actitud favorece el debate?", "Escuchar, respetar turnos y responder con razones", "Interrumpir constantemente", "Burlarse de otra delegación", 1),
            _language_question("¿Qué es una resolución?", "Un acuerdo escrito con acciones propuestas", "Un mapa físico", "Una opinión secreta", 2),
            _language_question("¿Por qué los problemas globales requieren cooperación?", "Porque afectan a varios países y necesitan acciones coordinadas", "Porque un país puede resolverlos todos solo", "Porque no tienen causas", 0),
            _language_question("¿Qué propuesta es más sostenible?", "Reducir emisiones y proteger comunidades vulnerables", "Aumentar residuos sin control", "Ignorar el impacto ambiental", 1),
            _language_question("¿Qué debe hacer una delegación si cambia de opinión?", "Explicar sus razones y buscar un acuerdo", "Ocultar el cambio", "Atacar a las demás", 2),
            _language_question("¿Qué aprendizaje consolida el Modelo ONU?", "Participar, argumentar y cooperar para resolver desafíos comunes", "Ganar una discusión por fuerza", "Decidir sin escuchar a nadie", 0),
        ],
    },
}


FIRST_GRADE_SCIENCE_CONTENT = {
    "science-life": {
        "title": "Mi cuerpo y mis sentidos",
        "description": "Reconoce partes del cuerpo, sentidos y hábitos para observar y cuidar la vida.",
        "objective": "Identificar partes del cuerpo, relacionar sentidos con estímulos y practicar hábitos de cuidado.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "lesson": [
            "El cuerpo está formado por partes que trabajan juntas. Podemos nombrarlas y observar cómo nos ayudan.",
            "Los sentidos nos permiten conocer el entorno: vemos con los ojos, escuchamos con los oídos, olemos con la nariz, saboreamos con la lengua y tocamos con la piel.",
            "Lavarnos las manos, alimentarnos bien, descansar y movernos ayudan a cuidar el cuerpo.",
            "Observar también significa usar los sentidos con atención y describir lo que encontramos.",
        ],
        "questions": [
            _language_question("¿Con qué vemos?", "Con los ojos", "Con las orejas", "Con las manos", 0),
            _language_question("¿Con qué escuchamos los sonidos?", "Con los oídos", "Con la nariz", "Con los pies", 1),
            _language_question("¿Qué sentido usamos para reconocer un olor?", "El olfato", "La vista", "El equilibrio", 2),
            _language_question("¿Qué parte del cuerpo usamos para caminar?", "Las piernas y los pies", "Los ojos", "Los dientes", 0),
            _language_question("¿Qué órgano usamos para saborear?", "La lengua", "La piel", "El cabello", 1),
            _language_question("¿Qué sentido usamos al tocar una superficie?", "El tacto", "La audición", "El gusto", 2),
            _language_question("¿Cuál hábito cuida el cuerpo?", "Lavarse las manos", "Dormir muy poco", "Comer solo dulces", 0),
            _language_question("¿Qué hacemos para cuidar los dientes?", "Los cepillamos", "Los cubrimos con tierra", "Dejamos de beber agua", 1),
            _language_question("¿Qué significa observar?", "Mirar o explorar con atención", "Inventar sin mirar", "Romper lo que encontramos", 2),
            _language_question("¿Qué debemos hacer si sentimos dolor?", "Contárselo a un adulto de confianza", "Ocultarlo siempre", "Seguir lastimándonos", 0),
        ],
    },
    "science-matter": {
        "title": "Materiales y sus propiedades",
        "description": "Observa objetos, compara materiales y clasifícalos según sus propiedades.",
        "objective": "Reconocer materiales naturales y fabricados y comparar propiedades observables de los objetos.",
        "learning_order": 2,
        "learning_phase": "Explorar",
        "lesson": [
            "Los objetos están hechos de materiales. Podemos observar sus propiedades: si son duros, suaves, flexibles, transparentes, opacos o absorbentes.",
            "Algunos materiales vienen de la naturaleza, como madera, piedra y algodón; otros son fabricados, como plástico y vidrio.",
            "Clasificar significa agrupar objetos que comparten una característica.",
            "Para investigar, compara con cuidado, describe lo que observas y usa los materiales de forma segura.",
        ],
        "questions": [
            _language_question("¿Qué material puede ser transparente?", "El vidrio", "La piedra", "La madera opaca", 0),
            _language_question("¿Qué objeto suele ser flexible?", "Una goma", "Un ladrillo", "Un vaso de vidrio", 1),
            _language_question("¿Qué significa clasificar?", "Agrupar por características", "Mezclar todo sin observar", "Romper los objetos", 2),
            _language_question("¿Cuál es un material natural?", "La madera", "El plástico", "El nailon", 0),
            _language_question("¿Qué material absorbe agua fácilmente?", "Una esponja", "Un espejo", "Una cuchara metálica", 1),
            _language_question("¿Cuál objeto es opaco?", "Una caja de cartón", "Una ventana limpia", "Un vaso transparente", 2),
            _language_question("¿Qué propiedad tiene una piedra?", "Puede ser dura", "Siempre es flexible", "Es transparente", 0),
            _language_question("¿Qué podemos hacer antes de elegir un material?", "Observar sus propiedades y su uso", "Usarlo sin cuidado", "Ignorar si es seguro", 1),
            _language_question("¿Qué material se fabrica a partir de plantas?", "El papel", "El vidrio", "El metal", 2),
            _language_question("¿Qué acción cuida los materiales?", "Reutilizar y ordenar los objetos", "Desperdiciarlos", "Dejarlos tirados", 0),
        ],
    },
    "science-earth": {
        "title": "Día, noche y cuidado de la Tierra",
        "description": "Observa cambios del cielo, reconoce día y noche y propone acciones para cuidar el planeta.",
        "objective": "Distinguir día y noche, observar cambios del tiempo y practicar el cuidado de la Tierra.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "project": "Diario del tiempo durante una semana",
        "lesson": [
            "El Sol ilumina la Tierra. Durante el día vemos más luz y por la noche observamos oscuridad y, a veces, la Luna y estrellas.",
            "El tiempo atmosférico puede cambiar: algunos días hay sol, nubes, lluvia o viento. Podemos observarlo y registrarlo.",
            "Las estaciones producen cambios en algunos lugares y se relacionan con la forma en que recibimos luz y calor del Sol.",
            "Cuidamos la Tierra ahorrando agua y energía, separando residuos y protegiendo plantas y animales.",
        ],
        "questions": [
            _language_question("¿Cuándo recibimos más luz del Sol?", "Durante el día", "Durante la noche siempre", "Dentro de una cueva", 0),
            _language_question("¿Qué podemos observar en el cielo nocturno?", "La Luna y las estrellas", "El arcoíris siempre", "El Sol brillando igual", 1),
            _language_question("¿Qué produce una sombra?", "Un objeto bloquea la luz", "El sonido", "Una comida", 2),
            _language_question("¿Qué describe el tiempo atmosférico?", "Si hay sol, nubes, lluvia o viento", "El nombre de una persona", "La edad de una casa", 0),
            _language_question("¿Qué instrumento ayuda a saber si llueve?", "Un pluviómetro", "Una almohada", "Un mapa de calles", 1),
            _language_question("¿Qué acción ahorra agua?", "Cerrar la llave mientras nos enjabonamos", "Dejarla abierta", "Jugar a desperdiciarla", 2),
            _language_question("¿Qué hacemos con una botella que puede reutilizarse?", "La usamos de nuevo o la llevamos al reciclaje", "La arrojamos al río", "La dejamos en el parque", 0),
            _language_question("¿Qué necesitan las plantas para vivir?", "Agua, luz y cuidado", "Solo juguetes", "Humo", 1),
            _language_question("¿Qué podemos anotar en un diario del tiempo?", "Nubes, lluvia, viento o temperatura aproximada", "El precio de una comida", "Los nombres de todos los vecinos", 2),
            _language_question("¿Por qué cuidamos la Tierra?", "Porque compartimos sus recursos con otros seres vivos", "Porque los recursos son infinitos", "Porque no necesitamos plantas", 0),
        ],
    },
    "science-technology": {
        "title": "Herramientas, higiene y seguridad",
        "description": "Reconoce herramientas sencillas, hábitos de higiene y normas para actuar con seguridad.",
        "objective": "Relacionar herramientas con sus usos y aplicar hábitos de higiene y seguridad en casa y escuela.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "lesson": [
            "Las herramientas ayudan a realizar tareas: una regla mide, unas tijeras cortan y una lupa permite observar detalles.",
            "La tecnología incluye objetos y conocimientos que las personas usan para resolver necesidades.",
            "La higiene protege nuestra salud: lavarnos las manos, cubrirnos al toser y mantener limpios los espacios son acciones importantes.",
            "Las normas de seguridad indican cómo prevenir accidentes. Pedimos ayuda adulta para usar objetos peligrosos o desconocidos.",
        ],
        "questions": [
            _language_question("¿Para qué sirve una regla?", "Para medir longitudes", "Para escuchar sonidos", "Para cocinar agua", 0),
            _language_question("¿Para qué sirve una lupa?", "Para observar detalles más grandes", "Para cortar papel", "Para medir la lluvia", 1),
            _language_question("¿Qué herramienta ayuda a cortar papel?", "Las tijeras", "La regla", "El termómetro", 2),
            _language_question("¿Cuándo debemos lavarnos las manos?", "Antes de comer y después de ir al baño", "Solo una vez al año", "Después de dormir únicamente", 0),
            _language_question("¿Qué hacemos al toser?", "Nos cubrimos con el codo o un pañuelo", "Tosemos sobre otras personas", "Quitamos todas las señales", 1),
            _language_question("¿Qué norma es segura?", "Pedir ayuda adulta para usar objetos peligrosos", "Tocar enchufes con las manos mojadas", "Correr con tijeras abiertas", 2),
            _language_question("¿Qué problema resuelve una herramienta?", "Facilita una tarea", "Hace que no debamos pensar", "Reemplaza todos los cuidados", 0),
            _language_question("¿Qué debemos hacer con los productos de limpieza?", "Mantenerlos fuera del alcance y seguir indicaciones adultas", "Probarlos", "Mezclarlos sin preguntar", 1),
            _language_question("¿Qué hábito cuida los espacios?", "Ordenar y limpiar después de trabajar", "Dejar objetos en el suelo", "Tirar residuos", 2),
            _language_question("¿Qué hacemos si encontramos un objeto desconocido?", "No lo tocamos y avisamos a un adulto", "Lo probamos inmediatamente", "Lo llevamos a la boca", 0),
        ],
    },
    "science-lab": {
        "title": "Clasifica seres vivos y objetos",
        "description": "Observa pistas del laboratorio y clasifica seres vivos, objetos y materiales.",
        "objective": "Consolidar observación, clasificación y cuidado de seres vivos y objetos del entorno.",
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "prerequisites": ["science-life", "science-matter"],
        "related_activity": "science-life",
        "questions": [
            _language_question("¿Cuál es un ser vivo?", "Una planta", "Una piedra", "Una silla", 0),
            _language_question("¿Cuál es un objeto fabricado?", "Un cuaderno", "Un perro", "Un árbol", 1),
            _language_question("¿Qué necesita una planta para vivir?", "Agua y luz", "Una televisión", "Una moneda", 2),
            _language_question("¿Qué característica comparten los seres vivos?", "Nacen, crecen y necesitan cuidados", "Nunca cambian", "Están hechos de plástico", 0),
            _language_question("¿Qué material puede ser transparente?", "El vidrio", "La madera opaca", "La piedra", 1),
            _language_question("¿Qué usamos para observar una hoja con detalle?", "Una lupa", "Una alcancía", "Una cuchara", 2),
            _language_question("¿Dónde clasificamos una pelota?", "Entre los objetos", "Entre las plantas", "Entre los animales", 0),
            _language_question("¿Qué acción cuida un ser vivo?", "Darle agua y tratarlo con respeto", "Lastimarlo", "Dejar basura cerca", 1),
            _language_question("¿Qué criterio sirve para agrupar objetos?", "El material o la forma", "El nombre de quien los mira", "Un color elegido al azar", 2),
            _language_question("¿Qué hace un científico al observar?", "Mira con atención, compara y registra", "Inventa sin mirar", "Rompe todo", 0),
        ],
    },
}


SECOND_GRADE_SCIENCE_CONTENT = {
    "science-life": {
        "title": "Ciclos de vida",
        "description": "Observa cómo nacen, crecen y cambian las plantas, los animales y las personas.",
        "objective": "Reconocer etapas de ciclos de vida y necesidades de plantas, animales y seres humanos.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "lesson": [
            "Los seres vivos nacen, crecen, cambian y cumplen un ciclo de vida. Cada especie tiene etapas diferentes.",
            "Una semilla puede germinar y convertirse en planta si recibe agua, luz y condiciones adecuadas.",
            "Algunos animales cambian mucho, como la oruga que se convierte en mariposa; otros se parecen más a sus padres al crecer.",
            "Observar y registrar cambios ayuda a comprender los ciclos sin lastimar a los seres vivos.",
        ],
        "questions": [
            _language_question("¿Qué es un ciclo de vida?", "Las etapas por las que pasa un ser vivo", "Una lista de objetos", "Un cambio de clima", 0),
            _language_question("¿Qué necesita una semilla para germinar?", "Agua y condiciones adecuadas", "Una batería", "Una moneda", 1),
            _language_question("¿En qué se convierte una oruga?", "En mariposa", "En pez", "En roca", 2),
            _language_question("¿Cuál es una etapa de la vida humana?", "La infancia", "La evaporación", "La sombra", 0),
            _language_question("¿Qué parte ayuda a una planta a absorber agua?", "La raíz", "El pétalo", "El fruto", 1),
            _language_question("¿Qué tienen en común los seres vivos?", "Nacen, crecen y realizan funciones vitales", "Son todos iguales", "Nunca cambian", 2),
            _language_question("¿Qué ocurre después de que una semilla germina?", "Crece una planta pequeña", "Se convierte en una piedra", "Desaparece siempre", 0),
            _language_question("¿Qué debemos hacer al observar un animal pequeño?", "Mirarlo con cuidado y no lastimarlo", "Perseguirlo y tocarlo con fuerza", "Quitarle su refugio", 1),
            _language_question("¿Qué registro ayuda a estudiar una planta?", "Dibujos y medidas de sus cambios", "Un ruido sin fecha", "Una adivinanza", 2),
            _language_question("¿Por qué cada ser vivo tiene un ciclo diferente?", "Porque las especies crecen y cambian de distintas maneras", "Porque ningún ser vivo cambia", "Porque todos necesitan exactamente lo mismo", 0),
        ],
    },
    "science-matter": {
        "title": "Agua, luz, sombras y fuerzas",
        "description": "Explora cambios del agua, formación de sombras, imanes y efectos de las fuerzas.",
        "objective": "Describir cambios de estado del agua y observar efectos de luz, imanes y fuerzas sencillas.",
        "learning_order": 2,
        "learning_phase": "Explorar",
        "lesson": [
            "El agua puede estar líquida, sólida como el hielo o gaseosa como el vapor. El calor y el frío producen cambios.",
            "Las sombras aparecen cuando un objeto bloquea el paso de la luz. Su forma y tamaño pueden cambiar según la posición de la luz.",
            "Los imanes atraen algunos metales, pero no todos los materiales. Hay que probar y observar antes de concluir.",
            "Empujar y halar son fuerzas que pueden mover, detener o cambiar la dirección de un objeto.",
        ],
        "questions": [
            _language_question("¿Cómo se llama el agua congelada?", "Hielo", "Vapor", "Arena", 0),
            _language_question("¿Qué ocurre al calentar agua?", "Puede evaporarse", "Se convierte en piedra", "Desaparece sin cambio", 1),
            _language_question("¿Qué ocurre al enfriar mucho el agua?", "Puede convertirse en hielo", "Siempre se convierte en humo", "Se vuelve madera", 2),
            _language_question("¿Qué produce una sombra?", "Un objeto bloquea la luz", "El sonido", "El agua sola", 0),
            _language_question("¿Qué puede atraer un imán?", "Algunos metales", "Todas las telas", "El agua siempre", 1),
            _language_question("¿Qué hacemos al empujar un carrito?", "Aplicamos una fuerza que puede moverlo", "Le quitamos su color", "Lo convertimos en agua", 2),
            _language_question("¿Qué necesita una sombra?", "Una fuente de luz y un objeto que la bloquee", "Solo oscuridad", "Una planta y una semilla", 0),
            _language_question("¿Cuál objeto puede ser atraído por un imán?", "Un clip de metal", "Una hoja de papel", "Una goma", 1),
            _language_question("¿Qué pasa si halamos una cuerda?", "Aplicamos una fuerza hacia nosotros", "La cuerda produce luz", "La cuerda se convierte en agua", 2),
            _language_question("¿Qué debemos hacer en un experimento?", "Observar, comparar y registrar lo que ocurre", "Cambiar todas las condiciones sin mirar", "Inventar el resultado", 0),
        ],
    },
    "science-earth": {
        "title": "Luna, ciclo del agua y reciclaje",
        "description": "Reconoce fases de la Luna, cambios del agua y acciones para reducir residuos.",
        "objective": "Relacionar fases lunares y ciclo del agua con acciones de reciclaje y cuidado del planeta.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "project": "Siembra y observa un frijol",
        "lesson": [
            "La Luna refleja la luz del Sol y parece cambiar de forma según la parte iluminada que observamos.",
            "En el ciclo del agua, el agua se evapora, forma nubes, cae como precipitación y puede regresar a ríos y mares.",
            "El agua cambia de lugar y de estado, pero debemos evitar contaminarla porque todos los seres vivos la necesitan.",
            "Reducir, reutilizar y reciclar disminuye residuos. Separar materiales facilita que puedan aprovecharse de nuevo.",
        ],
        "questions": [
            _language_question("¿Por qué vemos la Luna iluminada?", "Porque refleja la luz del Sol", "Porque produce su propia luz como una bombilla", "Porque es de fuego", 0),
            _language_question("¿Qué puede cambiar durante las fases de la Luna?", "La parte iluminada que vemos", "El tamaño real de la Luna cada noche", "La dirección del viento siempre", 1),
            _language_question("¿Qué es la evaporación?", "El agua líquida pasa a vapor", "El vapor se convierte en hielo", "La lluvia se convierte en piedra", 2),
            _language_question("¿Qué forma las nubes en el ciclo del agua?", "El vapor de agua se enfría y se reúne", "Las piedras se derriten", "El suelo produce humo", 0),
            _language_question("¿Qué es la precipitación?", "Agua que cae de las nubes como lluvia o granizo", "Agua que desaparece para siempre", "Luz de la Luna", 1),
            _language_question("¿Qué acción ayuda a reciclar?", "Separar papel, vidrio y plástico según corresponda", "Mezclar todos los residuos", "Arrojar basura al río", 2),
            _language_question("¿Qué debemos hacer con una llave abierta sin necesidad?", "Cerrar la llave para ahorrar agua", "Dejarla abierta", "Usarla para mojar el suelo", 0),
            _language_question("¿Qué puede observarse en una siembra de frijol?", "Cómo germina y crece una planta", "Cómo una piedra nace", "Cómo desaparece el agua siempre", 1),
            _language_question("¿Qué significa reutilizar?", "Volver a usar un objeto para otra función o la misma", "Botarlo inmediatamente", "Quemarlo sin cuidado", 2),
            _language_question("¿Por qué cuidamos el ciclo del agua?", "Porque el agua es necesaria para la vida", "Porque solo sirve para jugar", "Porque nunca puede contaminarse", 0),
        ],
    },
    "science-technology": {
        "title": "Inventos y soluciones reutilizadas",
        "description": "Observa cómo los inventos resuelven necesidades y diseña soluciones usando materiales reutilizados.",
        "objective": "Relacionar necesidades con soluciones tecnológicas y proponer un objeto seguro con material reutilizado.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "lesson": [
            "Una invención es una solución creada por personas para responder a una necesidad o resolver un problema.",
            "Diseñar implica observar el problema, imaginar una idea, elegir materiales, construir y probar.",
            "Reutilizar materiales puede reducir residuos y convertir un objeto usado en una solución nueva.",
            "Una solución tecnológica debe ser útil, segura y respetuosa con las personas y el ambiente.",
        ],
        "questions": [
            _language_question("¿Qué es una invención?", "Una solución creada para una necesidad", "Un objeto sin propósito", "Un residuo sin uso", 0),
            _language_question("¿Qué hacemos primero al diseñar una solución?", "Identificar el problema o la necesidad", "Construir sin observar", "Comprar cualquier material", 1),
            _language_question("¿Qué significa reutilizar?", "Usar de nuevo un material u objeto", "Destruirlo siempre", "Dejarlo en la calle", 2),
            _language_question("¿Qué podríamos fabricar con una botella limpia?", "Un recipiente para guardar objetos", "Una bebida peligrosa", "Un enchufe", 0),
            _language_question("¿Qué debemos hacer después de construir un objeto?", "Probarlo y revisar si es seguro", "Usarlo sin mirar", "Ocultar si se rompe", 1),
            _language_question("¿Qué material puede reutilizarse para hacer una maceta?", "Una botella de plástico limpia", "Una batería dañada", "Un producto de limpieza abierto", 2),
            _language_question("¿Qué característica debe tener una buena solución?", "Ser útil y segura", "Ser peligrosa", "Producir más residuos sin necesidad", 0),
            _language_question("¿Qué herramienta ayuda a unir cartón?", "Pegamento usado con cuidado", "Agua hirviendo", "Un enchufe", 1),
            _language_question("¿Qué pregunta hacemos al evaluar un invento?", "¿Resuelve el problema y cuida el ambiente?", "¿Es el más costoso?", "¿Puedo usarlo sin normas?", 2),
            _language_question("¿Qué idea combina tecnología y cuidado ambiental?", "Construir un organizador con cajas reutilizadas", "Botar todas las cajas", "Usar más materiales sin plan", 0),
        ],
    },
    "science-lab": {
        "title": "Ciclo de vida interactivo",
        "description": "Ordena etapas y descubre cómo cambian plantas, animales y otros seres vivos.",
        "objective": "Consolidar la comprensión de ciclos de vida mediante secuencias y observaciones.",
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "prerequisites": ["science-life"],
        "related_activity": "science-life",
        "questions": [
            _language_question("¿Qué ocurre primero en el ciclo de una planta?", "La semilla germina", "Aparece el fruto", "La planta produce semillas nuevas", 0),
            _language_question("¿Qué etapa sigue a la oruga?", "La crisálida", "El huevo siempre", "La piedra", 1),
            _language_question("¿Qué necesita una semilla para comenzar a crecer?", "Agua y condiciones adecuadas", "Una moneda", "Una pantalla", 2),
            _language_question("¿Qué observamos para comparar dos ciclos?", "Sus etapas y cambios", "Solo sus colores", "El nombre del observador", 0),
            _language_question("¿Qué ciclo pertenece al agua?", "Evaporación, condensación y precipitación", "Nacimiento, escuela y juego", "Corte, pegado y dibujo", 1),
            _language_question("¿Qué registro muestra el crecimiento de una planta?", "Dibujos con fechas", "Un grito", "Una moneda", 2),
            _language_question("¿Por qué cuidamos los seres vivos del laboratorio?", "Porque son seres que necesitan respeto y condiciones adecuadas", "Porque son objetos", "Porque no cambian nunca", 0),
            _language_question("¿Qué animal cambia de oruga a adulto alado?", "La mariposa", "El pez", "La tortuga siempre", 1),
            _language_question("¿Qué pregunta ayuda a estudiar un ciclo?", "¿Qué cambia en cada etapa?", "¿Qué color tiene mi cuaderno?", "¿Cuánto pesa una sombra?", 2),
            _language_question("¿Qué habilidad practica este juego?", "Ordenar, observar y explicar cambios", "Adivinar sin pistas", "Romper materiales", 0),
        ],
    },
}


THIRD_GRADE_SCIENCE_CONTENT = {
    "science-life": {
        "title": "Plantas, animales y cadenas alimentarias",
        "description": "Relaciona partes de las plantas, necesidades de los animales y cadenas alimentarias.",
        "objective": "Explicar funciones de partes de plantas y relaciones alimentarias entre productores y consumidores.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "lesson": [
            "Las plantas tienen partes con funciones diferentes: la raíz absorbe agua y fija la planta, el tallo sostiene y transporta, y las hojas captan luz.",
            "Las plantas producen su alimento usando luz, agua y aire; por eso se llaman productores.",
            "Los animales obtienen energía al alimentarse de plantas u otros animales y se relacionan dentro de cadenas alimentarias.",
            "Cuidar un ecosistema significa proteger productores, consumidores y los lugares donde viven.",
        ],
        "questions": [
            _language_question("¿Qué parte de la planta absorbe agua del suelo?", "La raíz", "El pétalo", "El fruto", 0),
            _language_question("¿Qué función cumple el tallo?", "Sostiene y transporta sustancias", "Produce sonidos", "Atrapa animales siempre", 1),
            _language_question("¿Qué parte capta mucha luz?", "La hoja", "La raíz", "La semilla enterrada", 2),
            _language_question("¿Qué organismo produce su propio alimento?", "Una planta", "Un león", "Un hongo de pan siempre", 0),
            _language_question("En hierba → conejo → zorro, la hierba es…", "Productor", "Consumidor primario", "Descomponedor siempre", 1),
            _language_question("En la cadena hierba → conejo → zorro, el conejo es…", "Consumidor", "Productor", "Planeta", 2),
            _language_question("¿Qué muestra una cadena alimentaria?", "Quién sirve de alimento a quién", "El tamaño de una roca", "La distancia al Sol", 0),
            _language_question("¿Qué podría ocurrir si desaparecen muchas plantas?", "Varios animales tendrían menos alimento", "Aumentaría el alimento para todos", "Nada cambiaría", 1),
            _language_question("¿Qué función tiene una flor en muchas plantas?", "Participar en la reproducción", "Absorber agua del suelo", "Moverse como un animal", 2),
            _language_question("¿Qué acción protege una cadena alimentaria?", "Cuidar los hábitats y evitar contaminar", "Eliminar todos los productores", "Destruir los refugios", 0),
        ],
    },
    "science-matter": {
        "title": "Mezclas, energía y máquinas simples",
        "description": "Separa mezclas, reconoce formas de energía y explora máquinas simples que facilitan el trabajo.",
        "objective": "Distinguir mezclas, transformaciones de energía y usos de máquinas simples en situaciones cotidianas.",
        "learning_order": 2,
        "learning_phase": "Explorar",
        "lesson": [
            "Una mezcla reúne dos o más materiales. Algunas mezclas pueden separarse usando propiedades como tamaño, magnetismo o solubilidad.",
            "La energía puede presentarse como luz, calor, movimiento o sonido y puede transformarse de una forma a otra.",
            "Las máquinas simples, como la palanca, la polea y el plano inclinado, ayudan a mover objetos aplicando fuerzas.",
            "Investigar implica describir materiales, anticipar qué ocurrirá y comprobarlo con cuidado.",
        ],
        "questions": [
            _language_question("¿Qué es una mezcla?", "La combinación de dos o más materiales", "Un material completamente solo", "Una sombra", 0),
            _language_question("¿Qué mezcla puede separarse con un colador?", "Arena y piedras", "Agua y azúcar disuelta", "Aire", 1),
            _language_question("¿Qué mezcla puede separarse con un imán?", "Clips y arena", "Agua y sal disuelta", "Papel y agua evaporada", 2),
            _language_question("¿Qué forma de energía da una bombilla encendida?", "Luz", "Masa", "Una planta", 0),
            _language_question("¿Qué forma de energía produce un tambor al sonar?", "Sonido", "Hielo", "Metal quieto", 1),
            _language_question("¿Qué máquina simple es una rampa?", "Un plano inclinado", "Un termómetro", "Una brújula", 2),
            _language_question("¿Qué hace una palanca?", "Ayuda a mover una carga", "Produce lluvia", "Mide la temperatura", 0),
            _language_question("¿Qué fuente de energía es renovable?", "El Sol", "El carbón", "El petróleo", 1),
            _language_question("¿Qué sucede al frotar dos superficies?", "Puede aparecer fricción", "Se crea una planta", "Desaparece la materia", 2),
            _language_question("¿Qué hacemos al investigar una mezcla?", "Observamos, probamos una separación segura y registramos", "Mezclamos todo sin mirar", "Inventamos el resultado", 0),
        ],
    },
    "science-earth": {
        "title": "Sistema solar, Tierra y volcanes",
        "description": "Ubica la Tierra en el sistema solar y reconoce capas, volcanes y cambios del planeta.",
        "objective": "Describir componentes del sistema solar, capas básicas de la Tierra y formación de volcanes.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "lesson": [
            "El sistema solar está formado por el Sol y cuerpos que se mueven a su alrededor, como planetas, satélites y otros objetos.",
            "La Tierra tiene capas; en su interior hay materiales muy calientes y en la superficie se encuentran continentes, océanos y seres vivos.",
            "Un volcán es una abertura por la que pueden salir lava, gases y cenizas desde el interior de la Tierra.",
            "Observar modelos y mapas ayuda a estudiar fenómenos que no podemos mirar directamente bajo la superficie.",
        ],
        "questions": [
            _language_question("¿Qué ocupa el centro del sistema solar?", "El Sol", "La Luna", "La Tierra siempre", 0),
            _language_question("¿Qué es la Tierra?", "Un planeta que gira alrededor del Sol", "Una estrella", "Un satélite del Sol", 1),
            _language_question("¿Qué gira alrededor de un planeta?", "Un satélite natural", "Una montaña", "Una nube de lluvia siempre", 2),
            _language_question("¿Qué encontramos en la superficie terrestre?", "Continentes, océanos y seres vivos", "Solo rocas calientes", "Únicamente gases", 0),
            _language_question("¿Qué es un volcán?", "Una abertura por donde pueden salir materiales del interior terrestre", "Una estrella cercana", "Una máquina para producir lluvia", 1),
            _language_question("¿Qué puede salir durante una erupción?", "Lava, gases y ceniza", "Hielo y algodón", "Agua dulce siempre", 2),
            _language_question("¿Qué capa está formada por el suelo y la parte rocosa superficial?", "La corteza", "El núcleo", "La atmósfera completa", 0),
            _language_question("¿Por qué usamos modelos de la Tierra?", "Para representar partes o procesos difíciles de observar directamente", "Para cambiar la forma real del planeta", "Para demostrar que no existen capas", 1),
            _language_question("¿Qué astro ilumina a la Tierra?", "El Sol", "Un volcán", "Una nube", 2),
            _language_question("¿Qué conducta es segura al estudiar un volcán?", "Observar modelos y seguir indicaciones adultas", "Acercarse a una erupción real", "Tocar lava", 0),
        ],
    },
    "science-technology": {
        "title": "Programación y soluciones tecnológicas",
        "description": "Ordena instrucciones y diseña soluciones tecnológicas para necesidades reales.",
        "objective": "Reconocer algoritmos sencillos y diseñar una solución tecnológica segura y sostenible.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "project": "Circuito simple (pila + LED)",
        "lesson": [
            "Un algoritmo es una serie ordenada de instrucciones para resolver un problema o realizar una tarea.",
            "En la programación por bloques usamos secuencias, repeticiones y decisiones para dar instrucciones claras.",
            "Diseñar una solución implica identificar una necesidad, proponer ideas, construir un prototipo y probarlo.",
            "Un circuito sencillo necesita una fuente de energía, un camino cerrado y un componente que use la energía. Las conexiones deben hacerse con supervisión adulta.",
        ],
        "questions": [
            _language_question("¿Qué es un algoritmo?", "Una serie ordenada de instrucciones", "Una colección de objetos", "Un material natural", 0),
            _language_question("¿Qué bloque ayuda a repetir una acción?", "Repetir", "Borrar", "Dibujar sin orden", 1),
            _language_question("¿Qué hace una condición en un programa?", "Permite decidir según una situación", "Apaga siempre todo", "Cambia un material en agua", 2),
            _language_question("¿Qué hacemos primero al diseñar una solución?", "Identificar la necesidad o problema", "Construir sin observar", "Elegir un color al azar", 0),
            _language_question("¿Qué es un prototipo?", "Un modelo inicial que se puede probar", "El resultado definitivo siempre", "Una instrucción aislada", 1),
            _language_question("¿Qué necesita un circuito simple para funcionar?", "Fuente, camino cerrado y componente", "Solo un dibujo", "Un camino roto", 2),
            _language_question("¿Qué hace un LED en un circuito?", "Puede emitir luz", "Produce suelo", "Mide el tiempo", 0),
            _language_question("¿Qué debemos hacer al probar un diseño?", "Observar resultados y mejorarlo", "Ocultar los errores", "Cambiar todo sin registrar", 1),
            _language_question("¿Qué solución es sostenible?", "Usar materiales adecuados y reducir residuos", "Desperdiciar energía", "Crear basura sin necesidad", 2),
            _language_question("¿Qué norma es importante con una pila y un LED?", "Seguir instrucciones y pedir supervisión adulta", "Conectar cables a enchufes sin ayuda", "Tocar conexiones con manos mojadas", 0),
        ],
    },
    "science-lab": {
        "title": "Construye una cadena alimentaria",
        "description": "Ordena productores y consumidores y descubre cómo se relacionan en un ecosistema.",
        "objective": "Consolidar la interpretación de cadenas alimentarias y el cuidado de los ecosistemas.",
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "prerequisites": ["science-life"],
        "related_activity": "science-life",
        "questions": [
            _language_question("¿Qué debe aparecer primero en muchas cadenas alimentarias?", "Un productor como una planta", "Un depredador siempre", "Una roca", 0),
            _language_question("En pasto → saltamontes → rana, ¿qué come el saltamontes?", "Pasto", "Rana", "Agua", 1),
            _language_question("En algas → pez → garza, la garza es…", "Un consumidor", "Un productor", "Una planta", 2),
            _language_question("¿Qué indican las flechas de una cadena?", "El paso del alimento y la energía", "La dirección del viento", "El tamaño de los animales", 0),
            _language_question("¿Qué ocurriría si desaparece un productor?", "Se afecta el alimento de otros seres", "Todos tendrían más alimento", "Nada cambiaría", 1),
            _language_question("¿Qué organismo produce alimento usando luz?", "Una planta", "Un zorro", "Un hongo siempre", 2),
            _language_question("¿Qué es un consumidor?", "Un ser vivo que obtiene alimento de otros", "Un objeto sin vida", "Una fuente de luz", 0),
            _language_question("¿Qué cadena está ordenada correctamente?", "Hierba → conejo → zorro", "Zorro → hierba → conejo", "Conejo → zorro → hierba siempre", 1),
            _language_question("¿Qué ayuda a mantener una cadena alimentaria?", "Proteger el hábitat y sus seres vivos", "Contaminar el agua", "Eliminar las plantas", 2),
            _language_question("¿Qué habilidad practica este juego?", "Construir, ordenar y explicar relaciones alimentarias", "Adivinar sin observar", "Separar mezclas con un imán", 0),
        ],
    },
}


FOURTH_GRADE_SCIENCE_CONTENT = {
    "science-life": {
        "title": "Sistemas del cuerpo y ecosistemas",
        "description": "Relaciona órganos, sistemas del cuerpo e interacciones entre seres vivos y ambiente.",
        "objective": "Explicar funciones de sistemas corporales y relaciones entre factores vivos y no vivos de un ecosistema.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "lesson": [
            "Los órganos trabajan juntos en sistemas. El sistema respiratorio incorpora oxígeno y el circulatorio transporta sustancias por el cuerpo.",
            "El sistema digestivo transforma alimentos para obtener nutrientes y energía; el cuidado del cuerpo requiere hábitos saludables.",
            "Los ecosistemas reúnen seres vivos y elementos no vivos que interactúan en un lugar.",
            "La biodiversidad y las relaciones entre organismos ayudan a mantener el equilibrio; proteger hábitats reduce daños.",
        ],
        "questions": [
            _language_question("¿Qué sistema permite respirar?", "El sistema respiratorio", "El sistema solar", "El sistema monetario", 0),
            _language_question("¿Qué transporta el sistema circulatorio?", "Sangre y sustancias por el cuerpo", "Aire por las calles", "Luz hacia las plantas", 1),
            _language_question("¿Qué hace el sistema digestivo?", "Transforma alimentos y absorbe nutrientes", "Produce sonidos", "Forma montañas", 2),
            _language_question("¿Qué es un ecosistema?", "Seres vivos y su ambiente en interacción", "Solo una especie", "Una máquina aislada", 0),
            _language_question("¿Cuál es un factor no vivo de un ecosistema?", "La luz", "Un conejo", "Un árbol", 1),
            _language_question("¿Qué es una población?", "Individuos de la misma especie en un lugar", "Todos los planetas", "Una sola célula", 2),
            _language_question("¿Qué acción favorece la biodiversidad?", "Proteger los hábitats", "Destruir nidos", "Contaminar ríos", 0),
            _language_question("¿Qué relación existe entre plantas y animales en un ecosistema?", "Pueden relacionarse mediante alimento y refugio", "Nunca interactúan", "Solo comparten el color", 1),
            _language_question("¿Qué hábito ayuda a cuidar el sistema respiratorio?", "Evitar el humo y mantener espacios ventilados", "Respirar humo", "No beber agua nunca", 2),
            _language_question("¿Qué puede causar la pérdida de biodiversidad?", "Desequilibrios en los ecosistemas", "Más hábitats para todos", "Agua siempre más limpia", 0),
        ],
    },
    "science-matter": {
        "title": "Circuitos, energías renovables y palancas",
        "description": "Explora circuitos eléctricos, fuentes renovables y máquinas simples que facilitan el trabajo.",
        "objective": "Explicar circuitos cerrados, distinguir energías renovables y reconocer el uso de palancas.",
        "learning_order": 2,
        "learning_phase": "Explorar",
        "lesson": [
            "La electricidad circula por un circuito cuando existe un camino cerrado con una fuente, conductores y componentes.",
            "El cobre conduce electricidad y el plástico puede aislarla. Manipular circuitos requiere normas de seguridad.",
            "El Sol, el viento y el agua son fuentes renovables porque pueden regenerarse; usarlas responsablemente reduce impactos.",
            "Una palanca ayuda a mover una carga aplicando fuerza alrededor de un punto de apoyo.",
        ],
        "questions": [
            _language_question("¿Qué necesita un circuito para funcionar?", "Un camino cerrado", "Un camino roto", "Solo un dibujo", 0),
            _language_question("¿Qué material conduce bien la electricidad?", "El cobre", "El plástico", "La goma", 1),
            _language_question("¿Qué fuente de energía es renovable?", "El viento", "El carbón", "El petróleo", 2),
            _language_question("¿Qué ocurre si se abre un circuito?", "La corriente deja de circular", "La corriente aumenta siempre", "Se forma una planta", 0),
            _language_question("¿Qué función cumple una batería?", "Proporciona energía al circuito", "Aísla todos los cables", "Mide la lluvia", 1),
            _language_question("¿Qué hace una palanca?", "Ayuda a mover una carga", "Produce oxígeno", "Forma nubes", 2),
            _language_question("¿Qué acción ahorra energía?", "Apagar luces innecesarias", "Dejar aparatos encendidos", "Abrir el refrigerador mucho tiempo", 0),
            _language_question("¿Qué aprovecha la energía eólica?", "El movimiento del viento", "El calor de una roca", "La fuerza de una sombra", 1),
            _language_question("¿Por qué usamos plástico alrededor de un cable?", "Porque puede actuar como aislante", "Porque produce corriente", "Porque atrae todas las cargas", 2),
            _language_question("¿Qué norma es importante al armar un circuito?", "Trabajar con supervisión y evitar enchufes peligrosos", "Tocar cables mojados", "Unir cualquier cable sin revisar", 0),
        ],
    },
    "science-earth": {
        "title": "Relieve, ríos, mapas y riesgos naturales",
        "description": "Interpreta el relieve y los ríos mediante mapas y reconoce acciones ante riesgos naturales.",
        "objective": "Relacionar relieve, agua, mapas y prevención frente a riesgos naturales.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "project": "Modelo de volcán o relieve",
        "lesson": [
            "El relieve incluye montañas, valles, llanuras, mesetas y costas. Estas formas influyen en los paisajes y actividades humanas.",
            "Los ríos nacen en zonas altas y recorren el territorio hasta desembocar en otro río, lago o mar.",
            "Los mapas físicos representan relieve y cuerpos de agua; la escala, orientación y leyenda ayudan a leerlos.",
            "Un riesgo natural es la posibilidad de daño por fenómenos como inundaciones, terremotos o erupciones. Prevenir es conocer rutas y seguir indicaciones.",
        ],
        "questions": [
            _language_question("¿Qué es el relieve?", "Las formas de la superficie terrestre", "Una ley", "Una profesión", 0),
            _language_question("¿Qué es una llanura?", "Un terreno amplio y relativamente plano", "Una montaña muy alta siempre", "Un río subterráneo", 1),
            _language_question("¿Dónde suelen nacer los ríos?", "En zonas altas como montañas", "En el centro de una nube", "En una ciudad siempre", 2),
            _language_question("¿Qué muestra un mapa físico?", "Relieve, ríos y otras formas naturales", "Solo fronteras políticas", "El precio de las viviendas", 0),
            _language_question("¿Para qué sirve la escala?", "Para relacionar distancia del mapa y distancia real", "Para medir la lluvia directamente", "Para elegir una bandera", 1),
            _language_question("¿Qué es una inundación?", "Acumulación de agua que cubre lugares normalmente secos", "Una sequía", "Un movimiento de una estrella", 2),
            _language_question("¿Qué debemos hacer ante una alerta de riesgo?", "Seguir el plan y las indicaciones de seguridad", "Acercarnos a mirar el peligro", "Ignorar a las autoridades", 0),
            _language_question("¿Qué forma del relieve está rodeada de agua por varios lados?", "Una península", "Una llanura interior", "Un valle cerrado siempre", 1),
            _language_question("¿Qué puede representar un mapa de riesgos?", "Zonas que podrían verse afectadas por un fenómeno", "Solo nombres de animales", "El menú de una escuela", 2),
            _language_question("¿Por qué construimos un modelo de relieve?", "Para representar formas terrestres y comprenderlas", "Para cambiar el relieve real", "Para provocar una erupción", 0),
        ],
    },
    "science-technology": {
        "title": "Robótica, sensores y biomimética",
        "description": "Relaciona sensores y robots con soluciones inspiradas en la naturaleza y decisiones éticas.",
        "objective": "Comprender el funcionamiento básico de sensores y valorar impactos éticos de soluciones tecnológicas.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "lesson": [
            "Un sensor detecta cambios, como luz, temperatura, distancia o movimiento, y envía información a un sistema.",
            "Un robot combina estructura, energía, instrucciones y, en algunos casos, sensores para realizar tareas.",
            "La biomimética busca ideas en la naturaleza: una superficie puede inspirarse en una hoja o una estructura en un panal.",
            "La tecnología debe diseñarse con seguridad, accesibilidad y responsabilidad, considerando a quién beneficia y qué impactos produce.",
        ],
        "questions": [
            _language_question("¿Qué hace un sensor?", "Detecta cambios del entorno", "Produce una montaña", "Reemplaza todas las decisiones humanas", 0),
            _language_question("¿Qué puede detectar un sensor de luz?", "La cantidad de luz", "El sabor de una fruta", "La historia de un lugar", 1),
            _language_question("¿Qué necesita un robot para realizar una tarea?", "Energía e instrucciones", "Solo una decoración", "Una planta viva siempre", 2),
            _language_question("¿Qué es la biomimética?", "Inspirarse en la naturaleza para diseñar soluciones", "Imitar sonidos sin estudiar", "Destruir ecosistemas para construir", 0),
            _language_question("¿En qué puede inspirarse una estructura resistente?", "En un panal de abejas", "En una sombra", "En una nube sin forma", 1),
            _language_question("¿Qué debe considerar un diseño tecnológico?", "Seguridad, accesibilidad e impacto", "Solo que sea llamativo", "Que use más energía siempre", 2),
            _language_question("¿Qué hace un sensor de distancia?", "Detecta qué tan cerca está un objeto", "Cambia el clima", "Produce alimentos", 0),
            _language_question("¿Qué relación hay entre robot y programación?", "Las instrucciones orientan sus acciones", "Un robot funciona sin energía ni instrucciones", "La programación solo sirve para dibujar", 1),
            _language_question("¿Cuál solución es más ética?", "Una tecnología accesible que protege datos y personas", "Una máquina que excluye sin razón", "Un sistema que oculta sus riesgos", 2),
            _language_question("¿Qué hacemos al probar un prototipo?", "Registramos resultados y mejoramos el diseño", "Ignoramos errores", "Lo usamos sin normas", 0),
        ],
    },
    "science-lab": {
        "title": "Simulador de ecosistema",
        "description": "Observa relaciones entre seres vivos y ambiente y decide cómo proteger el equilibrio del ecosistema.",
        "objective": "Consolidar la comprensión de ecosistemas, biodiversidad e impacto de las acciones humanas.",
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "prerequisites": ["science-life", "science-earth"],
        "related_activity": "science-life",
        "questions": [
            _language_question("¿Qué elementos forman un ecosistema?", "Seres vivos y factores no vivos que interactúan", "Solo animales", "Solo agua", 0),
            _language_question("¿Qué factor no vivo influye en una planta?", "La luz", "Un conejo", "Un hongo siempre", 1),
            _language_question("¿Qué puede ocurrir si desaparece un hábitat?", "Muchas especies pierden refugio y alimento", "Aumenta siempre la biodiversidad", "Nada cambia", 2),
            _language_question("¿Qué acción protege un ecosistema?", "Restaurar hábitats y reducir contaminación", "Destruir nidos", "Introducir residuos", 0),
            _language_question("¿Qué relación muestra una cadena alimentaria?", "El paso de alimento y energía entre organismos", "El tamaño de las montañas", "La distancia a una ciudad", 1),
            _language_question("¿Qué es biodiversidad?", "Variedad de seres vivos", "Una sola especie", "Una máquina", 2),
            _language_question("¿Qué decisión mantiene un río saludable?", "Evitar verter contaminantes", "Arrojar basura", "Eliminar plantas de la orilla", 0),
            _language_question("¿Qué se puede observar en un simulador?", "Cómo cambian las relaciones al modificar condiciones", "El futuro exacto sin datos", "Una historia sin ambiente", 1),
            _language_question("¿Qué significa equilibrio de un ecosistema?", "Que sus relaciones pueden mantenerse sin cambios destructivos", "Que ningún organismo interactúa", "Que todos son iguales", 2),
            _language_question("¿Qué habilidad practica este juego?", "Analizar relaciones y tomar decisiones de conservación", "Adivinar sin observar", "Construir una oración", 0),
        ],
    },
}


FIFTH_GRADE_SCIENCE_CONTENT = {
    "science-life": {
        "title": "Células, adaptaciones y evolución",
        "description": "Comprende la célula como unidad de vida y relaciona adaptaciones con supervivencia y evolución.",
        "objective": "Reconocer células, niveles de organización y adaptaciones que favorecen la supervivencia de las especies.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "lesson": [
            "La célula es la unidad básica de los seres vivos. Algunas especies tienen una sola célula y otras están formadas por muchas.",
            "Las células cumplen funciones como obtener energía, crecer y reproducirse; en organismos complejos se organizan en tejidos y órganos.",
            "Las adaptaciones son características que ayudan a una población a vivir y reproducirse en un ambiente determinado.",
            "La evolución ocurre a lo largo de generaciones cuando las poblaciones cambian; no es una transformación inmediata de un individuo.",
        ],
        "questions": [
            _language_question("¿Qué es una célula?", "La unidad básica de un ser vivo", "Un planeta", "Un mineral", 0),
            _language_question("¿Qué pueden formar varias células organizadas?", "Tejidos y órganos", "Una nube", "Una montaña", 1),
            _language_question("¿Qué función cumple una célula?", "Realizar funciones vitales", "Producir mapas", "Medir una frontera", 2),
            _language_question("¿Qué es una adaptación?", "Una característica que ayuda a vivir en un ambiente", "Un cambio de ropa voluntario", "Un objeto fabricado", 0),
            _language_question("¿Qué adaptación ayuda al oso polar?", "Su pelaje aislante", "Sus alas", "Sus branquias", 1),
            _language_question("¿Qué adaptación ayuda a un pez?", "Las branquias para obtener oxígeno del agua", "El pelaje grueso", "Las raíces", 2),
            _language_question("¿Qué es una población?", "Individuos de la misma especie en un lugar", "Todos los planetas", "Una sola célula aislada", 0),
            _language_question("¿Qué significa que una población evoluciona?", "Cambia a lo largo de generaciones", "Cada individuo cambia de inmediato", "Deja de reproducirse siempre", 1),
            _language_question("¿Qué puede causar la pérdida de biodiversidad?", "Desequilibrios en los ecosistemas", "Más adaptaciones para todas las especies", "Hábitats siempre más seguros", 2),
            _language_question("¿Qué acción protege la diversidad de seres vivos?", "Conservar hábitats y reducir amenazas", "Destruir refugios", "Introducir contaminantes", 0),
        ],
    },
    "science-matter": {
        "title": "Reacciones, electricidad y método científico",
        "description": "Investiga transformaciones de la materia, circuitos eléctricos y conclusiones basadas en datos.",
        "objective": "Distinguir reacciones, comprender circuitos y aplicar pasos del método científico con evidencias.",
        "learning_order": 2,
        "learning_phase": "Explorar",
        "lesson": [
            "Una reacción química transforma unas sustancias en otras. Cambios de color, temperatura, gas o precipitado pueden ser evidencias.",
            "La electricidad se relaciona con cargas y puede circular por circuitos. Conductores y aislantes cumplen funciones diferentes.",
            "El método científico implica formular una pregunta, proponer una hipótesis, planear una prueba, recoger datos y elaborar una conclusión.",
            "Una conclusión debe responder la pregunta usando datos; si los resultados no apoyan la hipótesis, también enseñan algo.",
        ],
        "questions": [
            _language_question("¿Qué es una reacción química?", "Una transformación de sustancias", "Un cambio de lugar sin transformación", "Una sombra", 0),
            _language_question("¿Cuál puede ser una evidencia de reacción?", "Aparición de gas o cambio de color", "El objeto cambia de sitio solamente", "El nombre del experimento", 1),
            _language_question("¿Qué material conduce bien la electricidad?", "El cobre", "El plástico", "La goma", 2),
            _language_question("¿Qué hace un aislante?", "Dificulta el paso de la corriente", "Produce siempre electricidad", "Mide la masa", 0),
            _language_question("¿Qué necesita un circuito para funcionar?", "Un camino cerrado y una fuente", "Un camino roto", "Solo una etiqueta", 1),
            _language_question("¿Qué es una hipótesis?", "Una explicación provisional que se puede poner a prueba", "El resultado conocido antes de investigar", "Una opinión imposible de revisar", 2),
            _language_question("¿Qué se hace después de recoger datos?", "Se analizan para construir una conclusión", "Se eliminan si no gustan", "Se cambian sin registro", 0),
            _language_question("¿Qué variable se cambia en un experimento controlado?", "La variable que se quiere estudiar", "Todas al mismo tiempo siempre", "Ninguna condición", 1),
            _language_question("¿Qué debe hacer una conclusión?", "Responder con base en los datos", "Inventar resultados", "Ignorar observaciones", 2),
            _language_question("¿Qué norma protege al investigar electricidad?", "Usar materiales seguros y supervisión adecuada", "Tocar cables pelados", "Trabajar con agua cerca", 0),
        ],
    },
    "science-earth": {
        "title": "Universo, placas y cambio climático",
        "description": "Relaciona el universo, el movimiento de placas y el cambio climático con evidencias científicas.",
        "objective": "Explicar fenómenos del universo y la Tierra y reconocer causas y acciones frente al cambio climático.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "lesson": [
            "El universo contiene galaxias, estrellas, planetas y otros cuerpos. El sistema solar forma parte de la galaxia donde vivimos.",
            "La superficie terrestre está dividida en placas que se mueven lentamente; sus movimientos pueden relacionarse con terremotos y volcanes.",
            "El cambio climático incluye variaciones del clima; las actividades humanas pueden aumentar el calentamiento al emitir gases de efecto invernadero.",
            "Ahorrar energía, proteger ecosistemas y usar fuentes renovables son acciones que ayudan a reducir impactos.",
        ],
        "questions": [
            _language_question("¿Qué es una galaxia?", "Un conjunto de estrellas, gas y otros cuerpos", "Un solo planeta", "Una nube de lluvia", 0),
            _language_question("¿Dónde está el sistema solar?", "En una galaxia", "Dentro de un volcán", "En un océano", 1),
            _language_question("¿Qué son las placas tectónicas?", "Grandes fragmentos de la superficie terrestre que se mueven lentamente", "Nubes que producen lluvia", "Satélites artificiales", 2),
            _language_question("¿Qué puede producir el movimiento de placas?", "Terremotos y volcanes", "Cambios de color en las plantas solamente", "El día y la noche", 0),
            _language_question("¿Qué es el clima?", "Condiciones habituales de la atmósfera durante periodos largos", "El tiempo de una sola hora solamente", "La forma de una montaña", 1),
            _language_question("¿Qué puede aumentar el calentamiento global?", "La emisión excesiva de gases de efecto invernadero", "La protección de bosques", "El ahorro de energía", 2),
            _language_question("¿Qué efecto puede tener el cambio climático?", "Cambios en temperaturas, lluvias y ecosistemas", "Que desaparezcan todas las estaciones de inmediato", "Que no cambie ningún hábitat", 0),
            _language_question("¿Qué fuente ayuda a reducir combustibles fósiles?", "La energía solar", "El carbón", "El petróleo", 1),
            _language_question("¿Qué acción ayuda a enfrentar el cambio climático?", "Ahorrar energía y proteger bosques", "Aumentar residuos", "Quemar más combustibles", 2),
            _language_question("¿Por qué usamos evidencias para estudiar el clima?", "Para distinguir cambios observados de opiniones", "Para inventar datos", "Para evitar medir", 0),
        ],
    },
    "science-technology": {
        "title": "IA ética, datos y prototipos STEM",
        "description": "Diseña prototipos y reflexiona sobre inteligencia artificial, datos, tecnología y responsabilidad.",
        "objective": "Integrar ciencia, tecnología, ingeniería y matemáticas en prototipos responsables y decisiones éticas.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "project": "Proyecto feria de ciencias",
        "lesson": [
            "Un proyecto STEM integra ciencia, tecnología, ingeniería y matemáticas para investigar una pregunta o resolver una necesidad.",
            "Los datos son información que puede analizarse para encontrar patrones, pero deben recogerse y protegerse de manera responsable.",
            "La inteligencia artificial reconoce patrones mediante modelos y datos; no reemplaza automáticamente el juicio humano.",
            "Un prototipo se prueba y mejora. La ética exige considerar privacidad, inclusión, seguridad, sesgos e impacto ambiental.",
        ],
        "questions": [
            _language_question("¿Qué integra un proyecto STEM?", "Ciencia, tecnología, ingeniería y matemáticas", "Solo dibujos", "Únicamente opiniones", 0),
            _language_question("¿Qué son los datos?", "Información que puede observarse y analizarse", "Rumores sin registro", "Objetos que no informan", 1),
            _language_question("¿Qué puede hacer una inteligencia artificial?", "Reconocer patrones a partir de datos y modelos", "Pensar igual que una persona en todo", "Garantizar que nunca se equivoca", 2),
            _language_question("¿Qué protege la privacidad?", "Usar datos personales con permiso y cuidado", "Publicarlos sin preguntar", "Compartir contraseñas", 0),
            _language_question("¿Qué es un prototipo?", "Un modelo que se prueba y mejora", "Un producto que nunca se revisa", "Una conclusión sin datos", 1),
            _language_question("¿Qué es un sesgo en un sistema?", "Una tendencia que puede producir resultados injustos", "Una medida exacta siempre", "Un componente eléctrico", 2),
            _language_question("¿Qué debe hacer un equipo STEM?", "Definir un problema, investigar, diseñar y evaluar", "Copiar sin probar", "Ocultar los errores", 0),
            _language_question("¿Qué característica tiene una tecnología inclusiva?", "Considera necesidades y accesibilidad de distintas personas", "Funciona solo para un grupo sin razón", "Impide participar", 1),
            _language_question("¿Qué impacto debe evaluar un prototipo?", "Efectos sociales, ambientales y de seguridad", "Solo su apariencia", "Únicamente su precio", 2),
            _language_question("¿Qué se presenta en una feria de ciencias?", "Pregunta, procedimiento, datos, resultados y conclusión", "Solo una decoración", "Un resultado inventado", 0),
        ],
    },
    "science-lab": {
        "title": "Laboratorio virtual",
        "description": "Formula hipótesis, interpreta datos y decide cómo investigar fenómenos científicos.",
        "objective": "Consolidar el método científico, la interpretación de datos y la toma de decisiones responsables.",
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "prerequisites": ["science-matter", "science-technology"],
        "related_activity": "science-matter",
        "questions": [
            _language_question("¿Qué se formula antes de probar una idea?", "Una pregunta y una hipótesis", "Una conclusión definitiva", "Un resultado inventado", 0),
            _language_question("¿Qué permite comparar datos?", "Tablas o gráficas", "Rumores", "Cambiar unidades sin avisar", 1),
            _language_question("¿Qué se debe mantener igual en un experimento controlado?", "Las condiciones que no se están estudiando", "Todas las variables al azar", "Ninguna condición", 2),
            _language_question("¿Qué significa que un resultado apoye una hipótesis?", "Los datos son compatibles con la explicación propuesta", "La hipótesis se vuelve una ley de inmediato", "No se necesitan más preguntas", 0),
            _language_question("¿Qué puede mostrar una gráfica?", "Patrones o cambios en los datos", "Una opinión sin información", "El nombre del laboratorio solamente", 1),
            _language_question("¿Qué haces si los resultados no apoyan la hipótesis?", "Revisas la explicación y propones otra prueba", "Borras los resultados", "Cambias los datos", 2),
            _language_question("¿Qué protege a las personas en un laboratorio?", "Normas, materiales seguros y supervisión", "Trabajar sin instrucciones", "Probar sustancias desconocidas", 0),
            _language_question("¿Qué relación existe entre ciencia y tecnología?", "La ciencia explica y la tecnología puede aplicar conocimientos para resolver problemas", "Son exactamente lo mismo", "No tienen relación", 1),
            _language_question("¿Qué debe comunicar un informe científico?", "Procedimiento, evidencias, resultados y conclusión", "Solo una opinión", "Un resultado sin explicar", 2),
            _language_question("¿Qué habilidad practica este laboratorio?", "Investigar con evidencias y revisar decisiones", "Adivinar sin datos", "Ocultar errores", 0),
        ],
    },
}


FIRST_GRADE_ENGLISH_CONTENT = {
    "english-identity": {
        "title": "Hello! This is me",
        "description": "Saluda, di tu nombre y edad y reconoce colores y números del 1 al 10.",
        "objective": "Usar saludos y frases breves para presentarse, decir la edad y reconocer vocabulario básico.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "oral_challenge": "This is me: say hello, your name and your age.",
        "project": "This is me poster: crea un afiche con tu nombre, edad, cuatro colores y un saludo en inglés.",
        "lesson": [
            "Los saludos incluyen Hello! para saludar y Goodbye! para despedirte. Please y Thank you son expresiones amables.",
            "Para presentarte puedes decir: My name is Ana. Para decir la edad: I am six.",
            "Practica los números del one al ten y reconoce colores como red, blue, yellow y green.",
            "Escucha, repite y acompaña las palabras con gestos. Equivocarse y volver a intentar también es aprender.",
        ],
        "questions": [
            _language_question("How do you say «hola»?", "Hello", "Goodbye", "Thanks", 0),
            _language_question("Complete: My name ___ Ana.", "is", "are", "am", 1),
            _language_question("What color is the sun?", "yellow", "purple", "black", 2),
            _language_question("How old are you?", "I am six", "I am blue", "I am a book", 0),
            _language_question("Which number is three?", "three", "ten", "one", 1),
            _language_question("How do you say «gracias»?", "Thank you", "Goodbye", "Please sit", 2),
            _language_question("Which word is a color?", "green", "seven", "hello", 0),
            _language_question("What do you say when you leave?", "Goodbye", "Hello", "Thank you", 1),
            _language_question("Which number comes after two?", "three", "one", "ten", 2),
            _language_question("Which phrase introduces yourself?", "My name is Leo.", "Blue is run.", "Goodbye is a number.", 0),
        ],
    },
    "english-community": {
        "title": "My school and colors",
        "description": "Nombra lugares, personas y objetos de la escuela usando colores y frases básicas.",
        "objective": "Reconocer vocabulario de la escuela, colores y expresiones sencillas sobre el entorno.",
        "learning_order": 2,
        "learning_phase": "Explorar",
        "project": "My classroom tour: dibuja tu salón y presenta tres objetos usando This is… y sus colores.",
        "lesson": [
            "School, classroom, teacher y friend son palabras para hablar de la escuela y las personas que encontramos allí.",
            "Usa This is a book. para señalar un objeto y My pencil is blue. para decir su color.",
            "Aprende colores como red, blue, green, yellow, black y white con objetos cercanos.",
            "Escucha la palabra, señala el objeto y repite la frase completa para comunicar una idea.",
        ],
        "questions": [
            _language_question("Where do you learn?", "school", "hospital", "airport", 0),
            _language_question("What color is grass?", "green", "pink", "black", 1),
            _language_question("Complete: This is a ___.", "book", "run", "seven", 2),
            _language_question("Who teaches a class?", "teacher", "pilot", "farmer", 0),
            _language_question("Choose a classroom object.", "pencil", "banana", "cloud", 1),
            _language_question("What color is the sky on a sunny day?", "blue", "brown", "pink", 2),
            _language_question("Complete: My bag is ___.", "red", "run", "eight", 0),
            _language_question("Which place is in a school?", "classroom", "airport", "farm", 1),
            _language_question("Who learns at school?", "student", "doctor", "pilot", 2),
            _language_question("Which sentence is correct?", "This is my book.", "This my run.", "Book is seven.", 0),
        ],
    },
    "english-world": {
        "title": "Animals and actions",
        "description": "Reconoce animales y acciones mediante frases sencillas, canciones y movimiento.",
        "objective": "Nombrar animales y relacionarlos con acciones básicas usando comprensión y movimiento.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "project": "Animal action book: crea cuatro páginas con un animal, una imagen y una frase con A … can ….",
        "lesson": [
            "Aprende nombres de animales como cat, dog, fish, bird, lion y elephant.",
            "Usa can para hablar de una acción: A bird can fly. A fish can swim.",
            "Las canciones y los gestos ayudan a recordar acciones como jump, run, swim, fly y sleep.",
            "Escucha la frase, representa la acción y repítela con confianza.",
        ],
        "questions": [
            _language_question("Which animal says meow?", "cat", "fish", "bird", 0),
            _language_question("Complete: A bird can ___.", "fly", "swim in a book", "is red", 1),
            _language_question("Which animal lives in water?", "fish", "lion", "cow", 2),
            _language_question("What action is «jump»?", "saltar", "dormir", "comer", 0),
            _language_question("Choose an animal.", "elephant", "yellow", "run", 1),
            _language_question("Complete: A dog can ___.", "run", "blue", "seven", 2),
            _language_question("Which animal can fly?", "bird", "fish", "cow", 0),
            _language_question("What action is «swim»?", "nadar", "saltar", "dormir", 1),
            _language_question("Which animal is big?", "elephant", "ant", "fish", 2),
            _language_question("Which sentence is correct?", "The cat can run.", "Cat is seven.", "Run is yellow.", 0),
        ],
    },
    "english-culture": {
        "title": "Songs and celebrations",
        "description": "Participa en canciones y reconoce palabras sobre celebraciones, emociones y cortesía.",
        "objective": "Comprender expresiones de canciones, celebraciones, emociones y comunicación amable.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "project": "Friendly celebration: prepara una mini celebración respetuosa y practica Happy birthday!, Please y Thank you!.",
        "lesson": [
            "Una song es una canción y un festival o birthday son ocasiones para celebrar con otras personas.",
            "Usa Happy birthday! para felicitar y Thank you! para agradecer.",
            "Palabras como happy, sad y joy ayudan a expresar emociones sencillas.",
            "Participar con respeto significa escuchar, cantar, compartir y valorar que las personas celebren de distintas maneras.",
        ],
        "questions": [
            _language_question("What do you sing?", "a song", "a chair", "a number", 0),
            _language_question("Complete: Happy ___!", "birthday", "window", "run", 1),
            _language_question("Which is a celebration?", "festival", "pencil", "blue", 2),
            _language_question("How do you say «gracias»?", "Thank you", "Please sit", "Good night only", 0),
            _language_question("Which feeling is happy?", "joy", "table", "seven", 1),
            _language_question("What can people do at a festival?", "sing and dance", "sleep in class", "measure a map", 2),
            _language_question("Which word names an emotion?", "happy", "pencil", "school", 0),
            _language_question("What do you say after receiving a gift?", "Thank you", "Goodbye", "Run", 1),
            _language_question("Which word is related to a birthday?", "cake", "river", "window", 2),
            _language_question("Which action shows respect at a song?", "Listen and take turns.", "Shout at everyone.", "Break the instruments.", 0),
        ],
    },
    "word-quest": {
        "title": "Memory: words and sounds",
        "description": "Relaciona palabras, imágenes y sonidos básicos en inglés.",
        "objective": "Consolidar vocabulario de identidad, escuela, colores, animales y celebraciones.",
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "prerequisites": ["english-identity", "english-community"],
        "related_activity": "english-identity",
        "questions": [
            _language_question("Which word means «hola»?", "Hello", "Blue", "Fish", 0),
            _language_question("Which word is a color?", "green", "teacher", "jump", 1),
            _language_question("Which word is an animal?", "cat", "seven", "happy", 2),
            _language_question("Which word is a school object?", "pencil", "lion", "birthday", 0),
            _language_question("Which word means «gracias»?", "Thank you", "Goodbye", "Red", 1),
            _language_question("Which action can a bird do?", "fly", "book", "yellow", 2),
            _language_question("Which number is ten?", "ten", "two", "blue", 0),
            _language_question("Which word names a celebration?", "festival", "classroom", "swim", 1),
            _language_question("Complete: My name ___ Sara.", "is", "are", "blue", 2),
            _language_question("Which phrase is a friendly greeting?", "Hello!", "A pencil.", "Run seven.", 0),
        ],
    },
}


SECOND_GRADE_ENGLISH_CONTENT = {
    "english-identity": {
        "title": "My family and home",
        "description": "Nombra personas, espacios y objetos de la familia y la casa con frases sencillas.",
        "objective": "Describir familia, casa y pertenencias usando vocabulario y estructuras básicas en inglés.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "oral_challenge": "Describe your family or home with three short sentences.",
        "project": "My home album: dibuja tres espacios de tu casa y escribe una oración sencilla para cada uno.",
        "lesson": [
            "Usa family words como mother, father, brother, sister y grandma para hablar de personas cercanas.",
            "This is my home or house. y This is my bedroom. sirven para señalar lugares y objetos de la casa.",
            "Practica my, your, his y her con frases breves: This is my bag. Her room is small.",
            "Escucha la frase, señala la imagen correcta y repítela para ganar seguridad al hablar.",
        ],
        "questions": [
            _language_question("My mother's child is my…", "brother or sister", "teacher", "street", 0),
            _language_question("Complete: This is my ___.", "house", "run", "blue", 1),
            _language_question("Where do you sleep?", "In the bedroom", "In the kitchen floor", "At the school bus", 2),
            _language_question("What is the opposite of big?", "small", "happy", "old", 0),
            _language_question("Choose the family word.", "grandma", "window", "pencil", 1),
            _language_question("Complete: This is ___ mother.", "my", "run", "seven", 2),
            _language_question("Which room is for cooking?", "kitchen", "bedroom", "garden", 0),
            _language_question("What is a home object?", "chair", "brother", "school", 1),
            _language_question("Complete: Her room is ___.", "small", "eat", "Monday", 2),
            _language_question("Which sentence is correct?", "This is my family.", "Family my is.", "My is run.", 0),
        ],
    },
    "english-community": {
        "title": "My town and routines",
        "description": "Describe places in the town and daily actions using simple present phrases.",
        "objective": "Nombrar lugares de la ciudad y expresar rutinas diarias con frases breves.",
        "learning_order": 2,
        "learning_phase": "Explorar",
        "project": "My town map: crea un mapa sencillo con cuatro lugares y explica una rutina usando I go… o I visit….",
        "lesson": [
            "Town words como park, library, hospital, school y store ayudan a hablar de la comunidad.",
            "Usa I go to school. y We have lunch at noon. para describir rutinas.",
            "Los días y momentos ayudan a ordenar acciones: in the morning, at noon, on Monday.",
            "Combina sujeto, verbo y lugar: I play in the park. She reads at the library.",
        ],
        "questions": [
            _language_question("Where can you borrow books?", "library", "kitchen", "garden shoe", 0),
            _language_question("Complete: I go to school ___ Monday.", "on", "in a", "at the", 1),
            _language_question("Who helps sick people?", "doctor", "artist", "driver only", 2),
            _language_question("What is a place in town?", "park", "purple", "jump", 0),
            _language_question("Complete: We ___ lunch at noon.", "have", "has", "having is", 1),
            _language_question("Where do you see films?", "cinema", "library book", "school pencil", 2),
            _language_question("Complete: I ___ breakfast in the morning.", "eat", "eats", "eating", 0),
            _language_question("Which action is a routine?", "brush my teeth", "purple", "hospital", 1),
            _language_question("What place helps when you are sick?", "hospital", "park", "museum only", 2),
            _language_question("Which sentence is correct?", "I visit the park.", "I park visits.", "Visit I the.", 0),
        ],
    },
    "english-world": {
        "title": "Goldilocks and the three bears",
        "description": "Comprende personajes, lugares y acciones de un cuento breve en inglés.",
        "objective": "Seguir una secuencia narrativa sencilla y reconocer personajes, lugares y acciones en un cuento.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "project": "Story sequence: ordena seis escenas de Goldilocks y cuenta la historia con First, Next y Finally.",
        "lesson": [
            "Un cuento tiene characters, setting y actions. Goldilocks es la niña y the three bears son los personajes principales.",
            "Usa first, next y finally para ordenar lo que ocurre en la historia.",
            "Frases como She enters the house. y The bears come home. ayudan a comprender acciones.",
            "Escucha el cuento, repite palabras importantes y usa imágenes para comprobar el significado.",
        ],
        "questions": [
            _language_question("Who is Goldilocks?", "A girl", "A bear", "A house", 0),
            _language_question("Who lives in the house?", "Three bears", "Three pencils", "A school", 1),
            _language_question("Where does Goldilocks go?", "To the bears' house", "To an airport", "To a classroom", 2),
            _language_question("What does she try?", "The porridge, chairs and beds", "Cars and maps", "Books only", 0),
            _language_question("Which word shows the beginning?", "First", "Finally", "Yesterday", 1),
            _language_question("Which word shows the end?", "Finally", "First", "Blue", 2),
            _language_question("Complete: The bears ___ home.", "come", "comes yesterday", "coming is", 0),
            _language_question("What is a story character?", "A person or animal in the story", "A color", "A number only", 1),
            _language_question("Where can a bear live?", "In a forest", "In a pencil", "At a number", 2),
            _language_question("What does a story have?", "Characters, place and actions", "Only colors", "Only a list of numbers", 0),
        ],
    },
    "english-culture": {
        "title": "Food and festivals",
        "description": "Nombra alimentos, expresa gustos y participa en situaciones culturales cotidianas.",
        "objective": "Reconocer alimentos, expresar gustos y usar frases amables en festivales y celebraciones.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "project": "Healthy festival menu: diseña un menú ilustrado y presenta tres alimentos usando I like… y Can I have…?.",
        "lesson": [
            "Food words como bread, apples, rice y water sirven para hablar de alimentos y bebidas.",
            "Usa I like apples. y I do not like onions. para expresar gustos de forma sencilla.",
            "En un festival las personas pueden sing, dance, share food y celebrate.",
            "Can I have water, please? es una forma amable de pedir algo; Thank you! sirve para agradecer.",
        ],
        "questions": [
            _language_question("Which is food?", "bread", "bridge", "green", 0),
            _language_question("Complete: I like ___.", "apples", "running yesterday", "house are", 1),
            _language_question("What do people do at a festival?", "celebrate", "sleep in class", "measure a map", 2),
            _language_question("How do you ask politely?", "Can I have water, please?", "Water now yesterday.", "Give blue.", 0),
            _language_question("Which word means «comida»?", "food", "school", "friend", 1),
            _language_question("Which is a drink?", "water", "bread", "apple", 2),
            _language_question("Complete: I ___ bananas.", "like", "likes yesterday", "liking are", 0),
            _language_question("What can people share at a festival?", "food", "a grammar rule", "a number", 1),
            _language_question("What do you say after receiving food?", "Thank you", "Goodbye yesterday", "Run please", 2),
            _language_question("Which sentence expresses a preference?", "I like rice.", "Rice is run.", "I food yesterday.", 0),
        ],
    },
    "word-quest": {
        "title": "Sentence builder: family and routines",
        "description": "Ordena palabras y relaciona vocabulario para formar oraciones sencillas en inglés.",
        "objective": "Consolidar vocabulario y estructuras de familia, ciudad, rutinas, cuentos y alimentos.",
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "prerequisites": ["english-identity", "english-community"],
        "related_activity": "english-community",
        "questions": [
            _language_question("Choose the correct sentence.", "This is my house.", "House my is.", "My house run.", 0),
            _language_question("Complete: She ___ to school.", "goes", "go are", "going yesterday", 1),
            _language_question("Choose a town place.", "library", "purple", "eat", 2),
            _language_question("Put the routine in order: ___, I have breakfast.", "First", "Finally", "Blue", 0),
            _language_question("Complete: I ___ apples.", "like", "likes are", "liking yesterday", 1),
            _language_question("Choose a story character.", "the girl", "the blue", "quickly", 2),
            _language_question("Complete: We ___ lunch at noon.", "have", "has yesterday", "having are", 0),
            _language_question("Choose a polite request.", "Can I have water, please?", "Water now.", "Give blue.", 1),
            _language_question("Which word shows the end of a story?", "Finally", "First", "Green", 2),
            _language_question("Choose the correct phrase.", "My family is happy.", "Family my happy.", "Happy is run.", 0),
        ],
    },
}


THIRD_GRADE_ENGLISH_CONTENT = {
    "english-identity": {
        "title": "Daily routine and time",
        "description": "Describe rutinas, horas y actividades diarias con frases sencillas en inglés.",
        "objective": "Expresar rutinas y horarios usando presente simple y vocabulario de momentos del día.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "oral_challenge": "Tell a short story in English for 30 seconds.",
        "project": "My daily routine comic: crea seis viñetas y cuenta tu día usando First, Then y Finally.",
        "lesson": [
            "Usa I get up, I have breakfast, I go to school y I go to bed para contar una rutina.",
            "Para decir la hora puedes usar o'clock: It is seven o'clock. In the morning y at night ubican el momento del día.",
            "Con he, she o it el verbo puede cambiar: She reads. He plays.",
            "Ordena las acciones con first, then, after that y finally para contar una secuencia clara.",
        ],
        "questions": [
            _language_question("Complete: I ___ breakfast in the morning.", "eat", "eats", "eating", 0),
            _language_question("What time comes after seven?", "eight o'clock", "three o'clock", "one o'clock", 1),
            _language_question("Complete: She ___ books.", "reads", "read are", "reading is", 2),
            _language_question("How do you express a preference?", "I like music", "I am table", "Blue is run", 0),
            _language_question("Which activity is in the morning?", "having breakfast", "going to bed", "sleeping at night", 1),
            _language_question("Complete: He ___ football after school.", "plays", "play are", "playing yesterday", 2),
            _language_question("Which word shows the beginning of a routine?", "First", "Finally", "Yesterday only", 0),
            _language_question("What do you do at night?", "I go to bed.", "I am a school.", "I blue breakfast.", 1),
            _language_question("Which sentence is correct?", "I get up at seven.", "I up get seven.", "Seven get I up.", 2),
            _language_question("What does «daily routine» mean?", "Activities we do every day", "A place to visit", "A kind of animal", 0),
        ],
    },
    "english-community": {
        "title": "Hobbies and sports",
        "description": "Habla de gustos, hobbies, deportes y lugares de la comunidad.",
        "objective": "Expresar gustos y describir actividades de ocio y deportes usando frases sencillas.",
        "learning_order": 2,
        "learning_phase": "Explorar",
        "project": "Hobby club poster: crea un afiche de un club, incluye tres actividades y una invitación en inglés.",
        "lesson": [
            "Hobbies son actividades que disfrutamos: reading, drawing, cycling, swimming y playing music.",
            "Usa I like, I love o I do not like para expresar preferencias.",
            "Para hablar de deportes puedes decir I play football, I ride a bike o I go swimming.",
            "Relaciona cada actividad con su lugar: pool, park, library, field o sports center.",
        ],
        "questions": [
            _language_question("Which is a hobby?", "playing football", "Monday", "kitchen", 0),
            _language_question("Where do you swim?", "at the pool", "in the library", "on the pencil", 1),
            _language_question("Which is a sport?", "cycling", "Tuesday", "hospital", 2),
            _language_question("Complete: They ___ basketball on Fridays.", "play", "plays", "playing is", 0),
            _language_question("How do you express a preference?", "I like drawing.", "I drawing yesterday.", "Like is blue.", 1),
            _language_question("Where can you play football?", "on a field", "in a kitchen", "at a library book", 2),
            _language_question("Complete: She ___ swimming.", "goes", "go are", "going yesterday", 0),
            _language_question("Which activity uses a book?", "reading", "cycling", "running", 1),
            _language_question("What is a place in the community?", "sports center", "purple", "quickly", 2),
            _language_question("Which sentence is correct?", "I visit the park.", "I park visits.", "Visit I the.", 0),
        ],
    },
    "english-world": {
        "title": "Adventure: myths and legends",
        "description": "Comprende personajes, lugares y secuencias en aventuras, mitos y leyendas sencillas.",
        "objective": "Reconocer elementos de mitos y leyendas y describir acciones y personajes en inglés.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "project": "Mini legend: escribe o ilustra una leyenda breve con un personaje, un lugar, un problema y un final.",
        "lesson": [
            "An adventure has characters, a place, a problem and actions. A myth or legend can include traditional or magical elements.",
            "Usa past words sencillas como was, went, saw y found para contar lo que ocurrió.",
            "Los conectores first, then y finally ayudan a ordenar una aventura.",
            "Al leer una leyenda, respeta su cultura de origen y distingue los hechos imaginarios de la información real.",
        ],
        "questions": [
            _language_question("What is a story character?", "A person or animal in the story", "The blue", "Quickly", 0),
            _language_question("Where can an adventure happen?", "in a forest", "in a verb", "inside a color", 1),
            _language_question("What is the past of go?", "went", "goes", "going", 2),
            _language_question("Which sentence describes a character?", "She is brave.", "She yesterday.", "Brave is run.", 0),
            _language_question("What is a myth?", "A traditional story with extraordinary elements", "A shopping list", "A school object", 1),
            _language_question("Which word shows sequence?", "Then", "Purple", "Animal", 2),
            _language_question("Complete: The hero ___ a dragon.", "saw", "see are", "seeing tomorrow", 0),
            _language_question("What is a legend?", "A traditional story connected to a place or culture", "A number", "A classroom rule", 1),
            _language_question("Which word shows the end?", "Finally", "First", "Blue", 2),
            _language_question("What can an adventure have?", "A problem and a solution", "Only a color", "Only a number", 0),
        ],
    },
    "english-culture": {
        "title": "Pen-pal: email exchange",
        "description": "Escribe y comprende mensajes breves para presentarte e intercambiar información con un pen-pal.",
        "objective": "Organizar un correo sencillo con saludo, presentación, preguntas y despedida respetuosa.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "oral_challenge": "Read your short email aloud to a partner.",
        "project": "Pen-pal email: escribe un correo breve con saludo, gustos, una pregunta y despedida, sin compartir datos privados.",
        "lesson": [
            "Un email breve puede tener saludo (Dear…), presentación, información sobre gustos o rutina y despedida (Bye/Best wishes).",
            "Usa preguntas sencillas para conocer a tu pen-pal: What is your name? Where do you live? What do you like?",
            "Revisa que cada oración empiece con mayúscula y que el mensaje sea amable y claro.",
            "No compartas datos privados. Usa nombres, gustos y lugares generales con acompañamiento adulto.",
        ],
        "questions": [
            _language_question("What is a pen-pal?", "A friend you write to", "A kind of food", "A school object", 0),
            _language_question("Which phrase starts an email?", "Dear Alex,", "Goodbye yesterday", "Blue is run", 1),
            _language_question("Which question asks for a name?", "What is your name?", "Where is your pencil?", "How many colors?", 2),
            _language_question("What can you write about in an email?", "Your hobbies and routine", "A private password", "A secret address", 0),
            _language_question("Which phrase ends a friendly email?", "Best wishes", "First breakfast", "Run quickly", 1),
            _language_question("Complete: I ___ in Bogotá.", "live", "lives are", "living yesterday", 2),
            _language_question("How do you ask about a hobby?", "What do you like?", "What color yesterday?", "Run you where?", 0),
            _language_question("Which sentence is polite?", "Please write back.", "Write now, you!", "You blue email.", 1),
            _language_question("What should you protect in a message?", "Private information", "Your favorite color", "A greeting", 2),
            _language_question("Which email is organized?", "Greeting, message and goodbye", "Goodbye, title and random words", "Only a name", 0),
        ],
    },
    "word-quest": {
        "title": "Quiz show: English grammar",
        "description": "Resuelve retos de presente simple, preguntas, pasado y vocabulario de 3.º.",
        "objective": "Consolidar estructuras básicas para hablar de rutinas, gustos, lugares y cuentos.",
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "prerequisites": ["english-identity", "english-community"],
        "related_activity": "english-identity",
        "questions": [
            _language_question("Complete: She ___ books.", "reads", "read are", "reading is", 0),
            _language_question("Complete: They ___ basketball.", "play", "plays", "playing is", 1),
            _language_question("Which is a question?", "Where do you live?", "I live here.", "Live is blue.", 2),
            _language_question("What is the past of go?", "went", "goes", "going", 0),
            _language_question("Complete: I ___ music.", "like", "likes are", "liking yesterday", 1),
            _language_question("Which word shows sequence?", "then", "purple", "hospital", 2),
            _language_question("Complete: He ___ at seven.", "gets up", "get are", "getting yesterday", 0),
            _language_question("Which sentence is correct?", "They visit the park.", "They park visits.", "Visit they the.", 1),
            _language_question("Which phrase is an email goodbye?", "Best wishes", "First school", "Blue run", 2),
            _language_question("Which sentence is in the past?", "The hero went home.", "The hero goes home tomorrow.", "The hero is blue.", 0),
        ],
    },
}


FOURTH_GRADE_ENGLISH_CONTENT = {
    "english-identity": {
        "title": "Opinions and preferences",
        "description": "Expresa gustos, opiniones y comparaciones con frases conectadas en inglés.",
        "objective": "Expresar preferencias y opiniones respetuosas usando because, comparatives y vocabulario cotidiano.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "oral_challenge": "My hero: give a one-minute presentation.",
        "project": "My hero presentation: prepara una exposición de un minuto con tres cualidades y una razón usando because.",
        "lesson": [
            "Usa I like, I prefer y In my opinion para expresar gustos y opiniones.",
            "Puedes explicar una razón con because: I prefer cycling because it is healthy.",
            "Los comparativos ayudan a comparar: bigger, smaller, faster, more interesting.",
            "Una opinión respetuosa escucha otras ideas y puede usar I agree o I disagree because…",
        ],
        "questions": [
            _language_question("Complete: I think it is ___.", "interesting", "yesterday", "walked", 0),
            _language_question("Which is healthier?", "eating fruit", "never sleeping", "drinking only soda", 1),
            _language_question("Comparative of small.", "smaller", "smallestly", "more smalling", 2),
            _language_question("How do you give an opinion?", "I believe it is useful.", "I yesterday pencil.", "Run is house.", 0),
            _language_question("Complete: I prefer tea ___ it is warm.", "because", "yesterday", "but is", 1),
            _language_question("Which sentence shows agreement?", "I agree with you.", "I blue with you.", "Agree yesterday.", 2),
            _language_question("Which is faster?", "A bicycle is faster than walking.", "A bicycle is yesterday.", "Walking is blue.", 0),
            _language_question("Complete: She ___ drawing to running.", "prefers", "prefer are", "preferring yesterday", 1),
            _language_question("How can you disagree respectfully?", "I disagree because I have another idea.", "You are wrong!", "No listen.", 2),
            _language_question("Which sentence is correct?", "My favorite subject is science.", "My science favorite is.", "Science are yesterday.", 0),
        ],
    },
    "english-community": {
        "title": "Health and the body",
        "description": "Describe the body, habits and advice for staying healthy in everyday situations.",
        "objective": "Nombrar partes del cuerpo y expresar consejos y hábitos saludables usando should.",
        "learning_order": 2,
        "learning_phase": "Explorar",
        "project": "Healthy habits guide: crea una guía con cinco hábitos saludables y consejos usando You should….",
        "lesson": [
            "Body words como head, eyes, hands, stomach y legs ayudan a describir el cuerpo.",
            "Usa have/has para describir: I have two eyes. She has a headache.",
            "Should expresa consejo: You should drink water. You should rest.",
            "Relaciona hábitos con salud: wash your hands, eat fruit, sleep well y exercise.",
        ],
        "questions": [
            _language_question("What should you do when sick?", "see a doctor", "ignore every symptom", "never drink water", 0),
            _language_question("Complete: You must ___ your hands.", "wash", "washes", "washing are", 1),
            _language_question("Which place helps emergencies?", "hospital", "cinema only", "bedroom", 2),
            _language_question("Complete: The pharmacy is ___ the bank.", "next to", "yesterday", "quickly", 0),
            _language_question("Which sentence gives advice?", "You should rest.", "You rested blue.", "Rest is yesterday.", 1),
            _language_question("Which body part helps you see?", "eyes", "feet", "stomach", 2),
            _language_question("Complete: She ___ a headache.", "has", "have are", "having yesterday", 0),
            _language_question("Which habit is healthy?", "eating vegetables", "sleeping one hour", "drinking only soda", 1),
            _language_question("What should you do before eating?", "Wash your hands.", "Run to the street.", "Ignore the food.", 2),
            _language_question("Which sentence is correct?", "I have two hands.", "I has two hands.", "I hands have two.", 0),
        ],
    },
    "english-world": {
        "title": "Technology and the future",
        "description": "Habla de dispositivos, planes y posibilidades futuras con expresiones comprensibles.",
        "objective": "Describir tecnología y expresar planes o predicciones usando will y vocabulario de futuro.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "project": "Future invention: dibuja un invento, explica qué problema resuelve y presenta tres frases con will.",
        "lesson": [
            "A device es un aparato o herramienta, como phone, computer, robot o tablet.",
            "Usa will para hablar de futuro: We will build a robot. They will travel.",
            "Tomorrow, next year y in the future ubican acciones futuras.",
            "La tecnología puede resolver problemas, pero debemos usarla con seguridad y responsabilidad.",
        ],
        "questions": [
            _language_question("What is a device?", "A tool or machine", "A season", "A feeling only", 0),
            _language_question("Complete: We will ___ a robot.", "build", "built yesterday", "building are", 1),
            _language_question("Which is a future marker?", "tomorrow", "last year", "yesterday morning", 2),
            _language_question("What can technology help us do?", "solve problems", "erase every responsibility", "stop learning", 0),
            _language_question("Which sentence is future?", "They will travel.", "They travelled yesterday.", "They travel last week.", 1),
            _language_question("What is a safe technology habit?", "Protecting passwords and personal information", "Sharing passwords", "Using every device without rules", 2),
            _language_question("Complete: In the future, people ___ use clean energy.", "will", "yesterday", "are used", 0),
            _language_question("Which is a digital device?", "a computer", "a mountain", "a sandwich", 1),
            _language_question("What should a good invention do?", "Help people and reduce harm", "Create danger without purpose", "Waste all resources", 2),
            _language_question("Which sentence is correct?", "Technology can solve problems.", "Technology solve yesterday.", "Can technology problems is.", 0),
        ],
    },
    "english-culture": {
        "title": "Culture project: the UK and the USA",
        "description": "Compara aspectos culturales del Reino Unido y Estados Unidos con respeto y curiosidad.",
        "objective": "Investigar y presentar información sencilla sobre culturas anglófonas evitando estereotipos.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "project": "Culture comparison: compara una comida, música o celebración del Reino Unido y Estados Unidos usando Both… y but….",
        "lesson": [
            "Un culture project puede investigar lugares, comidas, música, celebraciones y formas de vida.",
            "The UK y the USA son lugares diversos: no todas las personas tienen las mismas costumbres.",
            "Usa This project is about… y People celebrate… para presentar información.",
            "Compara con respeto: Both places have…, but they are different in… Usa fuentes y distingue datos de opiniones.",
        ],
        "questions": [
            _language_question("What is culture?", "Shared ways of living and expressing", "Only a color", "A single math rule", 0),
            _language_question("What can a culture project include?", "Food, music and celebrations", "Only private passwords", "Random numbers", 1),
            _language_question("Which sentence compares two places?", "Both places have music, but their traditions differ.", "Both yesterday blue.", "Places is run.", 2),
            _language_question("What should we do with traditions?", "Learn respectfully", "Mock them", "Call them all the same", 0),
            _language_question("Which is a source for a project?", "A museum website or book", "A random rumor", "An invented title", 1),
            _language_question("Complete: People ___ different foods.", "eat", "eats yesterday", "eating are", 2),
            _language_question("What is a respectful question about culture?", "What music do people enjoy?", "Why are they all the same?", "Can I mock this tradition?", 0),
            _language_question("Which phrase presents a project?", "This project is about music.", "Project music yesterday.", "About is blue.", 1),
            _language_question("What should you do before sharing information?", "Check the source", "Invent the data", "Copy every rumor", 2),
            _language_question("Which statement avoids a stereotype?", "People in a country have different experiences.", "Everyone there is exactly the same.", "One tradition describes every person.", 0),
        ],
    },
    "word-quest": {
        "title": "Role-play: shop and restaurant",
        "description": "Practica diálogos para comprar, pedir alimentos y hablar con cortesía.",
        "objective": "Usar expresiones funcionales para comprar, ordenar alimentos y responder en situaciones cotidianas.",
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "prerequisites": ["english-community", "english-culture"],
        "related_activity": "english-community",
        "questions": [
            _language_question("How do you ask for a price?", "How much is it?", "Where yesterday?", "Price is run.", 0),
            _language_question("Complete: I would like ___ water, please.", "some", "yesterday", "running", 1),
            _language_question("What does a waiter do?", "Serves food", "Builds a mountain", "Teaches every class", 2),
            _language_question("Which phrase is polite?", "Can I have the menu, please?", "Menu now!", "Give blue.", 0),
            _language_question("Complete: How ___ are the apples?", "much", "many is yesterday", "more are", 1),
            _language_question("What do you say after a service?", "Thank you.", "Run yesterday.", "Blue please.", 2),
            _language_question("Which phrase orders food?", "I would like a sandwich.", "Sandwich yesterday run.", "I food blue.", 0),
            _language_question("What can you buy in a shop?", "a T-shirt", "a grammar", "a feeling only", 1),
            _language_question("Which response accepts an offer?", "Yes, please.", "No color.", "Yesterday yes run.", 2),
            _language_question("Which dialogue is polite?", "A: Can I help you? B: Yes, please.", "A: Give! B: No words.", "A: Blue? B: Yesterday.", 0),
        ],
    },
}


FIFTH_GRADE_ENGLISH_CONTENT = {
    "english-identity": {
        "title": "Environment and action",
        "description": "Habla de problemas ambientales y propone acciones usando ideas conectadas en inglés.",
        "objective": "Describir retos ambientales y proponer acciones sostenibles con razones sencillas.",
        "learning_order": 1,
        "learning_phase": "Construir",
        "oral_challenge": "Debate: Should we protect the planet?",
        "project": "Eco-action campaign: crea un afiche bilingüe con un problema ambiental, tres acciones y una razón para cada propuesta.",
        "lesson": [
            "Usa environment, pollution, waste, climate y animals para hablar de retos ambientales.",
            "Should y should not sirven para proponer acciones: We should recycle. We should not waste water.",
            "Conecta ideas con because, so, but y if: If we recycle, we reduce waste.",
            "Una propuesta clara nombra el problema, explica por qué importa y plantea una acción posible.",
        ],
        "questions": [
            _language_question("Complete: We should ___ the planet.", "protect", "protected yesterday", "protects it are", 0),
            _language_question("Which action is sustainable?", "reusing materials", "wasting water", "burning all trash", 1),
            _language_question("Complete: If we recycle, we ___ waste.", "reduce", "reduced yesterday", "reducing are", 2),
            _language_question("What is pollution?", "Harmful substances in the environment", "A healthy habit", "A kind of celebration", 0),
            _language_question("Complete: We should not ___ water.", "waste", "wastes yesterday", "wasting are", 1),
            _language_question("Which sentence gives an environmental reason?", "We should plant trees because they help the air.", "Trees yesterday blue.", "Plant is run.", 2),
            _language_question("What can reduce plastic waste?", "Using a reusable bottle", "Using a new plastic bottle every minute", "Throwing bottles in rivers", 0),
            _language_question("Which connector shows a result?", "so", "but", "yesterday", 1),
            _language_question("What should people do with trash?", "Separate and dispose of it responsibly", "Leave it in nature", "Throw it anywhere", 2),
            _language_question("Which sentence is correct?", "We can help the planet.", "We can helps yesterday.", "Planet help are.", 0),
        ],
    },
    "english-community": {
        "title": "News and media literacy",
        "description": "Comprende noticias sencillas y evalúa fuentes y mensajes de medios con pensamiento crítico.",
        "objective": "Distinguir hechos, opiniones y fuentes confiables en mensajes y noticias sencillas.",
        "learning_order": 2,
        "learning_phase": "Explorar",
        "project": "Fact-check a school news item: compara dos fuentes, identifica un hecho y una opinión y explica cuál evidencia encontraste.",
        "lesson": [
            "Una noticia informa sobre un hecho y suele responder qué ocurrió, dónde, cuándo y quiénes participaron.",
            "Una fuente confiable ofrece autoría, fecha, evidencias y un propósito identificable.",
            "Un hecho puede comprobarse; una opinión expresa una valoración. Los titulares también pueden intentar llamar la atención.",
            "Antes de compartir información, compara fuentes y pregunta si el mensaje tiene evidencias o solo repite un rumor.",
        ],
        "questions": [
            _language_question("What is a news source?", "A newspaper or reliable website", "A spoon", "A shoe", 0),
            _language_question("What is a reliable source?", "Information with evidence", "A random rumor", "An invented title", 1),
            _language_question("Which is a fact?", "The school opened at eight.", "It was the best school ever.", "Everyone should love it.", 2),
            _language_question("Which is an opinion?", "The festival was wonderful.", "The festival started on Monday.", "The festival had three activities.", 0),
            _language_question("What should you check before sharing news?", "The source, date and evidence", "Only the picture", "How exciting the title sounds", 1),
            _language_question("Complete: The article ___ published yesterday.", "was", "were are", "be yesterday", 2),
            _language_question("What is a headline?", "The title of a news story", "The final opinion of every reader", "A school uniform", 0),
            _language_question("What can a misleading title do?", "Make people believe something without enough context", "Prove every fact", "Show the complete evidence", 1),
            _language_question("What should you do with a doubtful message?", "Check more sources before sharing", "Share it quickly", "Change the facts", 2),
            _language_question("Which question helps analyze news?", "Who wrote it and what evidence is included?", "Is the picture colorful?", "Does it use many words?", 0),
        ],
    },
    "english-world": {
        "title": "Travel and the world",
        "description": "Comprende textos sobre viajes, países y experiencias culturales con vocabulario conectado.",
        "objective": "Describir viajes, lugares y experiencias respetando culturas y usando pasado y futuro básicos.",
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "project": "Responsible travel postcard: diseña una postal en inglés sobre un lugar, una experiencia cultural y dos formas de cuidarlo.",
        "lesson": [
            "Travel words como passport, airport, ticket, journey y museum ayudan a planear y contar un viaje.",
            "Usa past simple para contar experiencias: I visited a museum. I travelled by train.",
            "Usa will o going to para planes: We will visit a park. We are going to learn about the city.",
            "Viajar responsablemente implica respetar personas, normas, patrimonio y ambiente del lugar visitado.",
        ],
        "questions": [
            _language_question("What do you need at an airport?", "a passport", "a kitchen spoon", "a school color", 0),
            _language_question("Complete: I have ___ to Peru.", "travelled", "travel tomorrow are", "travels yesterday", 1),
            _language_question("Which is a place to visit?", "a museum", "a grammar", "a verb", 2),
            _language_question("What does journey mean?", "A trip", "A meal", "A color", 0),
            _language_question("Which action respects another country?", "learning about its culture", "mocking its people", "ignoring its rules", 1),
            _language_question("Complete: Tomorrow we ___ visit the museum.", "will", "visited yesterday", "visiting are", 2),
            _language_question("What can you use to find a place?", "a map", "a password", "a spoon", 0),
            _language_question("Which sentence is in the past?", "We visited the old town.", "We will visit the old town.", "We visit tomorrow.", 1),
            _language_question("What should travelers protect?", "Local culture and the environment", "Only their souvenirs", "No rules", 2),
            _language_question("Which sentence is correct?", "I have a passport.", "I passport have yesterday.", "Passport is travel are.", 0),
        ],
    },
    "english-culture": {
        "title": "Global English and careers",
        "description": "Usa inglés para comunicarte sobre estudios, trabajos, profesiones y retos globales.",
        "objective": "Hablar de profesiones y metas y participar en una comunicación respetuosa sobre retos globales.",
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "project": "Global careers fair: presenta una profesión, las habilidades que requiere y cómo puede contribuir a resolver un reto global.",
        "lesson": [
            "A career es un camino de trabajo y aprendizaje. Jobs como scientist, teacher, engineer y artist requieren habilidades diferentes.",
            "Usa I would like to be… y I want to learn… para hablar de metas y planes.",
            "El inglés global tiene hablantes de muchos países y acentos; comunicarse con claridad importa más que sonar igual.",
            "Para hablar de un reto global, presenta el problema, escucha perspectivas y apoya tus ideas con razones.",
        ],
        "questions": [
            _language_question("What is a career?", "A path of work and learning", "A single meal", "A weather event", 0),
            _language_question("Complete: I would like to be a ___.", "scientist", "science yesterday are", "being blue", 1),
            _language_question("Which phrase supports an opinion?", "because the evidence shows", "blue yesterday", "run a table", 2),
            _language_question("What is a global challenge?", "climate change", "a classroom pencil", "one private hobby", 0),
            _language_question("Which is respectful debate?", "I disagree because…", "You are wrong, be quiet", "I will ignore your reasons", 1),
            _language_question("Complete: She wants to ___ medicine.", "study", "studies yesterday", "studying are", 2),
            _language_question("Which job studies nature and experiments?", "scientist", "pilot only", "singer of colors", 0),
            _language_question("What should a good speaker do?", "Speak clearly and listen to others", "Interrupt everyone", "Hide the reasons", 1),
            _language_question("Which sentence describes a goal?", "I want to help people.", "I helped yesterday blue.", "Help is table.", 2),
            _language_question("What does global communication require?", "Respect, clarity and willingness to understand", "One accent only", "Ignoring differences", 0),
        ],
    },
    "word-quest": {
        "title": "Escape room: global English",
        "description": "Resuelve pistas de ambiente, noticias, viajes y comunicación para completar un reto.",
        "objective": "Consolidar vocabulario y estructuras de Inglés mediante problemas y pistas conectadas.",
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "prerequisites": ["english-identity", "english-community"],
        "related_activity": "english-identity",
        "questions": [
            _language_question("Choose the correct environmental action.", "We should recycle.", "We should wastes.", "We recycling yesterday.", 0),
            _language_question("Which is a reliable source?", "A dated article with evidence", "A random rumor", "An invented title", 1),
            _language_question("Complete: They ___ travelled by train.", "have", "has yesterday", "having are", 2),
            _language_question("Which word is related to travel?", "passport", "pollution only", "career yesterday", 0),
            _language_question("Which sentence gives an opinion?", "I believe this plan is useful.", "The meeting was on Monday.", "The plan has three steps.", 1),
            _language_question("Complete: If we act, we ___ help.", "can", "could yesterday are", "helping is", 2),
            _language_question("Which phrase starts a formal message?", "Dear team,", "Run blue.", "Yesterday hello table.", 0),
            _language_question("What should you do with doubtful news?", "Check the source.", "Share it immediately.", "Delete every fact.", 1),
            _language_question("Which phrase talks about a career?", "I would like to be an engineer.", "Engineer yesterday blue.", "Be is run.", 2),
            _language_question("Which skill does the escape room practice?", "Using clues to communicate and solve problems", "Memorizing random colors", "Ignoring information", 0),
        ],
    },
}


SUBJECT_GRADE_CONTENT = {
    ("Sociales", 1): FIRST_GRADE_SOCIAL_CONTENT,
    ("Sociales", 2): SECOND_GRADE_SOCIAL_CONTENT,
    ("Sociales", 3): THIRD_GRADE_SOCIAL_CONTENT,
    ("Sociales", 4): FOURTH_GRADE_SOCIAL_CONTENT,
    ("Sociales", 5): FIFTH_GRADE_SOCIAL_CONTENT,
    ("Ciencias Naturales", 1): FIRST_GRADE_SCIENCE_CONTENT,
    ("Ciencias Naturales", 2): SECOND_GRADE_SCIENCE_CONTENT,
    ("Ciencias Naturales", 3): THIRD_GRADE_SCIENCE_CONTENT,
    ("Ciencias Naturales", 4): FOURTH_GRADE_SCIENCE_CONTENT,
    ("Ciencias Naturales", 5): FIFTH_GRADE_SCIENCE_CONTENT,
    ("Inglés", 1): FIRST_GRADE_ENGLISH_CONTENT,
    ("Inglés", 2): SECOND_GRADE_ENGLISH_CONTENT,
    ("Inglés", 3): THIRD_GRADE_ENGLISH_CONTENT,
    ("Inglés", 4): FOURTH_GRADE_ENGLISH_CONTENT,
    ("Inglés", 5): FIFTH_GRADE_ENGLISH_CONTENT,
}


def _display_number(value, grade):
    if grade == 5:
        return f"{value / 100:.2f}".replace(".", ",")
    return str(value)


def questions_for_grade(activity, grade):
    """Genera ejercicios de cálculo adecuados al grado; el resto usa su banco didáctico."""
    grade = max(1, min(5, int(grade or 3)))
    language_variant = LANGUAGE_GRADE_CONTENT_BY_GRADE.get(grade, {}).get(activity.get("key"))
    subject_variant = SUBJECT_GRADE_CONTENT.get((activity.get("subject"), grade), {}).get(activity.get("key"))
    grade_variant = language_variant or subject_variant
    if grade_variant and grade_variant.get("questions"):
        return grade_variant["questions"]
    if activity.get("kind") == "Juego":
        return game_questions(activity, grade)
    if activity.get("curriculum"):
        return curriculum_for_grade(activity["curriculum"], grade)["questions"]
    if activity.get("grade_questions"):
        band = "early" if grade <= 2 else "middle" if grade == 3 else "upper"
        return activity["grade_questions"].get(band, activity["questions"])
    if activity["key"] not in {"math-sums", "math-race"}:
        return activity["questions"]
    questions = []
    for index in range(10):
        if grade == 1:
            first, second = (index + 2, 3 + index % 4) if index < 5 else (10 + index - 5, index - 4)
            operator = "+" if index < 5 else "−"
            answer = first + second if operator == "+" else first - second
            step = 1
        elif grade == 2:
            first, second = (18 + index, 7 + index % 5) if index < 5 else (30 + index, 8 + index % 4)
            operator = "+" if index < 5 else "−"
            answer = first + second if operator == "+" else first - second
            step = 1
        elif grade == 3:
            first, second = (126 + index * 7, 48 + index * 3) if index < 5 else (250 + index * 5, 73 + index * 2)
            operator = "+" if index < 5 else "−"
            answer = first + second if operator == "+" else first - second
            step = 10
        elif grade == 4:
            first, second = (6 + index, 4 + index % 5) if index < 5 else (72 + index, 3 + index % 6)
            operator = "×" if index < 5 else "÷"
            answer = first * second if operator == "×" else first // second
            if operator == "÷":
                first = answer * second
            step = 1
        else:
            first, second = (125 + index * 25, 75 + index * 10) if index < 5 else (450 + index * 20, 125 + index * 10)
            operator = "+" if index < 5 else "−"
            answer = first + second if operator == "+" else first - second
            step = 10
        options = [_display_number(answer - step, grade), _display_number(answer + step, grade), _display_number(answer, grade)]
        correct_index = index % 3
        options[correct_index], options[2] = options[2], options[correct_index]
        questions.append({
            "prompt": f"{_display_number(first, grade)} {operator} {_display_number(second, grade)} = ¿cuánto?",
            "options": options,
            "answer": correct_index,
        })
    return questions

def activity_for_grade(activity, grade):
    extra = curriculum_for_grade(activity["curriculum"], grade) if activity.get("curriculum") else {}
    path = learning_path_for(activity, grade)
    language_variant = LANGUAGE_GRADE_CONTENT_BY_GRADE.get(int(grade), {}).get(activity.get("key"))
    subject_variant = SUBJECT_GRADE_CONTENT.get((activity.get("subject"), int(grade)), {}).get(activity.get("key"))
    grade_variant = language_variant or subject_variant
    result = {
        **activity,
        **extra,
        **(grade_variant if grade_variant else {}),
        **path,
        "questions": questions_for_grade(activity, grade),
    }
    # El relato de 3.º reemplaza el texto base. ``public_activity`` selecciona
    # primero ``passage_by_grade`` cuando existe, por eso actualizamos también
    # ese mapa heredado para no mostrar el pasaje de otro nivel.
    if grade_variant and grade_variant.get("passage") and not grade_variant.get("passage_by_grade"):
        result["passage_by_grade"] = {
            "early": grade_variant["passage"],
            "middle": grade_variant["passage"],
            "upper": grade_variant["passage"],
        }
    return result


def public_activity(activity, grade=3):
    """No expone respuestas correctas al navegador."""
    activity = activity_for_grade(activity, grade)
    result = {key: value for key, value in activity.items() if key not in {"questions", "grade_questions", "passage_by_grade"}}
    if activity.get("passage_by_grade"):
        band = "early" if grade <= 2 else "upper" if grade >= 4 else "middle"
        result["passage"] = activity["passage_by_grade"][band] if band in activity["passage_by_grade"] else activity["passage"]
    result["grade"] = grade
    result["grades"] = [1, 2, 3, 4, 5]
    result["questions"] = [
        {"prompt": question["prompt"], "options": question["options"]}
        for question in activity["questions"]
    ]
    return result


from .extra_content import EXTRA_ACTIVITIES, curriculum_for_grade
from .subject_units import SUBJECT_ACTIVITIES
from juegos.backend.catalog import GAMES, game_questions
ACTIVITIES = BASE_ACTIVITIES + EXTRA_ACTIVITIES + SUBJECT_ACTIVITIES + GAMES


# Ruta recomendada para Matemáticas de 1.º. El catálogo sigue permitiendo
# explorar libremente, pero esta información permite presentar una secuencia
# pedagógica clara y relacionar cada juego con el aprendizaje que consolida.
FIRST_GRADE_MATH_PATH = {
    "math-counting": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Contar, comparar y representar cantidades de 0 a 20.",
        "prerequisites": [],
    },
    "math-sums": {
        "learning_order": 2,
        "learning_phase": "Construir",
        "objective": "Resolver situaciones de juntar y quitar con objetos y dibujos.",
        "prerequisites": ["math-counting"],
    },
    "math-fractions-geometry": {
        "learning_order": 3,
        "learning_phase": "Explorar",
        "objective": "Reconocer formas, cuerpos y posiciones en el espacio.",
        "prerequisites": ["math-counting"],
    },
    "math-laboratory": {
        "learning_order": 4,
        "learning_phase": "Descubrir",
        "objective": "Identificar patrones AB y ABB y leer pictogramas sencillos.",
        "prerequisites": ["math-counting"],
    },
    "math-market": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Usar el conteo y las operaciones en situaciones cotidianas.",
        "prerequisites": ["math-counting", "math-sums"],
    },
    "math-measures": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Comparar longitudes, tiempos, capacidades y pesos de objetos cercanos.",
        "prerequisites": ["math-counting"],
    },
    "math-balloons": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Consolidar el conteo hasta 20 de forma rápida y divertida.",
        "prerequisites": ["math-counting"],
        "related_activity": "math-counting",
    },
    "math-race": {
        "learning_order": 8,
        "learning_phase": "Consolidar",
        "objective": "Consolidar sumas hasta 10 y explicar estrategias de cálculo.",
        "prerequisites": ["math-sums"],
        "related_activity": "math-sums",
    },
}


# Ruta recomendada para Matemáticas de 2.º: ampliar el sentido numérico hasta
# 100, formalizar la reagrupación y aplicar las operaciones a medida, tiempo,
# dinero y lectura de datos.
SECOND_GRADE_MATH_PATH = {
    "math-counting": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Leer, descomponer, comparar y ordenar números hasta 100 usando decenas y unidades.",
        "prerequisites": [],
    },
    "math-sums": {
        "learning_order": 2,
        "learning_phase": "Construir",
        "objective": "Resolver sumas y restas hasta 100 con reagrupación y comprobar el procedimiento.",
        "prerequisites": ["math-counting"],
    },
    "math-fractions-geometry": {
        "learning_order": 3,
        "learning_phase": "Explorar",
        "objective": "Medir con centímetros y metros, leer la hora y resolver situaciones sencillas con dinero.",
        "prerequisites": ["math-counting", "math-sums"],
    },
    "math-laboratory": {
        "learning_order": 4,
        "learning_phase": "Descubrir",
        "objective": "Reconocer reglas de patrones y comparar datos representados en gráficas sencillas.",
        "prerequisites": ["math-counting"],
    },
    "math-market": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Usar la resta y el valor del dinero para calcular precios y cambios en compras cotidianas.",
        "prerequisites": ["math-counting", "math-sums", "math-fractions-geometry"],
    },
    "math-measures": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Resolver retos de longitud, duración y dinero eligiendo la unidad y la operación adecuadas.",
        "prerequisites": ["math-fractions-geometry"],
    },
    "math-balloons": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Practicar sumas y restas hasta 100 con reagrupación mediante retroalimentación inmediata.",
        "prerequisites": ["math-sums"],
        "related_activity": "math-sums",
    },
    "math-race": {
        "learning_order": 8,
        "learning_phase": "Consolidar",
        "objective": "Construir las primeras multiplicaciones como suma repetida de grupos iguales.",
        "prerequisites": ["math-sums"],
        "related_activity": "math-sums",
    },
}


THIRD_GRADE_MATH_PATH = {
    "math-counting": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Leer, descomponer, comparar y redondear números hasta 1000.",
        "prerequisites": [],
    },
    "math-sums": {
        "learning_order": 2,
        "learning_phase": "Construir",
        "objective": "Resolver multiplicaciones de las tablas 2, 3, 4, 5 y 10, y divisiones exactas como reparto.",
        "prerequisites": ["math-counting"],
    },
    "math-fractions-geometry": {
        "learning_order": 3,
        "learning_phase": "Explorar",
        "objective": "Calcular perímetros, reconocer ángulos y elegir unidades de masa y capacidad.",
        "prerequisites": ["math-counting", "math-sums"],
    },
    "math-laboratory": {
        "learning_order": 4,
        "learning_phase": "Descubrir",
        "objective": "Representar fracciones unitarias y leer gráficas de barras para comparar datos.",
        "prerequisites": ["math-counting"],
    },
    "math-market": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Aplicar multiplicaciones y divisiones a compras, grupos y repartos cotidianos.",
        "prerequisites": ["math-counting", "math-sums"],
    },
    "math-measures": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Resolver problemas de perímetro, conversión de unidades, masa, capacidad y ángulos.",
        "prerequisites": ["math-fractions-geometry"],
    },
    "math-balloons": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Practicar las tablas de multiplicar y las divisiones exactas con retroalimentación inmediata.",
        "prerequisites": ["math-sums"],
        "related_activity": "math-sums",
    },
    "math-race": {
        "learning_order": 8,
        "learning_phase": "Consolidar",
        "objective": "Consolidar la interpretación y comparación de fracciones unitarias.",
        "prerequisites": ["math-laboratory"],
        "related_activity": "math-laboratory",
    },
}


FOURTH_GRADE_MATH_PATH = {
    "math-counting": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Leer, comparar, representar y redondear números decimales hasta centésimas.",
        "prerequisites": [],
    },
    "math-sums": {
        "learning_order": 2,
        "learning_phase": "Construir",
        "objective": "Resolver multiplicaciones y divisiones multidígito y reconocer fracciones equivalentes.",
        "prerequisites": ["math-counting"],
    },
    "math-fractions-geometry": {
        "learning_order": 3,
        "learning_phase": "Explorar",
        "objective": "Calcular áreas y perímetros, convertir unidades y leer el tiempo en formato de 24 horas.",
        "prerequisites": ["math-counting", "math-sums"],
    },
    "math-laboratory": {
        "learning_order": 4,
        "learning_phase": "Descubrir",
        "objective": "Calcular medias y describir probabilidades cualitativas a partir de datos sencillos.",
        "prerequisites": ["math-counting"],
    },
    "math-market": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Resolver problemas cotidianos de varios pasos seleccionando y ordenando operaciones.",
        "prerequisites": ["math-sums", "math-fractions-geometry"],
    },
    "math-measures": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Aplicar área, perímetro, conversiones y duración en situaciones reales.",
        "prerequisites": ["math-fractions-geometry"],
    },
    "math-balloons": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Practicar sumas y restas de décimas y centésimas con retroalimentación inmediata.",
        "prerequisites": ["math-counting"],
        "related_activity": "math-counting",
    },
    "math-race": {
        "learning_order": 8,
        "learning_phase": "Consolidar",
        "objective": "Consolidar la resolución de problemas matemáticos de varios pasos.",
        "prerequisites": ["math-market"],
        "related_activity": "math-market",
    },
}


FIFTH_GRADE_MATH_PATH = {
    "math-counting": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Aplicar porcentajes, potencias de 10 y descomposición en factores primos.",
        "prerequisites": [],
    },
    "math-sums": {
        "learning_order": 2,
        "learning_phase": "Construir",
        "objective": "Resolver operaciones con decimales y sumar o restar fracciones heterogéneas.",
        "prerequisites": ["math-counting"],
    },
    "math-fractions-geometry": {
        "learning_order": 3,
        "learning_phase": "Explorar",
        "objective": "Calcular volúmenes, ubicar coordenadas y utilizar escalas en planos.",
        "prerequisites": ["math-counting", "math-sums"],
    },
    "math-laboratory": {
        "learning_order": 4,
        "learning_phase": "Descubrir",
        "objective": "Resolver proporciones, interpretar gráficas lineales y analizar situaciones de azar.",
        "prerequisites": ["math-counting"],
    },
    "math-market": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Aplicar porcentajes, descuentos y proporciones a decisiones de compra.",
        "prerequisites": ["math-counting", "math-sums"],
    },
    "math-measures": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Resolver situaciones de volumen, coordenadas y escala usando unidades adecuadas.",
        "prerequisites": ["math-fractions-geometry"],
    },
    "math-balloons": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Practicar porcentajes y proporciones con retroalimentación inmediata.",
        "prerequisites": ["math-market"],
        "related_activity": "math-market",
    },
    "math-race": {
        "learning_order": 8,
        "learning_phase": "Consolidar",
        "objective": "Resolver ecuaciones sencillas y comprobar el valor desconocido.",
        "prerequisites": ["math-sums"],
        "related_activity": "math-sums",
    },
}


# Ruta de Lengua Castellana para 3.º. Las cuatro primeras actividades siguen
# las unidades base del plan; las dos siguientes amplían vocabulario y
# gramática, y los juegos consolidan esas competencias.
THIRD_GRADE_LANGUAGE_PATH = {
    "reading-story": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Comprender inferencias, distinguir la idea principal y resumir con evidencias.",
        "prerequisites": [],
    },
    "language-write-create": {
        "learning_order": 2,
        "learning_phase": "Construir",
        "objective": "Planificar y escribir una narración de tres párrafos con un diálogo breve.",
        "prerequisites": ["reading-story"],
    },
    "language-grammar": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Analizar sujeto y predicado, tiempos verbales y prefijos frecuentes.",
        "prerequisites": ["language-write-create"],
    },
    "language-adventure": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Interpretar mitos y novelas gráficas y participar en un club de lectura.",
        "prerequisites": ["reading-story"],
    },
    "language-vocabulary": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Usar familias léxicas, campos semánticos y prefijos para ampliar el vocabulario.",
        "prerequisites": ["reading-story"],
    },
    "words-syllables": {
        "learning_order": 6,
        "learning_phase": "Consolidar",
        "objective": "Consolidar el análisis de oraciones y el uso de tiempos verbales al escribir.",
        "prerequisites": ["language-grammar"],
    },
    "language-balloons": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Practicar familias léxicas y relaciones de significado con retroalimentación inmediata.",
        "prerequisites": ["language-vocabulary"],
        "related_activity": "language-vocabulary",
    },
    "word-detective": {
        "learning_order": 8,
        "learning_phase": "Consolidar",
        "objective": "Practicar sujeto y predicado como detective de palabras.",
        "prerequisites": ["language-grammar"],
        "related_activity": "language-grammar",
    },
}


# Ruta de Lengua Castellana para 4.º: analizar, explicar, revisar y aplicar
# recursos de distintos géneros con una autonomía mayor.
FOURTH_GRADE_LANGUAGE_PATH = {
    "reading-story": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Analizar personajes y ambientes y justificar interpretaciones con evidencias.",
        "prerequisites": [],
    },
    "language-write-create": {
        "learning_order": 2,
        "learning_phase": "Construir",
        "objective": "Organizar un texto expositivo y elaborar una síntesis con ideas principales.",
        "prerequisites": ["reading-story"],
    },
    "words-syllables": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Construir oraciones compuestas y aplicar signos de puntuación con intención.",
        "prerequisites": ["language-write-create"],
    },
    "language-adventure": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Distinguir géneros literarios, reconocer recursos retóricos y leer teatro expresivamente.",
        "prerequisites": ["reading-story"],
    },
    "language-vocabulary": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Interpretar palabras polisémicas utilizando las pistas del contexto.",
        "prerequisites": ["reading-story"],
    },
    "language-grammar": {
        "learning_order": 6,
        "learning_phase": "Consolidar",
        "objective": "Usar conectores y referencias para construir textos cohesionados.",
        "prerequisites": ["words-syllables"],
    },
    "language-balloons": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Practicar polisemia y significado contextual con retroalimentación inmediata.",
        "prerequisites": ["language-vocabulary"],
        "related_activity": "language-vocabulary",
    },
    "word-detective": {
        "learning_order": 8,
        "learning_phase": "Consolidar",
        "objective": "Practicar conectores y cohesión para resolver casos de escritura.",
        "prerequisites": ["language-grammar"],
        "related_activity": "language-grammar",
    },
}


# Ruta de Lengua Castellana para 5.º: leer con criterio, argumentar con
# fuentes, analizar la lengua y dialogar con la literatura universal.
FIFTH_GRADE_LANGUAGE_PATH = {
    "reading-story": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Evaluar fuentes, reconocer sesgos y distinguir hechos, opiniones y evidencias.",
        "prerequisites": [],
    },
    "language-write-create": {
        "learning_order": 2,
        "learning_phase": "Construir",
        "objective": "Escribir un ensayo argumentativo con tesis, argumentos, citas y conclusión.",
        "prerequisites": ["reading-story"],
    },
    "words-syllables": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Analizar morfemas, oraciones subordinadas y registros según la situación.",
        "prerequisites": ["language-write-create"],
    },
    "language-adventure": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Analizar literatura universal y los efectos de la voz narrativa.",
        "prerequisites": ["reading-story"],
    },
    "language-vocabulary": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Interpretar lenguaje figurado e ironía considerando el contexto y la intención.",
        "prerequisites": ["reading-story"],
    },
    "language-grammar": {
        "learning_order": 6,
        "learning_phase": "Consolidar",
        "objective": "Construir textos cohesionados con conectores, referencias y subordinación.",
        "prerequisites": ["words-syllables"],
    },
    "language-balloons": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Practicar lenguaje figurado y sentido contextual con retroalimentación inmediata.",
        "prerequisites": ["language-vocabulary"],
        "related_activity": "language-vocabulary",
    },
    "word-detective": {
        "learning_order": 8,
        "learning_phase": "Consolidar",
        "objective": "Practicar cohesión textual y conectores para resolver casos de escritura.",
        "prerequisites": ["language-grammar"],
        "related_activity": "language-grammar",
    },
}


# Ruta de Sociales para 1.º, desde los espacios y vínculos cercanos hasta la
# toma de decisiones responsables en la comunidad.
FIRST_GRADE_SOCIAL_PATH = {
    "social-identity": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Reconocer familia, escuela, emociones y reglas básicas de convivencia.",
        "prerequisites": [],
        "project": "Árbol genealógico familiar",
    },
    "social-geography": {
        "learning_order": 2,
        "learning_phase": "Explorar",
        "objective": "Representar casa, escuela y barrio con mapas dibujados y referencias.",
        "prerequisites": ["social-identity"],
    },
    "social-history": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Ordenar experiencias en una línea de vida y diferenciar ayer, hoy y mañana.",
        "prerequisites": ["social-identity"],
    },
    "social-economy": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Diferenciar necesidades y deseos, y practicar decisiones de ahorro responsable.",
        "prerequisites": ["social-identity"],
    },
    "social-culture": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Reconocer tradiciones familiares y mostrar respeto por distintas culturas.",
        "prerequisites": ["social-identity"],
    },
    "social-media": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Identificar medios cercanos y usarlos con acompañamiento y seguridad.",
        "prerequisites": ["social-identity"],
    },
    "social-explorer": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Consolidar la orientación en el barrio con un mapa de pistas y referencias.",
        "prerequisites": ["social-geography"],
        "related_activity": "social-geography",
    },
}


# Ruta de Sociales para 2.º: ampliar la mirada desde la comunidad cercana
# hacia el municipio, su historia y sus intercambios cotidianos.
SECOND_GRADE_SOCIAL_PATH = {
    "social-identity": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Reconocer comunidad, roles, diversidad, derechos y formas de participación.",
        "prerequisites": [],
    },
    "social-geography": {
        "learning_order": 2,
        "learning_phase": "Explorar",
        "objective": "Leer mapas con leyenda, ubicar servicios municipales y observar el clima.",
        "prerequisites": ["social-identity"],
    },
    "social-history": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Investigar la historia local mediante generaciones, entrevistas y museos.",
        "prerequisites": ["social-identity"],
        "project": "Entrevista a un abuelo o vecino",
    },
    "social-economy": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Distinguir bienes y servicios y tomar decisiones responsables frente a la publicidad.",
        "prerequisites": ["social-identity"],
    },
    "social-culture": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Reconocer costumbres y patrimonio local respetando la diversidad cultural.",
        "prerequisites": ["social-identity"],
    },
    "social-media": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Identificar fuentes y consultar información con acompañamiento para evitar rumores.",
        "prerequisites": ["social-identity"],
    },
    "social-explorer": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Consolidar la lectura de mapas y servicios mediante una ruta comunitaria con códigos.",
        "prerequisites": ["social-geography"],
        "related_activity": "social-geography",
    },
}


# Ruta de Sociales para 3.º: comprender la participación democrática,
# interpretar el territorio y conectar trabajo, recursos y decisiones públicas.
THIRD_GRADE_SOCIAL_PATH = {
    "social-identity": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Relacionar derechos y responsabilidades y participar en decisiones democráticas escolares.",
        "prerequisites": [],
    },
    "social-geography": {
        "learning_order": 2,
        "learning_phase": "Explorar",
        "objective": "Interpretar la región, sus recursos, paisajes y actividades mediante mapas temáticos.",
        "prerequisites": ["social-identity"],
        "project": "Mapa temático de la región",
    },
    "social-history": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Construir líneas de tiempo y comparar fuentes para explicar cambios de la comunidad.",
        "prerequisites": ["social-identity"],
    },
    "social-economy": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Reconocer sectores económicos, valorar el trabajo y comprender el uso de los impuestos.",
        "prerequisites": ["social-geography"],
    },
    "social-culture": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Valorar la diversidad cultural y el patrimonio como parte de la identidad comunitaria.",
        "prerequisites": ["social-identity"],
    },
    "social-media": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Comparar fuentes sencillas y comunicar información con responsabilidad.",
        "prerequisites": ["social-history"],
    },
    "social-explorer": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Aplicar decisiones de presupuesto para mejorar servicios de la comunidad.",
        "prerequisites": ["social-economy"],
        "related_activity": "social-economy",
    },
}


# Ruta de Sociales para 4.º: pasar de la comunidad y la región al análisis
# ciudadano, la historia nacional y las decisiones económicas complejas.
FOURTH_GRADE_SOCIAL_PATH = {
    "social-identity": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Comprender ciudadanía, Constitución, derechos, deberes e inclusión.",
        "prerequisites": [],
    },
    "social-geography": {
        "learning_order": 2,
        "learning_phase": "Explorar",
        "objective": "Interpretar mapas políticos y físicos y relacionar relieve, clima y regiones.",
        "prerequisites": ["social-identity"],
        "project": "Mapa temático de una región del país",
    },
    "social-history": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Analizar etapas, personajes y fuentes de la historia nacional en contexto.",
        "prerequisites": ["social-identity"],
        "project": "Investiga un personaje histórico",
    },
    "social-economy": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Organizar presupuestos y comprender empresa, banco y comercio responsable.",
        "prerequisites": ["social-geography"],
    },
    "social-culture": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Valorar patrimonio, diversidad cultural e inclusión en el país.",
        "prerequisites": ["social-identity"],
    },
    "social-media": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Evaluar información de medios y participar responsablemente en la vida democrática.",
        "prerequisites": ["social-history"],
    },
    "social-explorer": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Aplicar comercio, rutas, presupuesto y cooperación en una misión internacional.",
        "prerequisites": ["social-economy", "social-geography"],
        "related_activity": "social-economy",
    },
}


# Ruta de Sociales para 5.º: ampliar la mirada desde el país hacia la
# ciudadanía global, la historia mundial y la acción sostenible local.
FIFTH_GRADE_SOCIAL_PATH = {
    "social-identity": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Comprender ciudadanía global, derechos humanos y cooperación internacional.",
        "prerequisites": [],
    },
    "social-geography": {
        "learning_order": 2,
        "learning_phase": "Explorar",
        "objective": "Interpretar continentes, husos horarios, globalización y relaciones geopolíticas.",
        "prerequisites": ["social-identity"],
    },
    "social-history": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Explicar civilizaciones y revoluciones mediante causas, consecuencias y fuentes.",
        "prerequisites": ["social-geography"],
    },
    "social-economy": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Analizar emprendimiento, finanzas, desigualdad e impacto de proyectos sostenibles.",
        "prerequisites": ["social-identity", "social-geography"],
        "project": "Proyecto ODS local",
    },
    "social-culture": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Valorar identidades multiculturales y combatir prejuicios y estereotipos.",
        "prerequisites": ["social-identity"],
    },
    "social-media": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Evaluar medios y fuentes para participar responsablemente en debates globales.",
        "prerequisites": ["social-history", "social-identity"],
    },
    "social-explorer": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Argumentar, negociar y construir acuerdos mediante un Modelo ONU simplificado.",
        "prerequisites": ["social-identity", "social-geography"],
        "related_activity": "social-identity",
    },
}


# Ruta de Ciencias Naturales para 1.º: observar el cuerpo y el entorno,
# clasificar, registrar cambios y actuar con cuidado y seguridad.
FIRST_GRADE_SCIENCE_PATH = {
    "science-life": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Reconocer cuerpo, sentidos y hábitos básicos de cuidado.",
        "prerequisites": [],
    },
    "science-matter": {
        "learning_order": 2,
        "learning_phase": "Explorar",
        "objective": "Observar y clasificar materiales por sus propiedades.",
        "prerequisites": ["science-life"],
    },
    "science-earth": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Distinguir día y noche, registrar el tiempo y cuidar la Tierra.",
        "prerequisites": ["science-life"],
        "project": "Diario del tiempo durante una semana",
    },
    "science-technology": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Usar herramientas sencillas y aplicar hábitos de higiene y seguridad.",
        "prerequisites": ["science-matter"],
    },
    "science-health": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Consolidar higiene, alimentación, descanso y hábitos saludables.",
        "prerequisites": ["science-life"],
    },
    "science-living": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Reconocer plantas y animales cercanos y sus necesidades de cuidado.",
        "prerequisites": ["science-life"],
    },
    "science-lab": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Clasificar seres vivos y objetos usando observación y pistas del laboratorio.",
        "prerequisites": ["science-life", "science-matter"],
        "related_activity": "science-life",
    },
}


# Ruta de Ciencias Naturales para 2.º: observar ciclos y cambios, explicar
# fenómenos sencillos y diseñar soluciones sostenibles.
SECOND_GRADE_SCIENCE_PATH = {
    "science-life": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Reconocer ciclos de vida y necesidades de plantas, animales y personas.",
        "prerequisites": [],
    },
    "science-matter": {
        "learning_order": 2,
        "learning_phase": "Explorar",
        "objective": "Explicar estados del agua y observar efectos de luz, sombras, imanes y fuerzas.",
        "prerequisites": ["science-life"],
    },
    "science-earth": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Relacionar Luna, ciclo del agua y reciclaje con el cuidado del planeta.",
        "prerequisites": ["science-matter"],
        "project": "Siembra y observa un frijol",
    },
    "science-technology": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Diseñar una solución segura usando materiales reutilizados.",
        "prerequisites": ["science-matter"],
    },
    "science-health": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Consolidar hábitos de salud, higiene, alimentación y descanso.",
        "prerequisites": ["science-life"],
    },
    "science-living": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Clasificar seres vivos cercanos y reconocer cómo cuidarlos.",
        "prerequisites": ["science-life"],
    },
    "science-lab": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Ordenar etapas y explicar cambios en ciclos de vida mediante un juego interactivo.",
        "prerequisites": ["science-life"],
        "related_activity": "science-life",
    },
}


# Ruta de Ciencias Naturales para 3.º: comprender relaciones de los seres
# vivos, fenómenos de la Tierra y soluciones tecnológicas.
THIRD_GRADE_SCIENCE_PATH = {
    "science-life": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Explicar partes de plantas, productores, consumidores y cadenas alimentarias.",
        "prerequisites": [],
    },
    "science-matter": {
        "learning_order": 2,
        "learning_phase": "Explorar",
        "objective": "Investigar mezclas, energía y máquinas simples en situaciones cotidianas.",
        "prerequisites": ["science-life"],
    },
    "science-earth": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Reconocer sistema solar, capas de la Tierra y fenómenos volcánicos.",
        "prerequisites": ["science-matter"],
    },
    "science-technology": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Usar secuencias y programación por bloques para diseñar soluciones seguras.",
        "prerequisites": ["science-matter"],
        "project": "Circuito simple (pila + LED)",
    },
    "science-health": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Consolidar hábitos de salud y explicar decisiones que protegen el bienestar.",
        "prerequisites": ["science-life"],
    },
    "science-living": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Reconocer diversidad de seres vivos y relaciones de cuidado en los ecosistemas.",
        "prerequisites": ["science-life"],
    },
    "science-lab": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Construir y explicar cadenas alimentarias mediante un reto interactivo.",
        "prerequisites": ["science-life"],
        "related_activity": "science-life",
    },
}


# Ruta de Ciencias Naturales para 4.º: integrar sistemas, energía, territorio
# y tecnología con pensamiento preventivo y responsabilidad ambiental.
FOURTH_GRADE_SCIENCE_PATH = {
    "science-life": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Explicar sistemas del cuerpo y relaciones entre seres vivos y ambiente.",
        "prerequisites": [],
    },
    "science-matter": {
        "learning_order": 2,
        "learning_phase": "Explorar",
        "objective": "Analizar circuitos, energías renovables y máquinas simples.",
        "prerequisites": ["science-life"],
    },
    "science-earth": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Interpretar relieve, ríos, mapas y acciones de prevención ante riesgos naturales.",
        "prerequisites": ["science-matter"],
        "project": "Modelo de volcán o relieve",
    },
    "science-technology": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Relacionar robótica, sensores y biomimética con soluciones tecnológicas éticas.",
        "prerequisites": ["science-matter", "science-earth"],
    },
    "science-health": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Consolidar decisiones saludables y comprender relaciones entre cuerpo y ambiente.",
        "prerequisites": ["science-life"],
    },
    "science-living": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Valorar biodiversidad, hábitats y acciones de conservación.",
        "prerequisites": ["science-life"],
    },
    "science-lab": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Simular cambios en un ecosistema y tomar decisiones para conservar su equilibrio.",
        "prerequisites": ["science-life", "science-earth"],
        "related_activity": "science-life",
    },
}


# Ruta de Ciencias Naturales para 5.º: investigar desde la célula y la Tierra
# hasta proyectos STEM, datos e innovación responsable.
FIFTH_GRADE_SCIENCE_PATH = {
    "science-life": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Comprender células, adaptaciones, poblaciones y evolución.",
        "prerequisites": [],
    },
    "science-matter": {
        "learning_order": 2,
        "learning_phase": "Explorar",
        "objective": "Investigar reacciones, electricidad y método científico con evidencias.",
        "prerequisites": ["science-life"],
    },
    "science-earth": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Relacionar universo, placas tectónicas y cambio climático.",
        "prerequisites": ["science-matter"],
    },
    "science-technology": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Diseñar prototipos STEM y evaluar IA, datos, privacidad e impacto.",
        "prerequisites": ["science-matter", "science-earth"],
        "project": "Proyecto feria de ciencias",
    },
    "science-health": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Analizar salud pública, hábitos y decisiones basadas en evidencias.",
        "prerequisites": ["science-life"],
    },
    "science-living": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Valorar conservación, servicios ecosistémicos y diversidad de seres vivos.",
        "prerequisites": ["science-life", "science-earth"],
    },
    "science-lab": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Aplicar método científico, analizar datos y comunicar conclusiones responsables.",
        "prerequisites": ["science-matter", "science-technology"],
        "related_activity": "science-matter",
    },
}


# Ruta de Inglés para 1.º: escuchar, repetir, comprender y usar expresiones
# breves en situaciones cercanas y lúdicas.
FIRST_GRADE_ENGLISH_PATH = {
    "english-identity": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Saludar, presentarse y reconocer colores y números del 1 al 10.",
        "prerequisites": [],
        "oral_challenge": "This is me: say hello, your name and your age.",
    },
    "english-community": {
        "learning_order": 2,
        "learning_phase": "Explorar",
        "objective": "Nombrar escuela, personas, objetos y colores con frases básicas.",
        "prerequisites": ["english-identity"],
    },
    "english-world": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Reconocer animales y acciones mediante canciones, gestos y frases cortas.",
        "prerequisites": ["english-identity"],
    },
    "english-culture": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Participar en canciones y hablar de celebraciones, emociones y cortesía.",
        "prerequisites": ["english-identity"],
    },
    "english-food": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Reconocer alimentos y expresiones de gusto en situaciones cotidianas.",
        "prerequisites": ["english-community"],
    },
    "english-nature": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Describir animales y naturaleza con vocabulario básico.",
        "prerequisites": ["english-world"],
    },
    "word-quest": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Consolidar vocabulario con memoria, imágenes y sonidos.",
        "prerequisites": ["english-identity", "english-community"],
        "related_activity": "english-identity",
    },
}


# Ruta de Inglés para 2.º: ampliar vocabulario, comprender cuentos y usar
# frases breves para hablar de la vida cotidiana y la cultura.
SECOND_GRADE_ENGLISH_PATH = {
    "english-identity": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Describir familia, casa y pertenencias con vocabulario básico.",
        "prerequisites": [],
        "oral_challenge": "Describe your family or home with three short sentences.",
    },
    "english-community": {
        "learning_order": 2,
        "learning_phase": "Explorar",
        "objective": "Nombrar lugares de la ciudad y expresar rutinas diarias.",
        "prerequisites": ["english-identity"],
    },
    "english-world": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Comprender personajes, lugares y secuencias en un cuento como Goldilocks.",
        "prerequisites": ["english-identity"],
    },
    "english-culture": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Hablar de alimentos, gustos, festivales y peticiones amables.",
        "prerequisites": ["english-community"],
    },
    "english-food": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Consolidar alimentos, gustos y hábitos cotidianos en inglés.",
        "prerequisites": ["english-culture"],
    },
    "english-nature": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Describir animales y naturaleza con frases sencillas.",
        "prerequisites": ["english-world"],
    },
    "word-quest": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Ordenar palabras y construir oraciones sobre familia y rutinas.",
        "prerequisites": ["english-identity", "english-community"],
        "related_activity": "english-community",
    },
}


# Ruta de Inglés para 3.º: pasar de frases cotidianas a secuencias,
# narraciones breves y comunicación escrita con un pen-pal.
THIRD_GRADE_ENGLISH_PATH = {
    "english-identity": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Describir rutinas, horarios y actividades diarias en presente simple.",
        "prerequisites": [],
        "oral_challenge": "Tell a short story in English for 30 seconds.",
    },
    "english-community": {
        "learning_order": 2,
        "learning_phase": "Explorar",
        "objective": "Expresar gustos y describir hobbies, deportes y lugares.",
        "prerequisites": ["english-identity"],
    },
    "english-world": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Comprender aventuras, mitos y leyendas con personajes y secuencias.",
        "prerequisites": ["english-identity"],
    },
    "english-culture": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Escribir un correo breve para presentarse e intercambiar información con un pen-pal.",
        "prerequisites": ["english-community"],
        "oral_challenge": "Read your short email aloud to a partner.",
    },
    "english-food": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Consolidar vocabulario de alimentos, salud y gustos en situaciones cotidianas.",
        "prerequisites": ["english-community"],
    },
    "english-nature": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Describir animales y naturaleza usando frases conectadas.",
        "prerequisites": ["english-world"],
    },
    "word-quest": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Consolidar gramática básica mediante un concurso de preguntas y respuestas.",
        "prerequisites": ["english-identity", "english-community"],
        "related_activity": "english-identity",
    },
}


# Ruta de Inglés para 4.º: expresar opiniones, cuidar la salud, hablar del
# futuro y comunicar información cultural en situaciones auténticas.
FOURTH_GRADE_ENGLISH_PATH = {
    "english-identity": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Expresar opiniones, preferencias y comparaciones con razones sencillas.",
        "prerequisites": [],
        "oral_challenge": "My hero: give a one-minute presentation.",
    },
    "english-community": {
        "learning_order": 2,
        "learning_phase": "Explorar",
        "objective": "Describir cuerpo, hábitos y consejos para cuidar la salud.",
        "prerequisites": ["english-identity"],
    },
    "english-world": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Hablar de dispositivos, planes y posibilidades tecnológicas futuras.",
        "prerequisites": ["english-identity"],
    },
    "english-culture": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Investigar y presentar un proyecto cultural sobre el Reino Unido y Estados Unidos.",
        "prerequisites": ["english-community"],
    },
    "english-food": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Consolidar alimentos, salud y preferencias en conversaciones cotidianas.",
        "prerequisites": ["english-community"],
    },
    "english-nature": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Describir animales y naturaleza relacionando acciones y características.",
        "prerequisites": ["english-world"],
    },
    "word-quest": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Representar diálogos funcionales de tienda y restaurante con cortesía.",
        "prerequisites": ["english-community", "english-culture"],
        "related_activity": "english-community",
    },
}


# Ruta de Inglés para 5.º: comunicar ideas conectadas, evaluar información,
# hablar del mundo y participar en debates y proyectos.
FIFTH_GRADE_ENGLISH_PATH = {
    "english-identity": {
        "learning_order": 1,
        "learning_phase": "Construir",
        "objective": "Describir problemas ambientales y proponer acciones sostenibles con razones.",
        "prerequisites": [],
        "oral_challenge": "Debate: Should we protect the planet?",
    },
    "english-community": {
        "learning_order": 2,
        "learning_phase": "Explorar",
        "objective": "Analizar noticias, distinguir hechos y opiniones y evaluar fuentes.",
        "prerequisites": ["english-identity"],
    },
    "english-world": {
        "learning_order": 3,
        "learning_phase": "Descubrir",
        "objective": "Describir viajes y experiencias culturales usando pasado y futuro básicos.",
        "prerequisites": ["english-identity"],
    },
    "english-culture": {
        "learning_order": 4,
        "learning_phase": "Aplicar",
        "objective": "Hablar de profesiones, metas, comunicación global y retos compartidos.",
        "prerequisites": ["english-community", "english-world"],
    },
    "english-food": {
        "learning_order": 5,
        "learning_phase": "Aplicar",
        "objective": "Consolidar salud, alimentos y decisiones responsables en conversaciones.",
        "prerequisites": ["english-identity"],
    },
    "english-nature": {
        "learning_order": 6,
        "learning_phase": "Aplicar",
        "objective": "Describir naturaleza y acciones ambientales con ideas conectadas.",
        "prerequisites": ["english-identity", "english-world"],
    },
    "word-quest": {
        "learning_order": 7,
        "learning_phase": "Consolidar",
        "objective": "Resolver pistas de comunicación global en un escape room de Inglés.",
        "prerequisites": ["english-community", "english-culture"],
        "related_activity": "english-community",
    },
}


def learning_path_for(activity, grade):
    if grade == 1 and activity.get("subject") == "Matemáticas":
        return FIRST_GRADE_MATH_PATH.get(activity["key"], {})
    if grade == 2 and activity.get("subject") == "Matemáticas":
        return SECOND_GRADE_MATH_PATH.get(activity["key"], {})
    if grade == 3 and activity.get("subject") == "Matemáticas":
        return THIRD_GRADE_MATH_PATH.get(activity["key"], {})
    if grade == 4 and activity.get("subject") == "Matemáticas":
        return FOURTH_GRADE_MATH_PATH.get(activity["key"], {})
    if grade == 5 and activity.get("subject") == "Matemáticas":
        return FIFTH_GRADE_MATH_PATH.get(activity["key"], {})
    if grade == 3 and activity.get("subject") == "Lengua Castellana":
        return THIRD_GRADE_LANGUAGE_PATH.get(activity["key"], {})
    if grade == 4 and activity.get("subject") == "Lengua Castellana":
        return FOURTH_GRADE_LANGUAGE_PATH.get(activity["key"], {})
    if grade == 5 and activity.get("subject") == "Lengua Castellana":
        return FIFTH_GRADE_LANGUAGE_PATH.get(activity["key"], {})
    if grade == 1 and activity.get("subject") == "Sociales":
        return FIRST_GRADE_SOCIAL_PATH.get(activity["key"], {})
    if grade == 2 and activity.get("subject") == "Sociales":
        return SECOND_GRADE_SOCIAL_PATH.get(activity["key"], {})
    if grade == 3 and activity.get("subject") == "Sociales":
        return THIRD_GRADE_SOCIAL_PATH.get(activity["key"], {})
    if grade == 4 and activity.get("subject") == "Sociales":
        return FOURTH_GRADE_SOCIAL_PATH.get(activity["key"], {})
    if grade == 5 and activity.get("subject") == "Sociales":
        return FIFTH_GRADE_SOCIAL_PATH.get(activity["key"], {})
    if grade == 1 and activity.get("subject") == "Ciencias Naturales":
        return FIRST_GRADE_SCIENCE_PATH.get(activity["key"], {})
    if grade == 2 and activity.get("subject") == "Ciencias Naturales":
        return SECOND_GRADE_SCIENCE_PATH.get(activity["key"], {})
    if grade == 3 and activity.get("subject") == "Ciencias Naturales":
        return THIRD_GRADE_SCIENCE_PATH.get(activity["key"], {})
    if grade == 4 and activity.get("subject") == "Ciencias Naturales":
        return FOURTH_GRADE_SCIENCE_PATH.get(activity["key"], {})
    if grade == 5 and activity.get("subject") == "Ciencias Naturales":
        return FIFTH_GRADE_SCIENCE_PATH.get(activity["key"], {})
    if grade == 1 and activity.get("subject") == "Inglés":
        return FIRST_GRADE_ENGLISH_PATH.get(activity["key"], {})
    if grade == 2 and activity.get("subject") == "Inglés":
        return SECOND_GRADE_ENGLISH_PATH.get(activity["key"], {})
    if grade == 3 and activity.get("subject") == "Inglés":
        return THIRD_GRADE_ENGLISH_PATH.get(activity["key"], {})
    if grade == 4 and activity.get("subject") == "Inglés":
        return FOURTH_GRADE_ENGLISH_PATH.get(activity["key"], {})
    if grade == 5 and activity.get("subject") == "Inglés":
        return FIFTH_GRADE_ENGLISH_PATH.get(activity["key"], {})
    return {}
