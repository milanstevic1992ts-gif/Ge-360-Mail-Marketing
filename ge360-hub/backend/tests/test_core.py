from fastapi.testclient import TestClient

from app.main import app


def test_root_and_health():
    with TestClient(app) as client:
        root = client.get("/")
        assert root.status_code == 200
        assert root.json()["service"] == "GE360 Mail Marketing"

        health = client.get("/api/health")
        assert health.status_code == 200
        assert health.json()["status"] == "ok"


def test_engine_registry():
    with TestClient(app) as client:
        response = client.get("/api/engines")
        assert response.status_code == 200
        payload = response.json()
        assert set(payload) == {"prospex", "twenty", "mautic", "opencrm"}
        assert "crm" in payload["twenty"]["capabilities"]


def test_contact_create_list_and_dedupe():
    with TestClient(app) as client:
        created = client.post(
            "/api/contacts",
            json={
                "contact_type": "geometra",
                "first_name": "Mario",
                "last_name": "Rossi",
                "company": "Studio Rossi",
                "email": "Mario.Rossi@example.test",
                "city": "Trieste",
                "source": "manual-test",
            },
        )
        assert created.status_code == 201
        ge360_id = created.json()["ge360_id"]
        assert ge360_id.startswith("CNT-")

        fetched = client.get(f"/api/contacts/{ge360_id}")
        assert fetched.status_code == 200
        assert fetched.json()["company"] == "Studio Rossi"

        candidates = client.get(
            "/api/contacts/dedupe/candidates",
            params={"email": "mario.rossi@EXAMPLE.TEST"},
        )
        assert candidates.status_code == 200
        assert any(item["ge360_id"] == ge360_id for item in candidates.json())
