
import logging as lg

from .models import db , Etudiant, SalleClass

def Post_etudiant(nom,prenom,age,sexe,Salclass,matricul):
    db.session.add(Etudiant(matricul,Salclass,nom,prenom,sexe,age))
    db.session.commit() 
    
def get_etudiant(id_etudiant):
    variable = []
    for etudi in db.session.query(Etudiant).filter_by(id=id_etudiant):
        variable.append(etudi.nom)
        variable.append(etudi.prenom)
        variable.append(etudi.sexe)
        variable.append(etudi.age)
        variable.append(etudi.classe)
        variable.append(etudi.mat)
        variable.append(etudi.id)
        
        
        print(variable[3])
    
    return variable

def get_classe(id_classe):
    variable = []
    for i in db.session.query(SalleClass).filter_by(id=id_classe):
        variable.append(i.nom)
        variable.append(i.nbPla)
        variable.append(i.id)
        
        print(variable[0])
    return variable


def delet_etudiant(id_etudiant):
    db.session.query(Etudiant).filter_by(id=id_etudiant).delete()
    db.session.commit()
    
    
    
      
