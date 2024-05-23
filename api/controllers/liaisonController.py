from flask import render_template, request, flash, url_for, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import SubmitField, StringField, HiddenField, SelectField
from wtforms.validators import InputRequired, ValidationError

from models.models import *

class addTeam(FlaskForm):
    id_field = HiddenField()
    team = SelectField('Equipe', [InputRequired()])
    submit = SubmitField('Enregistrer')

def ajouter(id_poule):
    form = addTeam()
    form.team.choices = [(g.name) for g in Team.query.order_by('name')]
    if form.validate_on_submit():
        poule_id = id_poule
        team = Team.query.filter(Team.name == form.team.data).first()
        team_id = team.id
        record = Liaison(poule_id, team_id, 0)
        db.session.add(record)
        db.session.commit()

        return 'Equipe ' + str(team.name) + ' ajoutée à la poule ' + str(Poule.query.filter(Poule.id == poule_id).first().name)
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form, field).label.text,
                    error
                ), 'error')
    return render_template('bone.html',title='Ajouter une équipe',H1='Ajouter une équipe', content="addTeam.html", form = form)
