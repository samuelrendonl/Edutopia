"""Unidades curriculares adicionales y práctica adaptada por grado."""

from decimal import Decimal


def question(prompt, correct, wrong1, wrong2, index=0):
    options = [str(correct), str(wrong1), str(wrong2)]
    offset = index % 3
    options = options[-offset:] + options[:-offset] if offset else options
    return {"prompt": prompt, "options": options, "answer": offset}


UNITS = [
    ("math-laboratory", "Matemáticas", "Laboratorio de números", "Descubre patrones y explica qué cambia en cada paso.", "patterns"),
    ("math-market", "Matemáticas", "El mercado de los números", "Cuenta, compra y reparte en situaciones cotidianas.", "market"),
    ("math-measures", "Matemáticas", "Exploradores de medidas", "Compara longitudes, tiempos, perímetros y áreas.", "measures"),
    ("language-vocabulary", "Lengua Castellana", "Un mundo de palabras", "Amplía tu vocabulario con sonidos, sinónimos y familias.", "vocabulary"),
    ("language-grammar", "Lengua Castellana", "Taller de oraciones", "Descubre cómo se organizan las palabras para expresar ideas.", "grammar"),
    ("language-adventure", "Lengua Castellana", "Crea tu propia aventura", "Reconoce las pistas, el orden y la intención de un relato.", "adventure"),
]
EXTRA_ACTIVITIES = [dict(key=key, subject=subject, title=title, description=description,
    curriculum=unit, kind="Aprendizaje", color="#5b5ce2" if subject == "Matemáticas" else "#b95079",
    icon="calculator" if subject == "Matemáticas" else "book", points=100, minutes=8,
    lesson=[], questions=[]) for key, subject, title, description, unit in UNITS]

LANGUAGE = {
"vocabulary": {
1: ("Sonidos y significados", "Pronuncia despacio: mesa comienza con m; sol comienza con s. Las palabras nombran seres, objetos y acciones.", [
("¿Qué palabra comienza con m?", "mesa", "luna", "sapo"), ("¿Qué palabra nombra un animal?", "gato", "mesa", "azul"), ("¿Qué palabra rima con gato?", "pato", "luna", "mesa"), ("¿Cuál es lo contrario de día?", "noche", "sol", "luz"), ("¿Qué usamos para leer?", "libro", "zapato", "vaso")]),
 2: ("Sinónimos y antónimos en contexto", "Los sinónimos tienen significados parecidos y los antónimos expresan ideas opuestas. Usa las pistas de la oración para elegir la palabra que comunica mejor la idea.", [
 ("Un sinónimo de feliz es…", "contento", "triste", "enojado"), ("El contrario de subir es…", "bajar", "trepar", "elevar"), ("¿Qué palabra pertenece a la familia de pan?", "panadero", "pantalla", "pantalón"), ("¿Cuál es el diminutivo de gato?", "gatito", "gatazo", "gatos"), ("El plural de flor es…", "flores", "florces", "flors"),
 ("Un sinónimo de comenzar es…", "empezar", "terminar", "romper"), ("¿Cuál es el antónimo de limpio?", "sucio", "brillante", "ordenado"), ("En «el camino es estrecho», lo contrario de estrecho es…", "ancho", "largo", "corto"), ("¿Qué palabra significa lo mismo que rápido?", "veloz", "pesado", "lento"), ("¿Cuál pareja contiene antónimos?", "frío / caliente", "bonito / hermoso", "feliz / contento")]),
 3: ("Familias léxicas y campos semánticos", "Las palabras de una familia comparten raíz y significado: flor, florero y florista. Un campo semántico reúne palabras relacionadas por un tema.", [
 ("¿Cuál pertenece a la familia de flor?", "florista", "flota", "flauta"), ("Rosa, tulipán y girasol son…", "flores", "frutas", "árboles"), ("Un sinónimo de veloz es…", "rápido", "lento", "quieto"), ("El antónimo de generoso es…", "egoísta", "solidario", "amable"), ("¿Cuál palabra no es un medio de transporte?", "almohada", "bicicleta", "tren"),
 ("¿Qué palabra comparte raíz con pan?", "panadería", "pantalón", "pantalla"), ("¿Qué indica re- en releer?", "volver a leer", "dejar de leer", "leer mal"), ("¿Cuál pareja pertenece a la misma familia?", "nación / nacional", "casa / camino", "sol / silla"), ("¿Cuál palabra pertenece al campo semántico de la escuela?", "cuaderno", "montaña", "cuchara"), ("¿Qué estrategia ayuda a comprender una palabra nueva?", "Usar su raíz y el contexto", "Ignorar la oración", "Cambiar todas sus letras")]),
 4: ("Polisemia y contexto", "Una palabra puede tener varios sentidos. El contexto permite elegir la acepción adecuada, como banco: asiento o entidad financiera.", [
 ("En «me senté en el banco», banco es…", "un asiento", "una entidad financiera", "un pez"), ("En «la copa del árbol», copa es…", "la parte con ramas y hojas", "un vaso", "un premio"), ("En «Ganó la copa del torneo», copa es…", "un trofeo", "una rama", "un recipiente"), ("En «Mueve el ratón para abrir el archivo», ratón es…", "un dispositivo", "un animal", "una herramienta"), ("Biblioteca y librería se relacionan con…", "libros", "deportes", "alimentos"),
 ("¿Qué pista ayuda a elegir un significado?", "Las palabras y la situación que lo rodean", "Solo la primera letra", "El número de sílabas"), ("En «La llave abre la puerta», llave es…", "un objeto para abrir", "una respuesta", "una planta"), ("En «Encontró la llave del problema», llave significa…", "la solución o clave", "un objeto metálico", "una puerta"), ("¿Qué estrategia confirma una acepción?", "Sustituirla y comprobar si la oración tiene sentido", "Elegir siempre la primera", "Ignorar el contexto"), ("¿Cuál palabra puede tener más de un sentido?", "claro", "cuaderno", "martes")]),
 5: ("Lenguaje figurado, ironía y contexto", "El lenguaje figurado usa comparaciones o imágenes. La ironía puede expresar lo contrario de las palabras, por eso debes observar el contexto y la intención.", [
 ("«Tengo un mar de dudas» significa…", "tengo muchas dudas", "nado en el mar", "no tengo dudas"), ("En «el tiempo vuela» se expresa que…", "parece pasar muy rápido", "tiene alas", "se ha detenido"), ("Si alguien llega tarde y oye «¡Qué puntualidad!», probablemente hay…", "ironía", "una definición", "una instrucción literal"), ("¿Qué par contiene antónimos?", "abundante / escaso", "feliz / contento", "veloz / rápido"), ("¿Cuál es un término más general que perro y gato?", "animal", "labrador", "bigote"),
 ("¿Qué recurso relaciona dos elementos sin usar necesariamente «como»?", "metáfora", "definición", "instrucción"), ("«Sus palabras fueron flechas» significa que fueron…", "hirientes o directas", "objetos lanzados", "silenciosas"), ("¿Qué ayuda a reconocer una ironía?", "El contexto, el tono y la intención", "Solo la primera letra", "El número de sílabas"), ("¿Cuál expresión está en sentido literal?", "La ventana está abierta.", "Tiene un corazón de piedra.", "La ciudad despertó."), ("¿Qué pregunta ayuda a interpretar una expresión figurada?", "¿Qué idea comunica en este contexto?", "¿Cuántas letras tiene?", "¿Está al principio del libro?")])},
"grammar": {
1: ("Oraciones pequeñas", "Una oración comunica una idea. «La niña canta.» comienza con mayúscula y termina con punto. Canta dice qué hace la niña.", [
("¿Qué oración está bien escrita?", "Ana juega.", "ana juega", "Ana juega"), ("¿Qué palabra nombra una acción?", "saltar", "mesa", "verde"), ("Completa: El gato ___.", "duerme", "azul", "la"), ("¿Con qué comienza una oración?", "mayúscula", "coma", "punto"), ("¿Qué signo cierra «El sol brilla»?", ".", ",", "¿")]),
 2: ("Artículos, adjetivos y concordancia", "Los artículos acompañan al sustantivo: el, la, los y las. Los adjetivos describen cómo es o cómo son las personas, animales o cosas y deben concordar en género y número.", [
 ("En «flor roja», el adjetivo es…", "roja", "flor", "ninguno"), ("¿Cuál es un sustantivo?", "pelota", "correr", "suave"), ("Completa: Las niñas ___.", "juegan", "juega", "jugamos"), ("¿Cuál es un nombre propio?", "Bogotá", "ciudad", "parque"), ("Elige la concordancia correcta.", "Los gatos blancos", "Los gato blanco", "Las gatos blanca"),
 ("¿Qué artículo acompaña a «árbol»?", "el", "la", "las"), ("Elige el grupo en femenino plural.", "las casas grandes", "los casas grandes", "la casa grandes"), ("¿Qué palabra es un adjetivo en «caballos rápidos»?", "rápidos", "caballos", "los"), ("¿Cuál palabra aguda está bien escrita?", "canción", "cancion", "cáncion"), ("Completa: La mochila ___ está en la mesa.", "azul", "azules", "azulo")]),
 3: ("Sujeto, predicado, verbos y prefijos", "El sujeto indica de quién se habla y el predicado expresa lo que se dice de él. También podemos reconocer el tiempo verbal y formar palabras con prefijos.", [
 ("En «Pedro dibuja un árbol», el sujeto es…", "Pedro", "dibuja", "un árbol"), ("El predicado de «El gato duerme» es…", "duerme", "El gato", "gato"), ("¿Qué verbo está en pasado?", "cantó", "canta", "cantará"), ("Completa: Mañana nosotros ___.", "viajaremos", "viajamos ayer", "viajó"), ("¿Qué palabra sustituye a «María»?", "ella", "ellos", "nosotros"),
 ("En «Las niñas cantan», el predicado es…", "cantan", "Las niñas", "niñas"), ("¿Cuál oración está en futuro?", "El grupo participará.", "El grupo participó.", "El grupo participa."), ("¿Qué expresa des- en desordenar?", "invertir o quitar la acción", "repetir la acción", "hacerla antes"), ("¿Cuál oración concuerda?", "Los músicos ensayan.", "Los músicos ensaya.", "El músicos ensayan."), ("¿Qué palabra es el verbo en «El tren llegó»?", "llegó", "tren", "el")]),
 4: ("Conectores y cohesión", "Los conectores relacionan ideas: porque indica causa, pero introduce contraste y después indica orden. Las referencias evitan repeticiones y mantienen unido el texto.", [
 ("Completa: No salí ___ llovía.", "porque", "pero", "aunque"), ("¿Qué conector expresa contraste?", "pero", "después", "porque"), ("¿Qué pregunta está bien puntuada?", "¿Dónde vives?", "Dónde vives?", "¿Dónde vives."), ("¿Cuál oración contiene un adverbio de lugar?", "El libro está aquí.", "El libro es rojo.", "El libro pesa mucho."), ("¿Qué oración concuerda?", "Las aves vuelan.", "Las aves vuela.", "La aves vuelan."),
 ("¿Qué conector expresa consecuencia?", "por eso", "aunque", "primero"), ("Completa: Ana leyó el texto; ___, subrayó las ideas.", "después", "sin embargo", "porque"), ("¿Qué palabra evita repetir «Carlos»?", "él", "aquí", "aquello"), ("¿Cuál grupo es más cohesionado?", "Llovió. Por eso, llevamos paraguas.", "Llovió. Paraguas libro azul.", "Llovió y por."), ("¿Qué relación expresa «aunque»?", "contraste", "consecuencia", "orden")]),
 5: ("Cohesión, subordinación y registro", "Un texto claro mantiene relaciones entre sus ideas, usa subordinadas con precisión y adapta el registro a la situación comunicativa.", [
 ("Elige la frase correcta.", "Tú tienes tu cuaderno.", "Tu tienes tú cuaderno.", "Tú tienes tú cuaderno."), ("¿Qué oración usa bien la coma?", "Compré pan, leche y arroz.", "Compré, pan leche y arroz.", "Compré pan leche, y, arroz."), ("Completa: Si tuviera tiempo, ___ más.", "leería", "leí", "leeré ayer"), ("¿Qué conector indica consecuencia?", "por eso", "sin embargo", "aunque"), ("¿Cuál oración mantiene el tiempo pasado?", "Llegó, saludó y se sentó.", "Llegó, saluda y se sentará.", "Llega, saludó y se sentará."),
 ("¿Cuál oración contiene una subordinada?", "Pienso que la propuesta es posible.", "La propuesta clara.", "La propuesta llegó."), ("¿Qué relación expresa «sin embargo»?", "contraste", "suma", "orden"), ("¿Qué palabra evita repetir «El informe»?", "Este documento", "El informe informe", "Aquello aquí"), ("¿Qué registro conviene en una solicitud a la alcaldía?", "formal", "coloquial", "familiar"), ("¿Qué revisión mejora la cohesión?", "Comprobar referentes, conectores y relaciones entre ideas", "Eliminar todos los conectores", "Repetir el mismo sustantivo en cada oración")])},
"adventure": {
1: ("Un comienzo y un final", "Busca quién aparece, dónde está y qué hace. Para contar una historia, empieza por el inicio y termina con lo que ocurrió al final.", [
("¿Quién lleva la semilla?", "Lina", "un pez", "Tomás"), ("¿Dónde la planta?", "en una maceta", "en un zapato", "en una caja"), ("¿Qué hace después de plantar?", "la riega", "la tira", "la esconde"), ("¿Qué aparece al final?", "una planta", "un libro", "una pelota"), ("¿Qué título corresponde?", "La semilla de Lina", "El viaje del pez", "El libro perdido")]),
 2: ("Fábulas, leyendas y recitado", "Las fábulas suelen presentar animales, un problema y una moraleja. Las leyendas mezclan hechos y elementos tradicionales. Al recitar, lee con volumen, ritmo y pausas para que el público comprenda.", [
 ("¿Qué hace Lina primero?", "planta una semilla", "ve una planta", "regala flores"), ("¿Por qué la riega?", "para que crezca", "para secarla", "para esconderla"), ("¿Qué palabra indica el final?", "finalmente", "primero", "antes"), ("¿Dónde ocurre la historia?", "en el patio", "en el mar", "en el cine"), ("¿Qué describe mejor a Lina?", "cuidadosa", "desinteresada", "impaciente siempre"),
 ("¿Qué enseñanza suele dejar una fábula?", "Una moraleja", "Una lista de compras", "Un mapa"), ("¿Qué personajes aparecen con frecuencia en una fábula?", "Animales que hablan", "Robots de una fábrica", "Planetas sin historia"), ("¿Qué característica puede tener una leyenda?", "Cuenta una tradición de un lugar", "Solo presenta instrucciones", "No tiene personajes"), ("¿Qué ayuda a recitar un texto?", "Respetar las pausas y hablar con claridad", "Leer sin respirar", "Hablar sin mirar el texto"), ("¿Cuál expresión presenta una moraleja?", "Conviene ayudar a quien lo necesita", "El perro corrió al patio", "Había una vez un zorro")]),
 3: ("Mitos, novela gráfica y club de lectura", "Los mitos explican orígenes mediante relatos tradicionales y hechos extraordinarios. La novela gráfica combina viñetas, imágenes y diálogos; en un club de lectura compartimos interpretaciones con evidencias.", [
("¿Cuál es el problema?", "la tierra está seca", "se perdió la maceta", "no existe el patio"), ("¿Cómo lo resuelven?", "organizan turnos de riego", "rompen la maceta", "dejan de cuidar"), ("¿Qué hace Mateo?", "ayuda a regar", "esconde la semilla", "corta la planta"), ("¿Qué valor demuestra la solución?", "colaboración", "egoísmo", "indiferencia"), ("¿Qué parte muestra la solución?", "desenlace", "título", "inicio")]),
4: ("Inferimos con pistas", "Inferir es relacionar pistas para comprender algo que no se dice directamente. Diferencia una pista del texto de una idea que no tiene evidencia.", [
("¿Por qué Lina propone turnarse?", "para mantener el cuidado cada día", "para vender la maceta", "para evitar a Mateo"), ("¿Qué permite inferir que perseveraron?", "la cuidaron durante semanas", "la maceta era grande", "el patio tenía suelo"), ("¿Qué significa que el brote fue una recompensa?", "vieron el resultado de su esfuerzo", "recibieron dinero", "ganaron un trofeo"), ("¿Cuál es la idea central?", "el cuidado compartido permite crecer", "las plantas no necesitan agua", "Mateo perdió el patio"), ("¿Qué afirmación tiene evidencia?", "Mateo ayudó a cuidar la planta", "Lina compró cien macetas", "la planta creció en una hora")]),
5: ("Leemos con mirada crítica", "Distingue hechos, opiniones e inferencias. Resume sin inventar detalles y reconoce la intención: narrar, informar o convencer.", [
("¿Cuál es un hecho del relato?", "organizaron turnos de riego", "es la planta más hermosa del mundo", "todos deberían sembrar"), ("¿Qué oración expresa una opinión?", "Sembrar es la mejor diversión.", "Mateo ayudó a Lina.", "La tierra estaba seca."), ("La intención principal del relato es…", "narrar una experiencia de cuidado", "vender semillas", "dar cifras de cosechas"), ("¿Cuál es el mejor resumen?", "Dos niños se organizan para cuidar una planta y ven crecer un brote.", "Un niño compra un bosque.", "Una planta crece sin ayuda en un día."), ("¿Qué conclusión se apoya en el texto?", "la constancia y la colaboración ayudaron", "todas las semillas crecen igual", "las plantas nunca necesitan luz")])}
}


