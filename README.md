# Read-me

<center>Vous pouvez modifier ce fichier (cf. Brief)</center>

## Comment gérer cette évaluation ?

1. Le rendu s'effectuera **uniquement** au travers de Github Classroom (clonez bien le repository créé par Github Classroom, et travaillez dedans. N'en recréez pas un nouveau). 
2. Une Pull-Request est automatiquement générée par Github Classroom, **ne la fermez pas**. Elle me permettra de vous faire un feedback sous forme de code annoté. 
3. Mettez-vous en condition d'une mise en situation professionnelle : le client (fictif, bien entendu) attend une app fonctionnelle qui répond au besoin énoncé, c'est tout :) 
4. Lisez bien l'entièreté du brief avant de démarrer, n'hésitez pas à poser votre architecture sur papier (ou du moins à y réfléchir sur un support autre que l'IDE) avant de coder. 

➡️ [Cliquez ici pour lire le brief du client](BRIEF.md)

docker-compose up --build flask-app

# Le Mixologue Augmenté

Application Flask pour générer des cocktails créatifs avec l'IA.

## Comment gérer cette évaluation ?

1. Le rendu s'effectuera **uniquement** au travers de Github Classroom
2. Une Pull-Request est automatiquement générée par Github Classroom, **ne la fermez pas**
3. Mettez-vous en condition d'une mise en situation professionnelle
4. Lisez bien l'entièreté du brief avant de démarrer

➡️ [Cliquez ici pour lire le brief du client](BRIEF.md)

## Démarrage avec Docker

```bash
# Construire et démarrer l'application
docker-compose up --build flask-app

# En arrière-plan
docker-compose up -d --build flask-app

# Voir les logs
docker-compose logs -f flask-app

# Arrêter le service
docker-compose down
```

## Démarrage en développement local

```bash
# Activer l'environnement virtuel
source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Démarrer l'application
python app.py
```

## Accès

- Application web : http://localhost:5000
- API REST : http://localhost:5000/api/cocktails
- Documentation : [Voir le brief](BRIEF.md)

## Test de l'API avec Insomnia

Voir les exemples dans [`testApiWithIsomnia.md`](testApiWithIsomnia.md)