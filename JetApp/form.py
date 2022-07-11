from tkinter import N
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, RadioField
from wtforms.validators import DataRequired


class ResiterForm(FlaskForm):
    nom = StringField('name', validators=[DataRequired()])
    prenom = StringField('prenom', validators=[DataRequired()])
    SalClass = StringField('salClass', validators=[DataRequired()])
    date_nais = DateField("date_nais",validators=[DataRequired()],format="%d-%m-%Y")
    sexe = RadioField("sexe",validators=[],choices=["H","F"])
    boton = SubmitField("Inscription")