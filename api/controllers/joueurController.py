from flask import render_template, request, flash, url_for, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import SubmitField, StringField, HiddenField
from wtforms.validators import InputRequired

from models.models import *

class createJoueur(FlaskForm):
    id_field = HiddenField()
    nom = StringField('Nom', [InputRequired()])
    prenom = StringField('Prénom', [InputRequired()])
    submit = SubmitField('Ajouter')

def create(team):
    form = createJoueur()
    if form.validate_on_submit():
        nom = form.nom.data
        prenom = form.prenom.data
        record(nom, prenom,team)
        db.session.commit()
    return redirect(url_for('team_bp.liste'))