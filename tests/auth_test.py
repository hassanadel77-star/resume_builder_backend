from app import application
import uuid


def test_base_route():
    client = application.test_client()
    url = '/'
    response = client.get(url)
    assert response.get_data() == b'Welcome to this page'
    assert response.status_code == 200

def test_register_route_missing_data():
    client = application.test_client()
    url = '/register'

    mock_request_data = {
        "username": "",
        "password": "",
        "email": "hassan.adel@test.com"
    }
    response = client.post(url, json=mock_request_data)
    assert response.status_code == 400

def test_register_route_invalid_email():
    client = application.test_client()
    url = '/register'

    mock_request_data = {
        "username": "hassan.adel",
        "password": "test",
        "email": "hassan.adel"
    }
    response = client.post(url, json=mock_request_data)
    assert response.status_code == 400

def test_register_route():
    client = application.test_client()
    url = '/register'
    random_user = str(uuid.uuid4())
    mock_request_data = {
        "username": random_user,
        "password": "test",
        "email": "{user}@test.com".format(user=random_user)
    }
    response = client.post(url, json=mock_request_data)
    assert response.status_code == 200


