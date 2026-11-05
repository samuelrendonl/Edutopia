"""Catálogo y reglas de los juegos. No depende de Flask ni de MySQL."""
from decimal import Decimal

GAMES = [
    dict(key="math-balloons", subject="Matemáticas", game="balloons", title="Globos matemáticos", description="Atrapa el globo con la respuesta correcta. Puedes pausar el movimiento.", icon="sparkles", color="#5254c7"),
    dict(key="math-race", subject="Matemáticas", game="race", title="Misión cohete", description="Resuelve cálculos y lleva tu cohete hasta las estrellas.", icon="rocket", color="#247ba6"),
    dict(key="language-balloons", subject="Lengua Castellana", game="word-balloons", title="Burbujas de palabras", description="Atrapa palabras siguiendo pistas de sonidos, vocabulario y significado.", icon="book", color="#a84474"),
    dict(key="word-detective", subject="Lengua Castellana", game="detective", title="Detectives de palabras", description="Abre expedientes y encuentra la pista que resuelve cada caso.", icon="sparkles", color="#157965"),
    dict(key="science-lab", subject="Ciencias Naturales", game="science-lab", curriculum="science-life", title="Laboratorio de ciencias", description="Observa seres vivos y resuelve retos del laboratorio.", icon="sparkles", color="#21a889"),
    dict(key="social-explorer", subject="Sociales", game="social-explorer", curriculum="social-geography", title="Expedición social", description="Interpreta mapas, comunidades y pistas del territorio.", icon="globe", color="#e66a9b"),
    dict(key="word-quest", subject="Inglés", game="word-quest", curriculum="english-identity", title="Word Quest", description="Resuelve pistas y demuestra cuánto inglés puedes usar.", icon="rainbow", color="#3ba9dd"),
]
for game in GAMES:
    game.update(kind="Juego", points=100, minutes=6, lesson=[], questions=[])


