def test_with_client(client):
    response = client.get('/posts')
    assert response.status_code == 301
    response = client.get(response.url)
    assert b"article1" in response.content