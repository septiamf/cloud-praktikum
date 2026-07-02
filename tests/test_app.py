import sys
import os

# Menambahkan folder utama project ke Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

client = app.test_client()

def test_home():
    response = client.get("/")
    assert response.status_code == 404

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"