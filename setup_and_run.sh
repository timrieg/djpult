#!/bin/bash

# Setze das Arbeitsverzeichnis auf das Verzeichnis dieses Skripts
cd "$(dirname "$0")"

# Prüfe, ob Python installiert ist
if ! command -v python3 &> /dev/null; then
    echo "Python3 ist nicht installiert. Bitte installiere Python3 und versuche es erneut."
    exit 1
fi

# Prüfe, ob pip installiert ist
if ! command -v pip3 &> /dev/null; then
    echo "pip3 ist nicht installiert. Bitte installiere pip3 und versuche es erneut."
    exit 1
fi

# Erstelle eine virtuelle Umgebung, falls sie nicht existiert
if [ ! -d "venv" ]; then
    echo "Erstelle virtuelle Umgebung..."
    python3 -m venv venv
fi

# Aktiviere die virtuelle Umgebung
source venv/bin/activate

# Installiere benötigte Python-Abhängigkeiten
pip install --upgrade pip
pip install flask

# Starte die Anwendung
echo "Starte die DJ-Pult Anwendung..."
python app.py
