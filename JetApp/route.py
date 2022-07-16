

from os import abort
from .models import Etudiant, db

from config import PASSWD, USERNAME
from .views import app


from flask import  flash, jsonify, redirect, render_template, request, session, url_for

from .form import ResiterForm, Filtre, PlusForm
from .fonction import  listeDesEtudiant
from .gestion import get_message, post_message, Post_etudiant,delet_etudiant, get_classe, get_etudiant, update_etudiant



@app.route('/')
def index():
    
    entries = get_message()
    return render_template('index.html',entries=entries,title="Page d'acceuil")




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
    age = request.form['date_nais']
    print('tttttttttttttttttttttttttttttttttttttttttt')
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
            return redirect(url_for('home'))
    return render_template("login.html",form=ResiterForm,error=error, )











@app.route("/messagerie")
def home():
    entries = get_message()
    return render_template("messageri.html", entries=entries ,title="Page d'acceuil")



@app.route("/addmessage", methods=["POST"])
def add_entry():
    """Adds new post to the database."""
    """ if not session.get("logged_in"):
        abort(401) """
    post_message(request.form["title"], request.form["text"])

    flash("New entry was successfully posted")
    return redirect(url_for("home"))














@app.route("/index")
def logout():
    #Deconection de l'utilisateur et fermeture de sa session
    session.pop("logged_in",None)
    flash("Merci et a bientôt !")
    return redirect(url_for("index"))
    
@app.route('/listeEtu')
def listeEtudiant():
    plus =PlusForm()
    filtre = Filtre()
    description =" Liste des etudiants "
    liste = listeDesEtudiant()
    print(liste)
    dim = 0
    
    
    return render_template('listeEtu.html' ,
                           dim=dim ,
                           liste =liste,
                           plus = plus,
                           
                           
                           title="Liste des Etudiants ", desc=description)



@app.route('/pres', methods=['POST','GET'])
def etudiant():
    
    id = request.form['id_et']
    description =" Information sur l'etudiant "
    infoEtudiant = get_etudiant(id)
    infoClasse = get_classe(infoEtudiant[4])
    
    return render_template('pres.html', 
                           id1 =id,
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


@app.route('/modif',methods=['POST'])
def modif():
    val = request.form['id_et']

    print(val)
    modi = True
    print(modi)
    print(request.form)
    if request.form["submit"]=="Supprimer":
        delet_etudiant(val)
        print("la requette est ok")
        return redirect(url_for("listeEtudiant"))
        
    print("JE SUIS ICICICICICICICICICICICICICICICI")
    infoEtudiant = get_etudiant(val)
    infoClasse = get_classe(infoEtudiant[4])
    formmul = ResiterForm()
    return render_template("pres.html",
                           form = formmul,
                           etudiant = infoEtudiant,
                           classe = infoClasse,
                           val = val,
                           modi=modi) 
    
    
    
@app.route('/update', methods=['post'])
def update():
    dico = {"nom":request.form['lnom'],
            "prenom":request.form['prenom'],
            "classe":request.form['classe'],
            "sexe": request.form['sexe'],
            "age":request.form['lage']}
    print("PUTIN C'EST BON !!!!!!!!!!!!!!!!!!!!!!!!")
    id = request.form['id_et']
    
    update_etudiant(id,dico)
    print (id)
    formul = ResiterForm()
    return redirect(url_for("listeEtudiant"))
    
