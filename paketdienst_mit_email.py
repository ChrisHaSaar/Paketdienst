import subprocess
import os
import json
from datetime import datetime
from importlib import metadata
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Konfiguration
LOG_FOLDER = "Log-Files"
LOG_FILE_PREFIX = "pip_upgrade_log"
UPDATE_CONFIG_FILE = "update_config.json"
SMTP_SERVER = "your_smtp_server"
SMTP_PORT = 587
SMTP_USERNAME = "your_username"
SMTP_PASSWORD = "your_password"
SENDER_EMAIL = "your_email@example.com"
RECIPIENT_EMAIL = "recipient_email@example.com"



def upgrade_pip(logger):
    """ Führt ein Upgrade von pip durch, falls erforderlich. """
    log_step(logger, "Prüfe und aktualisiere pip...")
    result = subprocess.run("pip list --outdated", shell=True, capture_output=True, text=True)
    if 'pip' in result.stdout:
        subprocess.run("python -m pip install --upgrade pip", shell=True)
        log_step(logger, "pip aktualisiert.")
    else:
        log_step(logger, "pip ist bereits auf dem neuesten Stand.")



def log_step(logger, message):
    """ Protokolliert einen Schritt im Log. """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {message}"
    logger.info(log_entry)
    print(log_entry, end="")  # Gibt die Nachricht auch im Terminal aus


def configure_logger(log_file, log_level):
    """ Konfiguriert den Logger. """
    logger = logging.getLogger("PaketdienstLogger")
    logger.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def send_email(log_file):
    """ Sendet eine E-Mail mit dem Log-Datei-Anhang. """
    subject = "Paketdienst Update Report"
    body = "Der Aktualisierungsprozess wurde abgeschlossen. Details finden Sie im angehängten Log-File."

    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = RECIPIENT_EMAIL
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    attachment = MIMEText(open(log_file, "r").read())
    attachment.add_header("Content-Disposition", "attachment", filename=os.path.basename(log_file))
    message.attach(attachment)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message.as_string())


def main():
    # Pfad für den Log-Ordner festlegen und erstellen, falls nicht vorhanden
    script_directory = os.path.dirname(os.path.abspath(__file__))
    log_folder = os.path.join(script_directory, LOG_FOLDER)
    os.makedirs(log_folder, exist_ok=True)

    # Log-Datei-Pfad erstellen
    log_file = os.path.join(log_folder, f"{LOG_FILE_PREFIX}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    # Konfiguriere den Logger
    with open(UPDATE_CONFIG_FILE) as config_file:
        config = json.load(config_file)

    log_level = getattr(logging, config.get("log_level", "INFO").upper())
    logger = configure_logger(log_file, log_level)

    log_step(logger, "Aktualisierungsprozess gestartet.")

    # Führe die Aktualisierung durch
    auto_update_packages = config.get("auto_update", [])
    manual_update_packages = config.get("manual_update", [])

    if config.get("enable_email", False):
        upgrade_pip(logger)

        # Jedes Paket überprüfen und ggf. aktualisieren
        for dist in metadata.distributions():
            package = dist.metadata['Name']
            if package in auto_update_packages:
                # Automatische Aktualisierung
                batch_upgrade_decision(logger, auto_update_packages)
            elif package in manual_update_packages:
                # Manuelle Aktualisierung mit Bestätigung
                manual_confirmation_upgrade(logger, package)

        log_step(logger, "Aktualisierungsprozess abgeschlossen.")

        # Sende eine E-Mail mit dem Log-File-Anhang
        send_email(log_file)
    else:
        log_step(logger, "E-Mail-Funktion ist deaktiviert. Der Aktualisierungsprozess wird ohne E-Mail-Benachrichtigung durchgeführt.")


if __name__ == "__main__":
    main()
