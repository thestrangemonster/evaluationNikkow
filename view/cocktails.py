from flask import Blueprint, render_template, jsonify
from models import db, StockCocktails

cocktails_bp = Blueprint('cocktails', __name__)

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