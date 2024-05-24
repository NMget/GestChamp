from flask import Blueprint

from api.controllers.pouleController import *

poule_bp = Blueprint('poule_bp',__name__)

poule_bp.route('/create', methods=['GET', 'POST'])(create)
poule_bp.route('/liste', methods = ['GET', 'POST'])(liste)
poule_bp.route('/<name>', methods=['GET', 'POST'])(res)
poule_bp.route('/match/<name>', methods=['GET', 'POST'])(match)
poule_bp.route('/resMatch/<match>/<team>', methods=['GET', 'POST'])(resMatch)
