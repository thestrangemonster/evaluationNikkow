from flask import Blueprint, jsonify, request
import requests
import os
import json

responses_bp = Blueprint('responses', __name__)

@responses_bp.route('/api/responses', methods=['POST'])
def generate_response():
    """Générer un cocktail avec Ollama"""
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({'error': 'Le champ prompt est requis'}), 400
    
    prompt = data.get('prompt', '')
    
    try:
        # URL corrigée pour Docker
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
        
        # URL corrigée : /api/generate au lieu de /generate
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
        
        # Gestion plus robuste du parsing JSON
        try:
            cocktail_data = json.loads(ollama_data['response'])
        except (json.JSONDecodeError, KeyError):
            # Si le parsing échoue, renvoyer la réponse brute
            return jsonify({
                'error': 'Format de réponse Ollama invalide',
                'raw_response': ollama_data.get('response', 'Pas de réponse')
            }), 500
        
        # Ajouter le prompt original
        cocktail_data['cocktail_prompt'] = prompt
        
        return jsonify(cocktail_data), 200
        
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Erreur connexion Ollama: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Erreur générale: {str(e)}'}), 500

@responses_bp.route('/api/responses/test', methods=['GET'])
def test_ollama_connection():
    """Tester la connexion à Ollama"""
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