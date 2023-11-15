### Python-Paketaktualisierungsskript

**Beschreibung:**
Dieses Python-Skript mit dem Titel "Paketdienst" automatisiert den Prozess der Überprüfung und Aktualisierung von Python-Paketen mithilfe des Paketmanagers pip. Das Skript stellt sicher, dass pip selbst auf dem neuesten Stand ist, überprüft dann alle installierten Pakete und bietet die Möglichkeit, diese zu aktualisieren. Zusätzlich generiert es detaillierte Protokolldateien im Verzeichnis "Log-Files", um einen klaren Überblick über den Aktualisierungsprozess zu liefern.

**Neue Funktionen:**
1. **Batch-Entscheidungen:** Ermöglicht es dem Benutzer, Entscheidungen für mehrere Pakete gleichzeitig zu treffen, wie z.B. alle Minor-Updates oder alle Updates für eine bestimmte Auswahl von Paketen.
   
2. **Automatische Entscheidungen mit manueller Überprüfungsoption:** Führt standardmäßig alle Updates durch, bietet jedoch eine Option, bei der das Skript vor jedem Update pausiert, damit der Benutzer entscheiden kann.

**Funktionen:**
- Überprüft und aktualisiert pip auf die neueste Version, falls erforderlich.
- Untersucht installierte Pakete und führt automatische Aktualisierungen für vordefinierte Pakete durch.
- Ermöglicht manuelle Bestätigung vor der Aktualisierung bestimmter Pakete.
- Erstellt Protokolldateien im Verzeichnis "Log-Files", um den Aktualisierungsprozess detailliert zu dokumentieren.

**Autor:**
Christian Hammenstede  
E-Mail: christian.hammenstede@gmail.com  
Datum: 15.11.2023

**Verwendung:**
Führen Sie das Skript aus, um veraltete Pakete zu überprüfen. Pip wird automatisch aktualisiert, wenn erforderlich. Das Skript durchläuft installierte Pakete und aktualisiert automatisch oder manuell spezifizierte Pakete. Protokolldateien werden im Verzeichnis "Log-Files" generiert und bieten detaillierte Informationen über den Aktualisierungsprozess.

**Konfiguration:**
Das Skript liest Konfigurationseinstellungen aus der Datei update_config.json, um die Anpassung von Auto-Update- und Manuell-Update-Listen zu ermöglichen.

**Beispielverwendung:**
```bash

python Paketdienst.py

```

**Hinweis:**
Überprüfen Sie die generierte Protokolldatei für einen umfassenden Überblick über den Aktualisierungsprozess.