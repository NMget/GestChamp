


# Gestion de Tournoi de Volley

Cette application web permet de gérer les tournois de volley de manière efficace. Elle offre des fonctionnalités de création de poules, de joueurs et d'équipes, de génération automatique de planning de match et de classement automatique des équipes suivant leur nombre de points.

## Fonctionnalités

- **Création de poules** : Créez des groupes de compétition pour structurer les tournois.
- **Création de joueurs et d'équipes** : Gérez les joueurs et les équipes avec des formulaires interactifs.
- **Génération de planning de match** : Génération automatique des rencontres entre équipes suivant les poules.
- **Classement automatique** : Mise à jour des points et classement des équipes en fonction des résultats des matchs.

## Technologies Utilisées

- **Framework** : Flask (Python)
- **ORM** : SQLAlchemy
- **SGBD** : PostgreSQL
- **Outil d'administration** : PGAdmin

## Installation

### Prérequis

- Python 3.x
- PostgreSQL
- Virtualenv

### Étapes

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/NMget/GestChamp.git
   cd GestChamp
   ```

2. Créez un environnement virtuel et activez-le :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Pour Windows, utilisez `venv\Scripts\activate`
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Configurez la base de données PostgreSQL :
   - Créez une base de données `volley_tournament`.
   - Mettez à jour l'URI de la base de données dans `app.py` :
     ```python
     SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/volley_tournament'
     ```

5. Initialisez la base de données :
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

6. Lancez l'application :
   ```bash
   flask run
   ```

7. Accédez à l'application via `http://127.0.0.1:5000`.

## Utilisation

### Création d'Équipe

1. Accédez à la page de création d'équipe.
2. Remplissez le formulaire avec le nom de l'équipe et l'URL de son logo.
3. Soumettez le formulaire pour enregistrer l'équipe.

### Création de Joueur

1. Accédez à la page de création de joueur.
2. Remplissez le formulaire avec les informations du joueur et sélectionnez son équipe.
3. Soumettez le formulaire pour enregistrer le joueur.

### Création de Poule

1. Accédez à la page de création de poule.
2. Remplissez le formulaire avec le nom de la poule.
3. Soumettez le formulaire pour enregistrer la poule.

### Assignation des Équipes aux Poules

1. Accédez à la page de gestion des poules.
2. Sélectionnez les équipes à assigner à chaque poule.
3. Soumettez le formulaire pour enregistrer les assignations.

### Génération de Matchs

1. Accédez à la page de génération de matchs.
2. Sélectionnez la poule pour laquelle vous souhaitez générer les matchs.
3. Cliquez sur le bouton pour générer les matchs automatiquement.

### Mise à Jour des Résultats et Classement

1. Accédez à la page de gestion des matchs.
2. Enregistrez les résultats des matchs joués.
3. Le classement des équipes sera mis à jour automatiquement en fonction des résultats.

## Contributions

Les contributions sont les bienvenues ! Veuillez suivre les étapes suivantes pour contribuer :

1. Forkez le dépôt.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalite`).
3. Commitez vos changements (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`).
4. Poussez vos changements (`git push origin feature/ma-fonctionnalite`).
5. Ouvrez une Pull Request.

## License

Ce projet est sous licence MIT. Veuillez consulter le fichier LICENSE pour plus d'informations.

## Auteurs

- [MEGNET Noah](https://github.com/NMget)

Merci d'utiliser notre application de gestion de tournoi de volley !

