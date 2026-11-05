"""Contenido curricular de Ciencias Naturales, Sociales e Inglés.

El módulo mantiene los datos separados del enrutador y expone el mismo
contrato que ``extra_content.curriculum_for_grade``: una lección y diez
preguntas adaptadas al grado.
"""

from .extra_content import question as make_question


SUBJECTS = [
    {
        "name": "Matemáticas",
        "icon": "calculator",
        "color": "#5b5ce2",
        "description": "Operaciones, problemas y retos.",
    },
    {
        "name": "Lengua Castellana",
        "icon": "book",
        "color": "#f28c28",
        "description": "Lectura, escritura y palabras.",
    },
    {
        "name": "Ciencias Naturales",
        "icon": "leaf",
        "color": "#21a889",
        "description": "Descubre la vida, la Tierra y la tecnología.",
    },
    {
        "name": "Sociales",
        "icon": "globe",
        "color": "#e66a9b",
        "description": "Comprende tu comunidad y el mundo.",
    },
    {
        "name": "Inglés",
        "icon": "rainbow",
        "color": "#3ba9dd",
        "description": "Aprende palabras y expresiones para comunicarte.",
    },
]


_UNIT_DEFINITIONS = [
    ("science-life", "Ciencias Naturales", "Seres vivos y cuerpo", "Observa los seres vivos y conoce cómo funciona tu cuerpo.", "leaf"),
    ("science-matter", "Ciencias Naturales", "Materia y energía", "Explora los materiales, el agua, la luz y las fuerzas.", "sun"),
    ("science-earth", "Ciencias Naturales", "Tierra y universo", "Descubre el cielo, el planeta y los cambios de la naturaleza.", "planet"),
    ("science-technology", "Ciencias Naturales", "Ciencia, tecnología y sociedad", "Usa la ciencia para resolver problemas de forma segura y sostenible.", "lightbulb"),
    ("social-identity", "Sociales", "Identidad y convivencia", "Reconoce quién eres, tus derechos y cómo convivir con otros.", "users"),
    ("social-geography", "Sociales", "Geografía y espacio", "Representa lugares, paisajes y relaciones entre las personas y su territorio.", "globe"),
    ("social-history", "Sociales", "Historia y tiempo", "Ordena hechos, conoce fuentes y comprende los cambios de las sociedades.", "clock"),
    ("social-economy", "Sociales", "Sociedad y economía", "Distingue necesidades, trabajo, bienes, servicios y decisiones responsables.", "hand"),
    ("english-identity", "Inglés", "This is me", "Saluda, presenta tu identidad y habla de tus gustos y rutinas.", "smile"),
    ("english-community", "Inglés", "My community", "Habla de tu familia, escuela, ciudad y actividades cotidianas.", "users"),
    ("english-world", "Inglés", "Stories and the world", "Describe animales, aventuras, viajes y situaciones del mundo.", "rainbow"),
    ("english-culture", "Inglés", "Culture and communication", "Expresa opiniones, conoce culturas y comunica ideas con claridad.", "flag"),
    ("science-health", "Ciencias Naturales", "Salud y hábitos", "Conoce hábitos de higiene, alimentación y descanso para cuidar tu salud.", "smile"),
    ("science-living", "Ciencias Naturales", "Diversidad de seres vivos", "Clasifica y cuida la variedad de seres vivos que habitan la Tierra.", "leaf"),
    ("social-culture", "Sociales", "Cultura, patrimonio y tradiciones", "Aprecia las tradiciones, el patrimonio y la diversidad cultural.", "flag"),
    ("social-media", "Sociales", "Medios, información y convivencia digital", "Usa la información y los medios con criterio y respeto.", "book"),
    ("english-food", "Inglés", "Food and health", "Talks about food, health and daily habits.", "smile"),
    ("english-nature", "Inglés", "Animals and nature", "Describes animals and nature with simple words.", "leaf"),
]

SUBJECT_UNIT_KEYS = {item[0] for item in _UNIT_DEFINITIONS}

SUBJECT_ACTIVITIES = [
    {
        "key": key,
        "subject": subject,
        "kind": "Aprendizaje",
        "title": title,
        "description": description,
        "curriculum": key,
        "color": "#21a889" if subject == "Ciencias Naturales" else "#e66a9b" if subject == "Sociales" else "#3ba9dd",
        "icon": icon,
        "points": 100,
        "minutes": 8,
        "lesson": [],
        "questions": [],
    }
    for key, subject, title, description, icon in _UNIT_DEFINITIONS
]


def _rows(*items):
    """Convierte filas legibles en diez preguntas sin repetir literalmente el enunciado."""
    questions = [make_question(prompt, correct, wrong1, wrong2, index=i) for i, (prompt, correct, wrong1, wrong2) in enumerate(items)]
    for i, (_, correct, wrong1, wrong2) in enumerate(items):
        questions.append(make_question(
            f"Repaso: elige la respuesta correcta sobre esta unidad (pista: {correct}).",
            correct,
            wrong1,
            wrong2,
            index=i + len(items),
        ))
    return questions


