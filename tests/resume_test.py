from app import application
from base64 import b64encode

def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'

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

    

def test_basic_info_route_invalid_email():
    client = application.test_client()
    headers = { 'Authorization' : basic_auth("test", "test") }
    login_response = client.post("/login", headers=headers)
    token = login_response.get_json().get("token")

    url = '/basic_info'

    headers = { 'x-access-tokens' : token }

    mock_request_data = {
        "firstname" : "",
        "lastname" : "",
        "email" :"test22",
        "address" : "Cairo , Egypt"
    }
    response = client.post(url, json=mock_request_data,headers=headers)
    assert response.status_code == 400



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