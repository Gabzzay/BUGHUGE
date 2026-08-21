from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "BUGHUGE"
    assert data["status"] == "operational"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"


def test_create_vulnerability():
    vulnerability_data = {
        "id": "CVE-2026-12345",
        "source": "NVD",
        "title": "Example vulnerability",
        "description": "Example vulnerability description",
        "severity": "HIGH",
        "cvss_score": 8.1,
    }

    response = client.post(
        "/vulnerabilities",
        json=vulnerability_data,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == "CVE-2026-12345"
    assert data["severity"] == "HIGH"
    assert data["cvss_score"] == 8.1