from flask import Flask, flash 
import logging as lg

from .views import app
from . import models
from .models import db , Etudiant

def Post_etudiant(nom,prenom,age,sexe,Salclass,matricul):
    db.session.add(Etudiant(matricul,Salclass,nom,prenom,sexe,age))
    db.session.commit() 
    
def get_etudiant(id_etudiant):
    etudi =db.session.query(Etudiant).get(id_etudiant)
    db.session.commit() 
    return etudi



def delet_etudiant(id_etudiant):
    etut = get_etudiant(id_etudiant)
    db.session.delete(etut)
    db.session.commit()
    
    
      
