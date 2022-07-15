from flask import Flask, url_for 

from .views import app
from . import models
from . import gestion
from . import route
from .models import Etudiant, db

models.db.init_app(app)


models.init_db() 
gestion.Post_etudiant("akesbi","nkomo",18,"M",2,"2FDE599")


