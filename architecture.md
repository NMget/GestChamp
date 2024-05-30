# Architecture de l'Application de Gestion de Tournoi de Volley

## Introduction

Cette documentation décrit l'architecture de l'application web de gestion de tournoi de volley, y compris les composants principaux, les modèles de données, les schémas de base de données et les interactions entre les différentes parties de l'application.

## Composants Principaux

L'application est divisée en plusieurs composants principaux :

1. **Frontend** : Interface utilisateur développée avec HTML, CSS et JavaScript.
2. **Backend** : Application serveur développée avec Flask (Python) qui gère la logique métier et les interactions avec la base de données.
3. **Base de données** : PostgreSQL utilisée pour stocker toutes les données de l'application.
4. **ORM** : SQLAlchemy utilisé pour interagir avec la base de données de manière déclarative.

## Modèle de Données

### Schéma de Base de Données

Le schéma de base de données comprend les tables suivantes :

- **Team** : Stocke les informations sur les équipes.
- **Player** : Stocke les informations sur les joueurs.
- **Group** : Stocke les informations sur les poules.
- **TeamGroup** : Stocke les liaisons entre les équipes et les poules.
- **Match** : Stocke les informations sur les matchs.

### Diagramme de la Base de Données

```plaintext
+------------------+
|      Team        |
+------------------+
| id (PK)          |
| name             |
| photo            |
+------------------+

+------------------+
|     Joueur       |
+------------------+
| id (PK)          |
| nom              |
| prenom           |
| id_team (FK)     |
+------------------+

+------------------+
|     Poule        |
+------------------+
| id (PK)          |
| name             |
+------------------+

+------------------+
|     Liaison      |
+------------------+
| id (PK)          |
| id_poule (FK)    |
| id_team  (FK)    |
| points           |
+------------------+

+------------------+
|      Match       |
+------------------+
| id (PK)          |
| id_poule (FK)    |
| id_team1 (FK)    |
| id_team2 (FK)    |
| resultat         |
+------------------+
```

### Relations entre les Tables

- Une équipe peut avoir plusieurs joueurs (relation un-à-plusieurs entre `Team` et `Joueur`).
- Une poule peut contenir plusieurs équipes (relation plusieurs-à-plusieurs entre `Poule` et `Team`, gérée par la table `Liaison`).
- Une poule peut avoir plusieurs matchs (relation un-à-plusieurs entre `Poule` et `Match`).
- Chaque match implique deux équipes (relation plusieurs-à-un entre `Match` et `Team`).

## Description des Classes

### Team

Représente une équipe participant au tournoi.

```python
class Team(db.Model):
    __tablename__ = "team"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    photo = db.Column(db.String)
    liaison = db.relationship("Liaison", backref='team')
    joueur = db.relationship("Joueur", backref='team')
```

### Joueur

Représente un joueur appartenant à une équipe.

```python
class Joueur(db.Model):
    __tablename__ = "joueur"
    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String)
    prenom = db.Column(db.String)
    id_team = db.Column(db.Integer, db.ForeignKey('team.id'))
```

### Poule

Représente une poule dans le tournoi.

```python
class Poule(db.Model):
    __tablename__="poule"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    liaison = db.relationship("Liaison", backref='poule')
    match = db.relationship("Match", backref='poule')
```

### Liaison

Gère la liaison entre les équipes et les poules, et stocke les points accumulés.

```python
class Liaison(db.Model):
    __tablename__ = "liaison"
    id = db.Column(db.Integer, primary_key = True)
    id_poule = db.Column(db.Integer, db.ForeignKey('poule.id'))
    id_team = db.Column(db.Integer, db.ForeignKey('team.id'))
    points = db.Column(db.Integer)
```

### Match

Représente un match entre deux équipes dans une poule.

```python
class Match(db.Model):
    __tablename__ = "match"
    id = db.Column(db.Integer, primary_key = True)
    id_poule = db.Column(db.Integer, db.ForeignKey('poule.id'))
    id_team1 = db.Column(db.Integer, db.ForeignKey('team.id'))
    id_team2 = db.Column(db.Integer, db.ForeignKey('team.id'))
    resultat = db.Column(db.Integer)
```

## Flux de Données

1. **Création d'Équipe et de Joueur** :
   - L'utilisateur soumet un formulaire de création d'équipe.
   - L'application enregistre l'équipe dans la base de données.
   - L'utilisateur peut ensuite ajouter des joueurs à cette équipe.

2. **Création de Poule et Assignation d'Équipes** :
   - L'utilisateur crée une poule via un formulaire.
   - L'utilisateur assigne des équipes à la poule.
   - Les liaisons sont enregistrées dans la table `Liaison`.

3. **Génération de Matchs** :
   - L'utilisateur sélectionne une poule pour laquelle générer des matchs.
   - L'application génère les matchs et les enregistre dans la table `Match`.

4. **Enregistrement des Résultats** :
   - L'utilisateur enregistre les résultats des matchs joués.
   - L'application met à jour les points des équipes en fonction des résultats.

## Conclusion

Cette architecture modulaire et bien structurée permet une gestion efficace et évolutive des tournois de volley. Chaque composant et relation a été conçu pour faciliter la gestion des équipes, des joueurs, des poules et des matchs, tout en offrant une interface utilisateur intuitive et facile à utiliser.
