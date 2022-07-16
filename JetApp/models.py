import imp
import logging as lg
from flask import session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null, nullslast
from .views import app  

#Creation de la l'object connection a la base de donnée 

db = SQLAlchemy(app)



#Creation des models 

class Humain():
    
    def __init__(self,nom,prenom,sexe,age=0):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.age = age

class AdminJet(db.Model):
    __tablename__= "adminjet"
    
    id = id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(15), nullable=False)
    passwd = db.Column(db.String(256), nullable=False)
    
    def __init__(self,login,passwd) -> None:
        self.login = login
        self.passwd = passwd
    
    
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
    id = db.Column(db.Integer(), primary_key=True)
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
    mat = db.Column(db.Integer(), db.ForeignKey('matier.id'),nullable=False)
    nom = db.Column(db.String(25), nullable=False)
    prenom = db.Column(db.String(25), nullable=False)
    sexe = db.Column(db.String(15), nullable=False)
    
    
    def __init__(self,matier, nom, prenom, sexe, age=0):
        super().__init__(nom, prenom, sexe, age)
        self.mat = matier
        


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return f"<title {self.title}>"



    
mati = ["SVT", "Maths", "Infromatique", "Histoire", "EPS", "Pysique", "Chimie"]
clss = [["6eme",25],["5eme",55],["4eme",30],["3eme",85],["2nde",45],["1er",25],["Tle",15]]
 
def init_db():
    db.drop_all()
    db.create_all()
    for i in range(len(mati)):
        db.session.add(Matier(mati[i]))
    for i in range(len(clss)):
        db.session.add(SalleClass(clss[i][0],clss[i][1]))
    db.session.commit()
    db.session.add(AdminJet('root',"theroot"))
    db.session.add(Prof(7,"Dr Nkamdem","juline","F"))
    
    
    
    db.session.commit()
    lg.warning("La base de donnée est initialiser")
  


def init_drop_db():
    
    db.drop_all()