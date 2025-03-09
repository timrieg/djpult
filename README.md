# DJ Pult Webanwendung

Diese Anwendung ist eine einfache Webanwendung zum Abspielen von lokal gespeicherten Musik-Snippets mit einer DJ-Pult-Oberfläche. Die Anwendung wurde mit **Python (Flask)** erstellt und bietet eine einfache Benutzeroberfläche mit Kategorisierung und Lautstärkesteuerung.

## Voraussetzungen
Damit die Anwendung auf jedem Gerät ausgeführt werden kann, werden folgende Abhängigkeiten benötigt:

- **Python** (Version 3.7 oder neuer)
- **Flask** (wird unten installiert)

## Installation & Start

### 1. Repository/Kopien vorbereiten
Falls das Projekt von Git oder einem anderen Speicherort heruntergeladen wurde, wechsle in das Verzeichnis:

```sh
cd pfad/zum/projekt
```

### 2. Virtuelle Umgebung (optional, empfohlen)
Um eine isolierte Umgebung für das Projekt zu erstellen, führe aus:

```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Abhängigkeiten installieren
Falls Flask noch nicht installiert ist, installiere es mit:

```sh
pip install flask
```

### 4. Starten der Anwendung
Die Anwendung kann direkt aus dem Terminal oder der Konsole gestartet werden:

```sh
python app.py
```

Nach dem Start ist die Anwendung unter folgender Adresse erreichbar:

```
http://127.0.0.1:5000/
```

Öffne diese URL in einem Webbrowser, um das DJ-Pult zu verwenden.

## Verwendung
- **Lieder abspielen:** Klicke auf einen Song-Button, um die Wiedergabe zu starten.
- **Stoppen mit Fading:** Der `Stop`-Button reduziert die Lautstärke über 3 Sekunden, bevor die Musik stoppt.
- **Lautstärke regeln:** Verwende die vertikale Lautstärkeregelung auf der rechten Seite.
- **Kategorisierte Wiedergabe:** Lieder sind nach `Ass/Angriff`, `Block`, `Gegner` und `Sonstiges` kategorisiert.

## Fehlerbehebung
Falls Fehler auftreten:

- Prüfe, ob Python und Flask installiert sind (`python --version`, `pip show flask`).
- Stelle sicher, dass sich die Musikdateien im `static/music/`-Verzeichnis befinden.
- Falls Port 5000 bereits belegt ist, starte die Anwendung mit einem anderen Port:
  
  ```sh
  python app.py --port=8080
  ```
  Dann die Anwendung unter `http://127.0.0.1:8080/` aufrufen.

## Lizenz
Dieses Projekt ist Open Source und darf nach Belieben modifiziert und verwendet werden.

