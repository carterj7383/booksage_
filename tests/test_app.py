import pytest
from app import app as flask_app

@pytest.fixture
def app():
    flask_app.config.update({
        'TESTING': True,
        'SECRET_KEY': 'test_key',
    })
    return flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200