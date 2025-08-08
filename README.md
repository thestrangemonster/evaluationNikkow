# Le Mixologue Augmenté 🍹

Un générateur de cocktails personnalisés utilisant l'intelligence artificielle avec Flask et Ollama.

## Description

Ce projet permet de créer des cocktails uniques en décrivant simplement ce que vous souhaitez. L'IA génère une recette complète avec les ingrédients, l'histoire du cocktail, l'ambiance musicale et une description pour l'image.

## Technologies utilisées

- **Flask** : Framework web Python
- **Jinja2** : Moteur de templates
- **SQLite** : Base de données
- **Ollama** : IA locale pour la génération de contenu
- **Docker** : Containerisation
- **Bootstrap** : Interface utilisateur


## Étapes

### 1. Cloner le projet

```bash
git clone https://github.com/thestrangemonster/evaluationNikkow.git
cd evaluationNikkow
```

### 2. Lancer l'application

```bash
docker-compose up --build
```

⚠️ **Premier démarrage** : Le téléchargement du modèle llama3.2 (~2GB) peut prendre quelques minutes selon votre connexion.

### 3. Accéder à l'application

- **Interface web** : http://localhost:5000
- **API** : http://localhost:5000/api/cocktails

### 4. (Optionnel) Vérifier que tout fonctionne

- Test de l'IA : http://localhost:5000/api/responses/test
- Doit retourner `{"status": "Ollama is working!"}`

## Utilisation
- Créer un cocktail : Décrivez votre cocktail idéal sur la page d'accueil
- Génération automatique : L'IA crée une recette unique
- Consultation : Retrouvez tous vos cocktails dans "Mes Cocktails"
- Suppression : Supprimez les cocktails que vous ne souhaitez plus garder


### Architecture des fichiers :
```
testNico/
├── view/
│   ├── main.py          # Routes principales (Blueprint)
│   ├── cocktails.py     # CRUD cocktails (Blueprint)  
│   └── responses.py     # Intégration IA (Blueprint)
├── templates/
│   ├── base.html        # Template de base
│   ├── home.html        # Page génération
│   └── cocktails.html   # Liste cocktails
├── models.py            # Modèle SQLAlchemy
├── app.py               # Point d'entrée
└── docker-compose.yml   # Configuration conteneurs
```

## API
- **GET /api/cocktails** : Récupérer tous les cocktails
- **POST /api/cocktails** : Créer un nouveau cocktail
- **DELETE /api/cocktails/<id>** : Supprimer un cocktail
- **GET /api/responses/test** : Tester la connexion Ollama

## Workflow Applicatif

### Processus de génération :
1. **Saisie utilisateur** → Formulaire HTML (home.html)
2. **Traitement Flask** → Route `/generate` (responses.py)
3. **Appel IA** → Ollama via API REST
4. **Parsing JSON** → Extraction des données structurées
5. **Sauvegarde** → SQLite via SQLAlchemy
6. **Affichage** → Redirection vers liste (cocktails.html)

### Communication inter-services :
```
[Navigateur] ←→ [Flask:5000] ←→ [Ollama:11434]
                      ↓
                 [SQLite DB]
```
## Stratégie de Test

### API de test intégrée :
- `GET /api/cocktails` : Vérification des données sauvegardées
- `GET /api/responses/test` : Test de connectivité Ollama
- `POST /api/cocktails` : Création manuelle de cocktails

### Validation des données :
- **Côté client** : Validation HTML5 (champs requis)
- **Côté serveur** : Gestion d'erreurs et fallbacks
- **Format IA** : Validation JSON stricte des réponses Ollama 

## Configuration

Les variables d'environnement sont configurées dans docker-compose.yml :

- **SQLALCHEMY_DATABASE_URI** : Chemin de la base de données
- **OLLAMA_URL** : URL du serveur Ollama
- **SECRET_KEY** : Clé secrète Flask

## Notes techniques
- La base de données SQLite est créée automatiquement au premier lancement
- Le modèle Ollama llama3.2 est téléchargé automatiquement
- L'application fonctionne sans GPU (mode CPU)

## Dépannage

### Problèmes courants :

**🔄 Premier démarrage lent**
- Le modèle llama3.2 (~2GB) se télécharge automatiquement
- Attendez que les logs affichent `"llama runner started"`

**🔗 Erreur de connexion Ollama**
- Vérifiez : http://localhost:5000/api/responses/test
- Si échec, redémarrez : `docker-compose restart ollama`

**🎨 Erreur 404 sur les styles**
- Normal, Bootstrap est chargé via CDN
- Vérifiez votre connexion internet

**🐳 Téléchargement manuel du modèle**
```bash
# Si le téléchargement automatique échoue
docker-compose exec ollama ollama pull llama3.2
```

**🗄️ Base de données vide**
- La base SQLite se crée automatiquement
- Vérifiez le dossier `instance/` local

## Développement

### Pour développer en local sans Docker :

- pip install -r requirements.txt
- export SQLALCHEMY_DATABASE_URI=sqlite:///bar_cocktails.db
- python app.py


Cette architecture minimaliste répond parfaitement au besoin identifié tout en conservant des possibilités d'évolution futures.

 *Projet réalisé dans le cadre d'un apprentissage de Flask et Docker*