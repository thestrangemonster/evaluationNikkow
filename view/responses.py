from flask import Blueprint, jsonify, request, render_template, redirect, url_for
import requests
import os
import json
from models import db, StockCocktails

responses_bp = Blueprint('responses', __name__)

# Route pour générer et sauvegarder un cocktail via formulaire HTML
@responses_bp.route('/generate', methods=['POST'])
def generate_and_save_cocktail():
    """Générer un cocktail avec Ollama et le sauvegarder en BDD"""
    prompt = request.form.get('prompt', '').strip()
    
    if not prompt:
        return redirect(url_for('main.index', error='Veuillez saisir une demande'))
    
    try:
        # Générer le cocktail avec Ollama
        ollama_api_url = os.getenv('OLLAMA_URL', 'http://ollama:11434')
        
        system_prompt = """Tu es un expert mixologue créatif. Génère un cocktail basé sur la demande de l'utilisateur.
        Réponds UNIQUEMENT au format JSON suivant :
        {
            "name_created": "nom créatif du cocktail",
            "ingredients": "liste des ingrédients séparés par des virgules",
            "story_describe": "description créative du cocktail et son histoire",
            "sound_ambiance": "type de musique qui accompagne ce cocktail",
            "picture_prompt": "prompt en anglais pour générer une image du cocktail"
        }"""
        
        ollama_response = requests.post(
            f"{ollama_api_url}/api/generate",
            json={
                "model": "llama3.2",
                "prompt": f"{system_prompt}\n\nDemande utilisateur: {prompt}",
                "format": "json",
                "stream": False
            },
            timeout=60
        )
        
        if ollama_response.status_code != 200:
            return redirect(url_for('main.index', error=f'Erreur Ollama: {ollama_response.status_code}'))
        
        ollama_data = ollama_response.json()
        
        # Parser la réponse JSON
        try:
            cocktail_data = json.loads(ollama_data['response'])
        except:
            return redirect(url_for('main.index', error='Erreur de format de réponse'))
        
        # Sauvegarder en base de données
        new_cocktail = StockCocktails(
            name_created=cocktail_data.get('name_created', 'Cocktail Sans Nom'),
            ingredients=cocktail_data.get('ingredients', 'Ingrédients non spécifiés'),
            story_describe=cocktail_data.get('story_describe', 'Histoire non disponible'),
            sound_ambiance=cocktail_data.get('sound_ambiance', 'Ambiance non spécifiée'),
            picture_prompt=cocktail_data.get('picture_prompt', 'Image non disponible'),
            cocktail_prompt=prompt
        )
        
        db.session.add(new_cocktail)
        db.session.commit()
        
        # Rediriger vers la page des cocktails
        return redirect(url_for('cocktails.show_cocktails'))
        
    except Exception as e:
        return redirect(url_for('main.index', error=f'Erreur: {str(e)}'))

# Garder vos routes API existantes...
@responses_bp.route('/api/responses', methods=['POST'])
def generate_response():
    """Générer un cocktail avec Ollama (API JSON)"""
    # ... votre code existant ...
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({'error': 'Le champ prompt est requis'}), 400
    
    prompt = data.get('prompt', '')
    
    try:
        ollama_api_url = os.getenv('OLLAMA_URL', 'http://ollama:11434')
        
        system_prompt = """Tu es un expert mixologue créatif. Génère un cocktail basé sur la demande de l'utilisateur.
        Réponds UNIQUEMENT au format JSON suivant :
        {
            "name_created": "nom créatif du cocktail",
            "ingredients": "liste des ingrédients séparés par des virgules",
            "story_describe": "description créative du cocktail et son histoire",
            "sound_ambiance": "type de musique qui accompagne ce cocktail",
            "picture_prompt": "prompt en anglais pour générer une image du cocktail"
        }"""
        
        ollama_response = requests.post(
            f"{ollama_api_url}/api/generate",
            json={
                "model": "llama3.2",
                "prompt": f"{system_prompt}\n\nDemande utilisateur: {prompt}",
                "format": "json",
                "stream": False
            },
            timeout=60
        )
        
        if ollama_response.status_code != 200:
            return jsonify({'error': f'Erreur Ollama: {ollama_response.status_code}'}), 500
        
        ollama_data = ollama_response.json()
        
        try:
            cocktail_data = json.loads(ollama_data['response'])
        except:
            return jsonify({
                'error': 'Format de réponse Ollama invalide',
                'raw_response': ollama_data.get('response', 'Pas de réponse')
            }), 500
        
        cocktail_data['cocktail_prompt'] = prompt
        return jsonify(cocktail_data), 200
        
    except Exception as e:
        return jsonify({'error': f'Erreur: {str(e)}'}), 500

@responses_bp.route('/api/responses/test', methods=['GET'])
def test_ollama_connection():
    # ... votre code existant ...
    try:
        ollama_api_url = os.getenv('OLLAMA_URL', 'http://ollama:11434')
        response = requests.get(f'{ollama_api_url}/api/tags', timeout=10)
        
        if response.status_code == 200:
            return jsonify({
                'status': 'connected',
                'message': 'Ollama est accessible',
                'models': response.json()
            })
        else:
            return jsonify({'status': 'error', 'message': f'Status: {response.status_code}'}), 500
            
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500