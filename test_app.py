import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_health_returns_ok(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_index_reports_version(client):
    resp = client.get("/")
    assert resp.status_code == 200
    body = resp.get_json()
    assert body["message"] == "Hello from the CI/CD POC"
    assert "version" in body


def test_add(client):
    resp = client.get("/add/2/3")
    assert resp.status_code == 200
    assert resp.get_json() == {"result": 5}


def test_add_rejects_non_integers(client):
    resp = client.get("/add/two/3")
    assert resp.status_code == 404
