
import os





basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'Theapp.db')


SECRET_KEY = "simstechmaker_key"
 
USERNAME = "simsroot"
PASSWD = "theroot237"
    

DB_DEV  = 'postgresql://sims:theroot@192.168.0.15/dev'
SECRET_KEY = "simstechmaker_key"

"""SQLALCHEMY_DATABASE_URI = DB_DEV"""

SQLALCHEMY_TRACK_MODIFICATIONS = False
