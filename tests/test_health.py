"""
Basic health check test for the E-Consultation Insight Engine API.
"""

import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert data["version"] == "1.0.0"


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "version" in data


def test_detailed_health_check():
    """Test the detailed health check endpoint."""
    response = client.get("/api/v1/health/detailed")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "database" in data
    assert "services" in data
    assert "configuration" in data


def test_database_health():
    """Test the database health endpoint."""
    response = client.get("/api/v1/health/database")
    assert response.status_code == 200
    data = response.json()
    assert "database_healthy" in data
    assert "timestamp" in data