from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from view.main import main_bp
from models import db

app = Flask(__name__)

db.init_app(app)

# Enregistrement des Blueprints
app.register_blueprint(main_bp)


if __name__ == '__main__':
    app.run(debug=True)



