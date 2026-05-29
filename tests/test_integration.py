from app.main import app

def test_health_integration():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200