GERMAN & ENGLISH

GERMAN/DEUTSCH
Python-Paketaktualisierungsskript

Beschreibung:
Dieses Python-Skript mit dem Titel "Paketdienst" automatisiert den Prozess der Überprüfung und Aktualisierung von Python-Paketen mithilfe des Paketmanagers pip. Das Skript stellt sicher, dass pip selbst auf dem neuesten Stand ist, überprüft dann alle installierten Pakete und bietet die Möglichkeit, diese zu aktualisieren. Zusätzlich generiert es detaillierte Protokolldateien im Verzeichnis "Log-Files", um einen klaren Überblick über den Aktualisierungsprozess zu liefern.

Neue Funktionen:

Batch-Entscheidungen: 
Ermöglicht es dem Benutzer, Entscheidungen für mehrere Pakete gleichzeitig zu treffen, wie z.B. alle Minor-Updates oder alle Updates für eine bestimmte Auswahl von Paketen.

Automatische Entscheidungen mit manueller Überprüfungsoption: Führt standardmäßig alle Updates durch, bietet jedoch eine Option, bei der das Skript vor jedem Update pausiert, damit der Benutzer entscheiden kann.

Funktionen:
Überprüft und aktualisiert pip auf die neueste Version, falls erforderlich.
Untersucht installierte Pakete und führt automatische Aktualisierungen für vordefinierte Pakete durch.
Ermöglicht manuelle Bestätigung vor der Aktualisierung bestimmter Pakete.
Erstellt Protokolldateien im Verzeichnis "Log-Files", um den Aktualisierungsprozess detailliert zu dokumentieren.

Autor:
Christian Hammenstede
E-Mail: christian.hammenstede@gmail.com
Datum: 15.11.2023

Verwendung:
Führen Sie das Skript aus, um veraltete Pakete zu überprüfen.
Pip wird automatisch aktualisiert, wenn erforderlich.
Das Skript durchläuft installierte Pakete und aktualisiert automatisch oder manuell spezifizierte Pakete.
Protokolldateien werden im Verzeichnis "Log-Files" generiert und bieten detaillierte Informationen über den Aktualisierungsprozess.

Konfiguration:
Das Skript liest Konfigurationseinstellungen aus der Datei update_config.json, um die Anpassung von Auto-Update- und Manuell-Update-Listen zu ermöglichen.

Beispielverwendung:

python Paketdienst.py

Hinweis:
Überprüfen Sie die generierte Protokolldatei für einen umfassenden Überblick über den Aktualisierungsprozess.

===========================================

ENGLISH:
Python Package Update Script

Description:
This Python script, titled "Paketdienst" (Package Service), automates the process of checking and updating Python packages using the pip package manager. The script ensures that pip itself is up to date and then examines all installed packages, offering the option to update them. Additionally, it generates detailed log files in the "Log-Files" directory, providing a clear record of the update process.

New Features:

Batch Decisions: 
Allows the user to make decisions for multiple packages simultaneously, such as all minor updates or all updates for a specific selection of packages.

Automatic Decisions with Manual Confirmation Option: Defaults to performing all updates but offers an option where the script pauses before each update for the user to decide.

Features:
Checks and upgrades pip to the latest version if needed.
Examines installed packages and performs automatic updates for predefined packages.
Allows for manual confirmation before updating specific packages.
Creates log files in the "Log-Files" directory to document the update process in detail.

Author:
Christian Hammenstede
Email: christian.hammenstede@gmail.com
Date: 15.11.2023

How to Use:
Run the script to check for outdated packages.
Pip is upgraded automatically if necessary.
The script iterates through installed packages, updating those specified for automatic or manual updates.
Log files are generated in the "Log-Files" directory, providing detailed information on the update process.

Configuration:
The script reads configuration settings from update_config.json, allowing customization of auto-update and manual-update lists.

Example Usage:

python Paketdienst.py

Note:
Ensure to review the generated log file for a comprehensive overview of the update process.