
from os import abort
from .views import app

from atexit import register
import re
from flask import Flask, flash, redirect, render_template, request, session, url_for

from .form import ResiterForm, Filtre, Scan
from .fonction import etudi4
from .gestion import Post_etudiant




infoEtudiant=etudi4
@app.route('/')
def index():
    return render_template('login.html',title="login")




""" @app.route("/add", methods=["POST"])
def add_etu():
    #""#Ajoute un etudiant a la base de donné
    #""
    if not session.get("logged_in"):
        abort(401)
    matricule = "request.form[]"
    nom = request.form['nom']
    prenom = request.form['prenom']
    classe = request.form['SalClass']
    sexe = request.form['sexe']
    age = str(request.form['date_nais'])
    Post_etudiant(nom,prenom,age,sexe,classe,matricule)
    flash ("Etudiant enregister avec succes !")
    return redirect(url_for("listeEtu"))
 """

    

    



@app.route('/listeEtu')
def listeEtudiant():
    filtre = Filtre()
    description =" Liste des etudiants "
    
    return render_template('listeEtu.html', form = filtre , title="Liste des Etudiants ", desc=description)

@app.route('/pres')
def etudiant():
    description =" Information sur l'etudiant "
    
    
    return render_template('pres.html', nomEtu= "infoEtudiant[0]", title="Etudiant",desc=description)


@app.route('/register',methods=['POST','GET'])
def register():
    persone = ResiterForm()
    description =" Enregistrement de l'etudiant "
    
    return render_template('regist.html',form=persone,title="Inscription",desc=description )
    
    
@app.route('/submit', methods=['POST'])
def submit_pwd():
    auth_pass = request.form['auth_pass']
    auth_user = request.form['auth_user']
    
    print("le nom du user est : ", auth_user, "le mot de passe est ", auth_pass)
    return render_template('index.html')

@app.route('/logout')
def logout():
    pass
""" if __name__ == "__main__":
    app.run() """