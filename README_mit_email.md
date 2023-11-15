# Paketdienst mit E-Mail-Benachrichtigung

Dieses Python-Skript "paketdienst_mit_email.py" erweitert das ursprüngliche "Paketdienst"-Skript um fortgeschrittene Funktionen für umfassende Berichterstattung und Benachrichtigungen. Der Aktualisierungsprozess wird detailliert protokolliert, und am Ende wird eine E-Mail-Benachrichtigung mit dem Protokoll als Anhang versendet.

## Funktionalitäten

- **Verbessertes Logging:** Das Skript erstellt eine detaillierte Protokolldatei, die jeden Schritt des Aktualisierungsprozesses dokumentiert, einschließlich Erfolg/Misserfolg der Aktualisierungen.

- **E-Mail-Benachrichtigung:** Nach Abschluss des Aktualisierungsprozesses wird automatisch eine E-Mail-Benachrichtigung versendet. Diese enthält das Protokoll als Anhang und informiert über den Abschluss des Skripts oder aufgetretene Probleme.

## Konfiguration

Für die E-Mail-Benachrichtigung sind einige Konfigurationsparameter erforderlich. Diese sind im Skript im Bereich `# Konfiguration` zu finden. Ersetzen Sie die Dummy-Werte durch Ihre eigenen SMTP-Einstellungen.

```python
SMTP_SERVER = "your_smtp_server"
SMTP_PORT = 587
SMTP_USERNAME = "your_username"
SMTP_PASSWORD = "your_password"
SENDER_EMAIL = "your_email@example.com"
RECIPIENT_EMAIL = "recipient_email@example.com"
```
## Verwendung

Führen Sie das Skript "paketdienst_mit_email.py" aus, um den erweiterten Aktualisierungsprozess zu starten.

```bash
python paketdienst_mit_email.py
```

## Hinweis

Überprüfen Sie die generierte Protokolldatei für eine umfassende Übersicht über den Aktualisierungsprozess. Beachten Sie, dass eine funktionierende Internetverbindung erforderlich ist, um die E-Mail-Benachrichtigung zu senden.

---

**Autor:** Christian Hammenstede  
**E-Mail:** christian.hammenstede@gmail.com  
**Datum:** 15.11.2023

--- 

*Hinweis: Ersetzen Sie alle Dummy-Werte durch Ihre eigenen Informationen.*
