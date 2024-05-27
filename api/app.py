from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed

from api.models.models import *


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
    return redirect(url_for('poule_bp.liste'))


if __name__ == '__main__':
    app.run(debug=True)
