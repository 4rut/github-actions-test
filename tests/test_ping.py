from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ping_ok():
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_unknown_path_404():
    resp = client.get("/nope")
    assert resp.status_code == 404
