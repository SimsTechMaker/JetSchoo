from flask import Flask, url_for 

from .views import app
from . import models
from . import gestion
from .models import Etudiant, db


models.db.init_app(app)


models.init_db()  




gestion.Post_etudiant("akesbi","nkomo",18,"M",2,"2FDE599")
gestion.Post_etudiant("NDI","Moussi",17,"F",2,"zzz575")


etudi =gestion.get_etudiant(1)
print(etudi.nom)
print("BONJOURRRRRRRRRRRRRRRRRRRRRRRRRRRRR")

gestion.delet_etudiant(1)

