from flask import Blueprint

from .get import get_bp
from .create import create_bp
from .update import update_bp

traffic_bp = Blueprint('traffic', __name__)

traffic_bp.register_blueprint(get_bp)
traffic_bp.register_blueprint(create_bp)
traffic_bp.register_blueprint(update_bp)
