from flask import Flask, render_template, jsonify
import requests
from datetime import datetime
import os

app = Flask(__name__, static_folder='static')

def fetch_mtg_sets():
    """
    Haal alle Magic: The Gathering sets op via de Scryfall API.
    """
    url = "https://api.scryfall.com/sets"
    headers = {
        "User-Agent": "MTG_Skill_Heroes_Project/1.0",
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("data", [])
    except requests.exceptions.RequestException as e:
        print(f"Fout bij ophalen van data: {e}")
        return []

def process_sets(sets_data):
    """
    Verwerk de sets data en sorteer op release datum.
    """
    processed_sets = []
    
    for set_obj in sets_data:
        set_info = {
            "code": set_obj.get("code", ""),
            "name": set_obj.get("name", ""),
            "scryfall_uri": set_obj.get("scryfall_uri", ""),
            "released_at": set_obj.get("released_at", ""),
            "icon_svg_uri": set_obj.get("icon_svg_uri", ""),
            "set_type": set_obj.get("set_type", ""),
            "card_count": set_obj.get("card_count", 0)
        }
        processed_sets.append(set_info)
    
    # Sorteer op release datum (oudste eerst)
    processed_sets.sort(key=lambda x: x["released_at"] or "")
    
    return processed_sets

@app.route('/')
def index():
    """
    Hoofdpagina met overzicht van alle MTG sets.
    """
    sets_data = fetch_mtg_sets()
    processed_sets = process_sets(sets_data)
    return render_template('index.html', sets=processed_sets)

@app.route('/api/sets')
def api_sets():
    """
    API endpoint die alle sets als JSON teruggeeft.
    """
    sets_data = fetch_mtg_sets()
    processed_sets = process_sets(sets_data)
    return jsonify(processed_sets)

@app.route('/set/<set_code>')
def set_detail(set_code):
    """
    Detailpagina voor een specifieke set.
    """
    sets_data = fetch_mtg_sets()
    processed_sets = process_sets(sets_data)
    
    # Zoek de specifieke set
    set_detail = next((s for s in processed_sets if s["code"] == set_code), None)
    
    if set_detail:
        return render_template('set_detail.html', set=set_detail)
    else:
        return "Set niet gevonden", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
