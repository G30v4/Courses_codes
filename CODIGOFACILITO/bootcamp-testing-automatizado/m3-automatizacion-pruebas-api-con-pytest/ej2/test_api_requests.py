'''
Ejemplos de pruebas de API con pytest
Code Online: "https://www.online-python.com/share/2o1sSj70Fk"
Try command:
    import pytest
    pytest.main(['test.py', '-v'])
'''
import requests
import pytest

# Tests GET
def test_get_success_all(base_url):
    res = requests.get(f'{base_url}/posts/1') # verify=False
    assert res.status_code == 200
    body = res.json()
    assert "title" in body
    assert isinstance(body['title'], str)

def test_get_success_status_code(base_url):
    res = requests.get(f'{base_url}/posts/1') # verify=False
    assert res.status_code == 200

def test_get_success_title(base_url):
    res = requests.get(f'{base_url}/posts/1') # verify=False
    body = res.json()
    assert "title" in body

def test_get_success_title_instance(base_url):
    res = requests.get(f'{base_url}/posts/1') # verify=False
    body = res.json()
    assert isinstance(body['title'], str)

# Tests POST
def test_create_success(base_url):
    data = {
        "title": "My title",
        "body": "Example data",
        "userId": 1
    }
    res = requests.post(f'{base_url}/posts', json=data) # headers=headers
    assert res.status_code == 201
    body = res.json()
    assert 'id' in body

# Test con prametrización
data_ids = [1,2,3,4,5]

@pytest.mark.parametrize('post_id', data_ids)
def test_multiple_get(base_url, post_id):
    res = requests.get(f'{base_url}/posts/{post_id}')
    assert res.status_code == 200
    assert 'id' in res.json()

# Test con medición
def test_response_time(base_url):
    res = requests.get(f'{base_url}/posts/1')
    assert res.elapsed.total_seconds() < 1.0
