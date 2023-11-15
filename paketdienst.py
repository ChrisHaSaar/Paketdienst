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
        print("Aktualisiere pip...")
        subprocess.run("python -m pip install --upgrade pip", shell=True)

# Pip zuerst aktualisieren
upgrade_pip()

# Pfad für den Log-Ordner festlegen und erstellen, falls nicht vorhanden
log_folder = "Log-Files"
os.makedirs(log_folder, exist_ok=True)

# Log-Datei-Pfad erstellen
log_file = os.path.join(log_folder, f"pip_upgrade_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

with open(log_file, "w") as log:
    # Liste aller installierten Pakete erhalten
    distributions = metadata.distributions()
    packages = [dist.metadata['Name'] for dist in distributions]

    # Jedes Paket aktualisieren und Log führen
    for package in packages:
        log.write(f"Aktualisiere {package}\n")
        result = subprocess.run(f"pip install --upgrade {package}", shell=True, capture_output=True, text=True)
        log.write(result.stdout)
        if result.stderr:
            log.write("Fehler:\n")
            log.write(result.stderr)
        log.write("\n")

print(f"Aktualisierung abgeschlossen. Log-Datei gespeichert unter: {log_file}")
