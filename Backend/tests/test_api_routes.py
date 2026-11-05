import importlib.util
from pathlib import Path
from unittest.mock import patch

from app import auth_sessions
from app.study_guide import routes as study_guide_routes


PROJECT_ROOT = Path(__file__).resolve().parents[2]
APP_FILE = PROJECT_ROOT / "Backend" / "app.py"
APP_SPEC = importlib.util.spec_from_file_location("edutopia_server", APP_FILE)
SERVER = importlib.util.module_from_spec(APP_SPEC)
APP_SPEC.loader.exec_module(SERVER)
SERVER.app.config.update(TESTING=True, SECRET_KEY="api-test-secret")


class TestApiRoutes:
    def setup_method(self):
        self.client = SERVER.app.test_client()

    def _token(self):
        with SERVER.app.app_context():
            return auth_sessions.issue_parent_token(9001)

    def test_learning_catalog_requires_authentication(self):
        response = self.client.get("/api/learning/activities?grade=1")

        assert response.status_code == 401

    def test_authenticated_learning_catalog_returns_public_math_content(self):
        token = self._token()
        with patch.object(auth_sessions, "query", return_value=[{"id": 9001}]):
            response = self.client.get(
                "/api/learning/activities?grade=1",
                headers={"X-Auth-Token": token},
            )

        assert response.status_code == 200
        payload = response.get_json()
        assert payload["grade"] == 1
        math = [item for item in payload["activities"] if item["subject"] == "Matemáticas"]
        counting = next(item for item in math if item["key"] == "math-counting")
        assert len(counting["questions"]) == 10
        assert all("answer" not in question for question in counting["questions"])

    def test_authenticated_children_route_uses_shared_auth_decorator(self):
        token = self._token()
        with (
            patch.object(auth_sessions, "query", return_value=[{"id": 9001, "name": "Familia"}]),
            patch.object(SERVER, "query", return_value=[]),
        ):
            response = self.client.get(
                "/api/children",
                headers={"X-Auth-Token": token},
            )

        assert response.status_code == 200
        assert response.get_json() == {"children": []}

    def test_math_game_check_still_works(self):
        response = self.client.post(
            "/api/games/check",
            json={"key": "math-race", "grade": 1, "round": 0, "answer": 0},
        )

        assert response.status_code == 200
        assert response.get_json()["correct"] is True

    def test_subject_catalog_exposes_all_curriculum_subjects(self):
        token = self._token()
        with patch.object(auth_sessions, "query", return_value=[{"id": 9001}]):
            response = self.client.get(
                "/api/learning/subjects",
                headers={"X-Auth-Token": token},
            )

        assert response.status_code == 200
        payload = response.get_json()
        assert payload["total_activities"] == 37
        assert {item["name"] for item in payload["subjects"]} == {
            "Matemáticas", "Lengua Castellana", "Ciencias Naturales", "Sociales", "Inglés",
        }
        assert all(item["available"] for item in payload["subjects"])

    def test_authenticated_admin_catalog_exposes_all_learning_units(self):
        token = self._token()
        with patch.object(auth_sessions, "query", return_value=[{"id": 9001, "role": "parent"}]):
            response = self.client.get(
                "/api/admin/catalog",
                headers={"X-Auth-Token": token},
            )

        assert response.status_code == 200
        payload = response.get_json()
        assert payload["total"] == 150
        assert all(item["kind"] == "Aprendizaje" for item in payload["activities"])

    def test_parent_cannot_manage_admin_users(self):
        token = self._token()
        with patch.object(auth_sessions, "query", return_value=[{"id": 9001, "role": "parent"}]):
            response = self.client.get(
                "/api/admin/users",
                headers={"X-Auth-Token": token},
            )

        assert response.status_code == 403

    def test_admin_can_read_role_permissions(self):
        token = self._token()
        with patch.object(auth_sessions, "query", return_value=[{"id": 9001, "role": "admin"}]):
            response = self.client.get(
                "/api/admin/roles",
                headers={"X-Auth-Token": token},
            )

        assert response.status_code == 200
        roles = response.get_json()["roles"]
        assert {role["name"] for role in roles} == {"parent", "teacher", "editor", "admin"}
        admin_role = next(role for role in roles if role["name"] == "admin")
        assert "users.manage" in admin_role["permissions"]

    def test_science_game_check_still_works(self):
        response = self.client.post(
            "/api/games/check",
            json={"key": "science-lab", "grade": 1, "round": 0, "answer": 0},
        )

        assert response.status_code == 200

    def test_study_guide_rejects_a_grade_that_does_not_match_the_child(self):
        token = self._token()
        with (
            patch.object(auth_sessions, "query", return_value=[{"id": 9001}]),
            patch.object(
                study_guide_routes,
                "query",
                return_value=[{"id": 42, "name": "Ana", "grade": 3}],
            ),
        ):
            response = self.client.get(
                "/api/study-guides/pdf?subject=matematicas&grade=1&child_id=42",
                headers={"X-Auth-Token": token},
            )

        assert response.status_code == 403
        payload = response.get_json()
        assert payload["child_grade"] == 3
        assert payload["requested_grade"] == 1

    def test_study_guide_requires_authentication(self):
        response = self.client.get("/api/study-guides/pdf?subject=ingles&grade=5")

        assert response.status_code == 401

    def test_study_guide_preview_keeps_subject_and_grade_selected(self):
        token = self._token()
        with patch.object(auth_sessions, "query", return_value=[{"id": 9001}]):
            response = self.client.get(
                "/api/study-guides/preview?subject=ingles&grade=5",
                headers={"X-Auth-Token": token},
            )

        assert response.status_code == 200
        payload = response.get_json()
        assert payload["subject"] == "Inglés"
        assert payload["grade"] == 5
        assert payload["units"][0]["title"] == "Environment and action"