# Cinco preguntas nucleares por grado y unidad. El bloque de repaso completa
# diez ejercicios, manteniendo una carga breve y reutilizable para los juegos.
SCIENCE = {
    "science-life": {
        1: ("Mi cuerpo y mis sentidos", "Reconoce las partes del cuerpo y usa los sentidos para observar.", [
            ("¿Con qué vemos?", "los ojos", "las orejas", "las manos"),
            ("¿Con qué escuchamos?", "los oídos", "la nariz", "los pies"),
            ("¿Cuál es un ser vivo?", "un perro", "una piedra", "una silla"),
            ("¿Qué necesita una planta?", "agua y luz", "una televisión", "un lápiz"),
            ("¿Qué hábito cuida el cuerpo?", "lavarse las manos", "no dormir", "comer solo dulces"),
        ]),
        2: ("Ciclos de vida", "Los seres vivos nacen, crecen, se reproducen y mueren; cada uno cambia de manera diferente.", [
            ("¿Qué necesita una semilla para germinar?", "agua y condiciones adecuadas", "una batería", "una moneda"),
            ("¿En qué se convierte una oruga?", "en mariposa", "en pez", "en roca"),
            ("¿Cuál es una etapa de la vida humana?", "la infancia", "la evaporación", "la sombra"),
            ("¿Qué parte ayuda a una planta a absorber agua?", "la raíz", "el pétalo", "el fruto"),
            ("¿Qué tienen en común los seres vivos?", "realizan funciones vitales", "son todos iguales", "no cambian nunca"),
        ]),
        3: ("Plantas, animales y cadenas", "Las plantas producen alimento y los animales se relacionan dentro de cadenas alimentarias.", [
            ("¿Qué parte de la planta capta mucha luz?", "la hoja", "la raíz", "la semilla"),
            ("¿Qué organismo produce su propio alimento?", "una planta", "un león", "un hongo de pan"),
            ("En hierba → conejo → zorro, el conejo es…", "consumidor", "productor", "planeta"),
            ("¿Qué función cumple la raíz?", "sujeta y absorbe", "vuela", "produce sonidos"),
            ("¿Qué relación muestra una cadena alimentaria?", "quién sirve de alimento a quién", "el tamaño de una roca", "la distancia al Sol"),
        ]),
        4: ("Sistemas y ecosistemas", "Los órganos trabajan en sistemas y los seres vivos interactúan con su ecosistema.", [
            ("¿Qué sistema permite respirar?", "el respiratorio", "el solar", "el monetario"),
            ("¿Qué es un ecosistema?", "seres vivos y su ambiente", "solo una especie", "una máquina"),
            ("¿Qué factor no vivo hay en un ecosistema?", "la luz", "un conejo", "un árbol"),
            ("¿Qué protege al cuerpo de muchos golpes?", "el esqueleto", "el estómago", "la lengua"),
            ("¿Qué acción favorece la biodiversidad?", "proteger los hábitats", "destruir nidos", "contaminar ríos"),
        ]),
        5: ("Células y adaptaciones", "La célula es la unidad básica de la vida y las adaptaciones ayudan a sobrevivir en un ambiente.", [
            ("¿Qué es la célula?", "la unidad básica de un ser vivo", "un planeta", "un mineral"),
            ("¿Qué adaptación ayuda al oso polar?", "su pelaje aislante", "sus alas", "sus branquias"),
            ("¿Qué sistema transporta sangre?", "el circulatorio", "el digestivo solamente", "el nervioso de una planta"),
            ("¿Qué es una población?", "individuos de la misma especie", "todos los planetas", "una sola célula"),
            ("¿Qué puede producir la pérdida de biodiversidad?", "desequilibrios en los ecosistemas", "más hábitats", "agua más limpia siempre"),
        ]),
    },
    "science-matter": {
        1: ("Materiales y propiedades", "Los objetos están hechos de materiales que podemos observar, comparar y clasificar.", [
            ("¿Qué material puede ser transparente?", "el vidrio", "la piedra", "la madera opaca"),
            ("¿Qué objeto suele ser flexible?", "una goma", "un ladrillo", "un vaso de vidrio"),
            ("¿Qué hacemos al clasificar?", "agrupamos por características", "mezclamos todo", "apagamos la luz"),
            ("¿Cuál es un material natural?", "la madera", "el plástico", "el nailon"),
            ("¿Qué material absorbe agua fácilmente?", "una esponja", "un espejo", "una cuchara metálica"),
        ]),
        2: ("Agua, luz y fuerzas", "El agua cambia de estado y la luz y las fuerzas producen efectos que podemos observar.", [
            ("¿Cómo se llama el agua congelada?", "hielo", "vapor", "arena"),
            ("¿Qué ocurre al calentar agua?", "puede evaporarse", "se convierte en piedra", "desaparece sin cambio"),
            ("¿Qué produce una sombra?", "un objeto bloquea la luz", "el sonido", "el viento solamente"),
            ("¿Qué es empujar?", "aplicar una fuerza alejando", "mirar un objeto", "medir el tiempo"),
            ("¿Qué atrae un imán?", "algunos metales", "todas las telas", "el agua siempre"),
        ]),
        3: ("Mezclas, energía y máquinas", "Las mezclas reúnen materiales y las máquinas simples ayudan a aplicar fuerzas.", [
            ("¿Qué mezcla puede separarse con un colador?", "arena y piedras", "agua y azúcar disuelta", "aire"),
            ("¿Qué forma de energía da una bombilla encendida?", "luz", "sonido de una roca", "masa"),
            ("¿Qué máquina simple es una rampa?", "plano inclinado", "termómetro", "brújula"),
            ("¿Qué sucede al frotar dos superficies?", "puede aparecer fricción", "se crea una planta", "desaparece la materia"),
            ("¿Qué fuente es renovable?", "el Sol", "el carbón", "el petróleo"),
        ]),
        4: ("Circuitos y energía", "La electricidad circula en un circuito cerrado y las fuentes renovables reducen impactos.", [
            ("¿Qué necesita un circuito para funcionar?", "un camino cerrado", "un camino roto", "solo un dibujo"),
            ("¿Qué material conduce bien la electricidad?", "el cobre", "el plástico", "la goma"),
            ("¿Qué fuente usa el viento?", "la energía eólica", "la energía fósil", "la energía muscular"),
            ("¿Qué hace una palanca?", "ayuda a mover una carga", "produce lluvia", "mide la temperatura"),
            ("¿Qué acción ahorra energía?", "apagar luces innecesarias", "dejar aparatos encendidos", "abrir el refrigerador mucho tiempo"),
        ]),
        5: ("Reacciones y método científico", "Las reacciones transforman sustancias y el método científico permite investigar con evidencias.", [
            ("¿Qué es una reacción química?", "una transformación de sustancias", "un cambio de lugar", "una sombra"),
            ("¿Qué se cambia en un experimento controlado?", "una variable", "todas las variables a la vez", "ningún dato"),
            ("¿Qué mide un voltímetro?", "diferencia de potencial", "longitud de una mesa", "cantidad de lluvia"),
            ("¿Qué material es buen aislante?", "el plástico", "el cobre", "el aluminio"),
            ("¿Qué debe hacer una conclusión?", "responder con base en los datos", "inventar resultados", "ignorar observaciones"),
        ]),
    },
    "science-earth": {
        1: ("Día, noche y cuidado de la Tierra", "El Sol ilumina la Tierra y nuestras acciones pueden cuidar el planeta.", [
            ("¿Cuándo vemos más luz solar?", "de día", "de noche", "en una cueva siempre"),
            ("¿Qué vemos en el cielo de noche?", "la Luna y estrellas", "un arcoíris siempre", "el fondo del mar"),
            ("¿Qué acción cuida la Tierra?", "reciclar", "tirar basura", "desperdiciar agua"),
            ("¿Qué necesitamos para vivir?", "aire y agua", "solo juguetes", "humo"),
            ("¿Qué produce una nube?", "gotas de agua agrupadas", "piedras secas", "luz sólida"),
        ]),
        2: ("Luna, agua y reciclaje", "La Luna cambia de apariencia y el agua circula mientras reducimos y reutilizamos residuos.", [
            ("¿Qué es una fase lunar?", "la apariencia visible de la Luna", "un tipo de roca", "un viento"),
            ("¿Qué ocurre en la evaporación?", "el agua pasa a vapor", "el hielo se vuelve piedra", "el vapor se vuelve arena"),
            ("¿Qué hacemos al reutilizar?", "usamos algo de nuevo", "lo tiramos inmediatamente", "lo quemamos"),
            ("¿Dónde cae el agua después de condensarse?", "como gotas", "como fuego", "como metal"),
            ("¿Qué residuo puede reciclarse?", "una botella limpia", "comida líquida en el suelo", "un charco"),
        ]),
        3: ("Sistema solar y volcanes", "La Tierra forma parte del sistema solar y su superficie cambia por procesos como el vulcanismo.", [
            ("¿Alrededor de qué gira la Tierra?", "del Sol", "de una nube", "de una montaña"),
            ("¿Qué es la Luna?", "un satélite natural", "una estrella", "un continente"),
            ("¿Qué expulsa un volcán en erupción?", "lava y gases", "hielo siempre", "hojas"),
            ("¿Qué capa es donde vivimos?", "la corteza", "el núcleo solar", "la atmósfera de Marte"),
            ("¿Qué instrumento ayuda a observar el cielo?", "un telescopio", "un colador", "una balanza"),
        ]),
        4: ("Relieve, ríos y riesgos", "El relieve y el agua forman paisajes; conocer los riesgos ayuda a prevenir y actuar.", [
            ("¿Qué es una montaña?", "una elevación del terreno", "una corriente de agua", "un planeta"),
            ("¿Dónde desemboca un río?", "en otro cuerpo de agua", "en una estrella", "en una nube seca"),
            ("¿Qué puede causar una inundación?", "lluvias intensas y desborde", "una noche despejada", "una sombra"),
            ("¿Qué muestra un mapa físico?", "relieve y accidentes naturales", "solo nombres de personas", "recetas"),
            ("¿Qué ayuda a prevenir riesgos?", "un plan de emergencia", "ignorar alertas", "acercarse al peligro"),
        ]),
        5: ("Universo y cambio climático", "El universo es enorme y las actividades humanas pueden alterar el clima de la Tierra.", [
            ("¿Qué es una galaxia?", "un conjunto de estrellas", "una sola gota", "una montaña"),
            ("¿Qué planeta habitamos?", "la Tierra", "Júpiter", "Venus"),
            ("¿Qué aumenta el efecto invernadero?", "gases emitidos por actividades humanas", "plantar árboles", "ahorrar energía"),
            ("¿Qué puede reducir emisiones?", "usar energías renovables", "quemar más carbón", "desperdiciar combustible"),
            ("¿Qué estudia la climatología?", "los climas y sus cambios", "la escritura", "los precios"),
        ]),
    },
    "science-technology": {
        1: ("Herramientas y seguridad", "Las herramientas resuelven tareas y deben usarse con cuidado y acompañamiento adulto.", [
            ("¿Para qué sirve una tijera?", "cortar", "medir la lluvia", "cocinar sola"),
            ("¿Qué hacemos antes de cruzar?", "mirar a ambos lados", "correr sin mirar", "cerrar los ojos"),
            ("¿Qué herramienta mide el tiempo?", "un reloj", "un martillo", "una cuchara"),
            ("¿Qué objeto protege la cabeza?", "un casco", "un lápiz", "una taza"),
            ("¿Qué debemos hacer con un enchufe?", "usarlo con seguridad y ayuda adulta", "tocarlo con manos mojadas", "introducir objetos"),
        ]),
        2: ("Inventos y diseño", "Las personas crean objetos para satisfacer necesidades y pueden reutilizar materiales.", [
            ("¿Qué resuelve un paraguas?", "proteger de la lluvia", "medir la altura", "enfriar la comida"),
            ("¿Qué material puede reutilizarse en un diseño?", "una caja de cartón", "basura mezclada", "agua sucia"),
            ("¿Qué paso va primero al diseñar?", "identificar una necesidad", "romper el prototipo", "ocultar el problema"),
            ("¿Qué invento permite comunicarnos a distancia?", "el teléfono", "una regla", "un vaso"),
            ("¿Qué mejora un prototipo?", "probarlo y corregirlo", "no observarlo", "copiar sin pensar"),
        ]),
        3: ("Máquinas y soluciones", "Las máquinas combinan piezas y las soluciones tecnológicas deben responder a un problema real.", [
            ("¿Qué máquina ayuda a levantar una carga?", "una polea", "un cuaderno", "una nube"),
            ("¿Qué es un algoritmo?", "pasos ordenados para resolver algo", "un material", "una emoción"),
            ("¿Qué debe tener una solución?", "una función y un propósito", "solo colores", "ninguna prueba"),
            ("¿Qué usa un robot para detectar luz?", "un sensor", "un lápiz", "una cuerda"),
            ("¿Qué se hace después de construir?", "evaluar y mejorar", "dejar de observar", "borrar el problema"),
        ]),
        4: ("Robótica y biomimética", "La robótica combina sensores y programación; la biomimética aprende de la naturaleza.", [
            ("¿Qué hace un sensor?", "detecta una condición", "escribe historias solo", "produce una montaña"),
            ("¿Qué estudia la biomimética?", "soluciones inspiradas en seres vivos", "los precios", "las fases lunares solamente"),
            ("¿Qué controla el comportamiento de un robot?", "un programa", "una piedra", "la lluvia"),
            ("¿Qué animal inspira superficies que nadan bien?", "un pez", "una roca", "un cactus seco"),
            ("¿Qué criterio es importante en una tecnología?", "seguridad y utilidad", "peligro innecesario", "desperdicio"),
        ]),
        5: ("Tecnología responsable", "La tecnología debe diseñarse con ética, privacidad, inclusión y cuidado del ambiente.", [
            ("¿Qué protege la privacidad?", "cuidar los datos personales", "publicar contraseñas", "compartir toda la información"),
            ("¿Qué significa que una tecnología sea inclusiva?", "que pueda usarla más gente", "que excluya usuarios", "que no tenga instrucciones"),
            ("¿Qué es un dato?", "información que puede analizarse", "una emoción sin registro", "un material aislante"),
            ("¿Qué acción reduce residuos electrónicos?", "reparar y reciclar dispositivos", "tirarlos al río", "cambiarlos cada día"),
            ("¿Qué debe considerar una decisión tecnológica?", "sus consecuencias", "solo su apariencia", "ninguna evidencia"),
        ]),
    },
    "science-health": {
        1: ("Mi cuerpo sano y fuerte", "Conoce hábitos simples de higiene, alimentación y descanso para cuidar tu salud.", [
            ("¿Qué debemos hacer al despertar?", "lavarnos la cara", "no comer nunca", "gritar fuerte"),
            ("¿Cuál es un alimento saludable?", "las verduras", "solo caramelos", "el refresco siempre"),
            ("¿Cómo cuidamos los dientes?", "cepillándolos", "sin limpiarlos", "comiendo piedras"),
            ("¿Qué ayuda a crecer sano?", "dormir bien", "no jugar nunca", "ver pantallas toda la noche"),
            ("¿Qué hacemos para evitar gérmenes?", "lavarnos las manos", "tocar la basura", "no lavarnos"),
        ]),
        2: ("Alimentos y energía", "Los alimentos nos dan energía y elegir bien ayuda a crecer, aprender y jugar.", [
            ("¿Qué nos dan los alimentos?", "energía y nutrientes", "solo sombra", "ruido"),
            ("¿Cuál es una proteína saludable?", "el huevo", "un dulce", "una piedra"),
            ("¿Qué bebida es mejor a diario?", "el agua", "la soda", "el aceite"),
            ("¿Qué alimento da mucha energía?", "arroz o pan", "aire", "una moneda"),
            ("¿Cómo elegimos alimentos?", "variados y equilibrados", "siempre dulces", "solo fritos"),
        ]),
        3: ("Enfermedades, vacunas y prevención", "Los microorganismos pueden causar enfermedad; la higiene y las vacunas nos protegen.", [
            ("¿Qué causa muchas enfermedades?", "gérmenes", "el juego", "la lectura"),
            ("¿Qué ayuda a prevenir enfermedades?", "vacunarse", "no lavarse", "comer basura"),
            ("¿Qué debemos hacer al toser?", "cubrir la boca", "soplar a otros", "gritar"),
            ("¿Qué es un antibiótico?", "un medicamento para infecciones bacterianas", "un dulce", "una fruta"),
            ("¿Por qué descansar al estar enfermo?", "recuperarse mejor", "por diversión", "para contagiar"),
        ]),
        4: ("Salud mental y emociones", "Las emociones y la convivencia también son parte de la salud y se cuidan con apoyo.", [
            ("¿Qué ayuda a sentir calma?", "hablar de lo que sentimos", "ignorar todo", "enojarse siempre"),
            ("¿Qué actividad alivia el estrés?", "ejercicio suave", "no dormir", "peleas"),
            ("¿A quién puedes pedir ayuda?", "a un adulto de confianza", "a nadie", "a una piedra"),
            ("¿Qué es un amigo de apoyo?", "alguien que escucha", "alguien que insulta", "un aparato"),
            ("¿Qué hábito favorece el sueño?", "horarios regulares", "pantallas sin límite", "café antes de dormir"),
        ]),
        5: ("Salud pública y bienestar", "Las decisiones colectivas, la higiene y el ambiente afectan la salud de la comunidad.", [
            ("¿Qué mejoró la salud pública?", "vacunación y sanidad", "contaminación", "desnutrición masiva"),
            ("¿Qué es una enfermedad contagiosa?", "una que se transmite entre personas", "una por herencia solo", "un invento"),
            ("¿Qué reduce el tabaquismo?", "campañas y regulaciones", "ignorar daños", "más propaganda"),
            ("¿Qué factor social influye en la salud?", "acceso a educación y agua", "el color de ropa", "la moda"),
            ("¿Qué acción protege a otros?", "aislarse al estar enfermo", "ocultar síntomas", "saludar muy cerca"),
        ]),
    },
    "science-living": {
        1: ("Plantas y animales cercanos", "Observa plantas y animales cercanos y reconoce lo que necesitan para vivir.", [
            ("¿Qué necesita una planta?", "agua y luz", "una televisión", "un lápiz"),
            ("¿Cuál es un ser vivo?", "un perro", "una piedra", "una silla"),
            ("¿Qué animal dice miau?", "el gato", "el pez", "la vaca"),
            ("¿Dónde vive un pez?", "en el agua", "en una nube", "en un libro"),
            ("¿Qué hábito cuida a los animales?", "darles agua y comida", "asustarlos", "tirar basura"),
        ]),
        2: ("Clasificamos seres vivos", "Los seres vivos se clasifican por rasgos y cumplen funciones en su hábitat.", [
            ("¿Qué es un mamífero?", "un animal que tiene pelo y amamanta a sus crías", "un pez", "una roca"),
            ("¿Cuál es un ser vivo acuático?", "el delfín", "una silla", "un vaso"),
            ("¿Qué necesitan los animales?", "alimento y refugio", "solo ruido", "una moneda"),
            ("¿Qué es un insecto?", "un animal con seis patas", "un árbol", "un planeta"),
            ("¿Dónde viven los árboles?", "en la tierra", "en el mar siempre", "en una nube"),
        ]),
        3: ("Adaptaciones y cadenas", "Las adaptaciones ayudan a sobrevivir y los seres vivos se relacionan en cadenas alimentarias.", [
            ("¿Qué adaptación tiene el camello?", "giba para guardar grasa", "alas para volar", "branquias"),
            ("En pasto → conejo → zorro, ¿qué es el conejo?", "consumidor", "productor", "planeta"),
            ("¿Qué parte de la planta produce alimento?", "la hoja", "la raíz", "la semilla"),
            ("¿Qué sucede si desaparece un eslabón?", "se desequilibra la cadena", "nada cambia", "crece más alimento"),
            ("¿Qué organismo produce su propio alimento?", "una planta", "un león", "un hongo de pan"),
        ]),
        4: ("Ecosistemas y biodiversidad", "Un ecosistema reúne seres vivos y su ambiente; la biodiversidad lo hace estable.", [
            ("¿Qué es la biodiversidad?", "variedad de seres vivos", "una sola especie", "un mineral"),
            ("¿Qué factor no vivo hay en un ecosistema?", "la luz", "un conejo", "un árbol"),
            ("¿Qué acción protege la biodiversidad?", "proteger hábitats", "destruir nidos", "contaminar ríos"),
            ("¿Qué es una población?", "individuos de la misma especie", "todos los planetas", "una célula"),
            ("¿Qué produce la pérdida de biodiversidad?", "desequilibrios", "más hábitats", "agua más limpia siempre"),
        ]),
        5: ("Conservación y servicio ecosistémico", "Los seres vivos prestan servicios esenciales y requieren acciones de conservación responsables.", [
            ("¿Qué es un servicio ecosistémico?", "un beneficio que brinda la naturaleza", "un producto comercial", "un impuesto"),
            ("¿Qué ayuda a conservar bosques?", "reforestación", "talar sin control", "quemas"),
            ("¿Qué son especies invasoras?", "especies que alteran un ecosistema", "especies nativas", "animales domésticos"),
            ("¿Qué mide la huella ecológica?", "impacto humano sobre la Tierra", "el tamaño de un animal", "la velocidad del viento"),
            ("¿Qué promueve la conservación?", "proteger y restaurar", "explotar sin límite", "ignorar las especies"),
        ]),
    },
}


