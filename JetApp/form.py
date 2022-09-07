
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, RadioField,IntegerField, SelectField, HiddenField
from wtforms.validators import DataRequired



class ResiterForm(FlaskForm):
    nom = StringField('name', validators=[DataRequired()])
    prenom = StringField('prenom', validators=[DataRequired()])
    SalClass = StringField('salClass', validators=[DataRequired()])
    date_nais = IntegerField("date_nais",validators=[DataRequired()])
    sexe = RadioField("sexe",validators=[],choices=["Homme","Femme"])
    boton = SubmitField("Inscription")


class LogForm(FlaskForm):
    username = StringField("usname",validators=[DataRequired()])
    passwd = PasswordField("passwd",validators=[DataRequired()])
    boton = SubmitField("Connection")


class Filtre(FlaskForm):
    salClass = SelectField("Classe",choices=['CM2','CM2'])
    sexe = SelectField("Sexe",choices=['H','M'])
    boton = SubmitField("Filtre")
    
    
class PlusForm(FlaskForm):
    id= HiddenField("id_et",)
    boton = SubmitField("plus")
    
    
class Scan(FlaskForm):
    nom = StringField('name')
    boton = SubmitField("Inscription")