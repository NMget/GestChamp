from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed

from models.models import *
from controllers.pouleController import *
from routes.poule_bp import *
from controllers.teamController import *
from routes.team_bp import *
from controllers.liaisonController import *
from routes.liaison_bp import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ahcestgang'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://default:VfXQ8iymq9HM@ep-lively-morning-a4ukm3yw.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"
app.config['SQLACHEMY_TRACK_MODIFICATION'] = False
db.init_app(app)

app.register_blueprint(poule_bp, url_prefix='/poule')
app.register_blueprint(liaison_bp, url_prefix=None)
app.register_blueprint(team_bp, url_prefix='/team')


@app.route("/")
def index():
    return redirect(url_for('poule_bp.liste'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')