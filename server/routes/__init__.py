from flask import Blueprint

# Blueprint'leri içe aktarın
from .select_routes import bp as select_bp
from .update_routes import bp as update_bp
from .delete_routes import bp as delete_bp
from .add_routes import bp as add_bp


def register_blueprints(app):
    app.register_blueprint(select_bp)
    app.register_blueprint(update_bp)
    app.register_blueprint(delete_bp)
    app.register_blueprint(add_bp)
