from time import sleep
import logging
import pytest

from main import app


class TestApp:

    @pytest.fixture
    def client(self, caplog):
        self.caplog = caplog
        self.caplog.set_level(logging.INFO)
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client

    def test_get_flowers(self, client):
        response = client.get('/flowers')
        assert response.status_code == 200
        assert len(response.json) == 5

    def test_create_flower(self, client):
        response = client.post('/flowers', json={'name': 'New flower', 'color': 'New color'})
        assert response.status_code == 201
        assert response.json['name'] == 'New flower'
        assert response.json['color'] == 'New color'

    def test_get_flower(self, client):
        response = client.get('/flowers/1')
        assert response.status_code == 200
        assert response.json['name'] == 'Rose'
        assert response.json['color'] == 'red'

    def test_get_flower_not_found(self, client):
        response = client.get('/flowers/100')
        assert response.status_code == 404
        assert response.json['error'] == 'flower not found'

    def test_update_flower(self, client):
        response = client.put('/flowers/1', json={'name': 'Updated flower', 'color': 'Updated color'})
        assert response.status_code == 200
        assert response.json['name'] == 'Updated flower'
        assert response.json['color'] == 'Updated color'

    def test_update_flower_not_found(self, client):
        response = client.put('/flowers/100', json={'name': 'Updated flower', 'color': 'Updated color'})
        assert response.status_code == 404
        assert response.json['error'] == 'flower not found'

    def test_delete_flower(self, client):

        logging.info("This is an informational log message.")
        logging.warning("This is a warning log message.")
        response = client.delete('/flowers/1')
        # sleep(5)
        assert response.status_code == 200
        assert response.json['message'] == 'flower deleted'

    def test_delete_flower_not_found(self, client):
        response = client.delete('/flowers/100')
        assert response.status_code == 404
        assert response.json['error'] == 'flower not found'

# https://github.com/MicrosoftLearning/AI-102-AIEngineer