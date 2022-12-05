from flask import Flask
from app import application, engine
import json
from flask import request, jsonify,make_response

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

    mock_request_data = {
        "username": "test",
        "password": "test",
        "email": "test@test.com"
    }
    response = client.post(url, json=mock_request_data)
    assert response.status_code == 200


# def test_basic_info_route_invalid_email():
#     client = application.test_client()
#     url = '/basic_info'

#     mock_request_data = {
#         "firstname" : "hassan",
#         "lastname" : "",
#         "email" :"test22",
#         "address" : "Cairo , Egypt"
#     }
#     response = client.post(url, json=mock_request_data)
#     assert response.status_code == 400

def test_basic_info_route_missing_token():
    client = application.test_client()
    url = '/basic_info'

    mock_request_data = {
        "firstname" : "hassan",
        "lastname" : "adel",
        "email" :"test@test.com",
        "address" : "Cairo , Egypt"
    }
    response = client.post(url, json=mock_request_data)
    assert response.status_code == 401

# def test_basic_info_route_missing_address():
#     client = application.test_client()
#     url = '/basic_info'

#     mock_request_data = {
#         "firstname" : "hassan",
#         "lastname" : "adel",
#         "email" :"test22",
#         "address" : ""
#     }
#     response = client.post(url, json=mock_request_data)
#     assert response.status_code == 400