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

# Pip zuerst aktualisieren
upgrade_pip()

# Pfad für den Log-Ordner festlegen und erstellen, falls nicht vorhanden
log_folder = "Log-Files"
os.makedirs(log_folder, exist_ok=True)

# Log-Datei-Pfad erstellen
log_file = os.path.join(log_folder, f"pip_upgrade_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

# Dry Run für alle Pakete durchführen und Ergebnisse sammeln
upgrade_candidates = []
for dist in metadata.distributions():
    package = dist.metadata['Name']
    dry_run_result = dry_run_upgrade(package)
    if dry_run_result.strip():
        upgrade_candidates.append(package)
        print(f"Vorgeschlagene Aktualisierung für {package}:\n{dry_run_result}")

# Benutzer um Entscheidung bitten
if upgrade_candidates:
    decision = input("Möchten Sie alle vorgeschlagenen Aktualisierungen durchführen? [y/n]: ").strip().lower()
    if decision == 'y':
        with open(log_file, "w") as log:
            for package in upgrade_candidates:
                log.write(f"Aktualisiere {package}\n")
                update_result = subprocess.run(f"pip install --upgrade {package}", shell=True, capture_output=True, text=True)
                log.write(update_result.stdout)
                if update_result.stderr:
                    log.write(f"Fehler bei der Aktualisierung von {package}:\n{update_result.stderr}\n")
                print(f"{package} wurde aktualisiert.")
    else:
        print("Aktualisierung abgebrochen.")
else:
    print("Keine Aktualisierungen notwendig.")

print(f"Aktualisierung abgeschlossen. Log-Datei gespeichert unter: {log_file}")
