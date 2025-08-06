from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from view.main import main_bp
from view.cocktails import cocktails_bp
from models import db
import os

app = Flask(__name__)

# Configuration de l'application pour Docker
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 
    'sqlite:///bar_cocktails.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

db.init_app(app)

# Enregistrement des Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(cocktails_bp)


if __name__ == '__main__':
    with app.app_context():
        os.makedirs('data', exist_ok=True)  # Crée le dossier data s'il n'existe pas
        db.create_all()  # Crée les tables dans la base de données si elles n'existent pas
    # Démarrer l'application Flask  
    app.run(debug=True, host='0.0.0.0', port=5000) # Exécute l'application sur toutes les interfaces réseau pour Docker



