"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/about"' in response.data
    assert b'href="/welcome"' in response.data
    assert b'href="/register"' in response.data



def test_request_index(client):
    """This makes the home page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data

def test_request_about(client):
    """This makes the about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data

def test_request_page1(client):
    """This makes the welcome page"""
    response = client.get("/welcome")
    assert response.status_code == 200
    assert b"welcome" in response.data

def test_request_request(client):
    """This makes the register page"""
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Register" in response.data

# check if login page works #7
def test_request_login(client):
    """This makes the login page"""
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data

# test to check if invalid simple page shows error #14

def test_request_page_not_found(client):
    """This checks the error"""
    response = client.get("/page5")
    assert response.status_code == 404