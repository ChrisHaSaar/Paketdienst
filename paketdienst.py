import pkg_resources
import subprocess
from datetime import datetime

# Log-Datei erstellen
log_file = f"pip_upgrade_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

with open(log_file, "w") as log:
    # Liste aller installierten Pakete erhalten
    packages = [dist.project_name for dist in pkg_resources.working_set]

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
