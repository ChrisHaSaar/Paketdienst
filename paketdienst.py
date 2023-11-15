"""
Python Paketdienst

Es wird geprüft, ob pip aktuell ist, falls nicht, wird es direkt geupdated.
Danach werden alle installierten Pakete gecheckt und notfalls erneuert.
In dem Verzeichnis Log-Files werden die entsprechenden Log-Dateien angelegt.
damit man weiß, was genau passiert ist.

Genauere Beschreibung findest Du in der README.md

geschrieben von:
Christian Hammenstede, 15.11.2023
christian.hammenstede@gmail.com

"""

import subprocess
import os
import json
from datetime import datetime
from importlib import metadata


def log_step(log, message):
    """ Protokolliert einen Schritt im Log. """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {message}\n"
    log.write(log_entry)
    print(log_entry, end="")  # Gibt die Nachricht auch im Terminal aus


def upgrade_pip(log):
    """ Führt ein Upgrade von pip durch, falls erforderlich. """
    log_step(log, "Prüfe und aktualisiere pip...")
    result = subprocess.run("pip list --outdated", shell=True, capture_output=True, text=True)
    if 'pip' in result.stdout:
        subprocess.run("python -m pip install --upgrade pip", shell=True)
        log_step(log, "pip aktualisiert.")


def dry_run_upgrade(log, package):
    """ Führt eine 'dry run' Aktualisierung durch, um zu sehen, was geändert würde. """
    log_step(log, f"Prüfe, was sich bei der Aktualisierung von {package} ändern würde...")
    result = subprocess.run(f"pip install --upgrade --dry-run {package}", shell=True, capture_output=True, text=True)
    log_step(log, result.stdout)


def batch_upgrade_decision(log, packages):
    """ Führt eine Aktualisierung für eine Liste von Paketen durch. """
    for package in packages:
        log_step(log, f"Aktualisiere {package} automatisch...")
        subprocess.run(f"pip install --upgrade {package}", shell=True)
        log_step(log, f"{package} aktualisiert.")


def manual_confirmation_upgrade(log, package):
    """ Führt eine manuelle Aktualisierung mit Bestätigung durch. """
    dry_run_upgrade(log, package)
    decision = input(f"Möchten Sie {package} aktualisieren? [y/n]: ").strip().lower()
    if decision == 'y':
        log_step(log, f"Aktualisiere {package} manuell...")
        subprocess.run(f"pip install --upgrade {package}", shell=True)
        log_step(log, f"{package} aktualisiert.")


def main():
    # Konfigurationsdatei lesen
    with open('update_config.json') as config_file:
        config = json.load(config_file)

    auto_update_packages = config.get("auto_update", [])
    manual_update_packages = config.get("manual_update", [])

    # Pfad für den Log-Ordner festlegen und erstellen, falls nicht vorhanden
    script_directory = os.path.dirname(os.path.abspath(__file__))
    log_folder = os.path.join(script_directory, "Log-Files")
    os.makedirs(log_folder, exist_ok=True)

    # Log-Datei-Pfad erstellen
    log_file = os.path.join(log_folder, f"pip_upgrade_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

    with open(log_file, "w") as log:
        log_step(log, "Aktualisierungsprozess gestartet.")

        upgrade_pip(log)

        # Jedes Paket überprüfen und ggf. aktualisieren
        for dist in metadata.distributions():
            package = dist.metadata['Name']
            if package in auto_update_packages:
                # Automatische Aktualisierung
                batch_upgrade_decision(log, auto_update_packages)
            elif package in manual_update_packages:
                # Manuelle Aktualisierung mit Bestätigung
                manual_confirmation_upgrade(log, package)

        log_step(log, "Aktualisierungsprozess abgeschlossen.")


if __name__ == "__main__":
    main()
