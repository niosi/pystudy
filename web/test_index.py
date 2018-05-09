import pytest

@pytest.fixture
def app():
    from web.flaskdemo import app
    return app



def test_index(client):
    rs = client.get('/')
    print(rs.data)
    assert b'This is Flask TestDemo'
