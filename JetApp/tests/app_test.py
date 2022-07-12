from views import app

def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html")

    assert response.status_code == 304