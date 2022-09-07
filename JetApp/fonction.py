
from textwrap import wrap

from flask import session, flash,request,render_template,jsonify
from . import gestion
from .models import db , Etudiant
from copy import deepcopy


def Login_requi(f):
    @wrap(f)
    def decoration_fonction(*args,**kwargs):
        if not session.get("loggend_in"):
            flash("S'il vous plaît connecter vous")
            return jsonify({"status" : 0, "message" : "S'il vous plaît connecter vous"}),401
        return f(*args,**kwargs)
    return decoration_fonction

def listeDesEtudiant():
    t=0
    dico ={}
    listeEtu = []
    for i in db.session.query(Etudiant).order_by(Etudiant.id):
        t += 1
        dico[i.id]= i
    for j in range(t+1):
        j+=1
        listeEtu.append(gestion.get_etudiant(j))
    print(listeEtu)
    print(dico)
    print(dico[1].nom)
    print(len(dico))
    return(dico)


""" infoEtudian = [ etudi4.nom,
                        etudi4.prenom,
                        etudi4.classe,
                        etudi4.age,
                        etudi4.mat]
infoEtudiant = deepcopy(infoEtudian)
 """
print("ICCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCI")
