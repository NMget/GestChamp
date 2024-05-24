from flask import render_template, request, flash, url_for, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import SubmitField, StringField, HiddenField
from wtforms.validators import InputRequired

from api.models.models import *

class UploadForm(FlaskForm):
    id_filed = HiddenField()
    name = StringField('Nom', [InputRequired()])
    photo = FileField('Logo', validators=[
        FileAllowed(['jpg', 'png', 'jpeg', 'svg'], 'Seuls les fichiers images sont autorisés!')
    ])
    submit = SubmitField('Ajouter')

class createJoueur(FlaskForm):
    id_field = HiddenField()
    nom = StringField('Nom', [InputRequired()])
    prenom = StringField('Prénom', [InputRequired()])
    submit = SubmitField('Ajouter')


def create():
    form = UploadForm()
    if form.validate_on_submit():
        name = form.name.data
        photo = form.photo.data
        path = str(photo.filename)
        photo.save("static/{}".format(photo.filename))
        record = Team(name, path)
        db.session.add(record)
        db.session.commit()
        
        return "equipe crée avec succès!"
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form, field).label.text,
                    error
                ), 'error')
    return render_template("bone.html", title="Créer une équipe", H1="Nouvelle équipe", content="create_team.html", form = form)

def liste():
    teams_with_poules = Liaison.query.join(Team).join(Poule).all()
    
    teams_dict = {}
    for liaison in teams_with_poules:
        if liaison.team not in teams_dict:
            teams_dict[liaison.team] = {'team': liaison.team, 'poules': []}
        teams_dict[liaison.team]['poules'].append(liaison.poule)

    return render_template('bone.html', title="Liste des équipes", H1="Liste des équipes", content="liste_team.html", teams_dict=teams_dict)

def addJoueur(team):
    form = createJoueur()
    if form.validate_on_submit():
        nom = form.nom.data
        prenom = form.prenom.data
        record = Joueur(nom, prenom,team)
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('team_bp.liste'))
    return render_template('bone.html', title = 'Ajouter un joueur', content="createJoueur.html", form=form)

def info(id):
    joueurs = Joueur.query.filter(Joueur.id_team == id)
    return render_template('bone.html', title = 'Infos', content='info_team.html', joueurs=joueurs)
