from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # SQLAlchemy ve CORS'i başlatıyoruz
    db.init_app(app)
    CORS(app)

    # Blueprint'leri kaydediyoruz
    from routes import select_routes, update_routes, delete_routes, add_routes

    app.register_blueprint(select_routes.bp)
    app.register_blueprint(update_routes.bp)
    app.register_blueprint(delete_routes.bp)
    app.register_blueprint(add_routes.bp)

    # Veritabanı tablolarını oluşturuyoruz (sadece ilk çalıştırmada gerekli)
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=5001, debug=True)
