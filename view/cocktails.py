from flask import Blueprint, render_template, jsonify, request
from models import db, StockCocktails

cocktails_bp = Blueprint('cocktails', __name__)


# Route pour récupérer les cocktails (JSON)
@cocktails_bp.route('/api/cocktails', methods=['GET'])
def get_cocktails():
    cocktails = StockCocktails.query.all()
    return jsonify([{
        'id': cocktail.id,
        'name_created': cocktail.name_created,
        'ingredients': cocktail.ingredients,
        'story_describe': cocktail.story_describe,
        'sound_ambiance': cocktail.sound_ambiance,
        'picture_prompt': cocktail.picture_prompt,
        'cocktail_prompt': cocktail.cocktail_prompt
    } for cocktail in cocktails])

# Ajouter un nouveau cocktail via l'API
@cocktails_bp.route('/api/cocktails', methods=['POST'])
def add_cocktail():
    data = request.get_json()
    new_cocktail = StockCocktails(
        name_created=data['name_created'],
        ingredients=data['ingredients'],
        story_describe=data['story_describe'],
        sound_ambiance=data['sound_ambiance'],
        picture_prompt=data['picture_prompt'],
        cocktail_prompt=data['cocktail_prompt']
    )
    db.session.add(new_cocktail)
    db.session.commit()
    return jsonify({'message': 'Cocktail added successfully!'}), 201


# Route pour afficher la page des cocktails (HTML  )
@cocktails_bp.route('/cocktails', methods=['GET'])
def show_cocktails():
    cocktails = StockCocktails.query.all()
    print(f"nb de cocktails: {len(cocktails)}")
    for cocktail in cocktails:
        print(f"Cocktail: {cocktail.name_created}")
    return render_template('cocktails.html', cocktails=cocktails)