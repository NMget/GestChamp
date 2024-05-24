from flask import Blueprint

from api.controllers.liaisonController import *

liaison_bp = Blueprint('liaison_bp',__name__)

liaison_bp.route('/addTeam/<id_poule>', methods=['GET', 'POST'])(ajouter)
