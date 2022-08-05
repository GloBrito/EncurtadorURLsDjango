def test_teste():
    teste = 11
    assert teste == 11

def test_StatusCode(client):
    response = client.get('')
    assert response.status_code == 200

