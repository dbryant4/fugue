def test_health_endpoint(client):
    """ Test that the health endpoint works as expected """

    result = client.get('/health')

    assert result.status_code == 200
    assert result.json == {'status': 'Ok'}


def test_index_endpoint(client):
    """ Test that the root path redirects to index.html """

    result = client.get('/')

    assert result.status_code == 302

    assert result.headers['Location'] == 'http://localhost/index.html'

def test_file_endpoint(client):
    """ Ensure that files are served on all other endpoints """

    result = client.get('/bootstrap.min.css')

    assert result.status_code == 200
    assert 'Bootstrap v4.1.1' in result.data
