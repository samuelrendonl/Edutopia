import unittest

from app.study_guide.pdf_generator import render_pdf
from app.study_guide.service import build_guide, guide_catalog, normalize_subject


class StudyGuideTests(unittest.TestCase):
    def test_catalog_contains_the_25_subject_grade_combinations(self):
        catalog = guide_catalog()
        self.assertEqual(len(catalog), 25)
        self.assertEqual(
            len({(item["subject_slug"], item["grade"]) for item in catalog}),
            25,
        )

    def test_subject_slugs_are_normalized(self):
        self.assertEqual(normalize_subject("matematicas"), "Matemáticas")
        self.assertEqual(normalize_subject("ciencias-naturales"), "Ciencias Naturales")
        self.assertEqual(normalize_subject("inglés"), "Inglés")
        self.assertIsNone(normalize_subject("artes"))

    def test_guide_contains_partial_examples_and_complete_solutions(self):
        guide = build_guide("matematicas", 3, "Ana Pérez", child_id=7)
        questions = [
            question
            for unit in guide.units
            for activity in unit.activities
            for question in activity.questions
        ]
        self.assertEqual(len(questions), len(guide.solutions))
        self.assertEqual(len(guide.calendar), 36)
        self.assertTrue(all(question.answer_text for question in guide.solutions))
        self.assertEqual(sum(question.example for question in questions), len(guide.units))
        self.assertTrue(all("child=7" in activity.qr_url for unit in guide.units for activity in unit.activities))

    def test_fifth_grade_english_guide_has_practical_projects(self):
        guide = build_guide("ingles", 5, "Estudiante")
        self.assertEqual(guide.subject, "Inglés")
        self.assertEqual(guide.grade, 5)
        self.assertGreaterEqual(len(guide.projects), 4)
        self.assertTrue(any("Eco-action" in project for project in guide.projects))
        self.assertTrue(any("Fact-check" in project for project in guide.projects))

    def test_all_english_grades_have_practical_projects(self):
        for grade in range(1, 6):
            with self.subTest(grade=grade):
                guide = build_guide("ingles", grade, "Estudiante")
                self.assertGreaterEqual(len(guide.projects), 4)

    def test_all_math_grades_have_practical_projects(self):
        for grade in range(1, 6):
            with self.subTest(grade=grade):
                guide = build_guide("matematicas", grade, "Estudiante")
                self.assertEqual(
                    [unit.activities[0].key for unit in guide.units],
                    [
                        "math-counting", "math-sums", "math-fractions-geometry",
                        "math-laboratory", "math-market", "math-measures",
                        "math-balloons", "math-race",
                    ],
                )
                self.assertGreaterEqual(len(guide.projects), 4)

    def test_all_social_grades_follow_the_catalog_route(self):
        expected = [
            "social-identity", "social-geography", "social-history",
            "social-economy", "social-culture", "social-media", "social-explorer",
        ]
        for grade in range(1, 6):
            with self.subTest(grade=grade):
                guide = build_guide("sociales", grade, "Estudiante")
                self.assertEqual(
                    [unit.activities[0].key for unit in guide.units],
                    expected,
                )
                self.assertEqual(len(guide.solutions), 70)
                self.assertGreaterEqual(len(guide.projects), 4)

    def test_all_science_grades_follow_the_catalog_route(self):
        expected = [
            "science-life", "science-matter", "science-earth",
            "science-technology", "science-health", "science-living", "science-lab",
        ]
        for grade in range(1, 6):
            with self.subTest(grade=grade):
                guide = build_guide("biologia", grade, "Estudiante")
                self.assertEqual(guide.subject, "Ciencias Naturales")
                self.assertEqual(
                    [unit.activities[0].key for unit in guide.units],
                    expected,
                )
                self.assertEqual(len(guide.solutions), 70)
                self.assertGreaterEqual(len(guide.projects), 4)

    def test_guide_follows_the_app_learning_route(self):
        guide = build_guide("ingles", 5, "Estudiante")
        first = guide.units[0].activities[0]
        game = guide.units[-1].activities[0]
        self.assertEqual(first.key, "english-identity")
        self.assertEqual(first.learning_phase, "Construir")
        self.assertEqual(first.questions[0].prompt, "Complete: We should ___ the planet.")
        self.assertEqual(game.key, "word-quest")
        self.assertEqual(game.learning_phase, "Consolidar")

    def test_all_25_guides_can_be_composed(self):
        for item in guide_catalog():
            with self.subTest(subject=item["subject"], grade=item["grade"]):
                guide = build_guide(item["subject_slug"], item["grade"])
                self.assertEqual(guide.subject_slug, item["subject_slug"])
                self.assertEqual(guide.grade, item["grade"])
                self.assertTrue(guide.units)
                self.assertTrue(guide.solutions)

    def test_pdf_starts_with_pdf_signature(self):
        pdf = render_pdf(build_guide("matematicas", 3, "Ana Pérez"))
        self.assertTrue(pdf.startswith(b"%PDF-"))
        self.assertGreater(len(pdf), 10_000)


if __name__ == "__main__":
    unittest.main()
