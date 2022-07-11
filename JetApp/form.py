from tkinter import N
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, RadioField, SelectField
from wtforms.validators import DataRequired



class ResiterForm(FlaskForm):
    nom = StringField('name', validators=[DataRequired()])
    prenom = StringField('prenom', validators=[DataRequired()])
    SalClass = StringField('salClass', validators=[DataRequired()])
    date_nais = DateField("date_nais",validators=[DataRequired()],format="%d-%m-%Y")
    sexe = RadioField("sexe",validators=[],choices=["Homme","Femme"])
    boton = SubmitField("Inscription")
    
class Filtre(FlaskForm):
    salClass = SelectField("Classe",choices=['CM2','CM2'])
    sexe = SelectField("Sexe",choices=['H','M'])
    boton = SubmitField("Filtre")
    
class Scan(FlaskForm):
    nom = StringField('name')
    boton = SubmitField("Inscription")