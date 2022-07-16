from flask_testing import LiveServerTestCase

from selenium import webdriver
from sqlalchemy import desc

from JetApp.views import app
from JetApp.models import init_db

PASSWORD ="theroot237"
USERNAME = "simsroot"

""" class TestUser(LiveServerTestCase):
    driver = webdriver.Firefox()
    def create_app(self):
        
        app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://sims:theroot@192.168.125.104/stage'
        app.config["LIVESERVER_TIMEOUT"] = 10
        return app
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        init_db
        
    def offTes(self):
        self.driver.quit() 
    
    def test_user_login(self):
        self.driver.get("http://localhost:4000/login")
        self.driver.find_element("id","auth_user").send_keys(USERNAME)
        self.driver.find_element("id","auth_pass").send_keys(PASSWORD)
        self.driver.find_element("name","accept").click() """
         
class TestFonction():
    app.config["SERVER_NAME "]= 'localhost:8943'
    driver = webdriver.Firefox()
        
        
    def offTes(self):
        self.driver.quit() 

    def test_user_login(self):
        self.driver.get("http://localhost:4000/login")
        self.driver.find_element("id","auth_user").send_keys(USERNAME)
        self.driver.find_element("id","auth_pass").send_keys(PASSWORD)
        self.driver.find_element("name","accept").click()
        