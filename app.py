from flask import Flask, jsonify
from api import api_bp
from decouple import config
import os

DEBUG = config("DEBUG", default=False, cast=bool)
app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_dir, "db.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Register Blueprints
app.register_blueprint(api_bp, url_prefix='/api')

if DEBUG is False:
    @app.errorhandler(Exception)
    def handle_error(e):
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=DEBUG)
