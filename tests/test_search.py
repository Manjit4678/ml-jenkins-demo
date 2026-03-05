from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_search():
    response = client.post(
        "/search",
        json={"query": "loan process"}
    )

    assert response.status_code == 200
    assert "results" in response.json()
