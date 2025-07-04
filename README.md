# KRAKEN-TOOL

KRAKEN-TOOL est un projet *open source* visant à expliquer le fonctionnement d'outils d'OSINT et de pentest. Each feature resides in the `modules/` directory and can be launched from an interactive menu.

## Installation / Setup

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

## Modules disponibles / Available Tools

Outils actuellement implémentés :

- **Whois Lookup** – récupère les informations WHOIS d'un domaine.
- **DNS Lookup** – résout les enregistrements DNS A d'un domaine.
- **IP Tracker** – localise une adresse IP via ip-api (HTTP seulement).
- **Port Scanner** – effectue un scan TCP simple sur une plage de ports.

D'autres modules seront ajoutés pour atteindre environ 50 fonctionnalités.

## Usage

```bash
python main.py
```

Un menu s'affiche et permet de sélectionner chaque outil. Each module begins
with a short explanation before execution.

## Tests

Run the unit tests from the project root. The `pytest.ini` enables quiet
output, but you still need to set the `PYTHONPATH` so the modules can be
imported correctly:

```bash
PYTHONPATH=. pytest -q
```

The tests mock network calls to verify the `ip_tracker` success path, the
`dns_lookup` handling of nonexistent domains and the `whois_lookup` response to
an invalid domain.

## Contribuer / Contributing

Les contributions sont bienvenues ! Ouvrez une issue ou une pull request pour
ajouter de nouveaux modules ou améliorer le code existant.

## License

Ce projet est distribué sous licence MIT. Voir le fichier `LICENSE` pour plus
d'informations.
