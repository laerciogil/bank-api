import pytest
from fastapi.testclient import TestClient

from bank_api.main import app as _app


@pytest.fixture(scope="module")
def app():
    """Instance of main app"""
    return _app


@pytest.fixture(scope="module")
def client():
    """Instance of Client"""
    return TestClient(app)
