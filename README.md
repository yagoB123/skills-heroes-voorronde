# MTG Sets Web App

Hey! Dit is mijn project voor de lokale spellenwinkel "You Lost The Game". Ze wilden een website om Magic: The Gathering sets te laten zien aan nieuwe spelers, dus heb ik dit gemaakt met de Scryfall API.

## Wat doet het?

- Haalt alle MTG sets op via Scryfall API
- Laat zien in een mooie website met zoekfunctie
- Kan ook data exporteren naar CSV
- Elke set heeft zijn eigen detailpagina

## Hoe te gebruiken?

### Eerst even installeren:

1. Installeer Python (3.7+) als je dat nog niet hebt
2. Maak een virtuele omgeving:
   ```bash
   python -m venv venv
   ```
3. Activeer hem:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Installeer de packages:
   ```bash
   pip install -r requirements.txt
   ```

### De app starten:

```bash
python app.py
```

Dan open je `http://localhost:5000` in je browser en klaar!

## CSV export

Als je gewoon de CSV wilt (zoals in de originele opdracht):

```bash
python mtg_sets_export.py
```

Dat maakt een `mtg_sets.csv` bestand met alle sets.

## Project structuur

```
skill-website/
├── app.py                      # De Flask webapp
├── mtg_sets_export.py          # CSV export script
├── requirements.txt            # Dependencies
├── README.md                   # Dit bestand
├── .vscode/
│   └── settings.json          # VS Code settings
├── static/
│   └── css/
│       ├── base.css           # Basis stijlen
│       ├── style.css          # Homepage stijlen
│       └── detail.css         # Detailpagina stijlen
└── templates/
    ├── index.html             # Homepage
    └── set_detail.html        # Detailpagina
```

## Features

- **Zoekfunctie**: Typ in de zoekbalk om sets te vinden
- **Detailpagina's**: Klik op een set voor meer info
- **API endpoint**: `/api/sets` geeft JSON terug als je dat nodig hebt
- **Mooie design**: FontAwesome icons en moderne styling

## Tech stuff

- Python met Flask
- Scryfall API voor de data
- HTML/CSS/JavaScript voor de frontend
- CSV export functionaliteit

## Belangrijk

De data komt van Scryfall en valt onder de Wizards of the Coast Fan Content Policy. Volg hun regels als je de data gebruikt.

---


"# skills-heroes-voorronde" 