def curriculum_for_grade(unit, grade):
    grade = max(1, min(5, int(grade)))
    questions = []

    # Las materias nuevas viven en un módulo separado para que este archivo
    # conserve las unidades originales de Matemáticas y Lengua.
    from .subject_units import SUBJECT_UNIT_KEYS, curriculum_for_grade as subject_curriculum_for_grade
    if unit in SUBJECT_UNIT_KEYS:
        return subject_curriculum_for_grade(unit, grade)

    if unit == "counting":
        if grade == 1:
            rows = [
                ("Hay 7 estrellas. ¿Cuántas estrellas hay?", "7", "6", "8"),
                ("Cuenta: 🍎 🍎 🍎 🍎 🍎. ¿Cuántas manzanas hay?", "5", "4", "6"),
                ("¿Qué número viene después de 9?", "10", "8", "11"),
                ("¿Qué número va antes de 15?", "14", "13", "16"),
                ("¿Qué número está entre 11 y 13?", "12", "10", "14"),
                ("No hay ningún lápiz. ¿Cuántos lápices hay?", "0", "1", "10"),
                ("¿Qué grupo tiene más objetos: 14 o 9?", "14", "9", "4"),
                ("10 y 6 forman el número…", "16", "15", "17"),
                ("Cuenta hacia atrás: 8, 7, 6, …", "5", "4", "7"),
                ("¿Cuál número representa diez y tres unidades?", "13", "10", "30"),
            ]
            lesson = [
                "Contar es decir los números en orden: 0, 1, 2, 3… hasta 20.",
                "El último número que dices al contar una colección indica cuántos objetos hay en total. Ese número se llama cardinal.",
                "Cada objeto se cuenta una sola vez. Puedes señalarlo o moverlo para no perderte.",
                "Los números también se pueden ordenar: uno va antes, otro después, y diez y algunas unidades forman números como 13 o 16.",
            ]
        elif grade == 2:
            rows = [
                ("En 47, ¿cuántas decenas hay?", "4", "7", "47"),
                ("En 63, ¿cuántas unidades hay?", "3", "6", "60"),
                ("¿Qué número forman 5 decenas y 8 unidades?", "58", "85", "13"),
                ("¿Qué número va después de 79?", "80", "78", "89"),
                ("¿Qué número va antes de 50?", "49", "51", "40"),
                ("¿Cuál es mayor: 68 o 86?", "86", "68", "80"),
                ("¿Cuál es menor: 37 o 73?", "37", "73", "70"),
                ("¿Cómo se descompone 92?", "90 + 2", "9 + 2", "20 + 9"),
                ("¿Qué número está entre 64 y 66?", "65", "63", "67"),
                ("¿Cuántas unidades forman una decena?", "10", "100", "1"),
            ]
            lesson = [
                "En 2.º grado trabajamos con números hasta 100. Una decena está formada por 10 unidades.",
                "El valor de una cifra depende de su posición: en 47, el 4 representa 4 decenas y el 7 representa 7 unidades.",
                "Puedes descomponer un número en decenas y unidades: 92 = 90 + 2.",
                "Para comparar números, observa primero las decenas y, si son iguales, compara las unidades.",
            ]
        elif grade == 3:
            rows = [
                ("En 374, ¿qué valor tiene el 7?", "70", "7", "700"),
                ("¿Cómo se descompone 608?", "600 + 8", "60 + 8", "600 + 80"),
                ("¿Qué número forman 4 centenas, 8 decenas y 2 unidades?", "482", "428", "842"),
                ("¿Cuál es mayor: 596 o 569?", "596", "569", "659"),
                ("¿Qué número va después de 899?", "900", "898", "909"),
                ("Redondea 347 a la decena más cercana.", "350", "340", "300"),
                ("Redondea 624 a la centena más cercana.", "600", "700", "620"),
                ("¿Qué número está entre 399 y 401?", "400", "398", "402"),
                ("¿Cuál es menor: 708 o 780?", "708", "780", "700"),
                ("¿Qué número va antes de 1000?", "999", "998", "1001"),
            ]
            lesson = [
                "En 3.º grado trabajamos con números de 0 a 1000. Una centena tiene 100 unidades, una decena tiene 10 y una unidad vale 1.",
                "El valor de una cifra depende de su posición: en 374, el 3 vale 300, el 7 vale 70 y el 4 vale 4. Podemos escribir 374 = 300 + 70 + 4.",
                "Para comparar números, observa primero las centenas, luego las decenas y finalmente las unidades.",
                "Redondear ayuda a estimar. Para redondear a decenas, mira las unidades; para redondear a centenas, mira las decenas. Si la cifra es 5 o más, sube.",
            ]
        elif grade == 4:
            rows = [
                ("En 4,37, ¿qué valor tiene el 3?", "0,3", "3", "0,03"),
                ("¿Cómo se lee 2,45?", "dos enteros y cuarenta y cinco centésimas", "dos enteros y cuarenta y cinco décimas", "doscientos cuarenta y cinco enteros"),
                ("¿Cuál es mayor: 3,5 o 3,05?", "3,5", "3,05", "3,005"),
                ("¿Qué número decimal equivale a 7/10?", "0,7", "0,07", "7,10"),
                ("¿Qué fracción equivale a 0,6?", "6/10", "6/100", "60/10"),
                ("Redondea 4,76 a la décima más cercana.", "4,8", "4,7", "5,0"),
                ("Redondea 2,376 a la centésima más cercana.", "2,38", "2,37", "2,40"),
                ("¿Cuál es la parte entera de 5,08?", "5", "8", "0,08"),
                ("¿Cuál es menor: 0,45 o 0,5?", "0,45", "0,5", "0,05"),
                ("¿Qué número tiene 6 unidades, 2 décimas y 4 centésimas?", "6,24", "6,42", "62,4"),
            ]
            lesson = [
                "En 4.º grado usamos décimas y centésimas. En 4,37, el 3 representa 3 décimas y el 7 representa 7 centésimas.",
                "La coma separa la parte entera de la parte decimal. 2,45 significa 2 enteros, 4 décimas y 5 centésimas.",
                "Para comparar decimales, compara primero la parte entera y luego las décimas y centésimas. Puedes agregar ceros: 3,5 = 3,50.",
                "Para redondear a décimas mira las centésimas; para redondear a centésimas mira las milésimas. Si la cifra siguiente es 5 o más, aumenta una unidad.",
            ]
        elif grade == 5:
            rows = [
                ("¿Cuál es el 25 % de 200?", "50", "25", "75"),
                ("¿Cuál es el 10 % de 450?", "45", "4,5", "450"),
                ("¿Qué número representa 10³?", "1000", "100", "10000"),
                ("¿Qué número representa 10⁴?", "10000", "1000", "100000"),
                ("¿Cuál de estos números es primo?", "29", "27", "33"),
                ("¿Cuál es la descomposición en factores primos de 18?", "2 × 3 × 3", "2 × 9 × 9", "3 × 6"),
                ("¿Qué porcentaje equivale a 0,75?", "75 %", "7,5 %", "750 %"),
                ("¿Qué fracción equivale al 20 %?", "1/5", "1/2", "2/5"),
                ("¿Cuál es el 40 % de 80?", "32", "24", "40"),
                ("¿Cuál número no es primo?", "51", "47", "53"),
            ]
            maximum = 100000
            lesson = [
                "Un porcentaje expresa una parte de cada 100. El 25 % de 200 se calcula como 200 × 25 ÷ 100 = 50.",
                "Las potencias de 10 indican cuántos ceros tiene el resultado: 10³ = 10 × 10 × 10 = 1000 y 10⁴ = 10 000.",
                "Un número primo tiene exactamente dos divisores positivos: 1 y él mismo. Puedes buscar divisores para comprobarlo.",
                "Relaciona representaciones: 0,75 = 75/100 = 75 % y 20 % = 20/100 = 1/5.",
            ]
        else:
            maximum = [0, 20, 100, 1000, 10000, 100000][grade]
            rows = []
            for i in range(10):
                value = min(maximum - 2, grade * 10 + i * 3)
                if i % 2:
                    prompt, answer, wrong = f"¿Qué número viene después de {value}?", value + 1, [value, value + 2]
                else:
                    prompt, answer, wrong = f"¿Qué número va antes de {value}?", value - 1, [value, value - 2]
                rows.append((prompt, str(answer), str(wrong[0]), str(wrong[1])))
            lesson = [
                f"En {grade}.º grado ampliamos el conteo hasta {maximum}.",
                "El valor de una colección se expresa con el último número contado.",
                "Ordena, compara y descompón los números para comprobar tus respuestas.",
            ]
        return {
            "title": "Contamos y representamos hasta " + ("20" if grade == 1 else "100" if grade == 2 else "1000" if grade == 3 else "10000" if grade == 4 else str(maximum)),
            "description": "Lee, compara y representa números naturales y decimales usando su valor posicional.",
            "lesson": [f"Grado {grade}.º · Conteo y cardinalidad", *lesson],
            "questions": [question(*row, index=i) for i, row in enumerate(rows)],
        }

    if unit == "operations":
        if grade == 1:
            rows = [
                ("3 + 2 = ¿cuánto? (fichas)", "5", "4", "6"),
                ("4 + 4 = ¿cuánto? (bloques)", "8", "7", "9"),
                ("6 + 3 = ¿cuánto? (lápices)", "9", "8", "10"),
                ("5 + 2 = ¿cuánto? (pegatinas)", "7", "6", "8"),
                ("7 + 3 = ¿cuánto? (manzanas)", "10", "9", "11"),
                ("8 − 1 = ¿cuánto? (globos)", "7", "6", "8"),
                ("9 − 4 = ¿cuánto? (cubos)", "5", "4", "6"),
                ("10 − 3 = ¿cuánto? (galletas)", "7", "6", "8"),
                ("12 − 2 = ¿cuánto? (colores)", "10", "9", "11"),
                ("14 − 4 = ¿cuánto? (botones)", "10", "9", "11"),
            ]
            lesson = [
                "Sumar significa juntar o agregar objetos. Puedes dibujar cada objeto y contarlos todos.",
                "Restar significa quitar o separar objetos. Tacha los que se van y cuenta los que quedan.",
                "Los números hasta 20 se pueden representar con objetos, dibujos y luego con signos: 3 + 2 = 5.",
                "Lee la historia, identifica si juntas o quitas y comprueba tu respuesta contando otra vez.",
            ]
        elif grade == 2:
            rows = [
                ("27 + 18 = ¿cuánto?", "45", "35", "55"),
                ("36 + 27 = ¿cuánto?", "63", "53", "73"),
                ("48 + 25 = ¿cuánto?", "73", "63", "83"),
                ("59 + 16 = ¿cuánto?", "75", "65", "85"),
                ("67 + 18 = ¿cuánto?", "85", "75", "95"),
                ("42 − 18 = ¿cuánto?", "24", "34", "14"),
                ("53 − 27 = ¿cuánto?", "26", "36", "16"),
                ("71 − 36 = ¿cuánto?", "35", "45", "25"),
                ("84 − 29 = ¿cuánto?", "55", "65", "45"),
                ("90 − 47 = ¿cuánto?", "43", "53", "33"),
            ]
            lesson = [
                "En 2.º grado sumamos y restamos números hasta 100, incluso cuando necesitamos reagrupar.",
                "Al sumar unidades, 10 unidades se cambian por una decena. Por ejemplo, 27 + 18: 7 + 8 = 15, escribimos 5 unidades y llevamos 1 decena.",
                "Al restar, si no hay suficientes unidades, cambiamos una decena por 10 unidades. En 42 − 18, 4 decenas y 2 unidades se convierten en 3 decenas y 12 unidades.",
                "Lee la operación, calcula por partes y comprueba el resultado con la operación inversa.",
            ]
        elif grade == 3:
            rows = [
                ("2 × 6 = ¿cuánto?", "12", "10", "14"),
                ("3 × 7 = ¿cuánto?", "21", "18", "24"),
                ("4 × 8 = ¿cuánto?", "32", "28", "36"),
                ("5 × 9 = ¿cuánto?", "45", "40", "50"),
                ("10 × 6 = ¿cuánto?", "60", "50", "70"),
                ("24 ÷ 2 = ¿cuánto?", "12", "10", "14"),
                ("36 ÷ 3 = ¿cuánto?", "12", "9", "15"),
                ("40 ÷ 4 = ¿cuánto?", "10", "8", "12"),
                ("45 ÷ 5 = ¿cuánto?", "9", "8", "10"),
                ("70 ÷ 10 = ¿cuánto?", "7", "6", "8"),
            ]
            lesson = [
                "Multiplicar es formar grupos iguales. Por ejemplo, 3 × 4 significa 3 grupos de 4 y también 4 + 4 + 4.",
                "En 3.º grado practicamos las tablas del 2, 3, 4, 5 y 10. Busca patrones y usa una suma repetida si necesitas comprobar.",
                "Dividir es repartir en partes iguales o averiguar cuántos grupos caben. Si 24 objetos se reparten entre 3 personas, cada una recibe 8.",
                "La multiplicación y la división son operaciones inversas: si 5 × 9 = 45, entonces 45 ÷ 5 = 9.",
            ]
        elif grade == 4:
            rows = [
                ("24 × 3 = ¿cuánto?", "72", "62", "82"),
                ("36 × 12 = ¿cuánto?", "432", "342", "442"),
                ("125 × 4 = ¿cuánto?", "500", "400", "520"),
                ("208 × 3 = ¿cuánto?", "624", "604", "684"),
                ("864 ÷ 4 = ¿cuánto?", "216", "206", "226"),
                ("936 ÷ 6 = ¿cuánto?", "156", "146", "166"),
                ("1440 ÷ 12 = ¿cuánto?", "120", "110", "130"),
                ("¿Qué fracción equivale a 1/2?", "2/4", "1/4", "3/4"),
                ("¿Qué fracción equivale a 3/5?", "6/10", "3/10", "9/10"),
                ("¿Qué fracción equivale a 4/8?", "1/2", "1/4", "2/3"),
            ]
            lesson = [
                "Para multiplicar números de varias cifras, descompón el segundo factor y suma los productos parciales. Por ejemplo, 36 × 12 = 36 × 10 + 36 × 2.",
                "En una división multidígito, calcula cuántas veces cabe el divisor y comprueba multiplicando cociente por divisor.",
                "Una fracción equivalente representa la misma cantidad con partes divididas de otra manera. Multiplicar numerador y denominador por el mismo número conserva su valor.",
                "Organiza cada procedimiento por pasos y estima el resultado antes de calcular para detectar errores.",
            ]
        elif grade == 5:
            rows = [
                ("12,5 + 3,75 = ¿cuánto?", "16,25", "15,25", "16,75"),
                ("8,4 − 2,65 = ¿cuánto?", "5,75", "5,85", "6,25"),
                ("2,5 × 4 = ¿cuánto?", "10", "8", "12"),
                ("7,2 ÷ 3 = ¿cuánto?", "2,4", "2,1", "3,4"),
                ("0,75 + 1,125 = ¿cuánto?", "1,875", "1,825", "1,975"),
                ("15,6 ÷ 1,2 = ¿cuánto?", "13", "12", "14"),
                ("1/2 + 1/3 = ¿cuánto?", "5/6", "2/5", "2/6"),
                ("3/4 − 1/6 = ¿cuánto?", "7/12", "2/8", "1/2"),
                ("2/3 + 1/4 = ¿cuánto?", "11/12", "3/7", "8/12"),
                ("5/6 − 1/4 = ¿cuánto?", "7/12", "4/10", "1/2"),
            ]
            lesson = [
                "Alinea las comas al sumar y restar decimales. Si faltan cifras, agrega ceros sin cambiar el valor: 2,5 = 2,500.",
                "Para multiplicar o dividir decimales, estima primero y revisa después la posición de la coma en el resultado.",
                "Para sumar o restar fracciones con denominadores diferentes, busca un denominador común. Por ejemplo, 1/2 + 1/3 = 3/6 + 2/6 = 5/6.",
                "Simplifica la fracción final cuando sea posible y comprueba que el resultado esté dentro de lo razonable.",
            ]
        else:
            rows = []
            for i in range(10):
                if grade == 3:
                    first, second = 126 + i * 7, 48 + i * 3
                    operator = "+" if i < 5 else "−"
                    answer = first + second if operator == "+" else first - second
                    step = 10
                elif grade == 4:
                    if i < 5:
                        first, second = 6 + i, 4 + i % 5
                        operator = "×"
                        answer = first * second
                    else:
                        second = 3 + i % 6
                        answer = (72 + i) // second
                        first = answer * second
                        operator = "÷"
                    step = 1
                else:
                    first = Decimal(125 + i * 25) / 100 if i < 5 else Decimal(450 + i * 20) / 100
                    second = Decimal(75 + i * 10) / 100 if i < 5 else Decimal(125 + i * 10) / 100
                    operator = "+" if i < 5 else "−"
                    answer = first + second if operator == "+" else first - second
                    step = Decimal("0.1")
                display = lambda value: str(value).replace(".", ",")
                rows.append((
                    f"{display(first)} {operator} {display(second)} = ¿cuánto?",
                    display(answer), display(answer + step), display(answer - step),
                ))
            lesson = [
                f"En {grade}.º grado resolvemos operaciones cada vez más complejas.",
                "Representa el problema, elige la operación y revisa el resultado.",
            ]
        return {
            "title": "Juntamos y quitamos" if grade == 1 else "Sumamos y restamos hasta 100" if grade == 2 else "Operaciones decimales y fracciones" if grade == 5 else "Multiplicamos, dividimos y equivalencias" if grade == 4 else "Multiplicamos y repartimos",
            "description": "Opera con decimales y suma o resta fracciones con denominadores diferentes." if grade == 5 else "Resuelve multiplicaciones y divisiones multidígito y reconoce fracciones equivalentes." if grade == 4 else "Resuelve situaciones de multiplicar grupos iguales y repartir cantidades de forma equitativa." if grade == 3 else "Resuelve situaciones de juntar, quitar, repetir y repartir usando dibujos y números.",
            "lesson": [f"Grado {grade}.º · {('Suma y resta con objetos' if grade <= 2 else 'Operaciones y problemas')}", *lesson],
            "questions": [question(*row, index=i) for i, row in enumerate(rows)],
        }

    if unit == "shapes":
        if grade == 1:
            rows = [
                ("¿Cuántos lados tiene un triángulo?", "3", "2", "4"),
                ("¿Cuántos lados tiene un cuadrado?", "4", "3", "5"),
                ("¿Qué figura no tiene lados ni vértices?", "círculo", "triángulo", "cuadrado"),
                ("¿Cuál es un cuerpo geométrico 3D?", "cubo", "círculo", "triángulo"),
                ("¿Qué cuerpo puede rodar fácilmente?", "esfera", "cubo", "cuadrado"),
                ("Una lata se parece a un…", "cilindro", "triángulo", "rectángulo"),
                ("La pelota está ___ de la caja: ⚽  📦", "a la izquierda", "a la derecha", "encima"),
                ("El libro está ___ de la mesa: 📖 sobre la mesa", "encima", "debajo", "dentro"),
                ("¿Qué figura tiene 4 lados iguales?", "cuadrado", "círculo", "triángulo"),
                ("Si el gato está dentro de la caja, el gato está…", "adentro", "afuera", "arriba"),
            ]
            lesson = [
                "Las figuras planas o 2D se pueden dibujar en una hoja. El triángulo tiene 3 lados y el cuadrado tiene 4 lados iguales.",
                "Los cuerpos geométricos o 3D ocupan espacio. Un cubo, una esfera y un cilindro son ejemplos.",
                "Observa la posición de los objetos: arriba, abajo, dentro, afuera, delante, detrás, a la izquierda o a la derecha.",
                "Toca, gira y dibuja objetos para relacionar sus formas con las figuras geométricas.",
            ]
        elif grade == 2:
            rows = [
                ("Una regla mide 30 cm y una cuerda 1 m. ¿Cuál es más larga?", "la cuerda", "la regla", "miden igual"),
                ("¿Cuántos centímetros hay en 1 metro?", "100", "10", "1"),
                ("¿Qué unidad conviene para medir un lápiz?", "centímetros", "metros", "horas"),
                ("¿Qué unidad conviene para medir la distancia entre dos barrios?", "metros", "centímetros", "pesos"),
                ("Si son las 3:00 y pasa una hora, ¿qué hora es?", "las 4:00", "las 2:00", "las 3:30"),
                ("¿Cuántos minutos tiene una hora?", "60", "30", "100"),
                ("Tienes 2 monedas de 500 pesos. ¿Cuánto dinero tienes?", "1000 pesos", "500 pesos", "1500 pesos"),
                ("Un juguete cuesta 800 pesos y pagas con 1000. ¿Cuánto recibes?", "200 pesos", "180 pesos", "1200 pesos"),
                ("¿Qué objeto pesa más: una pluma o una mochila?", "la mochila", "la pluma", "pesan igual"),
                ("¿Qué dura menos: un minuto o una hora?", "un minuto", "una hora", "duran igual"),
            ]
            lesson = [
                "En 2.º grado medimos objetos y distancias con centímetros y metros. Un metro equivale a 100 centímetros.",
                "Usa centímetros para objetos pequeños, como un lápiz, y metros para distancias u objetos grandes.",
                "Una hora tiene 60 minutos. Lee el reloj y piensa cuánto tiempo transcurre entre dos momentos.",
                "El dinero sirve para comprar y calcular cambios. Si pagas más de lo que cuesta algo, restas para encontrar la devolución.",
            ]
        elif grade == 3:
            rows = [
                ("Un cuadrado tiene lados de 5 cm. ¿Cuál es su perímetro?", "20 cm", "10 cm", "25 cm"),
                ("Un rectángulo mide 6 cm de largo y 3 cm de ancho. ¿Cuál es su perímetro?", "18 cm", "9 cm", "12 cm"),
                ("Un triángulo tiene lados de 3 cm, 4 cm y 5 cm. ¿Cuál es su perímetro?", "12 cm", "9 cm", "15 cm"),
                ("¿Qué ángulo forma la esquina de un libro?", "ángulo recto", "ángulo agudo", "ángulo llano"),
                ("¿Cuánto mide un ángulo recto?", "90°", "45°", "180°"),
                ("¿Qué unidad conviene para pesar una mochila?", "kilogramos", "gramos", "litros"),
                ("¿Qué unidad conviene para pesar un lápiz?", "gramos", "kilogramos", "litros"),
                ("¿Qué unidad conviene para medir el agua de una jarra?", "litros", "kilogramos", "gramos"),
                ("¿Cuántos gramos hay en 1 kilogramo?", "1000", "100", "10"),
                ("¿Cuántos mililitros hay en 1 litro?", "1000", "100", "10"),
            ]
            lesson = [
                "El perímetro es la medida del borde de una figura. Para encontrarlo, suma todos sus lados: un cuadrado de lado 5 cm tiene 5 + 5 + 5 + 5 = 20 cm.",
                "Un ángulo es la abertura entre dos lados. El ángulo recto mide 90° y se parece a la esquina de un cuaderno.",
                "Usa kilogramos para objetos pesados y gramos para objetos pequeños. Un kilogramo equivale a 1000 gramos.",
                "Para medir la capacidad de recipientes usamos litros y mililitros. Un litro equivale a 1000 mililitros.",
            ]
        elif grade == 4:
            rows = [
                ("Un rectángulo mide 8 cm de largo y 5 cm de ancho. ¿Cuál es su área?", "40 cm²", "26 cm²", "13 cm²"),
                ("Un cuadrado tiene lados de 7 cm. ¿Cuál es su área?", "49 cm²", "28 cm²", "14 cm²"),
                ("Un rectángulo mide 9 cm por 4 cm. ¿Cuál es su perímetro?", "26 cm", "36 cm", "13 cm"),
                ("¿Cuántos centímetros cuadrados hay en 1 m²?", "10000 cm²", "100 cm²", "1000 cm²"),
                ("¿Cuántos centímetros son 2,5 metros?", "250 cm", "25 cm", "205 cm"),
                ("¿Cuántos metros son 3 kilómetros?", "3000 m", "300 m", "30 m"),
                ("En formato de 24 horas, ¿qué hora es 15:00?", "3:00 p. m.", "5:00 p. m.", "3:00 a. m."),
                ("En formato de 24 horas, ¿qué hora es 21:30?", "9:30 p. m.", "11:30 p. m.", "9:30 a. m."),
                ("De 14:20 a 16:00 transcurren…", "1 h 40 min", "2 h 20 min", "1 h 20 min"),
                ("¿Qué fórmula usamos para calcular el área de un rectángulo?", "largo × ancho", "largo + ancho", "lado × 4"),
            ]
            lesson = [
                "El área mide la superficie interior de una figura. Para un rectángulo, multiplica largo × ancho; para un cuadrado, lado × lado.",
                "El perímetro mide el borde. No confundas perímetro con área: un rectángulo de 8 cm por 5 cm tiene área 40 cm² y perímetro 26 cm.",
                "Convierte antes de comparar: 1 m² equivale a 10 000 cm², 1 km equivale a 1000 m y 1 m equivale a 100 cm.",
                "El reloj de 24 horas cuenta desde 00:00 hasta 23:59. Para pasar de la tarde a formato de 12 horas, resta 12 a las horas mayores que 12.",
            ]
        elif grade == 5:
            rows = [
                ("Una caja mide 4 cm de largo, 3 cm de ancho y 2 cm de alto. ¿Cuál es su volumen?", "24 cm³", "9 cm³", "12 cm³"),
                ("Un cubo tiene aristas de 5 cm. ¿Cuál es su volumen?", "125 cm³", "25 cm³", "100 cm³"),
                ("¿Qué fórmula usamos para el volumen de un prisma rectangular?", "largo × ancho × alto", "largo + ancho + alto", "largo × ancho"),
                ("¿Qué punto está en la coordenada (3, 2)?", "3 unidades a la derecha y 2 arriba", "2 unidades a la derecha y 3 arriba", "3 unidades a la izquierda y 2 abajo"),
                ("En el punto (0, 4), ¿qué valor tiene x?", "0", "4", "−4"),
                ("En un mapa, 1 cm representa 2 km. ¿Cuántos km representan 5 cm?", "10 km", "7 km", "2,5 km"),
                ("Una escala 1:100 significa que 1 cm en el plano representa…", "100 cm reales", "10 cm reales", "1 cm real"),
                ("Si un rectángulo mide 6 cm en un plano a escala 1:50, ¿cuánto mide en la realidad?", "300 cm", "56 cm", "100 cm"),
                ("¿Qué coordenada indica 4 unidades a la izquierda y 3 abajo del origen?", "(−4, −3)", "(4, 3)", "(−3, −4)"),
                ("¿Qué unidad conviene para medir el volumen de una piscina?", "metros cúbicos", "centímetros", "kilogramos"),
            ]
            lesson = [
                "El volumen mide el espacio que ocupa un cuerpo. En un prisma rectangular se calcula largo × ancho × alto y se expresa en unidades cúbicas.",
                "En el plano cartesiano, la primera coordenada indica el movimiento horizontal (x) y la segunda el vertical (y). Empieza siempre en el origen (0,0).",
                "Una escala relaciona una medida del dibujo con la medida real. Si 1 cm representa 2 km, 5 cm representan 10 km.",
                "Elige la unidad adecuada: cm³ para objetos pequeños y m³ para espacios grandes. Revisa las unidades antes de responder.",
            ]
        else:
            rows = [
                ("¿Qué fracción representa una de cuatro partes iguales?", "1/4", "4/1", "1/2"),
                ("¿Cuál es mayor?", "5/8", "2/8", "1/8"),
                ("¿Cuántos lados tiene un pentágono?", "5", "4", "6"),
                ("La mitad de 12 es…", "6", "4", "8"),
                ("¿Qué figura tiene cuatro lados iguales?", "cuadrado", "círculo", "triángulo"),
                ("Una pizza tiene 8 partes y comes 3. ¿Qué fracción comes?", "3/8", "8/3", "5/8"),
                ("¿Cuántos centímetros hay en un metro?", "100", "10", "50"),
                ("¿Qué fracción equivale a la mitad?", "2/4", "1/3", "3/4"),
                ("Un rectángulo tiene…", "4 lados", "3 lados", "5 lados"),
                ("Si recorres 3 metros y luego 2 metros, recorres…", "5 metros", "1 metro", "6 metros"),
            ]
            lesson = [
                "Las figuras tienen lados, vértices y propiedades que puedes observar.",
                "Representa cada problema con un dibujo antes de elegir una respuesta.",
            ]
        return {
            "title": "Formas, cuerpos y posiciones" if grade == 1 else "Medidas, tiempo y dinero" if grade == 2 else "Perímetro, ángulos y medidas" if grade == 3 else "Área, conversiones y tiempo" if grade == 4 else "Volumen, coordenadas y escala",
            "description": "Calcula volumen, interpreta coordenadas y aplica escalas en planos." if grade == 5 else "Calcula áreas, perímetros, conversiones y duraciones usando estrategias ordenadas." if grade == 4 else "Calcula perímetros, reconoce ángulos y elige unidades de masa y capacidad." if grade == 3 else "Reconoce figuras, cuerpos geométricos y posiciones en el espacio.",
            "lesson": [f"Grado {grade}.º · {('Formas, cuerpos y posiciones' if grade == 1 else 'Medidas, tiempo y dinero' if grade == 2 else 'Perímetro, ángulos y medidas' if grade == 3 else 'Área, conversiones y tiempo' if grade == 4 else 'Volumen, coordenadas y escala')}", *lesson],
            "questions": [question(*row, index=i) for i, row in enumerate(rows)],
        }

    if unit in LANGUAGE:
        title, explanation, rows = LANGUAGE[unit][grade]
        result = {"lesson": [f"Grado {grade}.º · {title}", explanation,
            "Lee cada ejemplo y explica con tus palabras por qué elegiste tu respuesta. Si tienes dudas, vuelve a la lección."],
            "questions": [question(*row, index=i) for i, row in enumerate(rows)]}
        if unit == "adventure":
            result["passage"] = ("Lina está en el patio. Planta una semilla en una maceta y la riega. La cuida cada día. Al final aparece una planta." if grade <= 2 else
                "Lina plantó una semilla en el patio. Un día vio que la tierra estaba seca y pidió ayuda a Mateo. Organizaron turnos para regar sin encharcar y cuidaron la maceta durante semanas. Al ver un brote, Lina dijo: «Sembrar es la mejor diversión». El brote fue la recompensa de su constancia.")
        return result
    if unit == "patterns":
        if grade == 1:
            rows = [
                ("Completa el patrón AB: rojo, azul, rojo, …", "azul", "rojo", "verde"),
                ("Completa el patrón AB: ⭐, 🌙, ⭐, …", "🌙", "⭐", "☀️"),
                ("Completa el patrón ABB: círculo, cuadrado, cuadrado, …", "círculo", "cuadrado", "triángulo"),
                ("Completa el patrón ABB: 🐱, 🐶, 🐶, 🐱, …", "🐶", "🐱", "🐭"),
                ("¿Qué sigue en: grande, pequeño, grande, …?", "pequeño", "grande", "mediano"),
                ("En un pictograma, cada ★ vale 1 manzana. Ana tiene ★★★. ¿Cuántas tiene?", "3", "2", "4"),
                ("Cada ● vale 1 pelota. Bruno tiene ●●●●. ¿Cuántas tiene?", "4", "3", "5"),
                ("Cada ▲ vale 1 libro. Hay ▲▲. ¿Cuántos libros hay?", "2", "1", "3"),
                ("Cada ♥ vale 1 flor. Hay ♥♥♥♥♥. ¿Cuántas flores hay?", "5", "4", "6"),
                ("Cada ☀️ vale 1 día soleado. Hay ☀️☀️☀️☀️. ¿Cuántos días?", "4", "3", "5"),
            ]
            return {
                "title": "Patrones y pictogramas",
                "description": "Descubre qué se repite, completa secuencias y lee datos con dibujos.",
                "lesson": [
                    "Grado 1.º · Patrones y pictogramas",
                    "Un patrón es una regla que se repite. En AB se repiten dos elementos; en ABB, uno y luego dos iguales.",
                    "Un pictograma muestra datos con dibujos. Primero descubre cuánto vale cada dibujo y después cuenta.",
                    "Mira qué cambia y qué permanece igual antes de elegir lo que sigue.",
                ],
                "questions": [question(*row, index=i) for i, row in enumerate(rows)],
            }
        if grade == 2:
            rows = [
                ("Completa: 12, 22, 32, …", "42", "40", "52"),
                ("Completa: 5, 10, 15, …", "20", "16", "25"),
                ("Completa: 90, 80, 70, …", "60", "65", "50"),
                ("Completa: 3, 6, 9, …", "12", "11", "15"),
                ("Completa: 25, 35, 45, …", "55", "50", "65"),
                ("En una gráfica, Ana tiene 4 libros y Luis 7. ¿Quién tiene más?", "Luis", "Ana", "tienen igual"),
                ("En una gráfica, Sara tiene 6 puntos y Leo 2. ¿Cuántos más tiene Sara?", "4", "8", "3"),
                ("Cada ★ representa 2 votos. Hay ★★★. ¿Cuántos votos son?", "6", "3", "5"),
                ("Una gráfica muestra 5 manzanas y 3 peras. ¿Cuántas frutas hay?", "8", "2", "15"),
                ("¿Qué dato es mayor: 9 mascotas o 6 mascotas?", "9 mascotas", "6 mascotas", "son iguales"),
            ]
            return {
                "title": "Patrones y gráficas",
                "description": "Descubre reglas numéricas y representa datos sencillos en gráficas.",
                "lesson": [
                    "Grado 2.º · Patrones y gráficas",
                    "Un patrón sigue una regla. Observa cuánto aumenta o disminuye cada número: 12, 22, 32… aumenta de 10 en 10.",
                    "Una gráfica organiza datos para compararlos. Primero lee qué representa cada dibujo o barra y después cuenta.",
                    "Para responder, busca la diferencia entre dos cantidades o suma los datos que pertenecen a la misma gráfica.",
                ],
                "questions": [question(*row, index=i) for i, row in enumerate(rows)],
            }
        if grade == 3:
            rows = [
                ("¿Qué fracción unitaria representa una de 5 partes iguales?", "1/5", "5/1", "1/4"),
                ("Una torta se divide en 4 partes iguales. ¿Qué fracción es una parte?", "1/4", "4/1", "1/2"),
                ("¿Cuál es mayor: 1/3 o 1/6?", "1/3", "1/6", "1/9"),
                ("Una barra está dividida en 8 partes y tomas una. ¿Qué fracción tomas?", "1/8", "8/1", "1/4"),
                ("¿Qué fracción representa la mitad de una figura dividida en 2 partes?", "1/2", "2/1", "1/4"),
                ("En una gráfica de barras, Ana tiene 4 libros y Luis 7. ¿Cuántos libros más tiene Luis?", "3", "11", "2"),
                ("Una gráfica muestra 5 votos para el rojo y 3 para el azul. ¿Cuántos votos hay en total?", "8", "2", "15"),
                ("En una gráfica, lunes tiene 2 visitas y martes 6. ¿Qué día tiene más?", "martes", "lunes", "tienen igual"),
                ("Cada bloque de una gráfica vale 2 puntos. Si hay 4 bloques, ¿cuántos puntos son?", "8", "6", "4"),
                ("En una gráfica, fútbol tiene 9 votos y baloncesto 6. ¿Cuál es la diferencia?", "3", "15", "2"),
            ]
            return {
                "title": "Fracciones unitarias y gráficas",
                "description": "Reconoce fracciones de una unidad y lee datos en gráficas de barras.",
                "lesson": [
                    "Una fracción unitaria representa una sola parte igual de un todo: 1/4 significa una de cuatro partes iguales.",
                    "El denominador es el número de partes iguales y el numerador indica cuántas partes tomamos. En una fracción unitaria, el numerador es 1.",
                    "Cuando las fracciones unitarias tienen el mismo numerador, la que tiene menos partes iguales es mayor: 1/3 es mayor que 1/6.",
                    "Una gráfica de barras compara cantidades. Lee el nombre de cada categoría, observa la altura de las barras y calcula totales o diferencias.",
                ],
                "questions": [question(*row, index=i) for i, row in enumerate(rows)],
            }
        if grade == 4:
            rows = [
                ("¿Cuál es la media de 4, 6 y 8?", "6", "5", "7"),
                ("¿Cuál es la media de 10, 12 y 14?", "12", "11", "13"),
                ("Las notas son 5, 7, 8 y 10. ¿Cuál es su media?", "7,5", "7", "8"),
                ("En una bolsa hay 3 fichas rojas y 1 azul. ¿Qué color es más probable sacar?", "rojo", "azul", "son igual de probables"),
                ("Al lanzar una moneda, sacar cara es…", "tan probable como sacar sello", "imposible", "seguro"),
                ("Al lanzar un dado, sacar un 7 es…", "imposible", "seguro", "probable"),
                ("Al sacar una ficha de una bolsa que solo tiene fichas verdes, sacar verde es…", "seguro", "imposible", "poco probable"),
                ("Una ruleta tiene 4 partes iguales: 3 azules y 1 amarilla. ¿Qué color es más probable?", "azul", "amarillo", "son igual de probables"),
                ("¿Qué representa la media de un conjunto de datos?", "un valor central o representativo", "el dato siempre mayor", "el número de datos"),
                ("Si todos los datos de una lista aumentan 2, la media…", "aumenta 2", "no cambia", "disminuye 2"),
            ]
            return {
                "title": "Media y probabilidad",
                "description": "Calcula medias y describe posibilidades usando datos sencillos.",
                "lesson": [
                    "La media se calcula sumando todos los datos y dividiendo el total entre la cantidad de datos. La media de 4, 6 y 8 es 18 ÷ 3 = 6.",
                    "La media es un valor representativo: no tiene que coincidir con uno de los datos de la lista.",
                    "La probabilidad describe qué tan posible es un evento: puede ser imposible, poco probable, igualmente probable, probable o seguro.",
                    "Observa cuántos resultados favorecen cada evento. Si hay más fichas rojas que azules, sacar roja es más probable.",
                ],
                "questions": [question(*row, index=i) for i, row in enumerate(rows)],
            }
        if grade == 5:
            rows = [
                ("Si 3 cuadernos cuestan 6 pesos, ¿cuánto cuestan 5 al mismo precio?", "10 pesos", "8 pesos", "12 pesos"),
                ("Una receta usa 2 tazas de harina para 4 personas. ¿Cuántas usa para 8?", "4 tazas", "2 tazas", "6 tazas"),
                ("En una gráfica lineal, una planta mide 4 cm en enero y 7 cm en febrero. ¿Cuánto creció?", "3 cm", "11 cm", "2 cm"),
                ("Una gráfica muestra 12 visitantes el lunes y 18 el martes. ¿Cuántos más hubo el martes?", "6", "30", "5"),
                ("Una bolsa tiene 3 fichas rojas y 1 azul. ¿Cuál es la probabilidad de sacar roja?", "3/4", "1/4", "1/3"),
                ("En una caja hay 5 bolas verdes y 5 amarillas. Sacar verde es…", "igual de probable que amarilla", "más probable que amarilla", "imposible"),
                ("Si 4 lápices cuestan 8 pesos, ¿cuánto cuesta 1 lápiz?", "2 pesos", "4 pesos", "8 pesos"),
                ("Una distancia pasa de 20 km a 30 km. ¿Qué porcentaje aumentó?", "50 %", "10 %", "25 %"),
                ("En una gráfica lineal, los datos son 2, 5, 8, 11. ¿Qué regla siguen?", "aumentan de 3 en 3", "aumentan de 2 en 2", "se duplican"),
                ("Al lanzar un dado, ¿qué resultado es más probable: par o sacar 6?", "par", "sacar 6", "son igual de probables"),
            ]
            return {
                "title": "Proporción, gráficas y azar",
                "description": "Resuelve proporciones, interpreta gráficas lineales y analiza situaciones de azar.",
                "lesson": [
                    "Dos cantidades son proporcionales cuando mantienen la misma relación. Si 3 cuadernos cuestan 6 pesos, cada uno cuesta 2 y 5 cuestan 10.",
                    "Una gráfica lineal muestra cómo cambian los datos. Observa los ejes, compara puntos y describe aumentos o disminuciones.",
                    "La probabilidad puede expresarse con una fracción: si 3 de 4 fichas son rojas, la probabilidad de sacar roja es 3/4.",
                    "Distingue entre seguro, imposible, más probable, menos probable e igualmente probable usando todos los resultados posibles.",
                ],
                "questions": [question(*row, index=i) for i, row in enumerate(rows)],
            }
        steps = [1, 2, 5, 7, 10]
        step = steps[grade-1]
        for i in range(10):
            start = (i+1)*grade
            if grade == 5:
                seq = [start * 2**j for j in range(4)]; answer = seq[-1]*2
                wrong = [answer+2, seq[-1]+2]
            else:
                seq = [start+j*step for j in range(4)]; answer = seq[-1]+step
                wrong = [answer+1, answer-1]
            questions.append(question(f"¿Qué número sigue? {', '.join(map(str,seq))}, …", answer, *wrong, i))
        example = "3, 6, 12, 24: cada número se multiplica por 2; sigue 48." if grade==5 else f"2, {2+step}, {2+2*step}: sumamos {step} cada vez; sigue {2+3*step}."
        lesson = [f"Grado {grade}.º · Patrones numéricos", "Compara cada término con el anterior. Busca una regla que funcione en todos los pasos.", example, "Comprueba el siguiente número aplicando la misma regla. Luego inventa otra secuencia con esa regla."]
    elif unit == "market":
        if grade == 4:
            rows = [
                ("Compras 3 cajas con 12 cuadernos y regalas 5. ¿Cuántos quedan?", "31", "36", "29"),
                ("Compras 4 paquetes de 8 lápices y recibes 6 más. ¿Cuántos tienes?", "38", "32", "42"),
                ("Repartes 96 caramelos entre 4 niños y das 3 extra a cada uno. ¿Cuántos recibe cada niño?", "27", "24", "21"),
                ("Hay 5 estantes con 7 libros y se retiran 9. ¿Cuántos quedan?", "26", "35", "25"),
                ("Repartes 120 fichas entre 6 equipos y agregas 15 al total. ¿Cuántas fichas hay ahora?", "35", "20", "45"),
                ("Una granja tiene 6 corrales con 9 gallinas y vende 8. ¿Cuántas quedan?", "46", "54", "44"),
                ("Repartes 144 dulces entre 12 bolsas y agregas 7 a una bolsa. ¿Cuántos quedan en esa bolsa?", "19", "12", "20"),
                ("Compras 8 paquetes de 15 vasos y usas 20. ¿Cuántos vasos quedan?", "100", "120", "95"),
                ("Repartes 72 semillas entre 8 macetas y colocas 12 más en cada maceta. ¿Cuántas hay en cada una?", "21", "20", "24"),
                ("Compras 9 cajas de 11 tizas y entregas 14. ¿Cuántas tizas quedan?", "85", "99", "75"),
            ]
            return {
                "title": "Problemas de varios pasos",
                "description": "Resuelve problemas cotidianos que combinan multiplicación, división, suma y resta.",
                "lesson": [
                    "Un problema de varios pasos necesita más de una operación. Lee toda la historia, identifica qué ocurre primero y qué ocurre después.",
                    "Subraya los datos y escribe una operación para cada paso. Por ejemplo: 3 × 12 = 36 y luego 36 − 5 = 31.",
                    "Comprueba que cada resultado intermedio tenga sentido antes de continuar y revisa la unidad de la respuesta final.",
                    "Puedes estimar el resultado para saber si tu respuesta final es razonable.",
                ],
                "questions": [question(*row, index=i) for i, row in enumerate(rows)],
            }
        if grade == 5:
            rows = [
                ("Una camiseta cuesta 200 pesos. ¿Cuánto es el 10 %?", "20 pesos", "10 pesos", "30 pesos"),
                ("Un libro cuesta 400 pesos. ¿Cuánto es el 25 %?", "100 pesos", "25 pesos", "125 pesos"),
                ("Un juguete cuesta 800 pesos y tiene 20 % de descuento. ¿Cuánto pagas?", "640 pesos", "780 pesos", "680 pesos"),
                ("Una mochila cuesta 1500 pesos y tiene 10 % de descuento. ¿Cuánto pagas?", "1350 pesos", "1400 pesos", "150 pesos"),
                ("Si 3 jugos cuestan 900 pesos, ¿cuánto cuestan 5 al mismo precio?", "1500 pesos", "1200 pesos", "1800 pesos"),
                ("Una tienda vende 4 cuadernos por 1200 pesos. ¿Cuánto cuesta cada uno?", "300 pesos", "400 pesos", "240 pesos"),
                ("Un precio de 2500 pesos aumenta 20 %. ¿Cuál es el nuevo precio?", "3000 pesos", "2700 pesos", "2900 pesos"),
                ("De 60 productos, el 30 % son rojos. ¿Cuántos productos rojos hay?", "18", "20", "30"),
                ("Una compra cuesta 2400 pesos y pagas 3000. ¿Qué porcentaje del pago corresponde al precio?", "80 %", "70 %", "90 %"),
                ("Si 5 entradas cuestan 2500 pesos, ¿cuánto cuestan 8 entradas?", "4000 pesos", "3000 pesos", "4500 pesos"),
            ]
            return {
                "title": "Porcentajes y proporciones en el mercado",
                "description": "Aplica porcentajes, descuentos y relaciones proporcionales en situaciones de compra.",
                "lesson": [
                    "Para hallar un porcentaje, multiplica la cantidad por el porcentaje y divide entre 100. El 25 % de 400 es 400 × 25 ÷ 100 = 100.",
                    "Un descuento se resta del precio original. Si una mochila de 1500 pesos tiene 10 % de descuento, descuentas 150 y pagas 1350.",
                    "En una situación proporcional, encuentra primero el valor de una unidad y luego multiplica por la cantidad que necesitas.",
                    "Lee si la pregunta pide el descuento, el precio final, el valor unitario o el total antes de calcular.",
                ],
                "questions": [question(*row, index=i) for i, row in enumerate(rows)],
            }
        if grade == 5:
            rows = [
                ("Una caja mide 4 m de largo, 3 m de ancho y 2 m de alto. ¿Cuál es su volumen?", "24 m³", "9 m³", "12 m³"),
                ("Un cubo tiene aristas de 5 cm. ¿Cuál es su volumen?", "125 cm³", "25 cm³", "100 cm³"),
                ("En el punto (−2, 4), ¿cuál es la coordenada x?", "−2", "4", "2"),
                ("¿Qué punto está 3 unidades a la derecha y 2 arriba del origen?", "(3, 2)", "(2, 3)", "(−3, 2)"),
                ("Un plano usa la escala 1 cm = 5 m. ¿Cuánto representan 7 cm?", "35 m", "12 m", "30 m"),
                ("A escala 1:100, una pared de 4 cm en el plano mide…", "400 cm", "40 cm", "104 cm"),
                ("¿Cuántos litros caben en un tanque de 2 m³?", "2000 l", "200 l", "20 l"),
                ("Un prisma rectangular mide 10 cm × 2 cm × 3 cm. Su volumen es…", "60 cm³", "30 cm³", "15 cm³"),
                ("¿Qué coordenada representa 5 a la izquierda y 1 arriba?", "(−5, 1)", "(5, −1)", "(−1, 5)"),
                ("¿Qué unidad conviene para el volumen de una habitación?", "metros cúbicos", "centímetros cuadrados", "kilómetros"),
            ]
            return {
                "title": "Volumen, coordenadas y escala",
                "description": "Calcula volúmenes, ubica puntos y utiliza escalas para interpretar planos.",
                "lesson": [
                    "El volumen de un prisma rectangular se calcula largo × ancho × alto. Un cubo de lado 5 cm tiene 5 × 5 × 5 = 125 cm³.",
                    "En el plano cartesiano, x indica el desplazamiento horizontal y y el vertical. Los signos negativos señalan izquierda o abajo.",
                    "La escala permite pasar del dibujo a la realidad. Si 1 cm representa 5 m, multiplica la medida del plano por 5.",
                    "Recuerda que 1 m³ equivale a 1000 litros y escribe siempre la unidad cúbica o de capacidad adecuada.",
                ],
                "questions": [question(*row, index=i) for i, row in enumerate(rows)],
            }
        for i in range(10):
            if grade == 1:
                if i < 5:
                    a, b = i + 2, 3; prompt=f"Tienes {a} manzanas y recibes {b} más. ¿Cuántas tienes?"; answer=a+b
                else:
                    a, b = i + 5, 2; prompt=f"Tienes {a} manzanas y regalas {b}. ¿Cuántas quedan?"; answer=a-b
                delta=1
            elif grade == 2:
                prices = [(500, 200), (700, 300), (900, 400), (1200, 500), (1500, 600)]
                price, paid = prices[i % len(prices)]
                prompt = f"Un cuaderno cuesta {price} pesos y pagas {paid + price}. ¿Cuánto recibes?"
                answer = paid
                delta = 100
            elif grade == 3:
                if i < 5:
                    groups, size = i + 3, 4
                    prompt = f"Hay {groups} bolsas con {size} naranjas cada una. ¿Cuántas naranjas hay?"
                    answer, delta = groups * size, 4
                else:
                    children = i - 1
                    total = children * 6
                    prompt = f"Repartes {total} galletas entre {children} niños por igual. ¿Cuántas recibe cada uno?"
                    answer, delta = 6, 1
            elif grade == 4:
                b=3+i; a=b*6; prompt=f"Repartes {a} galletas entre {b} niños por igual. ¿Cuántas recibe cada uno?"; answer=6; delta=1
            else:
                a=2000+i*500; prompt=f"Un cuaderno cuesta {a} pesos y tiene 10 % de descuento. ¿Cuántos pesos pagas?"; answer=a*9//10; delta=100
            questions.append(question(prompt,answer,answer+delta,answer-delta,i))
        lesson=[
            f"Grado {grade}.º · Problemas cotidianos",
            [
                "Juntar cantidades se representa con una suma: 2 manzanas y 3 más son 5.",
                "Cuando se venden objetos, quedan menos: si hay 30 panes y vendes 12, quedan 18.",
                "Los grupos iguales se calculan multiplicando: 3 bolsas de 4 naranjas son 12 naranjas.",
                "Repartir por igual se calcula dividiendo: 24 galletas entre 4 niños son 6 para cada uno.",
                "El 10 % es una décima parte: el 10 % de 2000 es 200. Con ese descuento pagas 2000 − 200 = 1800 pesos.",
            ][grade-1],
            "Separa los datos, elige la operación y comprueba si el resultado tiene sentido en la historia.",
        ]
        if grade == 1:
            lesson = [
                "Grado 1.º · La tienda de las cantidades",
                "Imagina que compras o compartes objetos. Primero cuenta lo que tienes y luego decide si debes juntar o quitar.",
                "Dibuja las manzanas, juguetes o galletas antes de elegir la operación.",
                "Explica la respuesta con una frase: «Tengo ___ porque junté o quité ___».",
            ]
        elif grade == 2:
            lesson = [
                "Grado 2.º · Compras y cambios",
                "Para calcular un cambio, resta el precio al dinero que entregas: pago − precio = cambio.",
                "Lee los precios, escribe los datos y comprueba que el cambio sea menor que el dinero entregado.",
                "Puedes representar las cantidades con monedas y billetes antes de calcular.",
            ]
        elif grade == 4:
            lesson = [
                "Grado 4.º · Problemas de varios pasos",
                "Lee la historia completa, ordena los pasos y decide qué operación corresponde a cada parte.",
                "Comprueba los resultados intermedios y revisa que la respuesta final conserve la unidad del problema.",
            ]
        return {
            "title": "La tienda de las cantidades" if grade == 1 else "Compras y cambios" if grade == 2 else "Multiplicamos y repartimos en el mercado" if grade == 3 else "Problemas cotidianos",
            "description": "Aplica las operaciones a compras, repartos y situaciones de la vida diaria.",
            "lesson": lesson,
            "questions": questions,
        }
    else:
        if grade == 2:
            rows = [
                ("Una cinta mide 45 cm y otra 1 m. ¿Cuál es más larga?", "la de 1 m", "la de 45 cm", "miden igual"),
                ("¿Cuántos centímetros son 2 metros?", "200 cm", "20 cm", "102 cm"),
                ("Una película empieza a las 2:00 y dura 1 hora. ¿A qué hora termina?", "3:00", "1:00", "2:30"),
                ("¿Cuánto es 300 pesos + 200 pesos?", "500 pesos", "400 pesos", "600 pesos"),
                ("Un libro mide 20 cm y una mesa 2 m. ¿Cuál es más larga?", "la mesa", "el libro", "miden igual"),
                ("¿Qué dura más: 60 minutos o 1 hora?", "duran igual", "60 minutos", "1 hora"),
                ("Tienes 3 monedas de 100 pesos. ¿Cuánto tienes?", "300 pesos", "100 pesos", "400 pesos"),
                ("Una cuerda de 90 cm se corta en 30 cm. ¿Cuánto queda?", "60 cm", "120 cm", "70 cm"),
                ("¿Qué unidad usamos para medir la longitud de un salón?", "metros", "centímetros", "minutos"),
                ("Si son las 5:00 y pasan 2 horas, ¿qué hora es?", "7:00", "6:00", "8:00"),
            ]
            return {
                "title": "Retos de medida y tiempo",
                "description": "Resuelve situaciones de longitud, tiempo y dinero con unidades conocidas.",
                "lesson": [
                    "Grado 2.º · Retos de medida y tiempo",
                    "Convierte metros a centímetros cuando sea necesario y compara siempre usando la misma unidad.",
                    "Para calcular una hora de llegada, avanza el tiempo paso a paso en un reloj.",
                    "Para sumar o restar dinero, conserva la unidad pesos y revisa si el resultado tiene sentido.",
                ],
                "questions": [question(*row, index=i) for i, row in enumerate(rows)],
            }
        if grade == 4:
            rows = [
                ("Un rectángulo mide 8 cm de largo y 5 cm de ancho. ¿Cuál es su área?", "40 cm²", "26 cm²", "13 cm²"),
                ("Un cuadrado tiene lados de 6 cm. ¿Cuál es su área?", "36 cm²", "24 cm²", "12 cm²"),
                ("¿Cuántos centímetros son 3,2 metros?", "320 cm", "32 cm", "302 cm"),
                ("¿Cuántos metros son 2,5 kilómetros?", "2500 m", "250 m", "25 m"),
                ("En formato de 24 horas, ¿qué hora es 16:45?", "4:45 p. m.", "6:45 p. m.", "4:45 a. m."),
                ("En formato de 24 horas, ¿qué hora es 23:10?", "11:10 p. m.", "1:10 p. m.", "11:10 a. m."),
                ("Una clase empieza a las 08:35 y termina a las 10:15. ¿Cuánto dura?", "1 h 40 min", "2 h 20 min", "1 h 30 min"),
                ("¿Cuántos centímetros cuadrados hay en 2 m²?", "20000 cm²", "200 cm²", "2000 cm²"),
                ("Un cuadrado de lado 9 cm tiene un perímetro de…", "36 cm", "81 cm", "18 cm"),
                ("¿Qué mide el área de una figura?", "la superficie interior", "el borde", "la duración"),
            ]
            return {
                "title": "Área, conversiones y tiempo",
                "description": "Calcula áreas y perímetros, convierte unidades y resuelve duraciones en formato de 24 horas.",
                "lesson": [
                    "El área mide la superficie interior. En un rectángulo se calcula con largo × ancho y se expresa en unidades cuadradas.",
                    "El perímetro mide el borde. Un cuadrado de lado 9 cm tiene perímetro 9 × 4 = 36 cm.",
                    "Convierte las unidades antes de operar: 1 m = 100 cm, 1 km = 1000 m y 1 m² = 10 000 cm².",
                    "Para calcular duraciones, avanza desde la hora inicial hasta la final. El formato de 24 horas evita confundir la mañana con la tarde.",
                ],
                "questions": [question(*row, index=i) for i, row in enumerate(rows)],
            }
        for i in range(10):
            a=i+3
            if grade==1:
                rows = [
                    ("Una cinta mide 3 cm y otra 5 cm. ¿Cuál es más larga?", "la de 5 cm", "la de 3 cm", "son iguales"),
                    ("¿Qué objeto puedes medir con una regla?", "un lápiz", "una canción", "un olor"),
                    ("¿Qué es más corto?", "una hormiga", "una mesa", "una puerta"),
                    ("¿Qué unidad usamos para medir una mesa?", "centímetros", "litros", "días"),
                    ("¿Qué dura más tiempo?", "una hora", "un minuto", "un segundo"),
                    ("¿Qué hacemos primero por la mañana?", "despertarnos", "cenar", "dormir después de cenar"),
                    ("¿Qué recipiente puede contener más agua?", "una jarra", "una taza pequeña", "una cuchara"),
                    ("¿Qué objeto pesa menos?", "una pluma", "una mochila llena", "una silla"),
                    ("Si una cuerda mide 4 cm y otra 2 cm, ¿cuál es la diferencia?", "2 cm", "6 cm", "1 cm"),
                    ("¿Qué herramienta ayuda a medir una longitud?", "una regla", "un reloj", "un calendario"),
                ]
                prompt, answer, wrong1, wrong2 = rows[i]
                wrong = [wrong1, wrong2]
            elif grade==2: prompt=f"Caminas {a} metros y después 2 metros más. ¿Cuántos metros recorres?"; answer=a+2; wrong=[a,a-2]
            elif grade==3:
                rows = [
                    ("¿Cuántos gramos hay en 3 kilogramos?", "3000 g", "300 g", "30 g"),
                    ("¿Cuántos gramos hay en 5 kilogramos?", "5000 g", "500 g", "50 g"),
                    ("¿Cuántos mililitros hay en 2 litros?", "2000 ml", "200 ml", "20 ml"),
                    ("Un cuadrado tiene lados de 6 cm. ¿Cuál es su perímetro?", "24 cm", "12 cm", "36 cm"),
                    ("Un rectángulo mide 8 cm por 3 cm. ¿Cuál es su perímetro?", "22 cm", "24 cm", "11 cm"),
                    ("¿Qué unidad conviene para pesar una sandía?", "kilogramos", "gramos", "litros"),
                    ("¿Qué unidad conviene para medir la leche de una botella?", "litros", "kilogramos", "gramos"),
                    ("¿Cuánto mide un ángulo recto?", "90°", "45°", "180°"),
                    ("¿Cuántos centímetros hay en 4 metros?", "400 cm", "40 cm", "4000 cm"),
                    ("¿Qué mide el perímetro?", "el borde de una figura", "su superficie interior", "su peso"),
                ]
                prompt, answer, wrong1, wrong2 = rows[i]
                wrong = [wrong1, wrong2]
            elif grade==4: prompt=f"Un cuadrado tiene lados de {a} cm. ¿Cuál es su perímetro en cm?"; answer=a*4; wrong=[a*2,a*4+4]
            else: prompt=f"Un rectángulo mide {a} cm de largo y 4 cm de ancho. ¿Cuál es su área en cm²?"; answer=a*4; wrong=[a*4+1,a+4]
            questions.append(question(prompt,answer,*wrong,i))
        lesson=[
            f"Grado {grade}.º · Medimos el mundo",
            [
                "Si medimos con la misma unidad, el número mayor indica una longitud mayor: 5 cm es más largo que 3 cm.",
                "Para juntar recorridos en metros, suma sus medidas: 3 m + 2 m = 5 m.",
                "Un metro equivale a 100 centímetros. Para pasar metros a centímetros, multiplica por 100: 4 m = 400 cm.",
                "El perímetro es la suma de los lados. Un cuadrado de lado 3 cm tiene perímetro 3 + 3 + 3 + 3 = 12 cm.",
                "El kilogramo y el gramo miden masa; el litro y el mililitro miden capacidad. Elige la unidad según lo que estés midiendo.",
            ][grade-1],
            "Dibuja la situación y escribe siempre la unidad. Puedes practicar midiendo objetos con una regla.",
        ]
        if grade == 1:
            lesson = [
                "Grado 1.º · Medimos nuestro mundo",
                "Compara objetos usando palabras como largo, corto, alto, bajo, pesado y liviano.",
                "Mide con una regla, cuenta unidades y observa que una medida necesita un número y una unidad.",
                "Ordena objetos de menor a mayor y explica cómo decidiste.",
            ]
        return {
            "title": "Medimos nuestro mundo" if grade == 1 else "Perímetro, ángulos y medidas" if grade == 3 else "Medimos el mundo",
            "description": "Compara longitudes, tiempos, capacidades y pesos usando unidades sencillas.",
            "lesson": lesson,
            "questions": questions,
        }
    if unit == "patterns":
        return {
            "title": "Patrones numéricos",
            "description": "Descubre la regla de una secuencia y predice qué número sigue.",
            "lesson": lesson,
            "questions": questions,
        }
    raise ValueError(f"Unidad curricular desconocida: {unit}")
