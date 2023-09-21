import pytest

from RKA.keep_alive import app


@pytest.fixture
def client():
    return app.test_client()
