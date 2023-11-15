
# Technische Anleitung für "Paketdienst mit E-Mail-Benachrichtigung"

## Überblick
Dieses Dokument bietet eine detaillierte Anleitung für das Skript `paketdienst_mit_email.py`. Es beschreibt die Konfiguration, die Funktionsweise und die Einsatzmöglichkeiten des Skripts.

## Installation
Stellen Sie sicher, dass Python 3.8+ installiert ist und laden Sie die Dateien `paketdienst_mit_email.py` und `update_config.json` herunter.

## Konfigurationsdatei `update_config.json`

```json
{
  "_comments": {
    "auto_update": "Liste der Pakete für automatische Aktualisierung",
    "manual_update": "Liste der Pakete für manuelle Aktualisierung",
    "log_level": "Protokollierungsstufe (DEBUG, INFO, WARNING, ERROR, CRITICAL)",
    "enable_email": "Schalter, ob eine eMail gesendet werden soll oder nicht. (true, false)"
  },
  "auto_update": ["pandas", "numpy", "colorama"],
  "manual_update": ["requests"],
  "log_level": "DEBUG",
  "enable_email": false
}
```

### Hauptfunktionen des Skripts

1. **Automatische und manuelle Paketaktualisierungen:**
   - Automatische Aktualisierung der in `auto_update` gelisteten Pakete.
   - Manuelle Bestätigung für Pakete in `manual_update` vor der Aktualisierung.

2. **Verbessertes Logging:**
   - Detaillierte Protokollierung basierend auf dem eingestellten `log_level`.

3. **E-Mail-Benachrichtigung:**
   - Bei Aktivierung (`enable_email` = true) wird eine E-Mail mit dem Update-Protokoll versendet.
   - Konfigurieren Sie Ihre SMTP-Einstellungen im Skript für diese Funktion.

### SMTP-Einstellungen

Konfigurieren Sie die folgenden Variablen im Skript für die E-Mail-Funktionalität:

```python
SMTP_SERVER = "Ihr_SMTP_Server"
SMTP_PORT = 587
SMTP_USERNAME = "Ihr_Benutzername"
SMTP_PASSWORD = "Ihr_Passwort"
SENDER_EMAIL = "Ihre_Email@beispiel.com"
RECIPIENT_EMAIL = "Empfaenger_Email@beispiel.com"
```

### Skriptausführung

Starten Sie das Skript mit:

```bash
python paketdienst_mit_email.py
```

Überprüfen Sie nach Abschluss die Protokolldatei und, falls aktiviert, Ihren E-Mail-Posteingang.

## Wartung und Updates

- Halten Sie das Skript und die Python-Umgebung aktuell.
- Testen Sie Änderungen in einer sicheren Umgebung.

## Beispiele zur Einbindung des Skripts
1. **Automatisierung in CI/CD-Pipelines:**  
   - Das Skript kann in Continuous Integration und Continuous Deployment (CI/CD) Pipelines integriert werden, um die Python-Abhängigkeiten automatisch zu aktualisieren. Dies kann beispielsweise in einer Pipeline geschehen, die bei jedem Push in ein Git-Repository ausgelöst wird. Die Integration in die Pipeline stellt sicher, dass die Anwendung immer mit den neuesten und sichersten Paketversionen getestet und bereitgestellt wird.
  
  
2. **Verwaltung von Entwicklungs- und Testumgebungen:**  
   - In Entwicklungsteams, in denen mehrere Personen an demselben Projekt arbeiten, kann das Skript dazu verwendet werden, die Konsistenz der verwendeten Pakete in allen Entwicklungs- und Testumgebungen sicherzustellen. Indem das Skript regelmäßig ausgeführt wird, können Sie sicherstellen, dass alle Teammitglieder mit denselben Paketversionen arbeiten, was die Konsistenz und Zuverlässigkeit des Entwicklungsprozesses erhöht.

  
3. **Wartung von Servern und Produktionssystemen:**  
   - Das Skript kann auf Servern und in Produktionssystemen eingesetzt werden, um die dort laufenden Python-Anwendungen regelmäßig zu aktualisieren. Durch die Einrichtung eines Cron-Jobs oder eines ähnlichen zeitgesteuerten Mechanismus kann das Skript automatisch in festgelegten Intervallen ausgeführt werden, um die Sicherheit und Leistung der Anwendungen zu gewährleisten.

  
4. **Persönliche Automatisierungsaufgaben:**  
   - Auch für Einzelpersonen, die mehrere Python-Projekte verwalten, ist das Skript eine große Hilfe. Indem Sie es in Ihren persönlichen Workflow integrieren, können Sie Zeit sparen und sicherstellen, dass Ihre Projekte immer mit den aktuellen Paketversionen arbeiten.


## Programmierbeispiel zur Einbindung des Skripts
Stellen Sie sich vor, Sie haben ein Python-Skript, das verschiedene Aufgaben in Ihrem Projekt automatisiert. Sie möchten das "Paketdienst mit E-Mail-Benachrichtigung"-Skript in dieses übergeordnete Skript integrieren, um regelmäßig die Pakete zu aktualisieren. Hier ist ein einfaches Beispiel, wie dies aussehen könnte:

```python
import subprocess
import sys

def aktualisiere_pakete():
    try:
        # Ausführen des Paketdienst-Skripts
        subprocess.run(["python", "paketdienst_mit_email.py"], check=True)
        print("Paketaktualisierung erfolgreich durchgeführt.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Paketaktualisierung: {e}", file=sys.stderr)

def hauptaufgabe():
    # Hier könnten weitere Aufgaben Ihres Skripts stehen
    pass

if __name__ == "__main__":
    aktualisiere_pakete()
    hauptaufgabe()
```
In diesem Beispiel wird das Paketdienst-Skript mit subprocess.run aufgerufen. Dies ermöglicht es, das Skript als Teil eines größeren Automatisierungsprozesses zu verwenden. Fehler beim Ausführen des Skripts werden abgefangen und im Fehlerstrom ausgegeben, was bei der Fehlersuche hilfreich sein kann.


**Diese Beispiele sollen Ihnen helfen, das Skript in einer Weise zu verwenden, die Ihren spezifischen Anforderungen und dem Kontext Ihrer Arbeit entspricht.**
 

 

---
**Autor:** Christian Hammenstede  
**Kontakt:** christian.hammenstede@gmail.com  
**Version:** 1.0  
**Datum:** 15.11.2023

---