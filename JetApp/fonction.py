
from ast import arg
from textwrap import wrap

from flask import session, flash,request,render_template,jsonify
from . import gestion
from copy import deepcopy


etudi4 =gestion.get_etudiant(1)
print(etudi4)

def Login_requi(f):
    @wrap(f)
    def decoration_fonction(*args,**kwargs):
        if not session.get("loggend_in"):
            flash("S'il vous plaît connecter vous")
            return jsonify({"status" : 0, "message" : "S'il vous plaît connecter vous"}),401
        return f(*args,**kwargs)
    return decoration_fonction



""" infoEtudian = [ etudi4.nom,
                        etudi4.prenom,
                        etudi4.classe,
                        etudi4.age,
                        etudi4.mat]
infoEtudiant = deepcopy(infoEtudian)
 """
print("ICCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCI")