SOCIAL = {
    "social-identity": {
        1: ("Mi familia, escuela y reglas", "Las personas forman grupos diversos y las reglas ayudan a convivir con respeto.", [
            ("¿Qué es una familia?", "personas que se cuidan y acompañan", "solo una casa", "un mapa"),
            ("¿Para qué sirven las reglas?", "para convivir mejor", "para lastimar", "para excluir siempre"),
            ("¿Qué emoción aparece al recibir ayuda?", "alegría", "un continente", "una moneda"),
            ("¿Qué espacio usamos para aprender?", "la escuela", "el supermercado solamente", "un volcán"),
            ("¿Qué muestra respeto?", "escuchar a otros", "interrumpir siempre", "burlarse"),
        ]),
        2: ("Comunidad y diversidad", "Una comunidad reúne personas con roles y costumbres diferentes; todas merecen respeto.", [
            ("¿Qué es una comunidad?", "personas que comparten un lugar o intereses", "un objeto", "un solo edificio"),
            ("¿Qué hace un bombero?", "ayuda en emergencias", "vende frutas siempre", "enseña matemáticas en casa"),
            ("¿Qué significa diversidad?", "variedad de personas y formas de vivir", "que todos sean idénticos", "estar solos"),
            ("¿Qué derecho tienen los niños?", "recibir educación", "trabajar sin descanso", "no ser escuchados"),
            ("¿Cómo participamos?", "colaborando y dando ideas", "ignorando a todos", "rompiendo acuerdos"),
        ]),
        3: ("Derechos y democracia escolar", "Los derechos se acompañan de responsabilidades y la democracia permite participar en decisiones.", [
            ("¿Qué es un derecho?", "una protección que corresponde a las personas", "un premio secreto", "una deuda"),
            ("¿Qué hace una votación?", "recoge preferencias para decidir", "borra opiniones", "mide la lluvia"),
            ("¿Qué es una responsabilidad?", "cumplir un compromiso", "quitar derechos", "ignorar acuerdos"),
            ("¿Qué actitud ayuda al diálogo?", "escuchar razones", "gritar más fuerte", "no dejar hablar"),
            ("¿Qué institución protege derechos?", "la escuela y sus autoridades", "un juguete", "una montaña"),
        ]),
        4: ("Ciudadanía e inclusión", "La ciudadanía implica derechos, deberes e inclusión de personas con distintas capacidades y culturas.", [
            ("¿Qué significa incluir?", "permitir participación con apoyos", "dejar fuera", "tratar peor"),
            ("¿Qué documento organiza derechos y deberes de un país?", "la Constitución", "un horario", "un cuento"),
            ("¿Qué es discriminar?", "tratar injustamente por una diferencia", "ayudar con respeto", "escuchar"),
            ("¿Qué acción es ciudadana?", "cuidar los espacios públicos", "dañarlos", "evitar toda responsabilidad"),
            ("¿Cómo resolvemos un conflicto?", "dialogando y buscando acuerdos", "con violencia", "ocultándolo"),
        ]),
        5: ("Ciudadanía global y derechos humanos", "Las personas comparten derechos humanos y enfrentan retos globales que requieren cooperación.", [
            ("¿Qué son los derechos humanos?", "derechos de todas las personas", "privilegios de un grupo", "premios escolares"),
            ("¿Qué promueve la ONU?", "cooperación entre países", "aislamiento", "competencia sin reglas"),
            ("¿Qué es ciudadanía global?", "responsabilidad con el mundo común", "vivir sin comunidad", "ignorar otros países"),
            ("¿Qué ayuda a combatir un prejuicio?", "informarse y escuchar", "repetir estereotipos", "excluir"),
            ("¿Qué valor sostiene los derechos?", "dignidad", "desprecio", "indiferencia"),
        ]),
    },
    "social-geography": {
        1: ("Mi casa, escuela y barrio", "Los lugares cercanos pueden representarse con dibujos, recorridos y puntos de referencia.", [
            ("¿Qué es un mapa?", "un dibujo que representa un lugar", "una receta", "un juguete"),
            ("¿Qué usamos para orientarnos?", "puntos de referencia", "solo los ojos cerrados", "un plato"),
            ("¿Qué lugar pertenece al barrio?", "el parque", "la Luna", "el océano siempre"),
            ("¿Qué muestra un recorrido?", "por dónde vamos", "qué comemos", "la edad de alguien"),
            ("¿Qué cuidamos en el barrio?", "las calles y parques", "la basura en el suelo", "las señales"),
        ]),
        2: ("Municipio, mapas y clima", "El municipio organiza servicios y los mapas usan símbolos para representar lugares y fenómenos.", [
            ("¿Qué es un municipio?", "una comunidad con una organización local", "un planeta", "un animal"),
            ("¿Para qué sirve una leyenda?", "explica símbolos del mapa", "cuenta una historia de ficción", "mide la temperatura"),
            ("¿Qué describe el clima?", "condiciones habituales de la atmósfera", "el precio de un producto", "una familia"),
            ("¿Qué servicio presta una biblioteca?", "ofrece libros y lectura", "repara carreteras siempre", "produce lluvia"),
            ("¿Qué representa un símbolo?", "un lugar o elemento acordado", "una comida", "un sonido sin significado"),
        ]),
        3: ("Región y recursos", "Las regiones tienen paisajes, recursos y actividades que influyen en la vida de sus habitantes.", [
            ("¿Qué es una región?", "un espacio con características comunes", "una sola calle", "un objeto"),
            ("¿Qué es un recurso natural?", "algo de la naturaleza que usamos", "un edificio", "una regla"),
            ("¿Qué paisaje tiene mucha agua?", "la costa", "el desierto sin oasis", "una oficina"),
            ("¿Qué actividad usa el suelo para cultivar?", "agricultura", "astronomía", "programación solamente"),
            ("¿Qué hacemos para conservar recursos?", "usarlos responsablemente", "desperdiciarlos", "contaminarlos"),
        ]),
        4: ("País, relieve y regiones", "Los mapas políticos y físicos muestran cómo se organiza un país y cómo es su relieve.", [
            ("¿Qué muestra un mapa político?", "fronteras y divisiones administrativas", "solo montañas", "el menú"),
            ("¿Qué es el relieve?", "formas de la superficie terrestre", "una ley", "una profesión"),
            ("¿Qué línea puede separar países?", "una frontera", "un río de tinta sin mapa", "un paralelo escolar"),
            ("¿Qué factor influye en el clima?", "la altitud", "el color de una casa", "el nombre de una calle"),
            ("¿Qué representa la escala?", "relación entre mapa y realidad", "una opinión", "una temperatura"),
        ]),
        5: ("Continentes, globalización y geopolítica", "Los territorios se relacionan mediante intercambios, comunicaciones y decisiones políticas.", [
            ("¿Qué es un continente?", "una gran extensión de tierra", "un barrio", "un río pequeño"),
            ("¿Qué facilita la globalización?", "intercambios y comunicaciones", "el aislamiento total", "la desaparición de mapas"),
            ("¿Qué estudia la geopolítica?", "relaciones de poder y territorio", "las plantas", "la ortografía"),
            ("¿Qué línea divide hemisferios norte y sur?", "el ecuador", "el meridiano de Greenwich", "una frontera local"),
            ("¿Qué actitud favorece la cooperación internacional?", "respetar acuerdos", "romperlos siempre", "desinformar"),
        ]),
    },
    "social-history": {
        1: ("Ayer, hoy y mi historia", "El tiempo permite ordenar experiencias y reconocer cambios entre ayer y hoy.", [
            ("¿Qué significa ayer?", "el día anterior", "mañana", "ahora mismo"),
            ("¿Qué usamos para ordenar hechos?", "una línea del tiempo", "un mapa de colores", "una balanza"),
            ("¿Qué cambia con el tiempo?", "las personas y los lugares", "nada nunca", "solo el cielo"),
            ("¿Qué fuente cuenta una experiencia?", "una fotografía", "una piedra sin contexto", "un número solo"),
            ("¿Qué ocurrió primero en una rutina?", "el inicio", "el final", "el recuerdo futuro"),
        ]),
        2: ("Historia local y generaciones", "Las historias familiares y locales se conocen mediante recuerdos, objetos y testimonios.", [
            ("¿Qué es una generación?", "personas de edades cercanas en una época", "un lugar", "una moneda"),
            ("¿Qué fuente es oral?", "una entrevista", "un mapa físico", "una estatua sin explicación"),
            ("¿Qué conserva un museo?", "objetos y memoria", "solo alimentos", "el clima"),
            ("¿Qué pregunta sirve en una entrevista?", "¿Cómo era la escuela antes?", "¿Qué color es el silencio?", "¿Cuánto pesa un recuerdo?"),
            ("¿Qué muestra una fecha?", "cuándo ocurrió algo", "dónde está un río", "el precio actual siempre"),
        ]),
        3: ("Fuentes y línea del tiempo", "Comparar fuentes ayuda a construir una explicación de la historia de una comunidad.", [
            ("¿Qué es una fuente histórica?", "una evidencia del pasado", "una predicción", "un juguete nuevo"),
            ("¿Qué orden es cronológico?", "antes, durante y después", "después, antes y ayer", "sin fechas"),
            ("¿Qué fuente escrita puede informar?", "una carta", "un eco", "una sombra"),
            ("¿Por qué comparar fuentes?", "para reconocer coincidencias y diferencias", "para borrar datos", "para inventar hechos"),
            ("¿Qué hace un historiador?", "investiga el pasado con evidencias", "adivina sin fuentes", "mide volcanes solamente"),
        ]),
        4: ("Historia nacional", "Las sociedades cambian por decisiones, conflictos, intercambios y acciones de muchas personas.", [
            ("¿Qué estudia la historia nacional?", "procesos del país", "solo el clima", "una receta"),
            ("¿Qué es un proceso histórico?", "un conjunto de cambios relacionados", "un instante aislado siempre", "un mapa sin fecha"),
            ("¿Qué fuente puede mostrar una ley antigua?", "un documento", "un árbol sin registro", "una nube"),
            ("¿Por qué hay distintas perspectivas?", "las personas viven y recuerdan de forma diferente", "porque no existen hechos", "porque las fechas no importan"),
            ("¿Qué ayuda a interpretar una fuente?", "su contexto", "separarla de todo contexto", "cambiar sus palabras"),
        ]),
        5: ("Historia mundial", "Las civilizaciones, revoluciones y movimientos se relacionan y ayudan a comprender el mundo actual.", [
            ("¿Qué es una civilización?", "una sociedad con formas organizadas de vida", "una sola persona", "un fenómeno del clima"),
            ("¿Qué puede causar una revolución?", "cambios profundos en una sociedad", "un cambio de estación solamente", "una suma"),
            ("¿Qué conecta procesos históricos?", "causas y consecuencias", "colores sin significado", "datos inventados"),
            ("¿Qué debe hacer una explicación histórica?", "usar evidencias y contexto", "repetir rumores", "ocultar fechas"),
            ("¿Qué aprendemos al estudiar el pasado?", "comprender cambios y decisiones", "que nada influye", "que no existen perspectivas"),
        ]),
    },
    "social-economy": {
        1: ("Necesidades, deseos y ahorro", "Diferenciar lo necesario de lo que deseamos ayuda a tomar decisiones responsables.", [
            ("¿Qué es una necesidad?", "algo básico para vivir", "un lujo siempre", "un juguete solamente"),
            ("¿Qué es un deseo?", "algo que queremos tener", "aire para respirar", "agua para vivir"),
            ("¿Qué hace una alcancía?", "ayuda a ahorrar", "produce comida", "mide el tiempo"),
            ("¿Qué usamos para comprar?", "dinero", "una nube", "una regla"),
            ("¿Qué decisión es responsable?", "comparar antes de comprar", "gastar todo sin pensar", "desperdiciar"),
        ]),
        2: ("Bienes, servicios y mercado", "Las personas producen bienes y ofrecen servicios para satisfacer necesidades de la comunidad.", [
            ("¿Qué es un bien?", "un objeto que puede satisfacer una necesidad", "una actividad sin producto", "una emoción"),
            ("¿Qué es un servicio?", "una actividad que ayuda a alguien", "un mineral", "una montaña"),
            ("¿Quién vende productos?", "un comerciante", "un mapa", "una nube"),
            ("¿Qué hacemos en un mercado?", "intercambiamos bienes y servicios", "observamos planetas", "medimos el clima"),
            ("¿Qué es publicidad?", "un mensaje que intenta informar o convencer", "una ley natural", "un tipo de mapa"),
        ]),
        3: ("Trabajo, sectores e impuestos", "El trabajo organiza la producción y los impuestos ayudan a financiar servicios públicos.", [
            ("¿Qué es un sector económico?", "un grupo de actividades productivas", "un barrio", "un continente"),
            ("¿Qué actividad pertenece al sector primario?", "agricultura", "banca", "transporte digital"),
            ("¿Qué produce una fábrica?", "bienes elaborados", "solo ideas", "lluvia"),
            ("¿Para qué sirven los impuestos?", "financiar servicios públicos", "comprar juguetes de una persona", "ocultar ingresos"),
            ("¿Qué derecho acompaña al trabajo?", "condiciones dignas", "ninguna protección", "trabajar sin descanso"),
        ]),
        4: ("Empresa, banco y presupuesto", "Un presupuesto organiza ingresos y gastos para decidir con responsabilidad.", [
            ("¿Qué es un ingreso?", "dinero que recibimos", "un gasto", "una deuda siempre"),
            ("¿Qué es un gasto?", "dinero que usamos", "un ingreso", "un mapa"),
            ("¿Qué hace un banco?", "ofrece servicios financieros", "cultiva plantas", "mide el viento"),
            ("¿Qué muestra un presupuesto?", "ingresos y gastos previstos", "solo deseos", "el relieve"),
            ("¿Qué ayuda a evitar deudas innecesarias?", "planificar y comparar", "comprar sin revisar", "ocultar precios"),
        ]),
        5: ("Emprendimiento, finanzas y desigualdad", "Emprender implica identificar necesidades y la educación financiera ayuda a comprender oportunidades y desigualdades.", [
            ("¿Qué es emprender?", "crear una solución o proyecto", "gastar sin plan", "copiar sin propósito"),
            ("¿Qué es el interés?", "un costo o ganancia por usar dinero", "un mapa", "un impuesto natural"),
            ("¿Qué significa desigualdad?", "distribución injusta de oportunidades o recursos", "que todos tienen lo mismo", "un cambio de clima"),
            ("¿Qué evalúa un proyecto responsable?", "impacto social y ambiental", "solo el color", "ninguna consecuencia"),
            ("¿Qué hábito financiero ayuda?", "ahorrar y registrar gastos", "gastar más de lo que hay", "ignorar ingresos"),
        ]),
    },
    "social-culture": {
        1: ("Mi familia y tradiciones", "Las familias tienen costumbres y tradiciones que nos unen y nos identifican.", [
            ("¿Qué es una tradición?", "una costumbre que se repite", "un capricho", "una multa"),
            ("¿Qué celebramos en familia?", "fechas especiales", "nada nunca", "solo tareas"),
            ("¿Qué es el patrimonio?", "lo que heredamos y cuidamos", "un juguete roto", "una multa"),
            ("¿Para qué sirven las tradiciones?", "unir y recordar", "excluir siempre", "molestar"),
            ("¿Qué muestra respeto por la cultura?", "escuchar y participar", "burlarse", "ignorar"),
        ]),
        2: ("Cultura y costumbres del lugar", "Cada comunidad tiene costumbres, música, comidas y formas de expresarse.", [
            ("¿Qué es una costumbre?", "una práctica habitual de un grupo", "un accidente", "una dieta médica"),
            ("¿Qué representa la música folclórica?", "la identidad cultural", "un ruido", "una multa"),
            ("¿Qué compartimos en una feria?", "productos y cultura", "solo basura", "secretos"),
            ("¿Qué es el patrimonio cultural?", "bienes y saberes de una comunidad", "solo dinero", "un objeto roto"),
            ("¿Cómo cuidamos la cultura?", "conociéndola y respetándola", "destruyéndola", "olvidándola"),
        ]),
        3: ("Diversidad cultural y respeto", "Existen muchas culturas y todas merecen respeto, cuidado y diálogo.", [
            ("¿Qué es la diversidad cultural?", "variedad de formas de vivir y expresarse", "que todos sean iguales", "un solo idioma"),
            ("¿Qué es discriminar?", "tratar injustamente por una diferencia", "ayudar con respeto", "escuchar"),
            ("¿Qué promueve la inclusión?", "participación de todos", "dejar fuera", "burlarse"),
            ("¿Por qué conocer otras culturas?", "para entender y respetar", "para burlarse", "para evitar viajar"),
            ("¿Qué actitud es adecuada?", "respetar tradiciones ajenas", "mockearlas", "ignorarlas"),
        ]),
        4: ("Patrimonio histórico y cultural", "El patrimonio incluye monumentos, paisajes y saberes que se transmiten entre generaciones.", [
            ("¿Qué es un patrimonio material?", "construcciones y objetos valiosos", "ideas sin registro", "un clima"),
            ("¿Qué protege un museo?", "bienes culturales", "solo alimentos", "el tiempo"),
            ("¿Por qué restaurar un monumento?", "conservar memoria e identidad", "destruirlo", "venderlo"),
            ("¿Qué es patrimonio inmaterial?", "saberes, músicas y tradiciones", "un edificio", "una roca"),
            ("¿Quién cuida el patrimonio?", "la comunidad y el Estado", "nadie", "solo turistas"),
        ]),
        5: ("Identidad global y multiculturalidad", "Las personas combinan identidades locales y globales en un mundo multicultural.", [
            ("¿Qué es ser multicultural?", "vivir y valorar varias culturas", "rechazar otras", "aislarse"),
            ("¿Qué promueve la diversidad?", "enriquecer la convivencia", "uniformidad forzada", "exclusión"),
            ("¿Qué es un estereotipo?", "una idea fija y simplificada", "un hecho verificado", "un derecho"),
            ("¿Cómo combatir prejuicios?", "informarse y escuchar", "repetir estereotipos", "excluir"),
            ("¿Qué valor sostiene la diversidad?", "respeto a la dignidad", "desprecio", "indiferencia"),
        ]),
    },
    "social-media": {
        1: ("Medios que usamos", "Los medios nos informan y comunican; debemos usarlos con ayuda y seguridad.", [
            ("¿Qué es un medio de comunicación?", "algo que transmite información", "un juguete", "una piedra"),
            ("¿Qué medio usamos para ver noticias?", "televisión o internet", "un lápiz", "una regla"),
            ("¿Qué debemos hacer con anuncios?", "verlos con ayuda adulta", "creer todo", "comprar siempre"),
            ("¿Quién cuida la privacidad?", "nosotros y nuestras familias", "nadie", "los extraños"),
            ("¿Qué es una noticia?", "información sobre un hecho", "un invento", "un juego"),
        ]),
        2: ("Información y fuentes", "La información puede venir de fuentes diversas y debe verificarse.", [
            ("¿Qué es una fuente confiable?", "una que muestra evidencias", "un rumor", "un título vago"),
            ("¿Por qué verificar?", "para evitar desinformación", "por aburrimiento", "para confundir"),
            ("¿Qué es una noticia falsa?", "información inventada", "un hecho verificado", "una opinión"),
            ("¿Quién ayuda a evaluar información?", "profesores y familia", "solo extraños", "nadie"),
            ("¿Qué hacemos ante información dudosa?", "consultar más fuentes", "compartirla rápido", "ignorar siempre"),
        ]),
        3: ("Privacidad y convivencia digital", "En internet compartimos datos y debemos proteger nuestra privacidad y a otros.", [
            ("¿Qué es un dato personal?", "información que identifica a alguien", "un color", "una opinión"),
            ("¿Qué no debemos publicar?", "dirección y teléfono", "saludos", "ideas"),
            ("¿Qué es el ciberacoso?", "hostigamiento por medios digitales", "un juego", "una amistad"),
            ("¿Qué hacemos ante mensajes ofensivos?", "bloquear y reportar", "responder igual", "compartirlos"),
            ("¿Cómo cuidamos la convivencia?", "respetando a otros", "insultando", "excluyendo"),
        ]),
        4: ("Medios y democracia", "Los medios permiten informarse y participar, y requieren responsabilidad y pensamiento crítico.", [
            ("¿Qué es el pensamiento crítico?", "analizar y evaluar información", "creer todo", "ignorar todo"),
            ("¿Qué derecho protege a la prensa?", "la libertad de expresión", "el silencio forzado", "la censura"),
            ("¿Qué es un editorial?", "una opinión de un medio", "una noticia verificada", "un anuncio"),
            ("¿Qué hace la publicidad?", "intentar convencer al consumidor", "informar solo hechos", "enseñar ciencia"),
            ("¿Qué relación existe entre medios y democracia?", "informan para decidir mejor", "censuran siempre", "no influyen"),
        ]),
        5: ("Ética digital y ciudadanía", "La ciudadanía digital exige respeto, privacidad, verificación y participación responsable.", [
            ("¿Qué es la huella digital?", "rastro que dejamos en internet", "una pisada", "un documento"),
            ("¿Qué propiedad debemos respetar en internet?", "derechos de autor", "copiar todo", "plagiar"),
            ("¿Qué es la desinformación?", "información falsa difundida", "un estudio", "un dato verificado"),
            ("¿Qué promueve una buena convivencia digital?", "respeto y empatía", "insultos", "amenazas"),
            ("¿Qué derecho incluye el acceso a internet?", "informarse y expresarse", "censurar", "excluir"),
        ]),
    },
}


