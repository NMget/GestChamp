from flask import render_template, request, flash, url_for, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import SubmitField, StringField, HiddenField
from wtforms.validators import InputRequired, ValidationError

from models.models import *

class createPoule(FlaskForm):
    id_field = HiddenField()
    name = StringField('Nom', [InputRequired()])
    submit = SubmitField('Créer')

    def validate_name(self, name):
        existing_name = Poule.query.filter_by(name = name.data).first()

        if existing_name:
            raise ValidationError(
                "Une autre poule utilise déjà ce nom, veuillez en choisir un autre."
            )

def create():
    form = createPoule()
    if form.validate_on_submit():
        name = form.name.data
        record = Poule(name)
        db.session.add(record)
        db.session.commit()

        return redirect(url_for('poule_bp.liste'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form, field).label.text,
                    error
                ), 'error')
    
    return render_template('bone.html', title = "Création de poule", H1 = 'Nouvelle poule', content ='create_poule.html', form = form)


def liste():
    poules = Poule.query.order_by(Poule.id)
    return render_template('bone.html', title='Liste des poules', H1 = 'Liste des poules', content='liste_poule.html', poules = poules)


def res(name):
    poule = Poule.query.filter(Poule.name == name).first()
    liaisons = Liaison.query.filter(Liaison.id_poule == poule.id).order_by(Liaison.points.desc())
    matchs = Match.query.filter(Match.id_poule == poule.id, Match.resultat == 0)
    team =Team
    title = 'Résultat poule ' + str(name)
    return render_template('bone.html', title=title, H1 = 'Résultat poule '+ name, content='res.html', poule = poule, liaisons=liaisons, team = team, matchs=matchs)

def match(name):
    poule = Poule.query.filter(Poule.name == name).first()
    liaisons = Liaison.query.filter(Liaison.id_poule == poule.id)
    for i in range(liaisons.count()):
        for j in range(i+1, liaisons.count()):
            record = Match(poule.id, liaisons[i].id_team, liaisons[j].id_team,0)
            db.session.add(record)
            db.session.commit()
    return(redirect(url_for('poule_bp.res', name=name)))

def resMatch(match, team):
    match = Match.query.filter(Match.id == match).first()
    liaison = Liaison.query.filter(Liaison.id_poule == match.id_poule, Liaison.id_team == team).first()
    if match.id_team1 == team:
        match.resultat = 1
    else:
        match.resultat = 2

    liaison.points += 1


    db.session.commit()

    return redirect(url_for('poule_bp.liste'))
