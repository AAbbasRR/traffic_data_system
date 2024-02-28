from flask import Blueprint

from .traffic import traffic_bp

v1_bp = Blueprint('v1', __name__)
v1_bp.register_blueprint(traffic_bp, url_prefix='/traffic')
