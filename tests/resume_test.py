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

def test_basic_info_route_validation_schema():
    client = application.test_client()
    headers = { 'Authorization' : basic_auth("test", "test") }
    login_response = client.post("/login", headers=headers)
    token = login_response.get_json().get("token")

    url = '/basic_info'

    headers = { 'x-access-tokens' : token }

    mock_request_data = {
        "firstname" : "mock first name",
        "lastname" : "mock last name",
        "email" :"test22",
        "address" : "Cairo , Egypt"
    }
    response = client.post(url, json=mock_request_data,headers=headers)
    assert response.status_code == 400
    mock_request_data = {
        "firstname" : "mock first name",
        "lastname" : "mock last name",
        "email" :"test@test.com",
    }
    response = client.post(url, json=mock_request_data,headers=headers)
    assert response.status_code == 400
    mock_request_data = {
        "firstname" : "mock first name",
        "lastname" : "mock last name",
        "email" :"test@test.com",
        "address" : "Cairo"
    }
    response = client.post(url, json=mock_request_data,headers=headers)
    assert response.status_code == 200


def test_work_experience_route_missing_token():
    client = application.test_client()
    url = '/work_experience'

    mock_request_data = {
        "work_experiences": [
            {
                "company": "company 1",
                "location" : "Cairo",
                "title" : "Software engineer",
                "started_on" : "2020-12-01",
                "ended_on" : "2021-12-12"
            }
        ]
    }
    response = client.post(url, json=mock_request_data)
    assert response.status_code == 401

def test_work_experience_route_validation_schema():
    client = application.test_client()
    headers = { 'Authorization' : basic_auth("test", "test") }
    login_response = client.post("/login", headers=headers)
    token = login_response.get_json().get("token")

    url = '/work_experience'

    headers = { 'x-access-tokens' : token }

    mock_request_data = {
        "work_experiences": [
            {
                "company": "company 1",
                "location" : "Cairo",
                "title" : "Software engineer",
                "started_on" : "test",
                "ended_on" : "test"
            }
        ]
    }
    response = client.post(url, json=mock_request_data,headers=headers)
    assert response.status_code == 400
    mock_request_data = {
        "work_experiences": [
            {
                "started_on" : "2020-12-01",
                "ended_on" : "2021-12-12"
            }
        ]
    }
    response = client.post(url, json=mock_request_data,headers=headers)
    assert response.status_code == 400
    mock_request_data = {
        "work_experiences": [
            {
                "company": "company 1",
                "location" : "Cairo",
                "title" : "Software engineer",
                "started_on" : "2020-12-01",
                "ended_on" : "2021-12-12"
            }
        ]
    }
    response = client.post(url, json=mock_request_data,headers=headers)
    assert response.status_code == 200


def test_education_route_missing_token():
    client = application.test_client()
    url = '/education'

    mock_request_data = {
        "educations": [
            {
                "institution": "ITI",
                "eduction_level" : "BCs",
                "programe" : "E-Business",
                "started_on" : "2013-10-20",
                "ended_on" : "2014-04-12"
            }
        ]
    }
    response = client.post(url, json=mock_request_data)
    assert response.status_code == 401

def test_education_route_validation_schema():
    client = application.test_client()
    headers = { 'Authorization' : basic_auth("test", "test") }
    login_response = client.post("/login", headers=headers)
    token = login_response.get_json().get("token")

    url = '/education'

    headers = { 'x-access-tokens' : token }

    mock_request_data = {
        "educations": [
            {
                "institution": "ITI",
                "started_on" : "2013-10-20",
                "ended_on" : "2014-04-12"
            }
        ]
    }
    response = client.post(url, json=mock_request_data,headers=headers)
    assert response.status_code == 400
    mock_request_data = {
        "educations": [
            {
                "institution": "ITI",
                "eduction_level" : "BCs",
                "programe" : "E-Business",
                "started_on" : "invalid date",
                "ended_on" : "2014-04-12"
            }
        ]
    }
    response = client.post(url, json=mock_request_data,headers=headers)
    assert response.status_code == 400
    mock_request_data = {
        "educations": [
            {
                "institution": "ITI",
                "eduction_level" : "BCs",
                "programe" : "E-Business",
                "started_on" : "2013-10-20",
                "ended_on" : "2014-04-12"
            }
        ]
    }
    response = client.post(url, json=mock_request_data,headers=headers)
    assert response.status_code == 200


def test_certificates_route_missing_token():
    client = application.test_client()
    url = '/certificates'

    mock_request_data = {
        "certificates": [
            {
                "certification": "AI certificate",
                "organization" : "Coursera",
                "issue_date" : "2019-01-12",
                "expiration_date" : "2020-04-12"
            }
        ]
    }
    response = client.post(url, json=mock_request_data)
    assert response.status_code == 401

def test_certificates_route_validation_schema():
    client = application.test_client()
    headers = { 'Authorization' : basic_auth("test", "test") }
    login_response = client.post("/login", headers=headers)
    token = login_response.get_json().get("token")

    url = '/certificates'

    headers = { 'x-access-tokens' : token }

    mock_request_data = {
        "certificates": [
            {
                "certification": "AI certificate",
                "organization" : "Coursera",
                "issue_date" : "invalid date",
                "expiration_date" : "invalid date"
            }
        ]
    }
    response = client.post(url, json=mock_request_data,headers=headers)
    assert response.status_code == 400
    mock_request_data = {
        "certificates": [
            {
                "issue_date" : "2019-01-12",
                "expiration_date" : "2020-04-12"
            }
        ]
    }
    response = client.post(url, json=mock_request_data,headers=headers)
    assert response.status_code == 400
    mock_request_data = {
        "certificates": [
            {
                "certification": "AI certificate",
                "organization" : "Coursera",
                "issue_date" : "2019-01-12",
                "expiration_date" : "2020-04-12"
            }
        ]
    }
    response = client.post(url, json=mock_request_data,headers=headers)
    assert response.status_code == 200

