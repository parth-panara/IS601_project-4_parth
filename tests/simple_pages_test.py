"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200






def test_request_index(client):
    """This makes the home page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data
