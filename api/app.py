from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Team(db.Model):
    __tablename__ = "team"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    photo = db.Column(db.String)
    liaison = db.relationship("Liaison", backref='team')
    joueur = db.relationship("Joueur", backref='team')


    def __init__(self, name, photo):
        self.name = name
        self.photo = photo

class Poule(db.Model):
    __tablename__="poule"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    liaison = db.relationship("Liaison", backref='poule')
    match = db.relationship("Match", backref='poule')

    def __init__(self, name):
        self.name = name

class Liaison(db.Model):
    __tablename__ = "liaison"
    id = db.Column(db.Integer, primary_key = True)
    id_poule = db.Column(db.Integer, db.ForeignKey('poule.id'))
    id_team = db.Column(db.Integer, db.ForeignKey('team.id'))
    points = db.Column(db.Integer)

    def __init__(self, id_poule, id_team, points):
        self.id_poule = id_poule
        self.id_team = id_team
        self.points = points

class Joueur(db.Model):
    __tablename__ = "joueur"
    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String)
    prenom = db.Column(db.String)
    id_team = db.Column(db.Integer, db.ForeignKey('team.id'))

    def __init__(self, nom, prenom, id_team):
        self.nom = nom
        self.prenom = prenom
        self.id_team = id_team

class Match(db.Model):
    __tablename__ = "match"
    id = db.Column(db.Integer, primary_key = True)
    id_poule = db.Column(db.Integer, db.ForeignKey('poule.id'))
    id_team1 = db.Column(db.Integer, db.ForeignKey('team.id'))
    id_team2 = db.Column(db.Integer, db.ForeignKey('team.id'))
    resultat = db.Column(db.Integer)

    team1 = db.relationship('Team', foreign_keys=[id_team1], backref=db.backref('matches_as_team1', lazy=True))
    team2 = db.relationship('Team', foreign_keys=[id_team2], backref=db.backref('matches_as_team2', lazy=True))

    def __init__(self, id_poule, id_team1, id_team2, resultat):
        self.id_poule = id_poule
        self.id_team1 = id_team1
        self.id_team2 = id_team2
        self.resultat = resultat


from api.controllers.pouleController import *
from api.routes.poule_bp import *
from api.controllers.teamController import *
from api.routes.team_bp import *
from api.controllers.liaisonController import *
from api.routes.liaison_bp import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ahcestgang'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://default:VfXQ8iymq9HM@ep-lively-morning-a4ukm3yw-pooler.us-east-1.aws.neon.tech:5432/verceldb"
app.config['SQLACHEMY_TRACK_MODIFICATION'] = False
db.init_app(app)

app.register_blueprint(poule_bp, url_prefix='/poule')
app.register_blueprint(liaison_bp, url_prefix=None)
app.register_blueprint(team_bp, url_prefix='/team')


@app.route("/")
def index():
    return 'oui baguette'


if __name__ == '__main__':
    app.run(debug=True)
