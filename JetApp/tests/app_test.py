############# importation des modules 
from selenium import webdriver

from JetApp.views import app

####### Declaration des variables 
PASSWORD ="theroot237"
USERNAME = "simsroot"

####### le Test 
class TestFonction():
    app.config["SERVER_NAME "]= 'localhost:8943'  # Creation du server de test 
    driver = webdriver.Firefox() # initialisation du pilote pour le navigateur 
        
        
    def offTes(self): # Fermeture du navigateur 
        self.driver.quit() 

    def test_user_login(self): # Fonction test du senarion connection de l'utilisateur admin
        self.driver.get("http://localhost:4000/login") # ouverture de la page de connexion 
        self.driver.find_element("id","auth_user").send_keys(USERNAME)
        self.driver.find_element("id","auth_pass").send_keys(PASSWORD)
        self.driver.find_element("name","accept").click() # 
        