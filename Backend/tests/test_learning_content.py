import unittest
from decimal import Decimal
from fractions import Fraction

from app.learning_content import ACTIVITIES, activity_for_grade, public_activity
from app.subject_units import SUBJECTS


class LearningContentTests(unittest.TestCase):
    def test_catalog_has_learning_activities_and_games(self):
        self.assertGreaterEqual(len(ACTIVITIES), 16)
        self.assertGreaterEqual(sum(item["kind"] == "Aprendizaje" for item in ACTIVITIES), 12)
        self.assertGreaterEqual(sum(item["kind"] == "Juego" for item in ACTIVITIES), 4)

    def test_first_grade_math_covers_the_planned_units_and_games(self):
        math = {item["key"]: item for item in ACTIVITIES if item["subject"] == "Matemáticas"}
        planned = {
            "math-counting", "math-sums", "math-fractions-geometry", "math-laboratory",
            "math-balloons", "math-race",
        }
        self.assertTrue(planned.issubset(math))
        for key in planned:
            with self.subTest(activity=key):
                activity = activity_for_grade(math[key], 1)
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")

        self.assertIn("Conteo y cardinalidad", " ".join(activity_for_grade(math["math-counting"], 1)["lesson"]))
        self.assertIn("Formas, cuerpos y posiciones", " ".join(activity_for_grade(math["math-fractions-geometry"], 1)["lesson"]))
        self.assertIn("Patrones y pictogramas", " ".join(activity_for_grade(math["math-laboratory"], 1)["lesson"]))
        self.assertTrue(all("+" in question["prompt"] for question in activity_for_grade(math["math-race"], 1)["questions"]))

    def test_first_grade_math_has_a_progressive_learning_path(self):
        math = {item["key"]: item for item in ACTIVITIES if item["subject"] == "Matemáticas"}
        expected_order = [
            "math-counting", "math-sums", "math-fractions-geometry", "math-laboratory",
            "math-market", "math-measures", "math-balloons", "math-race",
        ]
        actual = sorted(
            (activity_for_grade(math[key], 1) for key in expected_order),
            key=lambda item: item["learning_order"],
        )
        self.assertEqual([item["key"] for item in actual], expected_order)
        self.assertEqual(actual[0]["prerequisites"], [])
        self.assertIn("math-counting", actual[1]["prerequisites"])
        self.assertEqual(actual[-1]["related_activity"], "math-sums")
        for item in actual:
            self.assertTrue(all(isinstance(line, str) for line in item["lesson"]))
            self.assertTrue(item["objective"])

    def test_second_grade_math_matches_the_planned_curriculum(self):
        math = {item["key"]: item for item in ACTIVITIES if item["subject"] == "Matemáticas"}
        expected_order = [
            "math-counting", "math-sums", "math-fractions-geometry", "math-laboratory",
            "math-market", "math-measures", "math-balloons", "math-race",
        ]
        activities = [activity_for_grade(math[key], 2) for key in expected_order]
        ordered = sorted(activities, key=lambda item: item["learning_order"])

        self.assertEqual([item["key"] for item in ordered], expected_order)
        self.assertIn("decenas", " ".join(activities[0]["lesson"]).lower())
        self.assertIn("reagrupar", " ".join(activities[1]["lesson"]).lower())
        self.assertIn("centímetros", " ".join(activities[2]["lesson"]).lower())
        self.assertIn("gráficas", " ".join(activities[3]["lesson"]).lower())
        self.assertEqual(activities[-1]["related_activity"], "math-sums")
        for item in activities:
            with self.subTest(activity=item["key"]):
                self.assertEqual(len(item["questions"]), 10)
                self.assertTrue(item["objective"])
                self.assertTrue(all(isinstance(line, str) for line in item["lesson"]))

    def test_second_grade_math_games_follow_the_planned_progression(self):
        math = {item["key"]: item for item in ACTIVITIES if item["subject"] == "Matemáticas"}
        balloons = activity_for_grade(math["math-balloons"], 2)["questions"]
        race = activity_for_grade(math["math-race"], 2)["questions"]

        self.assertTrue(any("+" in item["prompt"] for item in balloons))
        self.assertTrue(any("−" in item["prompt"] for item in balloons))
        self.assertTrue(all("grupos" in item["prompt"] for item in race))

    def test_second_grade_language_matches_the_planned_curriculum(self):
        language = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Lengua Castellana"
        }

        reading = activity_for_grade(language["reading-story"], 2)
        writing = activity_for_grade(language["language-write-create"], 2)
        spelling = activity_for_grade(language["words-syllables"], 2)
        grammar = activity_for_grade(language["language-grammar"], 2)
        literature = activity_for_grade(language["language-adventure"], 2)
        vocabulary = activity_for_grade(language["language-vocabulary"], 2)

        self.assertIn("fluidez", reading["description"])
        self.assertIn("literal", reading["objective"])
        self.assertIn("párrafo narrativo", writing["title"].lower())
        self.assertIn("conectores", " ".join(writing["lesson"]).lower())
        self.assertIn("agudas", spelling["title"].lower())
        self.assertIn("artículos", grammar["title"].lower())
        self.assertIn("fábulas", literature["title"].lower())
        self.assertIn("sinónimos", vocabulary["title"].lower())

        for key, activity in {
            "reading": reading,
            "writing": writing,
            "spelling": spelling,
            "grammar": grammar,
            "literature": literature,
            "vocabulary": vocabulary,
        }.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"])
                self.assertTrue(all("answer" in question for question in activity["questions"]))

        balloons = activity_for_grade(language["language-balloons"], 2)
        detective = activity_for_grade(language["word-detective"], 2)
        self.assertEqual(len(balloons["questions"]), 10)
        self.assertEqual(len(detective["questions"]), 10)

    def test_third_grade_language_matches_the_planned_curriculum(self):
        language = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Lengua Castellana"
        }
        activities = {
            key: activity_for_grade(language[key], 3)
            for key in language
        }

        self.assertIn("infer", activities["reading-story"]["title"].lower())
        self.assertIn("idea principal", activities["reading-story"]["description"].lower())
        self.assertIn("Inés", public_activity(language["reading-story"], 3)["passage"])
        self.assertIn("tres párrafos", activities["language-write-create"]["title"].lower())
        self.assertIn("diálogo", " ".join(activities["language-write-create"]["lesson"]).lower())
        self.assertIn("sujeto", activities["language-grammar"]["title"].lower())
        self.assertIn("prefijo", " ".join(activities["language-grammar"]["lesson"]).lower())
        self.assertIn("mitos", activities["language-adventure"]["title"].lower())
        self.assertIn("familias léxicas", activities["language-vocabulary"]["title"].lower())

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "reading-story", "language-write-create", "language-grammar",
                "language-adventure", "language-vocabulary", "words-syllables",
                "language-balloons", "word-detective",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_fourth_grade_language_matches_the_planned_curriculum(self):
        language = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Lengua Castellana"
        }
        activities = {
            key: activity_for_grade(language[key], 4)
            for key in language
        }

        self.assertIn("personajes", activities["reading-story"]["title"].lower())
        self.assertIn("ambiente", activities["reading-story"]["description"].lower())
        self.assertIn("Amalia", public_activity(language["reading-story"], 4)["passage"])
        self.assertIn("expositivos", activities["language-write-create"]["title"].lower())
        self.assertIn("síntesis", " ".join(activities["language-write-create"]["lesson"]).lower())
        self.assertIn("compuestas", activities["words-syllables"]["title"].lower())
        self.assertIn("puntuación", " ".join(activities["words-syllables"]["lesson"]).lower())
        self.assertIn("géneros", activities["language-adventure"]["title"].lower())
        self.assertIn("polisemia", activities["language-vocabulary"]["title"].lower())
        self.assertIn("cohesión", activities["language-grammar"]["title"].lower())

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "reading-story", "language-write-create", "words-syllables",
                "language-adventure", "language-vocabulary", "language-grammar",
                "language-balloons", "word-detective",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_fifth_grade_language_matches_the_planned_curriculum(self):
        language = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Lengua Castellana"
        }
        activities = {
            key: activity_for_grade(language[key], 5)
            for key in language
        }

        self.assertIn("sesgos", activities["reading-story"]["title"].lower())
        self.assertIn("fuentes", " ".join(activities["reading-story"]["lesson"]).lower())
        self.assertIn("humedal", public_activity(language["reading-story"], 5)["passage"])
        self.assertIn("argumentativo", activities["language-write-create"]["title"].lower())
        self.assertIn("citas", " ".join(activities["language-write-create"]["lesson"]).lower())
        self.assertIn("morfología", activities["words-syllables"]["title"].lower())
        self.assertIn("subordinada", " ".join(activities["words-syllables"]["lesson"]).lower())
        self.assertIn("literatura universal", activities["language-adventure"]["title"].lower())
        self.assertIn("figurad", activities["language-vocabulary"]["title"].lower())
        self.assertIn("cohesión", activities["language-grammar"]["title"].lower())

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "reading-story", "language-write-create", "words-syllables",
                "language-adventure", "language-vocabulary", "language-grammar",
                "language-balloons", "word-detective",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_first_grade_social_matches_the_planned_curriculum(self):
        social = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Sociales"
        }
        activities = {
            key: activity_for_grade(social[key], 1)
            for key in social
        }

        self.assertIn("familia", activities["social-identity"]["title"].lower())
        self.assertIn("reglas", " ".join(activities["social-identity"]["lesson"]).lower())
        self.assertEqual(activities["social-identity"]["project"], "Árbol genealógico familiar")
        self.assertIn("barrio", activities["social-geography"]["title"].lower())
        self.assertIn("mapa", " ".join(activities["social-geography"]["lesson"]).lower())
        self.assertIn("línea de vida", activities["social-history"]["title"].lower())
        self.assertIn("necesidades", activities["social-economy"]["title"].lower())
        self.assertIn("Mapa del tesoro", activities["social-explorer"]["title"])

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "social-identity", "social-geography", "social-history",
                "social-economy", "social-culture", "social-media",
                "social-explorer",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_second_grade_social_matches_the_planned_curriculum(self):
        social = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Sociales"
        }
        activities = {
            key: activity_for_grade(social[key], 2)
            for key in social
        }

        self.assertIn("comunidad", activities["social-identity"]["title"].lower())
        self.assertIn("diversidad", " ".join(activities["social-identity"]["lesson"]).lower())
        self.assertIn("municipio", activities["social-geography"]["title"].lower())
        self.assertIn("leyenda", " ".join(activities["social-geography"]["lesson"]).lower())
        self.assertIn("historia local", " ".join(activities["social-history"]["lesson"]).lower())
        self.assertEqual(activities["social-history"]["project"], "Entrevista a un abuelo o vecino")
        self.assertIn("bienes", activities["social-economy"]["title"].lower())
        self.assertIn("Ruta comunitaria", activities["social-explorer"]["title"])

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "social-identity", "social-geography", "social-history",
                "social-economy", "social-culture", "social-media",
                "social-explorer",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_third_grade_social_matches_the_planned_curriculum(self):
        social = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Sociales"
        }
        activities = {
            key: activity_for_grade(social[key], 3)
            for key in social
        }

        self.assertIn("derechos", activities["social-identity"]["title"].lower())
        self.assertIn("democracia", " ".join(activities["social-identity"]["lesson"]).lower())
        self.assertIn("región", activities["social-geography"]["title"].lower())
        self.assertEqual(activities["social-geography"]["project"], "Mapa temático de la región")
        self.assertIn("línea de tiempo", activities["social-history"]["title"].lower())
        self.assertIn("fuentes", " ".join(activities["social-history"]["lesson"]).lower())
        self.assertIn("sectores", activities["social-economy"]["title"].lower())
        self.assertIn("presupuesto", activities["social-explorer"]["title"].lower())

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "social-identity", "social-geography", "social-history",
                "social-economy", "social-culture", "social-media",
                "social-explorer",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_fourth_grade_social_matches_the_planned_curriculum(self):
        social = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Sociales"
        }
        activities = {
            key: activity_for_grade(social[key], 4)
            for key in social
        }

        self.assertIn("ciudadanía", activities["social-identity"]["title"].lower())
        self.assertIn("constitución", " ".join(activities["social-identity"]["lesson"]).lower())
        self.assertIn("relieve", activities["social-geography"]["title"].lower())
        self.assertEqual(activities["social-geography"]["project"], "Mapa temático de una región del país")
        self.assertIn("historia nacional", activities["social-history"]["title"].lower())
        self.assertEqual(activities["social-history"]["project"], "Investiga un personaje histórico")
        self.assertIn("presupuesto", activities["social-economy"]["title"].lower())
        self.assertIn("comercio internacional", activities["social-explorer"]["title"].lower())

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "social-identity", "social-geography", "social-history",
                "social-economy", "social-culture", "social-media",
                "social-explorer",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_fifth_grade_social_matches_the_planned_curriculum(self):
        social = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Sociales"
        }
        activities = {
            key: activity_for_grade(social[key], 5)
            for key in social
        }

        self.assertIn("ciudadanía global", activities["social-identity"]["title"].lower())
        self.assertIn("derechos humanos", " ".join(activities["social-identity"]["lesson"]).lower())
        self.assertIn("husos horarios", activities["social-geography"]["title"].lower())
        self.assertIn("globalización", " ".join(activities["social-geography"]["lesson"]).lower())
        self.assertIn("civilizaciones", activities["social-history"]["title"].lower())
        self.assertIn("revoluciones", " ".join(activities["social-history"]["lesson"]).lower())
        self.assertIn("desigualdad", activities["social-economy"]["title"].lower())
        self.assertEqual(activities["social-economy"]["project"], "Proyecto ODS local")
        self.assertIn("Modelo ONU", activities["social-explorer"]["title"])

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "social-identity", "social-geography", "social-history",
                "social-economy", "social-culture", "social-media",
                "social-explorer",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_first_grade_science_matches_the_planned_curriculum(self):
        science = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Ciencias Naturales"
        }
        activities = {
            key: activity_for_grade(science[key], 1)
            for key in science
        }

        self.assertIn("cuerpo", activities["science-life"]["title"].lower())
        self.assertIn("sentidos", " ".join(activities["science-life"]["lesson"]).lower())
        self.assertIn("materiales", activities["science-matter"]["title"].lower())
        self.assertIn("propiedades", " ".join(activities["science-matter"]["lesson"]).lower())
        self.assertIn("día", activities["science-earth"]["title"].lower())
        self.assertEqual(activities["science-earth"]["project"], "Diario del tiempo durante una semana")
        self.assertIn("seguridad", activities["science-technology"]["title"].lower())
        self.assertIn("Clasifica", activities["science-lab"]["title"])

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "science-life", "science-matter", "science-earth",
                "science-technology", "science-health", "science-living",
                "science-lab",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_first_grade_english_matches_the_planned_curriculum(self):
        english = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Inglés"
        }
        activities = {
            key: activity_for_grade(english[key], 1)
            for key in english
        }

        self.assertIn("hello", activities["english-identity"]["title"].lower())
        self.assertIn("saludos", " ".join(activities["english-identity"]["lesson"]).lower())
        self.assertEqual(
            activities["english-identity"]["oral_challenge"],
            "This is me: say hello, your name and your age.",
        )
        self.assertIn("school", activities["english-community"]["title"].lower())
        self.assertIn("animals", activities["english-world"]["title"].lower())
        self.assertIn("songs", activities["english-culture"]["title"].lower())
        self.assertIn("Memory", activities["word-quest"]["title"])

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "english-identity", "english-community", "english-world",
                "english-culture", "english-food", "english-nature", "word-quest",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_second_grade_english_matches_the_planned_curriculum(self):
        english = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Inglés"
        }
        activities = {
            key: activity_for_grade(english[key], 2)
            for key in english
        }

        self.assertIn("family", activities["english-identity"]["title"].lower())
        self.assertIn("home", " ".join(activities["english-identity"]["lesson"]).lower())
        self.assertEqual(
            activities["english-identity"]["oral_challenge"],
            "Describe your family or home with three short sentences.",
        )
        self.assertIn("town", activities["english-community"]["title"].lower())
        self.assertIn("routines", activities["english-community"]["title"].lower())
        self.assertIn("goldilocks", activities["english-world"]["title"].lower())
        self.assertIn("food", activities["english-culture"]["title"].lower())
        self.assertIn("Sentence builder", activities["word-quest"]["title"])

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "english-identity", "english-community", "english-world",
                "english-culture", "english-food", "english-nature", "word-quest",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_third_grade_english_matches_the_planned_curriculum(self):
        english = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Inglés"
        }
        activities = {
            key: activity_for_grade(english[key], 3)
            for key in english
        }

        self.assertIn("routine", activities["english-identity"]["title"].lower())
        self.assertIn("time", activities["english-identity"]["title"].lower())
        self.assertEqual(
            activities["english-identity"]["oral_challenge"],
            "Tell a short story in English for 30 seconds.",
        )
        self.assertIn("hobbies", activities["english-community"]["title"].lower())
        self.assertIn("myths", activities["english-world"]["title"].lower())
        self.assertIn("pen-pal", activities["english-culture"]["title"].lower())
        self.assertIn("Quiz show", activities["word-quest"]["title"])

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "english-identity", "english-community", "english-world",
                "english-culture", "english-food", "english-nature", "word-quest",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_fourth_grade_english_matches_the_planned_curriculum(self):
        english = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Inglés"
        }
        activities = {
            key: activity_for_grade(english[key], 4)
            for key in english
        }

        self.assertIn("opinions", activities["english-identity"]["title"].lower())
        self.assertEqual(
            activities["english-identity"]["oral_challenge"],
            "My hero: give a one-minute presentation.",
        )
        self.assertIn("health", activities["english-community"]["title"].lower())
        self.assertIn("future", activities["english-world"]["title"].lower())
        self.assertIn("culture project", activities["english-culture"]["title"].lower())
        self.assertIn("role-play", activities["word-quest"]["title"].lower())

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "english-identity", "english-community", "english-world",
                "english-culture", "english-food", "english-nature", "word-quest",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_fifth_grade_english_matches_the_planned_curriculum(self):
        english = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Inglés"
        }
        activities = {
            key: activity_for_grade(english[key], 5)
            for key in english
        }

        self.assertIn("environment", activities["english-identity"]["title"].lower())
        self.assertEqual(
            activities["english-identity"]["oral_challenge"],
            "Debate: Should we protect the planet?",
        )
        self.assertIn("news", activities["english-community"]["title"].lower())
        self.assertIn("travel", activities["english-world"]["title"].lower())
        self.assertIn("careers", activities["english-culture"]["title"].lower())
        self.assertIn("escape room", activities["word-quest"]["title"].lower())

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "english-identity", "english-community", "english-world",
                "english-culture", "english-food", "english-nature", "word-quest",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_second_grade_science_matches_the_planned_curriculum(self):
        science = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Ciencias Naturales"
        }
        activities = {
            key: activity_for_grade(science[key], 2)
            for key in science
        }

        self.assertIn("ciclos", activities["science-life"]["title"].lower())
        self.assertIn("germinar", " ".join(activities["science-life"]["lesson"]).lower())
        self.assertIn("agua", activities["science-matter"]["title"].lower())
        self.assertIn("sombras", " ".join(activities["science-matter"]["lesson"]).lower())
        self.assertIn("reciclaje", activities["science-earth"]["title"].lower())
        self.assertEqual(activities["science-earth"]["project"], "Siembra y observa un frijol")
        self.assertIn("reutilizadas", activities["science-technology"]["title"].lower())
        self.assertIn("Ciclo de vida", activities["science-lab"]["title"])

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "science-life", "science-matter", "science-earth",
                "science-technology", "science-health", "science-living",
                "science-lab",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_third_grade_science_matches_the_planned_curriculum(self):
        science = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Ciencias Naturales"
        }
        activities = {
            key: activity_for_grade(science[key], 3)
            for key in science
        }

        self.assertIn("plantas", activities["science-life"]["title"].lower())
        self.assertIn("cadenas alimentarias", " ".join(activities["science-life"]["lesson"]).lower())
        self.assertIn("mezclas", activities["science-matter"]["title"].lower())
        self.assertIn("máquinas simples", " ".join(activities["science-matter"]["lesson"]).lower())
        self.assertIn("sistema solar", activities["science-earth"]["title"].lower())
        self.assertIn("volcanes", activities["science-earth"]["title"].lower())
        self.assertIn("programación", activities["science-technology"]["title"].lower())
        self.assertEqual(activities["science-technology"]["project"], "Circuito simple (pila + LED)")
        self.assertIn("cadena alimentaria", activities["science-lab"]["title"].lower())

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "science-life", "science-matter", "science-earth",
                "science-technology", "science-health", "science-living",
                "science-lab",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_fourth_grade_science_matches_the_planned_curriculum(self):
        science = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Ciencias Naturales"
        }
        activities = {
            key: activity_for_grade(science[key], 4)
            for key in science
        }

        self.assertIn("sistemas", activities["science-life"]["title"].lower())
        self.assertIn("ecosistemas", " ".join(activities["science-life"]["lesson"]).lower())
        self.assertIn("circuitos", activities["science-matter"]["title"].lower())
        self.assertIn("renovable", " ".join(activities["science-matter"]["lesson"]).lower())
        self.assertIn("relieve", activities["science-earth"]["title"].lower())
        self.assertEqual(activities["science-earth"]["project"], "Modelo de volcán o relieve")
        self.assertIn("robótica", activities["science-technology"]["title"].lower())
        self.assertIn("biomimética", " ".join(activities["science-technology"]["lesson"]).lower())
        self.assertIn("Simulador de ecosistema", activities["science-lab"]["title"])

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "science-life", "science-matter", "science-earth",
                "science-technology", "science-health", "science-living",
                "science-lab",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_fifth_grade_science_matches_the_planned_curriculum(self):
        science = {
            item["key"]: item for item in ACTIVITIES
            if item["subject"] == "Ciencias Naturales"
        }
        activities = {
            key: activity_for_grade(science[key], 5)
            for key in science
        }

        self.assertIn("células", activities["science-life"]["title"].lower())
        self.assertIn("adaptaciones", " ".join(activities["science-life"]["lesson"]).lower())
        self.assertIn("reacciones", activities["science-matter"]["title"].lower())
        self.assertIn("método científico", " ".join(activities["science-matter"]["lesson"]).lower())
        self.assertIn("universo", activities["science-earth"]["title"].lower())
        self.assertIn("cambio climático", " ".join(activities["science-earth"]["lesson"]).lower())
        self.assertIn("IA ética", activities["science-technology"]["title"])
        self.assertEqual(activities["science-technology"]["project"], "Proyecto feria de ciencias")
        self.assertIn("Laboratorio virtual", activities["science-lab"]["title"])

        ordered = sorted(activities.values(), key=lambda item: item["learning_order"])
        self.assertEqual(
            [item["key"] for item in ordered],
            [
                "science-life", "science-matter", "science-earth",
                "science-technology", "science-health", "science-living",
                "science-lab",
            ],
        )
        for key, activity in activities.items():
            with self.subTest(activity=key):
                self.assertEqual(len(activity["questions"]), 10)
                self.assertTrue(activity["lesson"] or activity["kind"] == "Juego")
                self.assertTrue(all("answer" in question for question in activity["questions"]))

    def test_each_grade_gets_ten_math_questions_with_valid_answers(self):
        for grade in range(1, 6):
            with self.subTest(grade=grade):
                item = next(item for item in ACTIVITIES if item["key"] == "math-sums")
                questions = activity_for_grade(item, grade)["questions"]
                self.assertEqual(len(questions), 10)
                for question in questions:
                    self.assertEqual(len(question["options"]), 3)
                    self.assertIn(question["answer"], range(3))
                    prompt = question["prompt"]
                    if "fracción equivale" in prompt:
                        expected = {
                            "¿Qué fracción equivale a 1/2?": Fraction(1, 2),
                            "¿Qué fracción equivale a 3/5?": Fraction(3, 5),
                            "¿Qué fracción equivale a 4/8?": Fraction(1, 2),
                        }[prompt]
                        marked = Fraction(question["options"][question["answer"]])
                        self.assertEqual(marked, expected)
                        continue
                    if "/" in prompt and grade == 5:
                        # Fracción operación: 1/2 + 1/3 = ? (operadores Unicode: + − × ÷)
                        import re
                        m = re.match(r"(\d+/\d+)\s*([+\u2212\u00d7\u00f7])\s*(\d+/\d+)", prompt)
                        if m:
                            f1_str, op, f2_str = m.groups()
                            f1 = Fraction(f1_str)
                            f2 = Fraction(f2_str)
                            expected = {
                                "+": f1 + f2,
                                "\u2212": f1 - f2,
                                "\u00d7": f1 * f2,
                                "\u00f7": f1 / f2,
                            }[op]
                            marked = Fraction(question["options"][question["answer"]])
                            self.assertEqual(marked, expected)
                            continue
                    first, operator, second = prompt.split()[:3]
                    left = Decimal(first.replace(",", "."))
                    right = Decimal(second.replace(",", "."))
                    expected = {
                        "+": left + right,
                        "−": left - right,
                        "×": left * right,
                        "÷": left / right,
                    }[operator]
                    marked = Decimal(question["options"][question["answer"]].replace(",", "."))
                    self.assertEqual(marked, expected)

    def test_public_catalog_does_not_send_answer_keys(self):
        for grade in range(1, 6):
            with self.subTest(grade=grade):
                for item in ACTIVITIES:
                    public = public_activity(item, grade)
                    self.assertTrue(public["questions"])
                    self.assertTrue(all("answer" not in question for question in public["questions"]))

    def test_content_adapts_to_grade(self):
        math = next(item for item in ACTIVITIES if item["key"] == "math-sums")
        early_math = activity_for_grade(math, 1)["questions"][0]["prompt"]
        advanced_math = activity_for_grade(math, 5)["questions"][0]["prompt"]
        self.assertNotEqual(early_math, advanced_math)

        words = next(item for item in ACTIVITIES if item["key"] == "words-syllables")
        advanced_words = activity_for_grade(words, 5)["questions"][0]["prompt"]
        self.assertIn("extraordinario", advanced_words)

        story = next(item for item in ACTIVITIES if item["key"] == "reading-story")
        self.assertNotEqual(public_activity(story, 1)["passage"], public_activity(story, 5)["passage"])

    def test_all_subjects_have_four_learning_units_and_a_game(self):
        expected = {subject["name"] for subject in SUBJECTS}
        self.assertEqual({item["subject"] for item in ACTIVITIES}, expected)
        for subject in expected:
            items = [item for item in ACTIVITIES if item["subject"] == subject]
            with self.subTest(subject=subject):
                self.assertEqual(sum(item["kind"] == "Aprendizaje" for item in items), 6)
                self.assertEqual(sum(item["kind"] == "Juego" for item in items), 2 if subject in {"Matemáticas", "Lengua Castellana"} else 1)

    def test_new_subject_content_has_valid_questions_for_every_grade(self):
        new_subjects = {"Ciencias Naturales", "Sociales", "Inglés"}
        for item in ACTIVITIES:
            if item["subject"] not in new_subjects:
                continue
            for grade in range(1, 6):
                with self.subTest(activity=item["key"], grade=grade):
                    adapted = activity_for_grade(item, grade)
                    self.assertEqual(len(adapted["questions"]), 10)
                    self.assertTrue(adapted["lesson"])
                    for current in adapted["questions"]:
                        self.assertEqual(len(current["options"]), 3)
                        self.assertIn(current["answer"], range(3))

    def test_new_subject_public_content_hides_answers(self):
        for item in ACTIVITIES:
            if item["subject"] in {"Ciencias Naturales", "Sociales", "Inglés"}:
                public = public_activity(item, 3)
                self.assertEqual(len(public["questions"]), 10)
                self.assertTrue(all("answer" not in current for current in public["questions"]))


if __name__ == "__main__":
    unittest.main()
