# KRAKEN-TOOL

KRAKEN-TOOL est un projet éducatif regroupant divers outils d'OSINT et de pentest. Chaque fonctionnalité est implémentée dans un module séparé dans le dossier `modules/` et peut être appelée via un menu interactif dans le terminal.

## Installation

1. Clonez ce dépôt.
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Lancez le programme :
   ```bash
   python main.py
   ```

## Structure

- `main.py` : menu principal qui appelle les modules.
- `modules/` : répertoire contenant chaque outil sous forme de module Python.
- `requirements.txt` : liste des dépendances nécessaires.

## Modules disponibles

Pour l'instant, trois modules de base sont inclus :

- **Whois Lookup** : récupère les informations WHOIS d'un domaine.
- **DNS Lookup** : résout les enregistrements DNS A d'un domaine.
- **IP Tracker** : localise une adresse IP via ip-api.

D'autres modules seront ajoutés pour atteindre environ 50 fonctionnalités.
