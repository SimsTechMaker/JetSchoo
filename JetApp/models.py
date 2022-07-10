import imp
import logging as lg

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null, nullslast
from .views import app  

#Creation de la l'object connection a la base de donnée 

db = SQLAlchemy(app)



#Creation des models 

class Humain():
    
    def __init__(self,nom:str,prenom:str,sexe:str,age:int):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.age = age


class Matier(db.Model):
    
    __tablename__= "matier"
    
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(15), nullable=False)
    
    def __init__(self, nom) :
        self.nom = nom


class SalleClass(db.Model):
    __tablename__ = "salleclass"
    
    id = db.Column(db.Integer, primary_key=True) 
    nom = db.Column(db.String(15), nullable=False)
    nbPla = db.Column(db.Integer(), nullable=False)
    
    def __init__(self,nom,nbPla):
        self.nom = nom
        self.nbPla = nbPla
       

class Etudiant(Humain, db.Model):
    __tablename__ = "etudiant"
    id = db.Column(db.Integer, primary_key=True)
    mat = db.Column(db.String(15), nullable=False)
    
    nom = db.Column(db.String(25), nullable=False)
    prenom = db.Column(db.String(25), nullable=False)
    sexe = db.Column(db.String(15), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    classe = db.Column(db.Integer(), db.ForeignKey('salleclass.id'),nullable=False)
    
    def __init__(self,matricule,classe, nom, prenom, sexe, age):
        super().__init__(nom, prenom, sexe, age)
        self.mat = matricule
        self.classe = classe
    
    
        
        
class Prof (Humain, db.Model):
    __tablename__ = "professeur"
    
    id = db.Column(db.Integer, primary_key=True)
    
mati = ["SVT", "Maths", "Infromatique", "Histoire", "EPS", "Pysique", "Chimie"]
clss = ["6eme","5eme","4eme","3eme","2nde","1er","Tle"]

def init_db():
    db.drop_all()
    db.create_all()
    for i in range(len(mati)):
        db.session.add(Matier(mati(i)))
    for i in range(len(clss)):
        db.session.add(SalleClass(clss(i)))
    db.session.add(Etudiant(58,2,"sima","emmaneul","5",25))
    db.session.commit()
    lg.warning("La base de donnée est initialiser")
    
db.create_all()

db.create_all()
    
        