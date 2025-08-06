from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from view.main import main_bp
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bar_cocktails.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

db.init_app(app)

# Enregistrement des Blueprints
app.register_blueprint(main_bp)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crée les tables dans la base de données si elles n'existent pas
    # Démarrer l'application Flask  
    app.run(debug=True)