def game_questions(game, grade):
    # Importación diferida: el catálogo escolar también incorpora GAMES.
    from app.extra_content import curriculum_for_grade, question
    if game.get("curriculum"):
        return curriculum_for_grade(game["curriculum"], grade)["questions"]
    if game["subject"] == "Lengua Castellana":
        unit = "vocabulary" if game["game"] == "word-balloons" else "grammar"
        return curriculum_for_grade(unit, grade)["questions"]
    if grade == 1 and game["key"] == "math-balloons":
        # Progresión corta: primero reconoce cantidades pequeñas y luego
        # amplía el conteo hasta 20.
        counts = [1, 2, 3, 4, 5, 6, 8, 10, 15, 20]
        return [
            question(
                f"Hay {count} globos. ¿Cuántos globos debes contar?",
                count,
                count - 1 if count else 1,
                count + 1,
                index=i,
            )
            for i, count in enumerate(counts)
        ]
    if grade == 1 and game["key"] == "math-race":
        pairs = [(1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 3), (4, 4), (5, 4), (5, 5)]
        return [
            question(
                f"{first} + {second} = ¿cuánto?",
                first + second,
                first + second - 1,
                first + second + 1,
                index=i,
            )
            for i, (first, second) in enumerate(pairs)
        ]
    if grade == 2 and game["key"] == "math-balloons":
        rows = [
            ("27 + 18 = ¿cuánto?", 45, 35, 55),
            ("36 + 27 = ¿cuánto?", 63, 53, 73),
            ("48 + 25 = ¿cuánto?", 73, 63, 83),
            ("59 + 16 = ¿cuánto?", 75, 65, 85),
            ("67 + 18 = ¿cuánto?", 85, 75, 95),
            ("42 − 18 = ¿cuánto?", 24, 34, 14),
            ("53 − 27 = ¿cuánto?", 26, 36, 16),
            ("71 − 36 = ¿cuánto?", 35, 45, 25),
            ("84 − 29 = ¿cuánto?", 55, 65, 45),
            ("90 − 47 = ¿cuánto?", 43, 53, 33),
        ]
        return [question(prompt, answer, wrong1, wrong2, i) for i, (prompt, answer, wrong1, wrong2) in enumerate(rows)]
    if grade == 2 and game["key"] == "math-race":
        groups = [(2, 3), (3, 2), (4, 2), (5, 2), (2, 5), (3, 4), (4, 3), (5, 3), (2, 6), (10, 2)]
        return [
            question(
                f"{groups_count} grupos de {size}: {size} + " + " + ".join([str(size)] * (groups_count - 1)) + " = ¿cuánto?",
                groups_count * size,
                groups_count * size - 1,
                groups_count * size + 1,
                i,
            )
            for i, (groups_count, size) in enumerate(groups)
        ]
    if grade == 3 and game["key"] == "math-balloons":
        rows = [
            ("3 × 4 = ¿cuánto?", 12, 10, 14),
            ("5 × 6 = ¿cuánto?", 30, 25, 36),
            ("2 × 9 = ¿cuánto?", 18, 16, 20),
            ("4 × 7 = ¿cuánto?", 28, 24, 32),
            ("10 × 8 = ¿cuánto?", 80, 70, 90),
            ("24 ÷ 3 = ¿cuánto?", 8, 6, 9),
            ("40 ÷ 5 = ¿cuánto?", 8, 5, 10),
            ("36 ÷ 4 = ¿cuánto?", 9, 8, 12),
            ("50 ÷ 10 = ¿cuánto?", 5, 4, 6),
            ("45 ÷ 5 = ¿cuánto?", 9, 5, 10),
        ]
        return [question(prompt, answer, wrong1, wrong2, i) for i, (prompt, answer, wrong1, wrong2) in enumerate(rows)]
    if grade == 3 and game["key"] == "math-race":
        rows = [
            ("Una pizza se divide en 2 partes iguales. ¿Qué fracción es una parte?", "1/2", "1/3", "2/1"),
            ("Una barra se divide en 3 partes iguales. ¿Qué fracción es una parte?", "1/3", "1/2", "3/1"),
            ("Una torta se divide en 4 partes iguales. ¿Qué fracción es una parte?", "1/4", "1/5", "4/1"),
            ("Una tira se divide en 5 partes iguales. ¿Qué fracción es una parte?", "1/5", "1/4", "5/1"),
            ("Una figura se divide en 6 partes iguales. ¿Qué fracción es una parte?", "1/6", "1/3", "6/1"),
            ("Una tableta se divide en 8 partes iguales. ¿Qué fracción es una parte?", "1/8", "1/4", "8/1"),
            ("¿Cuál es mayor: 1/3 o 1/7?", "1/3", "1/7", "1/10"),
            ("¿Cuál es menor: 1/5 o 1/2?", "1/5", "1/2", "1/3"),
            ("¿Qué fracción unitaria representa una de 10 partes?", "1/10", "10/1", "1/2"),
            ("Una pizza tiene 4 partes iguales y tomas una. ¿Qué fracción tomaste?", "1/4", "2/4", "4/1"),
        ]
        return [question(prompt, answer, wrong1, wrong2, i) for i, (prompt, answer, wrong1, wrong2) in enumerate(rows)]
    if grade == 4 and game["key"] == "math-balloons":
        rows = [
            ("2,5 + 1,2 = ¿cuánto?", "3,7", "3,5", "3,8"),
            ("4,8 − 2,3 = ¿cuánto?", "2,5", "2,3", "2,6"),
            ("1,25 + 2,40 = ¿cuánto?", "3,65", "3,55", "3,75"),
            ("5,00 − 1,75 = ¿cuánto?", "3,25", "3,35", "4,25"),
            ("0,6 + 0,35 = ¿cuánto?", "0,95", "0,85", "1,05"),
            ("7,2 − 3,45 = ¿cuánto?", "3,75", "3,65", "4,25"),
            ("12,50 + 0,75 = ¿cuánto?", "13,25", "13,15", "12,75"),
            ("9,00 − 4,68 = ¿cuánto?", "4,32", "4,42", "5,32"),
            ("3,14 + 2,06 = ¿cuánto?", "5,20", "5,10", "4,20"),
            ("10,00 − 6,25 = ¿cuánto?", "3,75", "3,85", "4,25"),
        ]
        return [question(prompt, answer, wrong1, wrong2, i) for i, (prompt, answer, wrong1, wrong2) in enumerate(rows)]
    if grade == 4 and game["key"] == "math-race":
        rows = [
            ("Compras 3 cuadernos de 4 pesos y pagas con 20. ¿Cuánto recibes?", "8", "12", "16"),
            ("Hay 4 cajas con 6 lápices y se usan 5. ¿Cuántos quedan?", "19", "24", "17"),
            ("Repartes 48 fichas entre 6 equipos y cada equipo recibe 2 más. ¿Cuántas recibe cada uno?", "10", "8", "12"),
            ("Una biblioteca tiene 5 estantes con 12 libros y presta 15. ¿Cuántos quedan?", "45", "60", "40"),
            ("Compras 2 paquetes de 15 tarjetas y regalas 8. ¿Cuántas quedan?", "22", "30", "20"),
            ("Se reparten 72 semillas entre 8 niños y cada uno planta 3. ¿Cuántas conserva cada uno?", "6", "9", "5"),
            ("Hay 6 bolsas de 9 canicas y se pierden 7. ¿Cuántas quedan?", "47", "54", "45"),
            ("Una granja recoge 4 canastas de 18 huevos y vende 20. ¿Cuántos quedan?", "52", "72", "48"),
            ("Repartes 96 pegatinas entre 12 niños y cada uno recibe 1 extra. ¿Cuántas recibe cada uno?", "9", "8", "10"),
            ("Compras 7 cajas de 11 colores y entregas 14. ¿Cuántos quedan?", "63", "77", "53"),
        ]
        return [question(prompt, answer, wrong1, wrong2, i) for i, (prompt, answer, wrong1, wrong2) in enumerate(rows)]
    if grade == 5 and game["key"] == "math-balloons":
        rows = [
            ("¿Cuál es el 10 % de 300?", "30", "3", "300"),
            ("¿Cuál es el 25 % de 80?", "20", "15", "25"),
            ("¿Cuál es el 50 % de 240?", "120", "100", "140"),
            ("Si 4 cuadernos cuestan 12 pesos, ¿cuánto cuestan 6?", "18 pesos", "16 pesos", "24 pesos"),
            ("¿Cuál es el 20 % de 150?", "30", "20", "35"),
            ("Una receta para 2 personas usa 3 huevos. ¿Cuántos usa para 6?", "9 huevos", "6 huevos", "12 huevos"),
            ("¿Cuál es el 75 % de 40?", "30", "25", "35"),
            ("Si 5 entradas cuestan 250 pesos, ¿cuánto cuestan 8?", "400 pesos", "300 pesos", "450 pesos"),
            ("¿Cuál es el 30 % de 90?", "27", "21", "30"),
            ("Si 3 metros representan 12 km, ¿cuántos km representan 5 metros?", "20 km", "15 km", "24 km"),
        ]
        return [question(prompt, answer, wrong1, wrong2, i) for i, (prompt, answer, wrong1, wrong2) in enumerate(rows)]
    if grade == 5 and game["key"] == "math-race":
        rows = [
            ("x + 7 = 15. ¿Cuánto vale x?", "8", "7", "22"),
            ("x − 9 = 6. ¿Cuánto vale x?", "15", "3", "54"),
            ("3 × x = 21. ¿Cuánto vale x?", "7", "18", "24"),
            ("x ÷ 4 = 6. ¿Cuánto vale x?", "24", "10", "2"),
            ("2 × x + 3 = 11. ¿Cuánto vale x?", "4", "5", "7"),
            ("x + 12 = 30. ¿Cuánto vale x?", "18", "42", "2"),
            ("5 × x = 45. ¿Cuánto vale x?", "9", "8", "40"),
            ("x ÷ 3 = 8. ¿Cuánto vale x?", "24", "11", "5"),
            ("4 × x − 2 = 18. ¿Cuánto vale x?", "5", "4", "8"),
            ("x − 15 = 25. ¿Cuánto vale x?", "40", "10", "375"),
        ]
        return [question(prompt, answer, wrong1, wrong2, i) for i, (prompt, answer, wrong1, wrong2) in enumerate(rows)]
    rows=[]
    for i in range(10):
        if grade==1:
            a,b=2+i,1+i%4; op="+" if i%2==0 else "−"; answer=a+b if op=="+" else a-b
        elif grade==2:
            a,b=25+i*3,8+i; op="+" if i%2==0 else "−"; answer=a+b if op=="+" else a-b
        elif grade==3:
            a,b=3+i,2+i%5; op="×"; answer=a*b
        elif grade==4:
            b=2+i%7; answer=3+i; a=b*answer; op="÷"
        else:
            a,b=Decimal(125+i*25)/100,Decimal(50+i*5)/100; op="+" if i%2==0 else "−"; answer=a+b if op=="+" else a-b
        display=lambda n: str(n).replace('.', ',')
        delta=Decimal('0.1') if grade==5 else 1
        rows.append(question(f"{display(a)} {op} {display(b)} = ?", display(answer), display(answer+delta), display(answer-delta), i))
    return rows


def evaluate_game(activity, answers):
    return sum(answer == q["answer"] for answer,q in zip(answers,activity["questions"]))
