
from distutils.log import error
import errno
from os import abort
from JetApp.models import Etudiant, db

from config import PASSWD, USERNAME
from .views import app

from atexit import register
import re
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for

from .form import ResiterForm, LogForm, Filtre, Scan
from .fonction import Login_requi, etudi4, listeDesEtudiant
from .gestion import Post_etudiant, delet_etudiant, get_classe, get_etudiant



@app.route('/')
def index():
    return render_template('index.html',title="Page d'acceuil")




@app.route("/add", methods=["POST"])
def add_etu():
    #Ajoute un etudiant a la base de donné

    if not session.get("logged_in"):
        abort(401)
    matricule = "185455"
    nom = request.form['nom']
    prenom = request.form['prenom']
    classe = request.form['SalClass']
    sexe = request.form['sexe']
    age = str(request.form['date_nais'])
    Post_etudiant(nom,prenom,age,sexe,classe,matricule)
    flash ("Etudiant enregister avec succes !")
    return redirect(url_for("listeEtudiant"))

@app.route("/delete/<int:id_etudiant>", methods=['GET'])
#@Login_requi #la condition pour supprimer tu as besion d'etre en login admin
def del_etudiant(id_etudiant):
    #Suppression d'un etudiant 
    result = {"status" : 0, "message" : "Error"}
    try:
        delet_etudiant(id_etudiant)
        result = {"status": 1, "message": "Etudiant supprimer !"}
        flash("l'etudinat a est parfaitment supprimer !")
    except Exception as e:
        result = {"status":1,"message": repr(e)}
    return jsonify(result)

        
@app.route("/search", methods=['GET'])
def search():
    query = request.args.get("query")
    entries = db.session.query(Etudiant)  
    if query:
        return render_template("listeEtu.html", entries=entries, query=query)
    return render_template("listeEtu.html")    
 
   
@app.route("/login",  methods= ['GET','POST'])
def login():
    # authentification des utilisateurs et management de la session
    
    error =None
    if request.method == 'POST':
        if request.form["auth_user"] != USERNAME:
            error = "Nom d'utilisateur invalide !"
        elif request.form['auth_pass'] != PASSWD:
            error = "Mot de passe invalide !"
        else:
            session["logged_in"] = True
            flash("Succes connection !")
            return redirect(url_for('listeEtudiant'))
    return render_template("login.html",form=ResiterForm,error=error, )

@app.route("/logout")
def logout():
    #Deconection de l'utilisateur et fermeture de sa session
    session.pop("logged_in",None)
    flash("Merci et a bientôt !")
    return redirect(url_for("login"))
    
@app.route('/listeEtu')
def listeEtudiant():
    filtre = Filtre()
    description =" Liste des etudiants "
    liste = listeDesEtudiant()
    dim =len(liste)
    
    return render_template('listeEtu.html', form = filtre ,
                           dim=dim ,
                           liste =liste,
                           
                           title="Liste des Etudiants ", desc=description)

@app.route('/pres')
def etudiant():
    description =" Information sur l'etudiant "
    infoEtudiant = get_etudiant(1)
    infoClasse = get_classe(infoEtudiant[4])
    
    return render_template('pres.html', 
                           nomEtu= infoEtudiant[0],
                           prenEtu = infoEtudiant[1],
                           sexeEtu = infoEtudiant[2],
                           ageEtu = infoEtudiant[3],
                           classEtu = infoClasse[0],
                           matriEtu = infoEtudiant[5],
                            
                           title="Etudiant",
                           desc=description)

@app.route('/register',methods=['POST','GET'])
def register():
    persone = ResiterForm()
    description =" Enregistrement de l'etudiant "
    
    return render_template('regist.html',form=persone,title="Inscription",desc=description )
""" 

@app.route('/listeEtu')
def listeEtudiant():
    filtre = Filtre()
    description =" Liste des etudiants "
    
    return render_template('listeEtu.html', form = filtre , title="Liste des Etudiants ", desc=description)


@app.route('/register',methods=['POST','GET'])
def register():
    persone = ResiterForm()
    description =" Enregistrement de l'etudiant "
    
    return render_template('regist.html',form=persone,title="Inscription",desc=description )
     """
"""     
@app.route('/submit', methods=['POST'])
def submit_pwd():
    auth_pass = request.form['auth_pass']
    auth_user = request.form['auth_user']
    
    print("le nom du user est : ", auth_user, "le mot de passe est ", auth_pass)
    return render_template('index.html')
 """

""" if __name__ == "__main__":
    app.run() """