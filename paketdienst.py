"""
Python Paketdienst

Es wird geprüft, ob pip aktuell ist, falls nicht, wird es direkt geupdated.
Danach werden alle installierten Pakete gecheckt und notfalls erneuert.
In dem Verzeichnis Log-Files werden die entsprechenden Log-Dateien angelegt.
damit man weiß, was genau passiert ist.

geschrieben von:
Christian Hammenstede, 15.11.2023
christian.hammenstede@gmail.com

"""

import subprocess
import os
import json
from datetime import datetime
from importlib import metadata

def upgrade_pip():
    """ Führt ein Upgrade von pip durch, falls erforderlich. """
    result = subprocess.run("pip list --outdated", shell=True, capture_output=True, text=True)
    if 'pip' in result.stdout:
        subprocess.run("python -m pip install --upgrade pip", shell=True)

def dry_run_upgrade(package):
    """ Führt eine 'dry run' Aktualisierung durch, um zu sehen, was geändert würde. """
    result = subprocess.run(f"pip install --upgrade --dry-run {package}", shell=True, capture_output=True, text=True)
    return result.stdout

# Konfigurationsdatei lesen
with open('update_config.json') as config_file:
    config = json.load(config_file)
auto_update_packages = config.get("auto_update", [])
manual_update_packages = config.get("manual_update", [])

# Pfad für den Log-Ordner festlegen und erstellen, falls nicht vorhanden
log_folder = "Log-Files"
os.makedirs(log_folder, exist_ok=True)

# Log-Datei-Pfad erstellen
log_file = os.path.join(log_folder, f"pip_upgrade_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

# Pip zuerst aktualisieren
upgrade_pip()

with open(log_file, "w") as log:
    # Jedes Paket überprüfen und ggf. aktualisieren
    for dist in metadata.distributions():
        package = dist.metadata['Name']
        if package in auto_update_packages:
            # Automatische Aktualisierung
            log.write(f"Aktualisiere {package} automatisch\n")
            subprocess.run(f"pip install --upgrade {package}", shell=True)
        elif package in manual_update_packages:
            # Manuelle Aktualisierung mit Bestätigung
            dry_run_result = dry_run_upgrade(package)
            decision = input(f"Möchten Sie {package} aktualisieren? [y/n]: ").strip().lower()
            if decision == 'y':
                log.write(f"Aktualisiere {package} manuell\n")
                subprocess.run(f"pip install --upgrade {package}", shell=True)

print(f"Aktualisierung abgeschlossen. Log-Datei gespeichert unter: {log_file}")
