from flask import Blueprint

from controllers.teamController import *

team_bp = Blueprint('team_bp',__name__)

team_bp.route('/create', methods=['GET', 'POST'])(create)
team_bp.route('/liste', methods=['GET', 'POST'])(liste)
#team_bp.route('/<name>', methods=['GET', 'POST'])(image)
team_bp.route('/add/<team>', methods=['GET', 'POST'])(addJoueur)
team_bp.route('/<id>', methods=['GET', 'POST'])(info)