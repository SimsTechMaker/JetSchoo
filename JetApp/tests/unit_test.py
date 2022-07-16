import json
from pathlib import Path

import pytest

from JetApp.views import app, db
from JetApp.models import init_db, init_drop_db

from flask_testing import LiveServerTestCase

from selenium import webdriver
from sqlalchemy import desc



TEST_DB = "test.db"
PASSWORD ="theroot237"
USERNAME = "simsroot"




@pytest.fixture
def client():
    BASE_DIR = Path(__file__).resolve().parent.parent
    app.config["TESTING"] = True
    app.config["DATABASE"] = BASE_DIR.joinpath(TEST_DB)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://sims:theroot@192.168.0.15/stage'
    init_db()  # setup
    yield app.test_client()  # tests run here
    init_drop_db()  # teardown


def login(client, username, password):
    """Login helper function"""
    return client.post(
        "/login",
        data=dict(auth_user=username, auth_pass=password),
        follow_redirects=True,
    )


def logout(client):
    """Logout helper function"""
    return client.get("/logout", follow_redirects=True)


def test_index(client):
    response = client.get("/", content_type="html/text")
    assert response.status_code == 200

def test_login(client):
    a= login (client,"simsroot","theroot237")   
    assert b"<h2>Acceuil</h2>\n" in a.data
    



def test_empty_db(client):
    """Ensure database is blank"""
    rv = client.get("/")
    assert b"No entries yet. Add some!" in rv.data


def test_etudiant(client):
    login(client, USERNAME, PASSWORD)
    data = client.post("/add",
                       data = dict(nom="sima",
                                   prenom="prenom",
                                   SalClass=2,
                                   sexe="M",
                                   date_nais=25),
                       follow_redirects=True,)
    


def test_messages(client):
    """Ensure that user can post messages"""
    login(client, USERNAME, PASSWORD)
    rv = client.post(
        "/addmessage",
        data=  dict(title="<Hello>", text="<strong>HTML</strong> allowed here"),
        follow_redirects=True,
    )
    assert b"No entries here so far" not in rv.data
    assert b"&lt;Hello&gt;" in rv.data
    assert b"<strong>HTML</strong> allowed here" in rv.data