ENGLISH = {
    "english-identity": {
        1: ("Hello! This is me", "Usa saludos, colores, números y frases muy breves para presentarte.", [
            ("How do you say hola?", "Hello", "Goodbye", "Thanks"),
            ("Complete: My name ___ Ana.", "is", "are", "am"),
            ("What color is the sun?", "yellow", "purple", "black"),
            ("How old are you?", "I am six", "I am blue", "I am a book"),
            ("Which number is three?", "three", "ten", "one"),
        ]),
        2: ("My family and home", "Nombra personas, espacios y objetos de tu familia y tu casa.", [
            ("My mother's child is my…", "brother or sister", "teacher", "street"),
            ("Complete: This is my ___.", "house", "run", "blue"),
            ("Where do you sleep?", "In the bedroom", "In the kitchen floor", "At the school bus"),
            ("What is the opposite of big?", "small", "happy", "old"),
            ("Choose the family word.", "grandma", "window", "pencil"),
        ]),
        3: ("Routines and hobbies", "Describe rutinas, horas, gustos y actividades con frases sencillas.", [
            ("Complete: I ___ breakfast in the morning.", "eat", "eats", "eating"),
            ("Which is a hobby?", "playing football", "Monday", "kitchen"),
            ("What time comes after seven?", "eight o'clock", "three o'clock", "one o'clock"),
            ("Complete: She ___ books.", "reads", "read are", "reading is"),
            ("How do you express a preference?", "I like music", "I am table", "Blue is run"),
        ]),
        4: ("Opinions and health", "Expresa preferencias, comparaciones y hábitos saludables.", [
            ("Complete: I think it is ___.", "interesting", "yesterday", "walked"),
            ("Which is healthier?", "eating fruit", "never sleeping", "drinking only soda"),
            ("Comparative of small.", "smaller", "smallestly", "more smalling"),
            ("Complete: You should ___ water.", "drink", "drinks", "drinking"),
            ("How do you give an opinion?", "I believe it is useful", "I yesterday pencil", "Run is house"),
        ]),
        5: ("Environment and media", "Habla de acciones ambientales, noticias y profesiones usando ideas conectadas.", [
            ("Complete: We should ___ the planet.", "protect", "protected yesterday", "protects it are"),
            ("Which action is sustainable?", "reusing materials", "wasting water", "burning all trash"),
            ("What is a news source?", "a newspaper", "a spoon", "a shoe"),
            ("Complete: If we recycle, we ___ waste.", "reduce", "reduced yesterday", "reducing are"),
            ("Which is a job?", "scientist", "green", "quickly"),
        ]),
    },
    "english-community": {
        1: ("My school and colors", "Nombra lugares y objetos de la escuela con colores y expresiones básicas.", [
            ("Where do you learn?", "school", "hospital", "airport"),
            ("What color is grass?", "green", "pink", "black"),
            ("Complete: This is a ___.", "book", "run", "seven"),
            ("Who teaches a class?", "teacher", "pilot", "farmer"),
            ("Choose a classroom object.", "pencil", "banana", "cloud"),
        ]),
        2: ("Town and routines", "Describe lugares de la ciudad y acciones de la rutina diaria.", [
            ("Where can you borrow books?", "library", "kitchen", "garden shoe"),
            ("Complete: I go to school ___ Monday.", "on", "in a", "at the"),
            ("Who helps sick people?", "doctor", "artist", "driver only"),
            ("What is a place in town?", "park", "purple", "jump"),
            ("Complete: We ___ lunch at noon.", "have", "has", "having is"),
        ]),
        3: ("Hobbies and places", "Combina lugares, deportes y rutinas para describir tu comunidad.", [
            ("Where do you swim?", "at the pool", "in the library", "on the pencil"),
            ("Which is a sport?", "cycling", "Tuesday", "hospital"),
            ("Complete: They ___ basketball on Fridays.", "play", "plays", "playing is"),
            ("What is near a town?", "a museum", "a verb", "a color only"),
            ("Which sentence is correct?", "I visit the park.", "I park visits.", "Visit I the."),
        ]),
        4: ("Health and community", "Explica hábitos de salud y situaciones habituales en espacios públicos.", [
            ("What should you do when sick?", "see a doctor", "ignore every symptom", "never drink water"),
            ("Complete: You must ___ your hands.", "wash", "washes", "washing are"),
            ("Which place helps emergencies?", "hospital", "cinema only", "bedroom"),
            ("Complete: The pharmacy is ___ the bank.", "next to", "yesterday", "quickly"),
            ("Which sentence gives advice?", "You should rest.", "You rested blue.", "Rest is yesterday."),
        ]),
        5: ("News and global community", "Comprende información sencilla sobre comunidades, medios y responsabilidades compartidas.", [
            ("What is a reliable source?", "information with evidence", "a random rumor", "an invented title"),
            ("Complete: People ___ different languages.", "speak", "speaks are", "speaking yesterday"),
            ("Which action helps a community?", "volunteering", "spreading false news", "excluding neighbors"),
            ("What does global mean?", "related to the world", "inside one room", "only yesterday"),
            ("Which sentence is respectful?", "Different cultures are valuable.", "Only my culture matters.", "People must all be equal in every way."),
        ]),
    },
    "english-world": {
        1: ("Animals and actions", "Reconoce animales y acciones mediante frases y movimiento.", [
            ("Which animal says meow?", "cat", "fish", "bird"),
            ("Complete: A bird can ___.", "fly", "swim in a book", "is red"),
            ("Which animal lives in water?", "fish", "lion", "cow"),
            ("What action is jump?", "saltar", "dormir", "comer"),
            ("Choose an animal.", "elephant", "yellow", "run"),
        ]),
        2: ("Stories and animals", "Comprende personajes, lugares y acciones en cuentos breves.", [
            ("Who is a story character?", "the girl", "the blue", "quickly"),
            ("Where can a bear live?", "in a forest", "in a pencil", "at a number"),
            ("Complete: The boy ___ the door.", "opens", "open are", "opening yesterday"),
            ("What is a beginning?", "the first part", "the last page", "a color"),
            ("Which word shows sequence?", "then", "purple", "animal"),
        ]),
        3: ("Adventures and descriptions", "Describe characters, places y acciones en aventuras sencillas.", [
            ("Which adjective describes size?", "tall", "run", "yesterday"),
            ("Complete: The explorer ___ a map.", "has", "have yesterday", "having are"),
            ("Where can an adventure happen?", "in a forest", "in a verb", "inside a color"),
            ("What is the past of go?", "went", "goes", "going"),
            ("Which sentence describes a character?", "She is brave.", "She yesterday.", "Brave is run."),
        ]),
        4: ("Technology and future", "Habla de tecnología, planes y cambios futuros con expresiones comprensibles.", [
            ("What is a device?", "a tool or machine", "a season", "a feeling only"),
            ("Complete: We will ___ a robot.", "build", "built yesterday", "building are"),
            ("Which is a future marker?", "tomorrow", "last year", "yesterday morning"),
            ("What can technology help us do?", "solve problems", "erase every responsibility", "stop learning"),
            ("Which sentence is future?", "They will travel.", "They travelled yesterday.", "They travel last week."),
        ]),
        5: ("Travel and world", "Comprende textos sencillos sobre viajes, países y problemas compartidos.", [
            ("What do you need at an airport?", "a passport", "a kitchen spoon", "a school color"),
            ("Complete: I have ___ to Peru.", "travelled", "travel tomorrow are", "travels yesterday"),
            ("Which is a place to visit?", "a museum", "a grammar", "a verb"),
            ("What does journey mean?", "a trip", "a meal", "a color"),
            ("Which action respects another country?", "learning about its culture", "mocking its people", "ignoring its rules"),
        ]),
    },
    "english-culture": {
        1: ("Songs and celebrations", "Participa en canciones y reconoce palabras sobre celebraciones y emociones.", [
            ("What do you sing?", "a song", "a chair", "a number"),
            ("Complete: Happy ___!", "birthday", "window", "run"),
            ("Which is a celebration?", "festival", "pencil", "blue"),
            ("How do you say gracias?", "Thank you", "Please sit", "Good night only"),
            ("Which feeling is happy?", "joy", "table", "seven"),
        ]),
        2: ("Food and festivals", "Nombra alimentos y expresa gustos en situaciones culturales cotidianas.", [
            ("Which is food?", "bread", "bridge", "green"),
            ("Complete: I like ___.", "apples", "running yesterday", "house are"),
            ("What do people do at a festival?", "celebrate", "sleep in class", "measure a map"),
            ("How do you ask politely?", "Can I have water, please?", "Water now yesterday.", "Give blue."),
            ("Which word means comida?", "food", "school", "friend"),
        ]),
        3: ("Stories and communication", "Cuenta una historia breve y escribe mensajes sencillos para comunicarte.", [
            ("What is a story ending?", "the final part", "the title only", "a color"),
            ("Complete: First we ___, then we played.", "arrived", "arrive are", "arriving yesterday"),
            ("What is an email?", "a digital message", "a type of fruit", "a mountain"),
            ("Which phrase starts a story?", "Once upon a time", "See you yesterday", "Blue is quickly"),
            ("What makes communication clear?", "a clear message", "missing words", "random signs"),
        ]),
        4: ("Culture and opinions", "Compara costumbres y expresa opiniones respetuosas sobre culturas y medios.", [
            ("Complete: In my opinion, it is ___.", "interesting", "yesterday", "travelled"),
            ("What is culture?", "shared ways of living and expressing", "only a color", "a single rule of math"),
            ("Which comparison is correct?", "English is different from Spanish.", "English different yesterday.", "Different is speak."),
            ("What should we do with traditions?", "learn respectfully", "mock them", "call them all the same"),
            ("Which is a medium?", "a newspaper", "a spoon", "a cloud"),
        ]),
        5: ("Global English and careers", "Usa el inglés para comunicarte, argumentar y hablar de estudios, trabajos y retos globales.", [
            ("What is a career?", "a path of work and learning", "a single meal", "a weather event"),
            ("Complete: People should ___ evidence.", "check", "checks yesterday are", "checking was"),
            ("Which phrase supports an opinion?", "because the evidence shows", "blue yesterday", "run a table"),
            ("What is a global challenge?", "climate change", "a classroom pencil", "one private hobby"),
            ("Which is respectful debate?", "I disagree because…", "You are wrong, be quiet", "I will ignore your reasons"),
        ]),
    },
    "english-food": {
        1: ("Food and health", "Talks about healthy food and simple daily habits with basic words.", [
            ("Which is a fruit?", "apple", "chair", "shoe"),
            ("Complete: I eat ___.", "an apple", "blue square", "yesterday run"),
            ("Which drink is healthy?", "water", "only soda", "oil"),
            ("How do you say gracias?", "Thank you", "Please sit", "Good night only"),
            ("Which is food?", "bread", "bridge", "green"),
        ]),
        2: ("Healthy routines", "Describes routines, meals and habits with simple sentences.", [
            ("Complete: I eat breakfast in the ___.", "morning", "table color", "fast yesterday"),
            ("Which meal is first in the day?", "breakfast", "dinner", "snack night"),
            ("How do you ask politely?", "Can I have water, please?", "Water now yesterday.", "Give blue."),
            ("Which is a healthy snack?", "fruit", "candy always", "chips only"),
            ("Complete: Wash your ___.", "hands", "blue yesterday", "running table"),
        ]),
        3: ("Food and feelings", "Talks about likes, healthy choices and daily routines.", [
            ("Complete: I like ___.", "vegetables", "running yesterday", "house are"),
            ("Which is healthier?", "eating fruit", "never sleeping", "drinking only soda"),
            ("How do you express a preference?", "I like music", "I am table", "Blue is run"),
            ("Which word means comida?", "food", "school", "friend"),
            ("Complete: You should drink ___.", "water", "soda only every day", "oil"),
        ]),
        4: ("Health advice", "Gives simple advice and compares healthy habits in English.", [
            ("Complete: You should ___ vegetables.", "eat", "eats yesterday", "eating are"),
            ("Which advice is healthy?", "Sleep enough hours", "Never rest", "Eat only candy"),
            ("How do you give an opinion?", "I believe it is useful", "I yesterday pencil", "Run is house"),
            ("Which is healthier?", "walking daily", "sitting all day", "no breakfast"),
            ("Complete: Exercise helps you stay ___.", "healthy", "yesterday", "blue table"),
        ]),
        5: ("Wellness and community", "Talks about wellness, access to healthy food and community responsibility.", [
            ("What is a healthy habit?", "regular exercise", "smoking", "no sleep"),
            ("Complete: Communities should provide ___.", "healthy food", "only junk", "nothing"),
            ("Which action promotes wellness?", "balanced diet", "skipping meals", "sedentary life"),
            ("What is a reliable source?", "information with evidence", "a random rumor", "an invented title"),
            ("Which sentence gives advice?", "You should rest.", "You rested blue.", "Rest is yesterday."),
        ]),
    },
    "english-nature": {
        1: ("Animals and nature", "Recognizes animals and nature words with simple phrases.", [
            ("Which animal says meow?", "cat", "fish", "bird"),
            ("Complete: A bird can ___.", "fly", "swim in a book", "is red"),
            ("Which animal lives in water?", "fish", "lion", "cow"),
            ("What action is jump?", "saltar", "dormir", "comer"),
            ("Choose an animal.", "elephant", "yellow", "run"),
        ]),
        2: ("Stories and animals", "Understands characters, places and actions in short stories.", [
            ("Where can a bear live?", "in a forest", "in a pencil", "at a number"),
            ("Complete: The boy ___ the door.", "opens", "open are", "opening yesterday"),
            ("What is a beginning?", "the first part", "the last page", "a color"),
            ("Which word shows sequence?", "then", "purple", "animal"),
            ("Which animal likes water?", "duck", "cat", "snake always"),
        ]),
        3: ("Nature and descriptions", "Describes animals, places and habitats in simple English.", [
            ("Which adjective describes size?", "tall", "run", "yesterday"),
            ("Where can an animal live safely?", "in a protected habitat", "in traffic", "in garbage"),
            ("What is the past of go?", "went", "goes", "going"),
            ("Which sentence describes nature?", "The forest is green.", "Yesterday blue.", "Green is run."),
            ("What do trees produce?", "oxygen", "noise", "darkness"),
        ]),
        4: ("Environment and technology", "Talks about environment, future plans and technological solutions.", [
            ("What is an ecosystem?", "living and nonliving together", "only a city", "a single object"),
            ("Complete: We will ___ a park.", "build", "built yesterday", "building are"),
            ("Which is a future marker?", "tomorrow", "last year", "yesterday morning"),
            ("What can technology help us do?", "solve problems", "erase every responsibility", "stop learning"),
            ("Which sentence is future?", "They will travel.", "They travelled yesterday.", "They travel last week."),
        ]),
        5: ("Travel and world", "Understands simple texts about travel, countries and shared problems.", [
            ("What do you need at an airport?", "a passport", "a kitchen spoon", "a school color"),
            ("Which is a place to visit?", "a museum", "a grammar", "a verb"),
            ("What does journey mean?", "a trip", "a meal", "a color"),
            ("Which action respects nature?", "protecting ecosystems", "polluting rivers", "wasting water"),
            ("Which action respects another country?", "learning about its culture", "mocking its people", "ignoring its rules"),
        ]),
    },
}


ALL_CONTENT = {**SCIENCE, **SOCIAL, **ENGLISH}


def curriculum_for_grade(unit, grade):
    """Devuelve contenido adaptado a un grado válido para las materias nuevas."""
    grade = max(1, min(5, int(grade or 3)))
    title, explanation, rows = ALL_CONTENT[unit][grade]
    lessons = [
        f"Grado {grade}.º · {title}",
        explanation,
        "Relaciona cada pregunta con un ejemplo de tu vida cotidiana y explica por qué elegiste esa respuesta.",
    ]
    return {"lesson": lessons, "questions": _rows(*rows)}
