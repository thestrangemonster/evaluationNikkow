Le Mixologue Augmenté 🍹
Un générateur de cocktails personnalisés utilisant l'intelligence artificielle avec Flask et Ollama.

Description
Ce projet permet de créer des cocktails uniques en décrivant simplement ce que vous souhaitez. L'IA génère une recette complète avec les ingrédients, l'histoire du cocktail, l'ambiance musicale et une description pour l'image.

Technologies utilisées
Flask : Framework web Python
Jinja2 : Moteur de templates
SQLite : Base de données
Ollama : IA locale pour la génération de contenu
Docker : Containerisation
Bootstrap : Interface utilisateur
Architecture
Le projet utilise deux conteneurs Docker :

flask-app : Application web Flask
ollama : Serveur IA Ollama avec le modèle llama3.2
Installation et lancement
Prérequis
Docker
Docker Compose

Étapes

1 ## Cloner le projet
git clone <votre-repo>
cd testNico
2 ## Lancer l'application
docker-compose up --build
3 ## Accéder à l'application
Interface web : http://localhost:5000
API : http://localhost:5000/api/cocktails

## Utilisation
Créer un cocktail : Décrivez votre cocktail idéal sur la page d'accueil
Génération automatique : L'IA crée une recette unique
Consultation : Retrouvez tous vos cocktails dans "Mes Cocktails"
Suppression : Supprimez les cocktails que vous ne souhaitez plus garder
## Structure du projet
 testNico/
├── view/
│   ├── main.py          # Routes principales
│   ├── cocktails.py     # Gestion des cocktails
│   └── responses.py     # Génération IA
├── templates/
│   ├── base.html        # Template de base
│   ├── home.html        # Page d'accueil
│   └── cocktails.html   # Liste des cocktails
├── models.py            # Modèles de base de données
├── app.py               # Application principale
├── docker-compose.yml   # Configuration des conteneurs
└── requirements.txt     # Dépendances Python

## API
GET /api/cocktails : Récupérer tous les cocktails
POST /api/cocktails : Créer un nouveau cocktail
DELETE /api/cocktails/<id> : Supprimer un cocktail
GET /api/responses/test : Tester la connexion Ollama

## Configuration
Les variables d'environnement sont configurées dans docker-compose.yml :

SQLALCHEMY_DATABASE_URI : Chemin de la base de données
OLLAMA_URL : URL du serveur Ollama
SECRET_KEY : Clé secrète Flask

## Notes techniques
La base de données SQLite est créée automatiquement au premier lancement
Le modèle Ollama llama3.2 est téléchargé automatiquement
L'application fonctionne sans GPU (mode CPU)

## Dépannage
Erreur 404 sur les styles : Normal, Bootstrap est chargé via CDN
Génération lente : Premier appel plus long (téléchargement du modèle)
Problème de connexion Ollama : Vérifier avec /api/responses/test

## Développement
Pour développer en local sans Docker :

pip install -r requirements.txt
export SQLALCHEMY_DATABASE_URI=sqlite:///bar_cocktails.db
python app.py


### Projet réalisé dans le cadre d'un apprentissage de Flask et Docker