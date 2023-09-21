from flask.testing import FlaskClient


def test_run(client: FlaskClient):
    with client:
        assert client.get("/").status_code == 200
