import requests
import csv
from datetime import datetime

def fetch_mtg_sets():
    """
    Haal alle Magic: The Gathering sets op via de Scryfall API.
    
    Returns:
        list: Een lijst met set objecten van de Scryfall API
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
    
    Args:
        sets_data (list): Lijst met set objecten van de Scryfall API
        
    Returns:
        list: Gesorteerde lijst met verwerkte set data
    """
    processed_sets = []
    
    for set_obj in sets_data:
        # Haal de benodigde velden op
        set_info = {
            "code": set_obj.get("code", ""),
            "name": set_obj.get("name", ""),
            "scryfall_uri": set_obj.get("scryfall_uri", ""),
            "released_at": set_obj.get("released_at", ""),
            "icon_svg_uri": set_obj.get("icon_svg_uri", "")
        }
        processed_sets.append(set_info)
    
    # Sorteer op release datum (oudste eerst)
    processed_sets.sort(key=lambda x: x["released_at"] or "")
    
    return processed_sets

def write_to_csv(sets_data, filename="mtg_sets.csv"):
    """
    Schrijf de verwerkte sets data naar een CSV bestand.
    
    Args:
        sets_data (list): Lijst met verwerkte set data
        filename (str): Naam van het CSV bestand
    """
    # Kolomnamen volgens de opdracht specificatie
    fieldnames = ["code", "name", "scryfall_uri", "released_at", "icon_svg_uri"]
    
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sets_data)
        print(f"CSV bestand succesvol aangemaakt: {filename}")
        print(f"Totaal aantal sets: {len(sets_data)}")
    except IOError as e:
        print(f"Fout bij schrijven naar CSV: {e}")

def main():
    """
    Hoofdfunctie die het hele proces orchestreert.
    """
    print("MTG Sets Exporter - Scryfall API")
    print("=" * 40)
    
    # Stap 1: Haal sets op via API
    print("Sets ophalen via Scryfall API...")
    sets_data = fetch_mtg_sets()
    
    if not sets_data:
        print("Geen data ontvangen. Probeer het later opnieuw.")
        return
    
    print(f"{len(sets_data)} sets ontvangen.")
    
    # Stap 2: Verwerk en sorteer de data
    print("Data verwerken en sorteren...")
    processed_sets = process_sets(sets_data)
    
    # Stap 3: Schrijf naar CSV
    print("Schrijven naar CSV bestand...")
    write_to_csv(processed_sets)
    
    print("Klaar!")

if __name__ == "__main__":
    main()
